from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.use_case.detect_unintended_external_exposure.detect_unintended_external_exposure_use_case import (
    DetectUnintendedExternalExposureUseCase,
)


class TestDetectUnintendedExternalExposureUseCase:
    def test_execute_delegates_to_service_and_returns_response(self) -> None:
        from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_response import (
            DetectUnintendedExternalExposureResponse,
        )

        mock_service = MagicMock()
        expected = DetectUnintendedExternalExposureResponse(
            total_external_services_checked=5,
            summary="all clear",
        )
        mock_service.detect_unintended_exposure.return_value = expected

        use_case = DetectUnintendedExternalExposureUseCase(service=mock_service)
        command = DetectUnintendedExternalExposureCommand(
            allowlist=["api-gateway"],
            namespaces=["production"],
        )

        result = use_case.execute(command)

        mock_service.detect_unintended_exposure.assert_called_once_with(command)
        assert result is expected
        assert result.total_external_services_checked == 5

    def test_execute_passes_empty_command_to_service(self) -> None:
        mock_service = MagicMock()
        mock_service.detect_unintended_exposure.return_value = MagicMock()

        use_case = DetectUnintendedExternalExposureUseCase(service=mock_service)
        command = DetectUnintendedExternalExposureCommand()

        use_case.execute(command)

        mock_service.detect_unintended_exposure.assert_called_once_with(command)
