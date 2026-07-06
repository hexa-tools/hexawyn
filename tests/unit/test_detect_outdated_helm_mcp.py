"""RED → GREEN — MCP tool: detect_outdated_helm_releases."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.helm_release_version_port import (
    ChartLatestRawData,
    HelmReleaseRawData,
    HelmReleaseVersionPort,
)
from hexawyn.domain.errors import HelmNotFoundError


class TestDetectOutdatedHelmReleasesTool:
    def test_delegates_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=HelmReleaseVersionPort)
        mock_port.list_releases.return_value = [
            HelmReleaseRawData(
                release_name="nginx-ingress",
                namespace="default",
                chart_name="nginx-ingress",
                chart_version="4.7.1",
                is_pinned=False,
            ),
        ]
        mock_port.fetch_latest_version.return_value = ChartLatestRawData(
            chart_name="nginx-ingress",
            latest_version="4.10.3",
            breaking_changes="",
            repo_error="",
        )

        with patch(
            "hexawyn.mcp.server.build_helm_release_version_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.detect_outdated_helm_releases import (
                detect_outdated_helm_releases,
            )

            result = detect_outdated_helm_releases()

        assert result["total_releases"] == 1
        assert result["outdated_count"] == 1
        assert result["releases"][0]["delta_type"] == "minor"
        assert result["error"] is None

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_helm_release_version_adapter",
            side_effect=HelmNotFoundError(),
        ):
            from hexawyn.mcp.tools.detect_outdated_helm_releases import (
                detect_outdated_helm_releases,
            )

            result = detect_outdated_helm_releases()

        assert result["outdated_count"] == 0
        assert "helm" in result["error"].lower()

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.detect_outdated_helm_releases import register

        assert callable(register)
