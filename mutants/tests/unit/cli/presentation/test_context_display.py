from __future__ import annotations

from hexawyn.cli.presentation.context_display import format_context_switch_lines
from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext,
    KubernetesContextSwitchResult,
)


class TestFormatContextSwitchLines:
    def test_successful_switch_displays_context(self) -> None:
        ctx = ClusterContext(
            name="prod-eu",
            cluster="prod-eu-cluster",
            namespace="default",
            user="admin",
            is_current=True,
        )
        result = KubernetesContextSwitchResult(
            contexts=[ctx],
            current_context=ctx,
            connected=True,
            switched=True,
            kubeconfig_paths=[],
        )

        lines = format_context_switch_lines(result)

        joined = " ".join(text for text, _ in lines)
        assert "Context switched" in joined
        assert "prod-eu" in joined
        assert "default" in joined
        assert "Connection successful" in joined

    def test_connection_failure_shows_warning(self) -> None:
        ctx = ClusterContext(
            name="staging",
            cluster="staging-cluster",
            namespace="kube-system",
            user="admin",
            is_current=True,
        )
        result = KubernetesContextSwitchResult(
            contexts=[ctx],
            current_context=ctx,
            connected=False,
            switched=True,
            kubeconfig_paths=[],
        )

        lines = format_context_switch_lines(result)

        joined = " ".join(text for text, _ in lines)
        assert "Connection failed" in joined

    def test_null_current_context_shows_failed(self) -> None:
        result = KubernetesContextSwitchResult(
            contexts=[],
            current_context=None,
            connected=False,
            switched=False,
            kubeconfig_paths=[],
        )

        lines = format_context_switch_lines(result)

        assert len(lines) == 1
        assert "failed" in lines[0][0]

    def test_connection_error_shown_when_not_connected(self) -> None:
        ctx = ClusterContext(
            name="staging",
            cluster="staging-cluster",
            namespace="default",
            user="admin",
            is_current=True,
        )
        result = KubernetesContextSwitchResult(
            contexts=[ctx],
            current_context=ctx,
            connected=False,
            switched=True,
            kubeconfig_paths=[],
            connection_error="API server unreachable",
        )

        lines = format_context_switch_lines(result)

        joined = " ".join(text for text, _ in lines)
        assert "API server unreachable" in joined

    def test_connection_error_not_shown_when_connected(self) -> None:
        ctx = ClusterContext(
            name="prod",
            cluster="prod-cluster",
            namespace="default",
            user="admin",
            is_current=True,
        )
        result = KubernetesContextSwitchResult(
            contexts=[ctx],
            current_context=ctx,
            connected=True,
            switched=True,
            kubeconfig_paths=[],
            connection_error="old error",
        )

        lines = format_context_switch_lines(result)

        joined = " ".join(text for text, _ in lines)
        assert "old error" not in joined
