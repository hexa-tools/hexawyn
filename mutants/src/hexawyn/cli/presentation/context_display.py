from hexawyn.infrastructure.config.kubernetes_context import (
    KubernetesContextSwitchResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_format_context_switch_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_context_switch_lines__mutmut)
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


def x_format_context_switch_lines__mutmut_orig(
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


def x_format_context_switch_lines__mutmut_1(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = None
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


def x_format_context_switch_lines__mutmut_2(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is not None:
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


def x_format_context_switch_lines__mutmut_3(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("XX\u2717 Context switch failedXX", "red")]

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


def x_format_context_switch_lines__mutmut_4(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 context switch failed", "red")]

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


def x_format_context_switch_lines__mutmut_5(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 CONTEXT SWITCH FAILED", "red")]

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


def x_format_context_switch_lines__mutmut_6(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "XXredXX")]

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


def x_format_context_switch_lines__mutmut_7(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "RED")]

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


def x_format_context_switch_lines__mutmut_8(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = None
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


def x_format_context_switch_lines__mutmut_9(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "XXConnection successfulXX" if switch_result.connected else "Connection failed"
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


def x_format_context_switch_lines__mutmut_10(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "connection successful" if switch_result.connected else "Connection failed"
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


def x_format_context_switch_lines__mutmut_11(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "CONNECTION SUCCESSFUL" if switch_result.connected else "Connection failed"
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


def x_format_context_switch_lines__mutmut_12(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "XXConnection failedXX"
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


def x_format_context_switch_lines__mutmut_13(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "connection failed"
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


def x_format_context_switch_lines__mutmut_14(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "CONNECTION FAILED"
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


def x_format_context_switch_lines__mutmut_15(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = None
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


def x_format_context_switch_lines__mutmut_16(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "XXgreenXX" if switch_result.connected else "yellow"
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


def x_format_context_switch_lines__mutmut_17(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "GREEN" if switch_result.connected else "yellow"
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


def x_format_context_switch_lines__mutmut_18(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "XXyellowXX"
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


def x_format_context_switch_lines__mutmut_19(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "YELLOW"
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


def x_format_context_switch_lines__mutmut_20(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "yellow"
    lines = None
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_21(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "yellow"
    lines = [
        ("XX\u2713 Context switchedXX", "green"),
        ("", "dim"),
        (f"Current context: {current_context.name}", "bold"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_22(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "yellow"
    lines = [
        ("\u2713 context switched", "green"),
        ("", "dim"),
        (f"Current context: {current_context.name}", "bold"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_23(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "yellow"
    lines = [
        ("\u2713 CONTEXT SWITCHED", "green"),
        ("", "dim"),
        (f"Current context: {current_context.name}", "bold"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_24(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "yellow"
    lines = [
        ("\u2713 Context switched", "XXgreenXX"),
        ("", "dim"),
        (f"Current context: {current_context.name}", "bold"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_25(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "yellow"
    lines = [
        ("\u2713 Context switched", "GREEN"),
        ("", "dim"),
        (f"Current context: {current_context.name}", "bold"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_26(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "yellow"
    lines = [
        ("\u2713 Context switched", "green"),
        ("XXXX", "dim"),
        (f"Current context: {current_context.name}", "bold"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_27(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "yellow"
    lines = [
        ("\u2713 Context switched", "green"),
        ("", "XXdimXX"),
        (f"Current context: {current_context.name}", "bold"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_28(
    switch_result: KubernetesContextSwitchResult,
) -> list[tuple[str, str]]:
    current_context = switch_result.current_context
    if current_context is None:
        return [("\u2717 Context switch failed", "red")]

    conn_result = "Connection successful" if switch_result.connected else "Connection failed"
    conn_style = "green" if switch_result.connected else "yellow"
    lines = [
        ("\u2713 Context switched", "green"),
        ("", "DIM"),
        (f"Current context: {current_context.name}", "bold"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_29(
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
        (f"Current context: {current_context.name}", "XXboldXX"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_30(
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
        (f"Current context: {current_context.name}", "BOLD"),
        (f"Namespace: {current_context.namespace}", "dim"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_31(
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
        (f"Namespace: {current_context.namespace}", "XXdimXX"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_32(
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
        (f"Namespace: {current_context.namespace}", "DIM"),
        (conn_result, conn_style),
    ]
    if switch_result.connection_error and not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_33(
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
    if switch_result.connection_error or not switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_34(
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
    if switch_result.connection_error and switch_result.connected:
        lines.append((switch_result.connection_error, "dim"))
    return lines


def x_format_context_switch_lines__mutmut_35(
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
        lines.append(None)
    return lines


def x_format_context_switch_lines__mutmut_36(
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
        lines.append((switch_result.connection_error, "XXdimXX"))
    return lines


def x_format_context_switch_lines__mutmut_37(
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
        lines.append((switch_result.connection_error, "DIM"))
    return lines

mutants_x_format_context_switch_lines__mutmut['_mutmut_orig'] = x_format_context_switch_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_1'] = x_format_context_switch_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_2'] = x_format_context_switch_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_3'] = x_format_context_switch_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_4'] = x_format_context_switch_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_5'] = x_format_context_switch_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_6'] = x_format_context_switch_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_7'] = x_format_context_switch_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_8'] = x_format_context_switch_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_9'] = x_format_context_switch_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_10'] = x_format_context_switch_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_11'] = x_format_context_switch_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_12'] = x_format_context_switch_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_13'] = x_format_context_switch_lines__mutmut_13 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_14'] = x_format_context_switch_lines__mutmut_14 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_15'] = x_format_context_switch_lines__mutmut_15 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_16'] = x_format_context_switch_lines__mutmut_16 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_17'] = x_format_context_switch_lines__mutmut_17 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_18'] = x_format_context_switch_lines__mutmut_18 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_19'] = x_format_context_switch_lines__mutmut_19 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_20'] = x_format_context_switch_lines__mutmut_20 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_21'] = x_format_context_switch_lines__mutmut_21 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_22'] = x_format_context_switch_lines__mutmut_22 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_23'] = x_format_context_switch_lines__mutmut_23 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_24'] = x_format_context_switch_lines__mutmut_24 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_25'] = x_format_context_switch_lines__mutmut_25 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_26'] = x_format_context_switch_lines__mutmut_26 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_27'] = x_format_context_switch_lines__mutmut_27 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_28'] = x_format_context_switch_lines__mutmut_28 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_29'] = x_format_context_switch_lines__mutmut_29 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_30'] = x_format_context_switch_lines__mutmut_30 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_31'] = x_format_context_switch_lines__mutmut_31 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_32'] = x_format_context_switch_lines__mutmut_32 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_33'] = x_format_context_switch_lines__mutmut_33 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_34'] = x_format_context_switch_lines__mutmut_34 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_35'] = x_format_context_switch_lines__mutmut_35 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_36'] = x_format_context_switch_lines__mutmut_36 # type: ignore # mutmut generated
mutants_x_format_context_switch_lines__mutmut['x_format_context_switch_lines__mutmut_37'] = x_format_context_switch_lines__mutmut_37 # type: ignore # mutmut generated
