"""Unit tests for DiffHelmValuesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_service_port import (
    DiffHelmValuesServicePort,
)
from hexawyn.application.use_case.diff_helm_values.diff_helm_values_use_case import (
    DiffHelmValuesUseCase,
)


class TestDiffHelmValuesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DiffHelmValuesServicePort)
        use_case = DiffHelmValuesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.diff.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DiffHelmValuesServicePort)
        mock_service.diff.side_effect = RuntimeError("test error")
        use_case = DiffHelmValuesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
