"""Unit tests for DetectMissingProbesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_missing_probes.detect_missing_probes_service_port import (
    DetectMissingProbesServicePort,
)
from hexawyn.application.use_case.detect_missing_probes.detect_missing_probes_use_case import (
    DetectMissingProbesUseCase,
)


class TestDetectMissingProbesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectMissingProbesServicePort)
        use_case = DetectMissingProbesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect_missing_probes.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectMissingProbesServicePort)
        mock_service.detect_missing_probes.side_effect = RuntimeError("test error")
        use_case = DetectMissingProbesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
