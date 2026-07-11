"""RED → GREEN — MCP tool: diff_helm_values."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.helm_values_diff_port import (
    HelmReleaseValues,
    HelmValuesDiffPort,
)
from hexawyn.domain.errors import HelmNotFoundError


def _values(namespace: str, values: dict[str, object]) -> HelmReleaseValues:
    return HelmReleaseValues(release="payment-service", namespace=namespace, values=values)


class TestDiffHelmValuesTool:
    def test_delegates_and_returns_grouped_diff(self) -> None:
        mock_port = MagicMock(spec=HelmValuesDiffPort)
        mock_port.get_effective_values.side_effect = [
            _values("staging", {"image": {"tag": "v1.3"}, "replicaCount": 1}),
            _values("production", {"image": {"tag": "v1.2"}, "replicaCount": 3}),
        ]

        with patch(
            "hexawyn.mcp.server.build_helm_values_diff_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.diff_helm_values import diff_helm_values

            result = diff_helm_values(
                release="payment-service",
                source_namespace="staging",
                target_namespace="production",
            )

        assert result["release"] == "payment-service"
        assert result["in_sync"] is False
        assert result["total_differences"] == 2
        assert result["critical"][0]["key_path"] == "image.tag"
        assert result["warning"][0]["key_path"] == "replicaCount"
        assert result["error"] is None

    def test_redacts_secret_values(self) -> None:
        mock_port = MagicMock(spec=HelmValuesDiffPort)
        mock_port.get_effective_values.side_effect = [
            _values("staging", {"database": {"password": "s3cr3t-staging"}}),
            _values("production", {"database": {"password": "s3cr3t-prod"}}),
        ]

        with patch(
            "hexawyn.mcp.server.build_helm_values_diff_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.diff_helm_values import diff_helm_values

            result = diff_helm_values(
                release="payment-service",
                source_namespace="staging",
                target_namespace="production",
            )

        secret_diff = result["critical"][0]
        assert secret_diff["source_value"] == "[REDACTED]"
        assert secret_diff["target_value"] == "[REDACTED]"

    def test_handles_helm_error_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_helm_values_diff_adapter",
            side_effect=HelmNotFoundError(),
        ):
            from hexawyn.mcp.tools.diff_helm_values import diff_helm_values

            result = diff_helm_values(
                release="payment-service",
                source_namespace="staging",
                target_namespace="production",
            )

        assert result["in_sync"] is False
        assert result["total_differences"] == 0
        assert result["error"] is not None

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.diff_helm_values import register

        assert callable(register)
