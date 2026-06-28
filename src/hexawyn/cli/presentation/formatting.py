from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext as KubernetesClusterContext,
)
from hexawyn.infrastructure.config.kubernetes_context import (
    KubernetesContextSwitchResult,
    KubernetesStartupStatus,
)


def app_version() -> str:
    try:
        return version("hexawyn")
    except PackageNotFoundError:
        return "local"


def compact_project_directory() -> str:
    current_directory = Path.cwd()
    home_directory = Path.home()
    try:
        relative_directory = current_directory.resolve().relative_to(home_directory.resolve())
    except ValueError:
        return str(current_directory)
    return f"~/{relative_directory.as_posix()}"


def current_context_from(
    contexts: list[KubernetesClusterContext],
) -> KubernetesClusterContext | None:
    for context in contexts:
        if context.is_current:
            return context
    return None


def context_list_lines(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_ctx = current_context_from(contexts)
    current_ctx_name = current_ctx.name if current_ctx is not None else "unknown"
    lines = [(f"Current context: {current_ctx_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def missing_context_lines(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def startup_status_from_switch(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=switch_result.current_context,
        connected=switch_result.connected,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=switch_result.connection_error,
    )


def context_line(adapter: Any) -> str:
    ctx = adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(adapter.get_findings()) if hasattr(adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def connection_line(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and not startup_status.connected:
        return "[yellow]⚠ Disconnected[/yellow]"
    return "[green]✓ Connected[/green]"


def startup_lines(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_ctx = startup_status.current_context
    conn = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_ctx.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_ctx.namespace}[/bold]",
        conn,
    ]
