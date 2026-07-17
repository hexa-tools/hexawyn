"""Unit tests for DetectUnintendedExternalExposureUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_service_port import (
    DetectUnintendedExternalExposureServicePort,
)
from hexawyn.application.use_case.detect_unintended_external_exposure.detect_unintended_external_exposure_use_case import (
    DetectUnintendedExternalExposureUseCase,
)


class TestDetectUnintendedExternalExposureUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectUnintendedExternalExposureServicePort)
        use_case = DetectUnintendedExternalExposureUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect_unintended_exposure.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectUnintendedExternalExposureServicePort)
        mock_service.detect_unintended_exposure.side_effect = RuntimeError("test error")
        use_case = DetectUnintendedExternalExposureUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
