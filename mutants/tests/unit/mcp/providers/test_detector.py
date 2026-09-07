from __future__ import annotations

from unittest.mock import patch

from hexawyn.mcp.providers.detector import (
    _current_cluster_context,
    _detect_provider,
    _is_aws_eks_context,
    _is_azure_aks_context,
    _is_datadog_enabled,
    _is_gcp_gke_context,
)


class TestDetectProvider:
    def test_override_matches_provider_key(self) -> None:
        ctx = {"name": "prod", "cluster": "prod", "provider": "aws", "namespace": "default"}
        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="aws"
        ):
            assert _detect_provider(ctx, "aws", lambda c: False) is True

    def test_override_does_not_match(self) -> None:
        ctx = {"name": "prod", "cluster": "prod", "provider": "aws", "namespace": "default"}
        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="gcp"
        ):
            assert _detect_provider(ctx, "aws", lambda c: False) is False

    def test_no_override_calls_supports_true(self) -> None:
        ctx = {"name": "prod", "cluster": "prod", "provider": "aws", "namespace": "default"}
        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value=None
        ):
            assert _detect_provider(ctx, "aws", lambda c: True) is True

    def test_supports_raises_returns_false(self) -> None:
        ctx = {"name": "prod", "cluster": "prod", "provider": "aws", "namespace": "default"}
        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value=None
        ):
            assert _detect_provider(ctx, "aws", lambda c: 1 / 0) is False


class TestIsAwsEksContext:
    def test_delegates_to_detect_provider(self) -> None:
        ctx = {"name": "prod", "cluster": "prod", "provider": "aws", "namespace": "default"}
        with patch("hexawyn.mcp.providers.detector._detect_provider") as mock_detect:
            mock_detect.return_value = True
            assert _is_aws_eks_context(ctx) is True
            assert mock_detect.call_args[0][1] == "aws"


class TestIsGcpGkeContext:
    def test_delegates_to_detect_provider(self) -> None:
        ctx = {"name": "prod", "cluster": "prod", "provider": "gcp", "namespace": "default"}
        with patch("hexawyn.mcp.providers.detector._detect_provider") as mock_detect:
            mock_detect.return_value = False
            assert _is_gcp_gke_context(ctx) is False
            assert mock_detect.call_args[0][1] == "gcp"


class TestIsAzureAksContext:
    def test_delegates_to_detect_provider(self) -> None:
        ctx = {"name": "prod", "cluster": "prod", "provider": "azure", "namespace": "default"}
        with patch("hexawyn.mcp.providers.detector._detect_provider") as mock_detect:
            mock_detect.return_value = True
            assert _is_azure_aks_context(ctx) is True


class TestIsDatadogEnabled:
    def test_override_datadog(self) -> None:
        ctx = {"name": "prod", "cluster": "prod", "provider": "aws", "namespace": "default"}
        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override",
            return_value="datadog",
        ):
            assert _is_datadog_enabled(ctx) is True

    def test_override_not_datadog(self) -> None:
        ctx = {"name": "prod", "cluster": "prod", "provider": "aws", "namespace": "default"}
        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override",
            return_value="prometheus",
        ):
            assert _is_datadog_enabled(ctx) is False

    def test_no_override_falls_back_to_config(self) -> None:
        ctx = {"name": "prod", "cluster": "prod", "provider": "aws", "namespace": "default"}
        with (
            patch(
                "hexawyn.infrastructure.config.stack_config.get_stack_override",
                return_value=None,
            ),
            patch(
                "hexawyn.infrastructure.config.datadog_config.is_datadog_configured",
                return_value=True,
            ),
        ):
            assert _is_datadog_enabled(ctx) is True


class TestCurrentClusterContext:
    def test_default_context(self) -> None:
        with patch("hexawyn.mcp.providers.detector.context_name", "default"):
            import importlib

            importlib.reload(
                __import__("hexawyn.mcp.providers.detector", fromlist=["_current_cluster_context"])
            )
            ctx = _current_cluster_context()
            assert ctx["name"] == "default"
            assert ctx["provider"] == "unknown"

    def test_unknown_name_defaults(self) -> None:
        import hexawyn.mcp.providers.detector as mod

        mod.context_name = "unknown"
        ctx = mod._current_cluster_context()
        assert ctx["name"] == "default"
