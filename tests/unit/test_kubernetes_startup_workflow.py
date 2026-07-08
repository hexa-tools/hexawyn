from unittest.mock import MagicMock, patch

from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext,
    KubernetesStartupStatus,
)


def test_cli_app_builds_adapter_from_discovered_current_context() -> None:
    from hexawyn.cli.app import HexawynApp

    _ = KubernetesStartupStatus(
        contexts=[
            ClusterContext(
                name="prod",
                cluster="cluster-prod",
                namespace="default",
                user="user-prod",
                is_current=True,
            )
        ],
        current_context=ClusterContext(
            name="prod",
            cluster="cluster-prod",
            namespace="default",
            user="user-prod",
            is_current=True,
        ),
        connected=True,
        kubeconfig_paths=[],
    )

    with (
        patch.dict("os.environ", {"HEXAWYN_DEMO_MODE": "false"}, clear=False),
        patch("hexawyn.cli.app.FileKubernetesDiscoveryService") as discovery_service,
        patch("hexawyn.cli.app.build_adapters") as build_adapters,
        patch("hexawyn.cli.tui.HexawynTUI") as tui,
    ):
        discovery_service.return_value.current.return_value = ClusterContext(
            name="prod",
            cluster="cluster-prod",
            namespace="default",
            user="user-prod",
            is_current=True,
        )
        build_adapters.return_value = MagicMock()

        HexawynApp()._run_tui()

    build_adapters.assert_called_once_with("prod")
    tui.assert_called_once()


def test_session_screen_renders_kubernetes_startup_status() -> None:
    from hexawyn.cli.tui import _startup_lines

    startup_status = KubernetesStartupStatus(
        contexts=[
            ClusterContext(
                name="prod",
                cluster="cluster-prod",
                namespace="default",
                user="user-prod",
                is_current=True,
            ),
            ClusterContext(
                name="staging",
                cluster="cluster-staging",
                namespace="staging",
                user="user-staging",
                is_current=False,
            ),
        ],
        current_context=ClusterContext(
            name="prod",
            cluster="cluster-prod",
            namespace="default",
            user="user-prod",
            is_current=True,
        ),
        connected=False,
        kubeconfig_paths=[],
        connection_error="connection refused",
    )

    lines = _startup_lines(startup_status)

    assert "[green]✓[/green] Kubernetes detected" in lines
    assert "[dim]Detected 2 contexts[/dim]" in lines
    assert "[green]✓[/green] Current context: [bold]prod[/bold]" in lines
    assert "[green]✓[/green] Namespace: [bold]default[/bold]" in lines
    assert "[yellow]⚠[/yellow] Unable to connect" in lines
