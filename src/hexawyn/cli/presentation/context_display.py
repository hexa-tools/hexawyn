from hexawyn.infrastructure.config.kubernetes_context import (
    KubernetesContextSwitchResult,
)


def format_context_switch_lines(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "yellow"
    lines = [
        ("\u2713 Context switched", "green"),
        ("", "dim"),
        (f"Current context: {current_context.name}", "bold"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines
