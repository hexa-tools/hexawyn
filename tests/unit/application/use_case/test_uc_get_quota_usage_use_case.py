"""Unit tests for GetQuotaUsageUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_service_port import (
    GetQuotaUsageServicePort,
)
from hexawyn.application.use_case.get_quota_usage.get_quota_usage_use_case import (
    GetQuotaUsageUseCase,
)


class TestGetQuotaUsageUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GetQuotaUsageServicePort)
        use_case = GetQuotaUsageUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.execute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GetQuotaUsageServicePort)
        mock_service.execute.side_effect = RuntimeError("test error")
        use_case = GetQuotaUsageUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
