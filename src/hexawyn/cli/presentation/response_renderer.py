from rich import box
from rich.table import Table

from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import ChatCliResponse
from hexawyn.cli.presentation.constants import _POD_STATUS_COLORS
from hexawyn.cli.widgets.markdown_log import MarkdownLog


def render_result(log: MarkdownLog, result: ChatCliResponse) -> None:
    log.write("")
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    if result.kind == "debug":
        _render_markdown_result(log, result)
        return
    render_lines(log, result.lines)


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


def render_lines(log: MarkdownLog, lines: list[tuple[str, str]]) -> None:
    parts = [f"[{style}]{text}[/{style}]" if text else "" for text, style in lines]
    log.write("\n".join(parts))
