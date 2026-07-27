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
