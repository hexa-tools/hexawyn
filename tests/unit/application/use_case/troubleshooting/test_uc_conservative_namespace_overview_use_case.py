from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.command import (  # noqa: E501
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.conservative_namespace_overview_use_case import (  # noqa: E501
    ConservativeNamespaceOverviewUseCase,
)
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.response import (  # noqa: E501
    ConservativeNamespaceOverviewResponse,
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
