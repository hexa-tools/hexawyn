from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.command import (  # noqa: E501
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.conservative_namespace_overview_use_case import (  # noqa: E501
    ConservativeNamespaceOverviewUseCase,
    _to_resource_dict,
    _to_response,
)
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.response import (  # noqa: E501
    ConservativeNamespaceOverviewResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_overview import (
    NamespaceCounts,
    NamespaceHealthStatus,
    NamespaceOverviewReport,
    UnhealthyResource,
)


class TestConservativeNamespaceOverviewUseCase:
    def test_get_overview_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_namespace_summary.return_value = {
            "total_pods": 0,
            "total_deployments": 0,
            "total_services": 0,
            "total_crashlooping": 0,
        }
        port.list_unhealthy_resources.return_value = []
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = ConservativeNamespaceOverviewUseCase(
            port=port,
            k8s_port=k8s,
        )
        result = use_case.get_overview(ConservativeNamespaceOverviewCommand(namespace="default"))

        assert isinstance(result, ConservativeNamespaceOverviewResponse)

    def test_get_overview_raises_when_namespace_not_found(self) -> None:
        port = MagicMock()
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "other-ns", "status": "Active", "age": "30d"},
        ]

        use_case = ConservativeNamespaceOverviewUseCase(
            port=port,
            k8s_port=k8s,
        )

        with pytest.raises(ResourceNotFoundError, match="not found"):
            use_case.get_overview(ConservativeNamespaceOverviewCommand(namespace="missing-ns"))


class TestMapperFunctions:
    def test_to_resource_dict_converts_unhealthy_resource(self) -> None:
        resource = UnhealthyResource(
            name="crash-pod",
            kind="Pod",
            reason="CrashLoopBackOff",
        )

        result = _to_resource_dict(resource)

        assert isinstance(result, dict)
        assert result["name"] == "crash-pod"
        assert result["kind"] == "Pod"
        assert result["reason"] == "CrashLoopBackOff"

    def test_to_response_with_unhealthy_resources(self) -> None:
        report = NamespaceOverviewReport(
            namespace="default",
            namespace_status="Active",
            counts=NamespaceCounts(
                pods_total=5,
                pods_running=4,
                pods_failed=1,
                deployments_total=2,
                deployments_ready=2,
                services_total=3,
            ),
            health_status=NamespaceHealthStatus.DEGRADED,
            root_cause="Pod crash-pod is in CrashLoopBackOff",
            unhealthy_resources=[
                UnhealthyResource(name="crash-pod", kind="Pod", reason="CrashLoopBackOff"),
            ],
            warnings=["Warning: high memory usage"],
            has_more_unhealthy=False,
            remaining_unhealthy_count=0,
            estimated_tokens=120,
            is_empty=False,
            summary="Namespace 'default' has unhealthy pods.",
        )

        result = _to_response(report)

        assert result.namespace == "default"
        assert result.health_status == "Degraded"
        assert len(result.unhealthy_resources) == 1
        assert result.unhealthy_resources[0]["name"] == "crash-pod"
        assert result.summary == "Namespace 'default' has unhealthy pods."
