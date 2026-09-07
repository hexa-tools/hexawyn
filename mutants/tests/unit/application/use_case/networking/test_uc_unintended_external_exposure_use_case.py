from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.networking.unintended_external_exposure.command import (
    UnintendedExternalExposureCommand,
)
from hexawyn.application.use_case.networking.unintended_external_exposure.response import (
    UnintendedExternalExposureResponse,
)
from hexawyn.application.use_case.networking.unintended_external_exposure.unintended_external_exposure_use_case import (  # noqa: E501
    UnintendedExternalExposureUseCase,
)


class TestUnintendedExternalExposureUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.audit_external_exposure.return_value = []

        use_case = UnintendedExternalExposureUseCase(port=port)
        result = use_case.execute(UnintendedExternalExposureCommand())

        assert isinstance(result, UnintendedExternalExposureResponse)

    def test_execute_no_services_exposed(self) -> None:
        port = MagicMock()
        port.audit_external_exposure.return_value = []

        use_case = UnintendedExternalExposureUseCase(port=port)
        result = use_case.execute(UnintendedExternalExposureCommand(namespace="default"))

        assert result.total_services == 0
