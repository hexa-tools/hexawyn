"""Unit tests for AdaptiveNamespaceInvestigationService (mocks
ConservativeNamespaceOverviewServicePort + K8sPort + AdaptiveInvestigationPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_command import (
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_response import (
    ConservativeNamespaceOverviewResponse,
    UnhealthyResourceDict,
)
from hexawyn.application.service.adaptive_namespace_investigation_service import (
    AdaptiveNamespaceInvestigationService,
)
from hexawyn.domain.errors import ResourceNotFoundError


def _pod(name: str, restarts: int = 0) -> dict:
    return {
        "name": name,
        "namespace": "production",
        "status": "CrashLoopBackOff",
        "restarts": restarts,
        "age": "1d",
        "node": "n1",
    }


def _overview_response(
    unhealthy: list[UnhealthyResourceDict] | None = None,
) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace="production",
        namespace_status="Active",
        health_status="Critical",
        unhealthy_resources=unhealthy or [],
        summary="2 unhealthy resource(s) found in 'production'.",
    )


def _investigation_raw(
    events: list[str] | None = None,
    logs: list[str] | None = None,
    last_termination_reason: str | None = None,
) -> dict:
    return {
        "events": events or [],
        "logs": logs or [],
        "restart_count": 0,
        "last_termination_reason": last_termination_reason,
    }


def _make_service(
    overview_service: MagicMock | None = None,
    k8s_port: MagicMock | None = None,
    investigation_port: MagicMock | None = None,
) -> tuple[AdaptiveNamespaceInvestigationService, MagicMock, MagicMock, MagicMock]:
    if overview_service is None:
        overview_service = MagicMock()
        overview_service.get_overview.return_value = _overview_response()
    if k8s_port is None:
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = []
    if investigation_port is None:
        investigation_port = MagicMock()
        investigation_port.investigate_resource.return_value = _investigation_raw()
    service = AdaptiveNamespaceInvestigationService(
        overview_service=overview_service, k8s_port=k8s_port, investigation_port=investigation_port
    )
    return service, overview_service, k8s_port, investigation_port


class TestEcaReuse:
    def test_calls_overview_service_with_namespace(self) -> None:
        service, overview_service, _, _ = _make_service()

        service.investigate(AdaptiveNamespaceInvestigationCommand(namespace="production"))

        called_command = overview_service.get_overview.call_args[0][0]
        assert called_command.namespace == "production"

    def test_no_failing_resources_makes_zero_drilldown_calls(self) -> None:
        """TC2: no failing resources → no drill-down calls at all."""
        service, _, _, investigation_port = _make_service()

        response = service.investigate(
            AdaptiveNamespaceInvestigationCommand(namespace="production")
        )

        investigation_port.investigate_resource.assert_not_called()
        assert response.investigated_resources == []


class TestRestartCountMatching:
    def test_matches_pod_restart_counts_for_ranking(self) -> None:
        """Checker edge case: ranking must be consistent with restart_count —
        CrashLoop(45) must outrank OOMKilled(12) and be drilled first."""
        overview_service = MagicMock()
        overview_service.get_overview.return_value = _overview_response(
            [
                UnhealthyResourceDict(name="auth-pod-xyz", kind="Pod", reason="OOMKilled"),
                UnhealthyResourceDict(
                    name="payment-pod-abc", kind="Pod", reason="CrashLoopBackOff"
                ),
            ]
        )
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod("auth-pod-xyz", 12), _pod("payment-pod-abc", 45)]
        service, _, _, investigation_port = _make_service(
            overview_service=overview_service, k8s_port=k8s_port
        )

        service.investigate(AdaptiveNamespaceInvestigationCommand(namespace="production"))

        first_call_args = investigation_port.investigate_resource.call_args_list[0]
        assert first_call_args.args[2] == "payment-pod-abc"


class TestDepthPassthrough:
    def test_depth_one_limits_drilldown_calls(self) -> None:
        """TC3: depth=1 → only the top-ranked resource is drilled."""
        overview_service = MagicMock()
        overview_service.get_overview.return_value = _overview_response(
            [
                UnhealthyResourceDict(name="pod-a", kind="Pod", reason="CrashLoopBackOff"),
                UnhealthyResourceDict(name="pod-b", kind="Pod", reason="CrashLoopBackOff"),
            ]
        )
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod("pod-a", 10), _pod("pod-b", 5)]
        service, _, _, investigation_port = _make_service(
            overview_service=overview_service, k8s_port=k8s_port
        )

        response = service.investigate(
            AdaptiveNamespaceInvestigationCommand(namespace="production", depth=1)
        )

        assert investigation_port.investigate_resource.call_count == 1
        assert response.has_more_failing is True
        assert response.remaining_failing_count == 1


class TestResourceDisappearedMidDrilldown:
    def test_disappeared_resource_recorded_and_skipped(self) -> None:
        overview_service = MagicMock()
        overview_service.get_overview.return_value = _overview_response(
            [
                UnhealthyResourceDict(name="pod-a", kind="Pod", reason="CrashLoopBackOff"),
                UnhealthyResourceDict(name="pod-b", kind="Pod", reason="CrashLoopBackOff"),
            ]
        )
        k8s_port = MagicMock()
        k8s_port.list_pods.return_value = [_pod("pod-a", 10), _pod("pod-b", 5)]
        investigation_port = MagicMock()
        investigation_port.investigate_resource.side_effect = [
            ResourceNotFoundError("pod-a not found"),
            _investigation_raw(),
        ]
        service, _, _, _ = _make_service(
            overview_service=overview_service,
            k8s_port=k8s_port,
            investigation_port=investigation_port,
        )

        response = service.investigate(
            AdaptiveNamespaceInvestigationCommand(namespace="production")
        )

        assert response.skipped_resources == ["pod-a"]
        assert len(response.investigated_resources) == 1
        assert response.investigated_resources[0]["name"] == "pod-b"


class TestNodePressureContext:
    def test_all_pending_sets_node_pressure_context_no_drilldown(self) -> None:
        overview_service = MagicMock()
        overview_service.get_overview.return_value = _overview_response(
            [UnhealthyResourceDict(name="pod-a", kind="Pod", reason="Pending")]
        )
        service, _, _, investigation_port = _make_service(overview_service=overview_service)

        response = service.investigate(
            AdaptiveNamespaceInvestigationCommand(namespace="production")
        )

        investigation_port.investigate_resource.assert_not_called()
        assert response.node_pressure_context is not None
