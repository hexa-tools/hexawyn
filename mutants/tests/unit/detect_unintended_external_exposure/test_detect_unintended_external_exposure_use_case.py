from __future__ import annotations

from unittest.mock import MagicMock


class TestDetectUnintendedExternalExposureUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.networking.detect_unintended_external_exposure.command import (  # noqa: E501
            DetectUnintendedExternalExposureCommand,
        )
        from hexawyn.application.use_case.networking.detect_unintended_external_exposure.detect_unintended_external_exposure_use_case import (  # noqa: E501
            DetectUnintendedExternalExposureUseCase,
        )
        from hexawyn.application.use_case.networking.detect_unintended_external_exposure.response import (  # noqa: E501
            DetectUnintendedExternalExposureResponse,
        )

        port = MagicMock()
        port.list_external_services.return_value = []
        use_case = DetectUnintendedExternalExposureUseCase(port=port)
        result = use_case.execute(DetectUnintendedExternalExposureCommand())
        assert isinstance(result, DetectUnintendedExternalExposureResponse)
