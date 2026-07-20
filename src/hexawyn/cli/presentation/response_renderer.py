from rich import box
from rich.table import Table
from textual.widgets import RichLog

from hexawyn.application.use_case.chat_cli.chat_cli_response import ChatCliResponse
from hexawyn.cli.presentation.constants import _POD_STATUS_COLORS


def render_result(log: RichLog, result: ChatCliResponse) -> None:
    if result.kind == "pods" and result.pods is not None:
        _render_pod_table(log, result)
        return
    render_lines(log, result.lines)


def _render_pod_table(log: RichLog, result: ChatCliResponse) -> None:
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


def render_lines(log: RichLog, lines: list[tuple[str, str]]) -> None:
    for text, style in lines:
        if text:
            log.write(f"[{style}]{text}[/{style}]")
        else:
            log.write("")
