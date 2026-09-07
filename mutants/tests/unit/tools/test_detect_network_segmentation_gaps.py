from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectNetworkSegmentationGapsMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.detect_network_segmentation_gaps import (
            detect_network_segmentation_gaps,
        )

        mock_port = MagicMock()
        with patch(
            "hexawyn.mcp.server.build_network_policy_audit_adapter",
            return_value=mock_port,
        ):
            result = detect_network_segmentation_gaps()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert result["findings"] == []
        assert result["total_namespaces_checked"] == 0

    def test_returns_all_keys_even_on_empty_response(self) -> None:
        from hexawyn.mcp.tools.detect_network_segmentation_gaps import (
            detect_network_segmentation_gaps,
        )

        mock_port = MagicMock()
        with patch(
            "hexawyn.mcp.server.build_network_policy_audit_adapter",
            return_value=mock_port,
        ):
            result = detect_network_segmentation_gaps()

        expected_keys = {
            "findings",
            "excluded_namespaces",
            "total_namespaces_checked",
            "fully_open_count",
            "partially_restricted_count",
            "restricted_count",
            "summary",
            "error",
        }
        assert set(result.keys()) == expected_keys

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.detect_network_segmentation_gaps import (
            detect_network_segmentation_gaps,
        )

        with patch(
            "hexawyn.mcp.server.build_network_policy_audit_adapter",
            side_effect=RuntimeError("network policies unavailable"),
        ):
            result = detect_network_segmentation_gaps()

        assert isinstance(result, dict)
        assert "network policies unavailable" in str(result["error"])
        assert result["findings"] == []

    def test_exception_returns_same_key_shape(self) -> None:
        from hexawyn.mcp.tools.detect_network_segmentation_gaps import (
            detect_network_segmentation_gaps,
        )

        with patch(
            "hexawyn.mcp.server.build_network_policy_audit_adapter",
            side_effect=RuntimeError("boom"),
        ):
            result = detect_network_segmentation_gaps()

        assert "findings" in result
        assert "error" in result
        assert "total_namespaces_checked" in result
