from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetQuotaUsageMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.get_quota_usage import get_quota_usage

        mock_runtime = MagicMock()
        mock_runtime.check_quota.return_value = {
            "allowed": True,
            "used": 50,
            "limit": 100,
            "remaining": 50,
        }
        with (
            patch(
                "hexawyn.application.service.runtime_adapter.get_runtime",
                return_value=mock_runtime,
            ),
            patch(
                "hexawyn.adapters.secondary.runtime_quota_source._get_current_slack_quota",
                return_value=MagicMock(count=0, limit=50),
            ),
        ):
            result = get_quota_usage()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert len(result["quotas"]) == 2  # noqa: PLR2004

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.get_quota_usage import get_quota_usage

        with patch(
            "hexawyn.application.service.runtime_adapter.get_runtime",
            side_effect=RuntimeError("plan service down"),
        ):
            result = get_quota_usage()

        assert isinstance(result, dict)
        assert "plan service down" in str(result["error"])
        assert result["quotas"] == []
