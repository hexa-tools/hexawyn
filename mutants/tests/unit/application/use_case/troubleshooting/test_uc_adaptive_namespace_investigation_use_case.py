from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.adaptive_namespace_investigation_use_case import (  # noqa: E501
    AdaptiveNamespaceInvestigationUseCase,
)
from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.command import (  # noqa: E501
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.response import (  # noqa: E501
    AdaptiveNamespaceInvestigationResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError


class TestAdaptiveNamespaceInvestigationUseCase:
    def test_investigate_returns_response(self) -> None:
        overview = MagicMock()
        overview.get_overview.return_value = MagicMock(is_empty=True)
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]
        k8s.list_pods.return_value = []
        inv = MagicMock()
        inv.investigate_resource.return_value = {"events": [], "logs": []}

        use_case = AdaptiveNamespaceInvestigationUseCase(
            overview_service=overview,
            k8s_port=k8s,
            investigation_port=inv,
        )
        result = use_case.investigate(AdaptiveNamespaceInvestigationCommand(namespace="default"))

        assert isinstance(result, AdaptiveNamespaceInvestigationResponse)

    def test_investigate_with_unhealthy_resources(self) -> None:
        overview_response = MagicMock()
        overview_response.namespace = "default"
        overview_response.namespace_status = "Active"
        overview_response.health_status = "degraded"
        overview_response.unhealthy_resources = [
            {"name": "crash-pod", "kind": "Pod", "reason": "CrashLoopBackOff"},
        ]
        overview_response.summary = "1 unhealthy pod"
        overview = MagicMock()
        overview.get_overview.return_value = overview_response

        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {"name": "crash-pod", "restarts": 5},
        ]

        inv = MagicMock()
        inv.investigate_resource.return_value = {
            "events": ["BackOff: Back-off restarting failed container"],
            "logs": ["Error: container crashed"],
            "last_termination_reason": "Error",
        }

        use_case = AdaptiveNamespaceInvestigationUseCase(
            overview_service=overview,
            k8s_port=k8s,
            investigation_port=inv,
        )
        result = use_case.investigate(AdaptiveNamespaceInvestigationCommand(namespace="default"))

        assert isinstance(result, AdaptiveNamespaceInvestigationResponse)
        assert len(result.investigated_resources) >= 1

    def test_investigate_resource_not_found_skips_resource(self) -> None:
        overview_response = MagicMock()
        overview_response.namespace = "default"
        overview_response.namespace_status = "Active"
        overview_response.health_status = "degraded"
        overview_response.unhealthy_resources = [
            {"name": "missing-pod", "kind": "Pod", "reason": "CrashLoopBackOff"},
        ]
        overview_response.summary = "1 unhealthy pod"
        overview = MagicMock()
        overview.get_overview.return_value = overview_response

        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {"name": "missing-pod", "restarts": 5},
        ]

        inv = MagicMock()
        inv.investigate_resource.side_effect = ResourceNotFoundError("resource not found")

        use_case = AdaptiveNamespaceInvestigationUseCase(
            overview_service=overview,
            k8s_port=k8s,
            investigation_port=inv,
        )
        result = use_case.investigate(AdaptiveNamespaceInvestigationCommand(namespace="default"))

        assert isinstance(result, AdaptiveNamespaceInvestigationResponse)
        assert "missing-pod" in result.skipped_resources
