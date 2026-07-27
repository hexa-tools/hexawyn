from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetQuotaUsageMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.get_quota_usage import get_quota_usage

        mock_plan = MagicMock()
        mock_plan.get_limit.return_value = 100
        mock_plan.tier_required_for.return_value = None
        mock_meter = MagicMock()
        mock_meter.get_usage.return_value = 50

        with (
            patch(
                "hexawyn.mcp.server.build_pricing_plan_adapter",
                return_value=mock_plan,
            ),
            patch(
                "hexawyn.mcp.server.build_usage_meter_adapter",
                return_value=mock_meter,
            ),
        ):
            result = get_quota_usage()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert len(result["quotas"]) == 2  # noqa: PLR2004

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.get_quota_usage import get_quota_usage

        with patch(
            "hexawyn.mcp.server.build_pricing_plan_adapter",
            side_effect=RuntimeError("plan service down"),
        ):
            result = get_quota_usage()

        assert isinstance(result, dict)
        assert "plan service down" in str(result["error"])
        assert result["quotas"] == []
