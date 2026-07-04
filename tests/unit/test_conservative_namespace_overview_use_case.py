from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_response import (
    ConservativeNamespaceOverviewResponse,
)
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_service_port import (
    ConservativeNamespaceOverviewServicePort,
)
from hexawyn.application.use_case.conservative_namespace_overview.conservative_namespace_overview_use_case import (
    ConservativeNamespaceOverviewUseCase,
)


class TestConservativeNamespaceOverviewUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=ConservativeNamespaceOverviewServicePort)
        expected = ConservativeNamespaceOverviewResponse(namespace="staging")
        service.get_overview.return_value = expected
        use_case = ConservativeNamespaceOverviewUseCase(service=service)
        command = ConservativeNamespaceOverviewCommand(namespace="staging")

        result = use_case.execute(command)

        service.get_overview.assert_called_once_with(command)
        assert result is expected
