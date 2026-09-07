from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestManualChangeOutsideGitopsMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.manual_change_outside_gitops_detection import (
            detect_manual_changes_outside_gitops,
        )

        mock_port = MagicMock()
        mock_port.list_live_config_resources.return_value = []
        mock_port.fetch_audit_log_events.return_value = {
            "events": [],
            "available": False,
            "earliest_timestamp": None,
        }

        with patch(
            "hexawyn.mcp.server.build_audit_log_adapter",
            return_value=mock_port,
        ):
            result = detect_manual_changes_outside_gitops(namespace="default")

        assert isinstance(result, dict)
        assert result["error"] is None
        assert result["total_manual_changes"] == 0

    def test_passes_namespace_to_command(self) -> None:
        from hexawyn.mcp.tools.manual_change_outside_gitops_detection import (
            detect_manual_changes_outside_gitops,
        )

        mock_port = MagicMock()
        mock_port.list_live_config_resources.return_value = []
        mock_port.fetch_audit_log_events.return_value = {
            "events": [],
            "available": False,
            "earliest_timestamp": None,
        }

        with patch(
            "hexawyn.mcp.server.build_audit_log_adapter",
            return_value=mock_port,
        ):
            result = detect_manual_changes_outside_gitops(namespace="production")

        assert result["error"] is None

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.manual_change_outside_gitops_detection import (
            detect_manual_changes_outside_gitops,
        )

        with patch(
            "hexawyn.mcp.server.build_audit_log_adapter",
            side_effect=RuntimeError("audit log unavailable"),
        ):
            result = detect_manual_changes_outside_gitops()

        assert isinstance(result, dict)
        assert "audit log unavailable" in str(result["error"])
