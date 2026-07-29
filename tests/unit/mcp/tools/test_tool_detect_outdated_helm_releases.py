"""Unit tests for MCP tool: detect_outdated_helm_releases."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectOutdatedHelmReleasesTool:
    def test_detect_outdated_helm_releases_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_outdated_helm_releases import (
            detect_outdated_helm_releases,
        )

        with patch(
            "hexawyn.mcp.server.build_helm_release_version_adapter",
            return_value=MagicMock(),
        ):
            result = detect_outdated_helm_releases()

        assert isinstance(result, dict)
        assert "error" in result

    def test_detect_outdated_helm_releases_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_outdated_helm_releases import (
            detect_outdated_helm_releases,
        )

        with patch(
            "hexawyn.mcp.server.build_helm_release_version_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = detect_outdated_helm_releases()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_detect_outdated_helm_releases_success_path(self) -> None:
        from hexawyn.mcp.tools.detect_outdated_helm_releases import (
            detect_outdated_helm_releases,
        )

        mock_release = MagicMock()
        mock_release.release_name = "test-release"
        mock_release.namespace = "test-ns"
        mock_release.chart_name = "test-chart"
        mock_release.current_version = "1.0.0"
        mock_release.latest_version = "1.1.0"
        mock_release.delta_type = "minor"
        mock_release.breaking_changes = False
        mock_release.repo_error = None
        mock_result = MagicMock()
        mock_result.total_releases = 1
        mock_result.outdated_count = 1
        mock_result.up_to_date_count = 0
        mock_result.error_count = 0
        mock_result.releases = [mock_release]
        mock_response = MagicMock()
        mock_response.result = mock_result
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_helm_release_version_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.detect_outdated_helm_releases.DetectOutdatedHelmReleasesUseCase",
                return_value=mock_uc,
            ),
        ):
            result = detect_outdated_helm_releases()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_outdated_helm_releases")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
