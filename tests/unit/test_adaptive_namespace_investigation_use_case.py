from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_command import (
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_response import (
    AdaptiveNamespaceInvestigationResponse,
)
from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_service_port import (
    AdaptiveNamespaceInvestigationServicePort,
)
from hexawyn.application.use_case.adaptive_namespace_investigation.adaptive_namespace_investigation_use_case import (
    AdaptiveNamespaceInvestigationUseCase,
)


class TestAdaptiveNamespaceInvestigationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=AdaptiveNamespaceInvestigationServicePort)
        expected = AdaptiveNamespaceInvestigationResponse(namespace="production")
        service.investigate.return_value = expected
        use_case = AdaptiveNamespaceInvestigationUseCase(service=service)
        command = AdaptiveNamespaceInvestigationCommand(namespace="production")

        result = use_case.execute(command)

        service.investigate.assert_called_once_with(command)
        assert result is expected
