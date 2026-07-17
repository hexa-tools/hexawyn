"""Unit tests for VersionRegressionUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.version_regression.version_regression_service_port import (
    VersionRegressionServicePort,
)
from hexawyn.application.use_case.version_regression.version_regression_use_case import (
    VersionRegressionUseCase,
)


class TestVersionRegressionUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=VersionRegressionServicePort)
        use_case = VersionRegressionUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=VersionRegressionServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = VersionRegressionUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
