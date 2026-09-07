from rich import box
from rich.table import Table

from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import ChatCliResponse
from hexawyn.cli.presentation.constants import _POD_STATUS_COLORS
from hexawyn.cli.widgets.markdown_log import MarkdownLog


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_render_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_render_result__mutmut)
def render_result(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_orig(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_1(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write(None)
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_2(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("XXXX")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_3(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" or result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_4(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind != "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_5(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "XXpodsXX" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_6(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "PODS" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_7(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_8(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(None, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_9(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, None)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_10(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_11(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, )
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_12(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind != "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_13(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "XXdebugXX":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_14(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "DEBUG":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_15(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(None, result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_16(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, None)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_17(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(result)
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_18(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, )
        return
    render_lines(log, result.lines)


def x_render_result__mutmut_19(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(None, result.lines)


def x_render_result__mutmut_20(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, None)


def x_render_result__mutmut_21(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(result.lines)


def x_render_result__mutmut_22(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, )

mutants_x_render_result__mutmut['_mutmut_orig'] = x_render_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_1'] = x_render_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_2'] = x_render_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_3'] = x_render_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_4'] = x_render_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_5'] = x_render_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_6'] = x_render_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_7'] = x_render_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_8'] = x_render_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_9'] = x_render_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_10'] = x_render_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_11'] = x_render_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_12'] = x_render_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_13'] = x_render_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_14'] = x_render_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_15'] = x_render_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_16'] = x_render_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_17'] = x_render_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_18'] = x_render_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_19'] = x_render_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_20'] = x_render_result__mutmut_20 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_21'] = x_render_result__mutmut_21 # type: ignore # mutmut generated
mutants_x_render_result__mutmut['x_render_result__mutmut_22'] = x_render_result__mutmut_22 # type: ignore # mutmut generated
mutants_x__render_markdown_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_markdown_result__mutmut)
def _render_markdown_result(log: MarkdownLog, result: ChatCliResponse) -> None:
    """Render a debug result as markdown (the LLM answer is markdown)."""
    for text, _style in result.lines:
        if text:
            log.write(text)
    if result.suggestions:
        log.write("")
        log.write("**Suggestions:**")
        for suggestion in result.suggestions:
            log.write(f"- {suggestion}")


def x__render_markdown_result__mutmut_orig(log: MarkdownLog, result: ChatCliResponse) -> None:
    """Render a debug result as markdown (the LLM answer is markdown)."""
    for text, _style in result.lines:
        if text:
            log.write(text)
    if result.suggestions:
        log.write("")
        log.write("**Suggestions:**")
        for suggestion in result.suggestions:
            log.write(f"- {suggestion}")


def x__render_markdown_result__mutmut_1(log: MarkdownLog, result: ChatCliResponse) -> None:
    """Render a debug result as markdown (the LLM answer is markdown)."""
    for text, _style in result.lines:
        if text:
            log.write(None)
    if result.suggestions:
        log.write("")
        log.write("**Suggestions:**")
        for suggestion in result.suggestions:
            log.write(f"- {suggestion}")


def x__render_markdown_result__mutmut_2(log: MarkdownLog, result: ChatCliResponse) -> None:
    """Render a debug result as markdown (the LLM answer is markdown)."""
    for text, _style in result.lines:
        if text:
            log.write(text)
    if result.suggestions:
        log.write(None)
        log.write("**Suggestions:**")
        for suggestion in result.suggestions:
            log.write(f"- {suggestion}")


def x__render_markdown_result__mutmut_3(log: MarkdownLog, result: ChatCliResponse) -> None:
    """Render a debug result as markdown (the LLM answer is markdown)."""
    for text, _style in result.lines:
        if text:
            log.write(text)
    if result.suggestions:
        log.write("XXXX")
        log.write("**Suggestions:**")
        for suggestion in result.suggestions:
            log.write(f"- {suggestion}")


def x__render_markdown_result__mutmut_4(log: MarkdownLog, result: ChatCliResponse) -> None:
    """Render a debug result as markdown (the LLM answer is markdown)."""
    for text, _style in result.lines:
        if text:
            log.write(text)
    if result.suggestions:
        log.write("")
        log.write(None)
        for suggestion in result.suggestions:
            log.write(f"- {suggestion}")


def x__render_markdown_result__mutmut_5(log: MarkdownLog, result: ChatCliResponse) -> None:
    """Render a debug result as markdown (the LLM answer is markdown)."""
    for text, _style in result.lines:
        if text:
            log.write(text)
    if result.suggestions:
        log.write("")
        log.write("XX**Suggestions:**XX")
        for suggestion in result.suggestions:
            log.write(f"- {suggestion}")


def x__render_markdown_result__mutmut_6(log: MarkdownLog, result: ChatCliResponse) -> None:
    """Render a debug result as markdown (the LLM answer is markdown)."""
    for text, _style in result.lines:
        if text:
            log.write(text)
    if result.suggestions:
        log.write("")
        log.write("**suggestions:**")
        for suggestion in result.suggestions:
            log.write(f"- {suggestion}")


def x__render_markdown_result__mutmut_7(log: MarkdownLog, result: ChatCliResponse) -> None:
    """Render a debug result as markdown (the LLM answer is markdown)."""
    for text, _style in result.lines:
        if text:
            log.write(text)
    if result.suggestions:
        log.write("")
        log.write("**SUGGESTIONS:**")
        for suggestion in result.suggestions:
            log.write(f"- {suggestion}")


def x__render_markdown_result__mutmut_8(log: MarkdownLog, result: ChatCliResponse) -> None:
    """Render a debug result as markdown (the LLM answer is markdown)."""
    for text, _style in result.lines:
        if text:
            log.write(text)
    if result.suggestions:
        log.write("")
        log.write("**Suggestions:**")
        for suggestion in result.suggestions:
            log.write(None)

mutants_x__render_markdown_result__mutmut['_mutmut_orig'] = x__render_markdown_result__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_markdown_result__mutmut['x__render_markdown_result__mutmut_1'] = x__render_markdown_result__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_markdown_result__mutmut['x__render_markdown_result__mutmut_2'] = x__render_markdown_result__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_markdown_result__mutmut['x__render_markdown_result__mutmut_3'] = x__render_markdown_result__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_markdown_result__mutmut['x__render_markdown_result__mutmut_4'] = x__render_markdown_result__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_markdown_result__mutmut['x__render_markdown_result__mutmut_5'] = x__render_markdown_result__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_markdown_result__mutmut['x__render_markdown_result__mutmut_6'] = x__render_markdown_result__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_markdown_result__mutmut['x__render_markdown_result__mutmut_7'] = x__render_markdown_result__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_markdown_result__mutmut['x__render_markdown_result__mutmut_8'] = x__render_markdown_result__mutmut_8 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_pod_table__mutmut)
def _render_pod_table(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_orig(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_1(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = None
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_2(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=None, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_3(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style=None, box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_4(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=None)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_5(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_6(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_7(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", )
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_8(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=False, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_9(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="XXbold #8a93a6XX", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_10(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="BOLD #8A93A6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_11(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column(None)
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_12(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("XXNAMEXX")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_13(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("name")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_14(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column(None)
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_15(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("XXNAMESPACEXX")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_16(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("namespace")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_17(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column(None)
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_18(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("XXSTATUSXX")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_19(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("status")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_20(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column(None, justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_21(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify=None)
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_22(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column(justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_23(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", )
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_24(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("XXRESTARTSXX", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_25(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("restarts", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_26(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="XXrightXX")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_27(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="RIGHT")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_28(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_29(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = None
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_30(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(None, "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_31(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), None)
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_32(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get("white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_33(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), )
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_34(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(None), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_35(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["XXstatusXX"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_36(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["STATUS"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_37(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "XXwhiteXX")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_38(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "WHITE")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_39(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            None,
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_40(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            None,
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_41(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            None,
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_42(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            None,
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_43(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_44(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_45(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_46(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_47(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(None),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_48(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["XXnameXX"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_49(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["NAME"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_50(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(None),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_51(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["XXnamespaceXX"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_52(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["NAMESPACE"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_53(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['XXstatusXX']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_54(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['STATUS']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_55(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(None),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_56(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["XXrestartsXX"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_57(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["RESTARTS"]),
        )
    log.write(table)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_58(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(None)
    if result.summary:
        log.write(f"[dim]{result.summary}[/dim]")


def x__render_pod_table__mutmut_59(log: MarkdownLog, result: ChatCliResponse) -> None:
    table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
    table.add_column("NAME")
    table.add_column("NAMESPACE")
    table.add_column("STATUS")
    table.add_column("RESTARTS", justify="right")
    assert result.pods is not None
    for pod in result.pods:
        color = _POD_STATUS_COLORS.get(str(pod["status"]), "white")
        table.add_row(
            str(pod["name"]),
            str(pod["namespace"]),
            f"[{color}]{pod['status']}[/{color}]",
            str(pod["restarts"]),
        )
    log.write(table)
    if result.summary:
        log.write(None)

mutants_x__render_pod_table__mutmut['_mutmut_orig'] = x__render_pod_table__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_1'] = x__render_pod_table__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_2'] = x__render_pod_table__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_3'] = x__render_pod_table__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_4'] = x__render_pod_table__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_5'] = x__render_pod_table__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_6'] = x__render_pod_table__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_7'] = x__render_pod_table__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_8'] = x__render_pod_table__mutmut_8 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_9'] = x__render_pod_table__mutmut_9 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_10'] = x__render_pod_table__mutmut_10 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_11'] = x__render_pod_table__mutmut_11 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_12'] = x__render_pod_table__mutmut_12 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_13'] = x__render_pod_table__mutmut_13 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_14'] = x__render_pod_table__mutmut_14 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_15'] = x__render_pod_table__mutmut_15 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_16'] = x__render_pod_table__mutmut_16 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_17'] = x__render_pod_table__mutmut_17 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_18'] = x__render_pod_table__mutmut_18 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_19'] = x__render_pod_table__mutmut_19 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_20'] = x__render_pod_table__mutmut_20 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_21'] = x__render_pod_table__mutmut_21 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_22'] = x__render_pod_table__mutmut_22 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_23'] = x__render_pod_table__mutmut_23 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_24'] = x__render_pod_table__mutmut_24 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_25'] = x__render_pod_table__mutmut_25 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_26'] = x__render_pod_table__mutmut_26 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_27'] = x__render_pod_table__mutmut_27 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_28'] = x__render_pod_table__mutmut_28 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_29'] = x__render_pod_table__mutmut_29 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_30'] = x__render_pod_table__mutmut_30 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_31'] = x__render_pod_table__mutmut_31 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_32'] = x__render_pod_table__mutmut_32 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_33'] = x__render_pod_table__mutmut_33 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_34'] = x__render_pod_table__mutmut_34 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_35'] = x__render_pod_table__mutmut_35 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_36'] = x__render_pod_table__mutmut_36 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_37'] = x__render_pod_table__mutmut_37 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_38'] = x__render_pod_table__mutmut_38 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_39'] = x__render_pod_table__mutmut_39 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_40'] = x__render_pod_table__mutmut_40 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_41'] = x__render_pod_table__mutmut_41 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_42'] = x__render_pod_table__mutmut_42 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_43'] = x__render_pod_table__mutmut_43 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_44'] = x__render_pod_table__mutmut_44 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_45'] = x__render_pod_table__mutmut_45 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_46'] = x__render_pod_table__mutmut_46 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_47'] = x__render_pod_table__mutmut_47 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_48'] = x__render_pod_table__mutmut_48 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_49'] = x__render_pod_table__mutmut_49 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_50'] = x__render_pod_table__mutmut_50 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_51'] = x__render_pod_table__mutmut_51 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_52'] = x__render_pod_table__mutmut_52 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_53'] = x__render_pod_table__mutmut_53 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_54'] = x__render_pod_table__mutmut_54 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_55'] = x__render_pod_table__mutmut_55 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_56'] = x__render_pod_table__mutmut_56 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_57'] = x__render_pod_table__mutmut_57 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_58'] = x__render_pod_table__mutmut_58 # type: ignore # mutmut generated
mutants_x__render_pod_table__mutmut['x__render_pod_table__mutmut_59'] = x__render_pod_table__mutmut_59 # type: ignore # mutmut generated
mutants_x_render_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_render_lines__mutmut)
def render_lines(log: MarkdownLog, lines: list[tuple[str, str]]) -> None:
    parts = [f"[{style}]{text}[/{style}]" if text else "" for text, style in lines]
    log.write("\n".join(parts))


def x_render_lines__mutmut_orig(log: MarkdownLog, lines: list[tuple[str, str]]) -> None:
    parts = [f"[{style}]{text}[/{style}]" if text else "" for text, style in lines]
    log.write("\n".join(parts))


def x_render_lines__mutmut_1(log: MarkdownLog, lines: list[tuple[str, str]]) -> None:
    parts = None
    log.write("\n".join(parts))


def x_render_lines__mutmut_2(log: MarkdownLog, lines: list[tuple[str, str]]) -> None:
    parts = [f"[{style}]{text}[/{style}]" if text else "XXXX" for text, style in lines]
    log.write("\n".join(parts))


def x_render_lines__mutmut_3(log: MarkdownLog, lines: list[tuple[str, str]]) -> None:
    parts = [f"[{style}]{text}[/{style}]" if text else "" for text, style in lines]
    log.write(None)


def x_render_lines__mutmut_4(log: MarkdownLog, lines: list[tuple[str, str]]) -> None:
    parts = [f"[{style}]{text}[/{style}]" if text else "" for text, style in lines]
    log.write("\n".join(None))


def x_render_lines__mutmut_5(log: MarkdownLog, lines: list[tuple[str, str]]) -> None:
    parts = [f"[{style}]{text}[/{style}]" if text else "" for text, style in lines]
    log.write("XX\nXX".join(parts))

mutants_x_render_lines__mutmut['_mutmut_orig'] = x_render_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x_render_lines__mutmut['x_render_lines__mutmut_1'] = x_render_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x_render_lines__mutmut['x_render_lines__mutmut_2'] = x_render_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x_render_lines__mutmut['x_render_lines__mutmut_3'] = x_render_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x_render_lines__mutmut['x_render_lines__mutmut_4'] = x_render_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x_render_lines__mutmut['x_render_lines__mutmut_5'] = x_render_lines__mutmut_5 # type: ignore # mutmut generated
