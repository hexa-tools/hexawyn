from collections.abc import Callable, Mapping
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, Protocol

from rich import box
from rich.table import Table
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.events import Key
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, Input, RichLog, Static

from hexawyn.adapters.secondary.adapter_factory import build_adapters
from hexawyn.cli.command_router import CommandResult, route_command
from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext as KubernetesClusterContext,
)
from hexawyn.infrastructure.config.kubernetes_context import (
    KubernetesContextSwitchResult,
    KubernetesStartupStatus,
)


class ContextService(Protocol):
    def discover(self) -> list[KubernetesClusterContext]:
        """Return available Kubernetes contexts."""

    def switch_context(self, context_name: str) -> KubernetesContextSwitchResult:
        """Switch Hexawyn runtime context."""


_POD_STATUS_COLORS = {
    "Running": "green",
    "CrashLoop": "red",
    "Pending": "yellow",
    "Succeeded": "green",
}

# Big block-letter "hexawyn" banner (hexa in white, wyn in brand blue).
_LOGO_BANNER = [
    "[bold]█   █ █████ █   █   █  [/bold]  [bold #3B82F6]█   █ █   █ █   █[/bold #3B82F6]",
    "[bold]█   █ █      █ █   █ █ [/bold]  [bold #3B82F6]█   █ █   █ ██  █[/bold #3B82F6]",
    "[bold]█   █ █       █   █   █[/bold]  [bold #3B82F6]█   █  █ █  █ █ █[/bold #3B82F6]",
    "[bold]█████ ████    █   █████[/bold]  [bold #3B82F6]█ █ █   █   █  ██[/bold #3B82F6]",
    "[bold]█   █ █      █ █  █   █[/bold]  [bold #3B82F6]█ █ █   █   █   █[/bold #3B82F6]",
    "[bold]█   █ █     █   █ █   █[/bold]  [bold #3B82F6]██ ██   █   █   █[/bold #3B82F6]",
    "[bold]█   █ █████ █   █ █   █[/bold]  [bold #3B82F6]█   █   █   █   █[/bold #3B82F6]",
]


def _app_version() -> str:
    try:
        return version("hexawyn")
    except PackageNotFoundError:
        return "local"


def _compact_project_directory() -> str:
    current_directory = Path.cwd()
    home_directory = Path.home()
    try:
        relative_directory = current_directory.resolve().relative_to(home_directory.resolve())
    except ValueError:
        return str(current_directory)
    return f"~/{relative_directory.as_posix()}"


def _current_context_from(
    contexts: list[KubernetesClusterContext],
) -> KubernetesClusterContext | None:
    for context in contexts:
        if context.is_current:
            return context
    return None


def _context_list_lines(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    current_context = _current_context_from(contexts)
    current_context_name = current_context.name if current_context is not None else "unknown"
    lines = [(f"Current context: {current_context_name}", "bold"), ("", "dim")]
    lines.append(("Available contexts:", "bold"))
    for context in contexts:
        marker = "*" if context.is_current else " "
        lines.append((f"{marker} {context.name}", "green" if context.is_current else "dim"))
    return lines


def _missing_context_lines(contexts: list[KubernetesClusterContext]) -> list[tuple[str, str]]:
    lines = [("✗ Context not found", "red"), ("", "dim"), ("Available contexts:", "bold")]
    lines.extend((f"- {context.name}", "dim") for context in contexts)
    return lines


def _startup_status_from_switch(
    switch_result: KubernetesContextSwitchResult,
) -> KubernetesStartupStatus:
    return KubernetesStartupStatus(
        contexts=switch_result.contexts,
        current_context=switch_result.current_context,
        connected=switch_result.connected,
        kubeconfig_paths=switch_result.kubeconfig_paths,
        connection_error=switch_result.connection_error,
    )


class CommandInput(Input):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.history: list[str] = []
        self._history_pos = 0

    def remember(self, value: str) -> None:
        if value and (not self.history or self.history[-1] != value):
            self.history.append(value)
        self._history_pos = len(self.history)

    async def _on_key(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(self._history_pos + 1, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)


def _context_line(app: "HexawynTUI") -> str:
    ctx = app.adapter.get_cluster_context()
    namespace = ctx.get("namespace", "default")
    warnings = len(app.adapter.get_findings()) if hasattr(app.adapter, "get_findings") else 0
    warn_color = "yellow" if warnings else "green"
    warn_label = f"{warnings} warning" + ("s" if warnings != 1 else "")
    return (
        f"[dim]Context[/dim] [bold #3ddc84]{ctx.get('name', '')}[/bold #3ddc84] "
        f"[dim]·[/dim] [dim]namespace[/dim] [bold]{namespace}[/bold] "
        f"[dim]·[/dim] [{warn_color}]{warn_label}[/{warn_color}]"
    )


def _safe_findings(adapter: Any) -> list[Any]:
    if not hasattr(adapter, "get_findings"):
        return []
    try:
        findings = adapter.get_findings()
    except Exception:
        return []
    return list(findings)


def _safe_pods(adapter: Any) -> list[Mapping[object, object]]:
    if not hasattr(adapter, "list_pods"):
        return []
    try:
        pods = adapter.list_pods()
    except Exception:
        return []
    return [pod for pod in pods if isinstance(pod, Mapping)]


def _safe_metrics(adapter: Any) -> Mapping[object, object]:
    if not hasattr(adapter, "get_cluster_metrics"):
        return {}
    try:
        metrics = adapter.get_cluster_metrics()
    except Exception:
        return {}
    return metrics if isinstance(metrics, Mapping) else {}


def _safe_health_score(adapter: Any) -> int:
    if not hasattr(adapter, "get_health_score"):
        return 100
    try:
        score = adapter.get_health_score()
    except Exception:
        return 100
    return score if isinstance(score, int) else 100


def _safe_suggestions(adapter: Any) -> list[str]:
    if not hasattr(adapter, "get_suggestion_chips"):
        return []
    try:
        suggestions = adapter.get_suggestion_chips()
    except Exception:
        return []
    return [str(suggestion) for suggestion in suggestions][:3]


def _mapping_text(mapping: Mapping[object, object], key: str, default: str) -> str:
    value = mapping.get(key)
    return value if isinstance(value, str) else default


def _mapping_int(mapping: Mapping[object, object], key: str, default: int) -> int:
    value = mapping.get(key)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return default


def _running_pod_count(pods: list[Mapping[object, object]]) -> int:
    return sum(1 for pod in pods if _mapping_text(pod, "status", "") == "Running")


def _pending_pod_count(pods: list[Mapping[object, object]]) -> int:
    return sum(1 for pod in pods if _mapping_text(pod, "status", "") == "Pending")


def _failed_pod_count(pods: list[Mapping[object, object]]) -> int:
    failed_statuses = {"Failed", "Error", "CrashLoop", "CrashLoopBackOff"}
    return sum(1 for pod in pods if _mapping_text(pod, "status", "") in failed_statuses)


def _namespace_count(pods: list[Mapping[object, object]], fallback_namespace: str) -> int:
    namespaces = {
        _mapping_text(pod, "namespace", fallback_namespace)
        for pod in pods
        if _mapping_text(pod, "namespace", fallback_namespace)
    }
    return len(namespaces) if namespaces else 1


def _crashloop_finding_count(findings: list[Any]) -> int:
    return sum(1 for finding in findings if "CrashLoopBackOff" in str(finding))


def _restarting_finding_count(findings: list[Any]) -> int:
    return sum(1 for finding in findings if "restarted" in str(finding).lower())


def _issue_name(finding: Any) -> str:
    message = _finding_message(finding)
    if message.startswith("Pod "):
        resource = message.split()[1]
        return resource.split("/", maxsplit=1)[-1]
    return message.split(maxsplit=1)[0] if message else "unknown"


def _issue_reason(finding: Any) -> str:
    message = _finding_message(finding)
    if "CrashLoopBackOff" in message:
        return "CrashLoopBackOff"
    if "restarted" in message:
        return message.split(" restarted ", maxsplit=1)[-1].replace(" times", " restarts")
    return message


def _finding_message(finding: Any) -> str:
    if isinstance(finding, Mapping):
        message = finding.get("message")
        return message if isinstance(message, str) else ""
    return str(finding)


def _connection_line(startup_status: KubernetesStartupStatus | None) -> str:
    if startup_status is not None and not startup_status.connected:
        return "[yellow]⚠ Disconnected[/yellow]"
    return "[green]✓ Connected[/green]"


def _startup_lines(startup_status: KubernetesStartupStatus | None) -> list[str]:
    if startup_status is None or startup_status.current_context is None:
        return []

    current_context = startup_status.current_context
    connection_line = (
        "[green]✓[/green] Connected"
        if startup_status.connected
        else "[yellow]⚠[/yellow] Unable to connect"
    )
    return [
        "[green]✓[/green] Kubernetes detected",
        f"[dim]Detected {len(startup_status.contexts)} contexts[/dim]",
        f"[green]✓[/green] Current context: [bold]{current_context.name}[/bold]",
        f"[green]✓[/green] Namespace: [bold]{current_context.namespace}[/bold]",
        connection_line,
    ]


class WelcomeScreen(Screen[None]):
    CSS = """
    WelcomeScreen {
        align: center middle;
        background: #05070d;
    }

    #welcome-root {
        width: 82;
        height: auto;
        content-align: center middle;
    }

    #welcome-logo {
        width: 100%;
        content-align: center middle;
        color: #f2f4f8;
        text-style: bold;
        margin-bottom: 3;
    }

    #welcome-panel {
        width: 62;
        height: auto;
        background: #151515;
        border-left: thick #3B82F6;
        padding: 1 2;
        margin: 0 10;
    }

    #welcome-input {
        border: none;
        background: #151515;
        color: #d8dee9;
        height: 1;
        margin-bottom: 1;
    }

    #welcome-input:focus {
        border: none;
    }

    #welcome-mode {
        color: #8a93a6;
        height: 1;
    }

    #welcome-shortcuts {
        width: 100%;
        content-align: center middle;
        color: #8a93a6;
        margin-top: 1;
    }

    #welcome-tip {
        width: 100%;
        content-align: center middle;
        color: #8a93a6;
        margin-top: 4;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id="welcome-input",
                )
                yield Static(
                    "[bold #3B82F6]Build[/bold #3B82F6] · Hexawyn Kubernetes · "
                    "[bold #f5a623]high[/bold #f5a623]",
                    id="welcome-mode",
                )
            yield Static(
                "tab agents   ctrl+p commands",
                id="welcome-shortcuts",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",
                id="welcome-tip",
            )

    def on_mount(self) -> None:
        self.query_one("#welcome-input", CommandInput).focus()

    def action_clear_input(self) -> None:
        cmd_input = self.query_one("#welcome-input", CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return
        app = self.app
        assert isinstance(app, HexawynTUI)
        app.push_screen(SessionScreen(initial_command=text))


class ContextPickerScreen(ModalScreen[str | None]):
    CSS = """
    ContextPickerScreen {
        align: center middle;
        background: rgba(5, 7, 13, 0.72);
    }

    #context-picker {
        width: 58;
        height: auto;
        background: #0b0f17;
        border: round #3B82F6;
        padding: 1 2;
    }

    #context-picker-title {
        text-style: bold;
        color: #f2f4f8;
        margin-bottom: 1;
    }

    #context-picker-help {
        color: #8a93a6;
        margin-bottom: 1;
    }

    Button.context-option {
        width: 100%;
        background: #131826;
        color: #c7d0e0;
        border: round #2b3850;
        margin-bottom: 1;
    }

    Button.context-option:hover {
        border: round #3B82F6;
        color: #ffffff;
    }

    Button.current-context {
        color: #3ddc84;
    }

    #context-cancel {
        width: 100%;
        background: #0b0f17;
        color: #8a93a6;
        border: round #2b3850;
        margin-top: 1;
    }
    """

    BINDINGS = [
        Binding("up", "focus_previous_context", "Previous", show=False),
        Binding("down", "focus_next_context", "Next", show=False),
        Binding("escape", "cancel", "Cancel", show=False),
    ]

    def __init__(self, contexts: list[KubernetesClusterContext]) -> None:
        super().__init__()
        self._contexts = contexts
        self._focused_context_index = self._current_context_index()

    def compose(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="context-picker-help",
            )
            for context in self._contexts:
                current_marker = "✓ " if context.is_current else "  "
                classes = (
                    "context-option current-context" if context.is_current else "context-option"
                )
                yield Button(
                    f"{current_marker}{context.name}  ·  {context.namespace}",
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def on_mount(self) -> None:
        self._focus_context_button()

    def action_focus_next_context(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index + 1) % len(self._contexts)
        self._focus_context_button()

    def action_focus_previous_context(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index - 1) % len(self._contexts)
        self._focus_context_button()

    def action_cancel(self) -> None:
        self.dismiss(None)

    def _current_context_index(self) -> int:
        for context_index, context in enumerate(self._contexts):
            if context.is_current:
                return context_index
        return 0

    def _focus_context_button(self) -> None:
        if not self._contexts:
            self.query_one("#context-cancel", Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", Button).focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removeprefix("context-"))

    def action_clear_input(self) -> None:
        self.dismiss(None)


class SessionScreen(Screen[None]):
    CSS = """
    SessionScreen {
        layout: horizontal;
        background: #05070d;
    }

    #main-col {
        width: 1fr;
        height: 100%;
        padding: 1 2;
    }

    #conversation {
        height: 1fr;
        background: #05070d;
    }

    #chips {
        height: 3;
        margin-top: 1;
    }

    Button.chip {
        background: #131826;
        color: #c7d0e0;
        border: round #2b3850;
        min-width: 0;
        margin-right: 1;
    }

    Button.chip:hover {
        border: round #3B82F6;
        color: #ffffff;
    }

    #cmd-input {
        border: round #2b3850;
        margin-top: 1;
    }

    #cmd-input:focus {
        border: round #3B82F6;
    }

    #footer {
        height: 1;
        color: #5b6472;
        margin-top: 1;
    }

    #aside {
        width: 46;
        height: 100%;
        background: #0b0f17;
        border-left: solid #2b3850;
        padding: 1 2;
    }

    #aside-content {
        height: 1fr;
    }

    #aside Static {
        margin-bottom: 1;
    }

    #aside-project {
        color: #8a93a6;
        margin-bottom: 1;
    }

    #aside-brand {
        color: #c7d0e0;
        margin-bottom: 0;
    }

    .aside-heading {
        color: #5b6472;
        text-style: bold;
    }
    """

    def __init__(self, initial_command: str | None = None) -> None:
        super().__init__()
        self.initial_command = initial_command

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="main-col"):
                yield RichLog(id="conversation", wrap=True, markup=True)
                yield Horizontal(id="chips")
                yield CommandInput(placeholder="Describe what you want to do…", id="cmd-input")
                with Horizontal(id="footer"):
                    yield Static(
                        "[bold]Enter[/bold] send   [bold]↑↓[/bold] history   "
                        "[bold]Ctrl+C[/bold] cancel   [bold]Ctrl+Q[/bold] quit",
                        id="footer-hints",
                    )
            with Vertical(id="aside"):
                with VerticalScroll(id="aside-content"):
                    yield Static("", id="aside-body")
                yield Static(_compact_project_directory(), id="aside-project")
                yield Static(
                    f"hexa[bold #3B82F6]wyn[/bold #3B82F6] [dim]{_app_version()}[/dim]",
                    id="aside-brand",
                )

    async def on_mount(self) -> None:
        self.query_one("#cmd-input", CommandInput).focus()
        self._refresh_aside()

        app = self.app
        assert isinstance(app, HexawynTUI)
        log = self.query_one("#conversation", RichLog)
        log.write("\n".join(_LOGO_BANNER))
        log.write("")
        for startup_line in _startup_lines(app.startup_status):
            log.write(startup_line)
        if app.startup_status is not None:
            log.write("")
        log.write(_context_line(app))
        log.write("")

        if app.startup_result is not None:
            self._render_startup_result(log, app.startup_result)

        log.write('[dim]Try: "list pods", "debug payments-api", ' '"why is the pod pending?"[/dim]')

        if app.run_startup_scan:
            self.run_worker(self._run_startup_scan, thread=True)  # type: ignore[arg-type]

        if not app.expert_mode and hasattr(app.adapter, "get_suggestion_chips"):
            chips = list(app.adapter.get_suggestion_chips())[:4]
            if app.extra_chip:
                chips.append(app.extra_chip)
            chips = chips[:4]
            if chips:
                await self._update_chips(chips)

        if self.initial_command:
            await self._handle_command(self.initial_command)

    def _refresh_aside(self) -> None:
        app = self.app
        assert isinstance(app, HexawynTUI)
        self.query_one("#aside-body", Static).update("\n".join(self._aside_lines()))

    def _aside_lines(self) -> list[str]:
        app = self.app
        assert isinstance(app, HexawynTUI)
        ctx = app.adapter.get_cluster_context()
        pods = _safe_pods(app.adapter)
        metrics = _safe_metrics(app.adapter)
        findings = _safe_findings(app.adapter)
        suggestions = _safe_suggestions(app.adapter)

        cluster_name = str(ctx.get("name", "unknown"))
        namespace = str(ctx.get("namespace", "default"))
        pod_count = _mapping_int(metrics, "pod_count", len(pods))
        node_count = _mapping_int(metrics, "node_count", 0)

        lines = [
            "[bold]HEXAWYN[/bold]",
            "",
            _connection_line(app.startup_status),
            "",
            f"Cluster: [bold]{cluster_name}[/bold]",
            f"Namespaces: [bold]{_namespace_count(pods, namespace)}[/bold]",
            f"Nodes: [bold]{node_count}[/bold]",
            f"Pods: [bold]{pod_count}[/bold]",
        ]

        if app.startup_result is not None:
            health_score = app.startup_result.get("health_score", 100)
            if isinstance(health_score, int):
                if health_score >= 80:
                    score_color = "green"
                elif health_score >= 50:
                    score_color = "yellow"
                else:
                    score_color = "red"
                lines.append("")
                lines.append(
                    f"Health Score: [bold {score_color}]{health_score}/100[/bold {score_color}]"
                )
        else:
            lines.append("")
            lines.append(f"Health Score: [bold]{_safe_health_score(app.adapter)}/100[/bold]")

        lines.extend(
            [
                "",
                "[bold #5b6472]Findings:[/bold #5b6472]",
                "[dim]─────────────────────────────[/dim]",
                "",
                f"🟢 Running Pods      {_running_pod_count(pods)}",
                f"🟡 Pending Pods       {_pending_pod_count(pods)}",
                f"🔴 Failed Pods        {_failed_pod_count(pods)}",
                "",
            ]
        )
        lines.extend(self._finding_warning_lines(findings))
        lines.extend(self._suggestion_lines(app, suggestions))

        return lines

    def _finding_warning_lines(self, findings: list[Any]) -> list[str]:
        lines: list[str] = []
        crashloop_count = _crashloop_finding_count(findings)
        restarting_count = _restarting_finding_count(findings)
        if crashloop_count:
            lines.append(f"⚠ {crashloop_count} CrashLoopBackOff detected")
        if restarting_count:
            lines.append(f"⚠ {restarting_count} Pods restarting frequently")
        if not lines:
            lines.append("[green]No active warnings[/green]")
        return lines

    def _top_issue_lines(self, findings: list[Any]) -> list[str]:
        if not findings:
            return [
                "",
                "[dim]─────────────────────────────[/dim]",
                "",
                "[bold]Top Issues[/bold]",
                "No active issues",
            ]

        lines = ["", "[dim]─────────────────────────────[/dim]", "", "[bold]Top Issues[/bold]", ""]
        for issue_index, finding in enumerate(findings[:2], start=1):
            lines.append(f"{issue_index}. {_issue_name(finding)}")
            lines.append(f"   {_issue_reason(finding)}")
            lines.append("")
        return lines

    def _suggestion_lines(self, app: "HexawynTUI", suggestions: list[str]) -> list[str]:
        lines: list[str] = [
            "[dim]─────────────────────────────[/dim]",
            "",
            "[bold]Suggestions[/bold]",
            "",
        ]

        if app.startup_result is not None:
            startup_suggestions = app.startup_result.get("suggestions", [])
            if isinstance(startup_suggestions, list):
                for sug in startup_suggestions:
                    if isinstance(sug, dict):
                        label = str(sug.get("label", ""))
                        explanation = str(sug.get("explanation", ""))
                        severity = str(sug.get("severity", "info"))
                        sev_icon = (
                            "🔴"
                            if severity == "critical"
                            else "🟡"
                            if severity == "warning"
                            else "⚪"
                        )
                        if label and explanation:
                            lines.append(f"{sev_icon} {label}")
                            lines.append(f"   [dim]{explanation}[/dim]")
                        elif label:
                            lines.append(f"{sev_icon} {label}")

            narrative = str(app.startup_result.get("narrative_summary", ""))
            if narrative:
                lines.append("")
                lines.append(f"[dim italic]{narrative}[/dim italic]")

        if not lines or len(lines) <= 5:
            if not suggestions:
                lines.append("• list pods")
            else:
                lines.extend(f"• {s}" for s in suggestions[:4])

        return lines

    def action_clear_input(self) -> None:
        cmd_input = self.query_one("#cmd-input", CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    async def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id == "cmd-input" and event.value.strip():
            await self._clear_chips()

    async def _clear_chips(self) -> None:
        container = self.query_one("#chips", Horizontal)
        if container.children:
            await container.remove_children()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        input_widget = self.query_one("#cmd-input", CommandInput)
        if not text:
            return
        input_widget.remember(text)
        await self._handle_command(text)
        input_widget.value = ""

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id and event.button.id.startswith("chip-"):
            await self._handle_command(str(event.button.label))

    async def _handle_command(self, text: str) -> None:
        app = self.app
        assert isinstance(app, HexawynTUI)
        log = self.query_one("#conversation", RichLog)
        log.write(f"[bold #3B82F6]›[/bold #3B82F6] {text}")

        if text.strip() == "/setup":
            self._render_setup_info(log)
            return

        if self._is_context_command(text.strip()):
            await self._handle_context_command(text.strip(), log)
            return

        result = route_command(text, app.adapter)

        if app.expert_mode:
            log.write(f"[dim]{result!r}[/dim]")
            return

        self._render_result(log, result)
        if result.chips:
            await self._update_chips(result.chips)
        self._refresh_aside()

    def _is_context_command(self, text: str) -> bool:
        command_name = text.split(maxsplit=1)[0] if text else ""
        return command_name in {"/context", "/ctx"}

    def _render_setup_info(self, log: RichLog) -> None:
        from hexawyn.infrastructure.config.config_manager import get_llm_config

        cfg = get_llm_config()
        provider = cfg.get("provider", "Not configured")
        base_url = cfg.get("base_url", "N/A")
        has_key = bool(cfg.get("api_key"))

        log.write("[bold]LLM Configuration[/bold]")
        log.write("")
        log.write(f"Provider: [bold]{provider}[/bold]")
        log.write(f"Base URL: [dim]{base_url}[/dim]")
        log.write(
            f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}"
        )
        log.write("")

        if not has_key:
            log.write(
                "[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]"
            )
        else:
            log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")

    async def _handle_context_command(self, text: str, log: RichLog) -> None:
        app = self.app
        assert isinstance(app, HexawynTUI)
        if app.context_service is None:
            self._render_lines(log, [("Kubernetes context switching is unavailable.", "yellow")])
            return

        context_name = self._requested_context_name(text)
        if context_name is None:
            await self._open_context_picker()
            return

        self._switch_context(context_name)

    def _switch_context(self, context_name: str | None) -> None:
        if context_name is None:
            return

        app = self.app
        assert isinstance(app, HexawynTUI)
        log = self.query_one("#conversation", RichLog)
        if app.context_service is None:
            self._render_lines(log, [("Kubernetes context switching is unavailable.", "yellow")])
            return

        switch_result = app.context_service.switch_context(context_name)
        if not switch_result.switched or switch_result.current_context is None:
            self._render_lines(log, _missing_context_lines(switch_result.contexts))
            return

        app.startup_status = _startup_status_from_switch(switch_result)
        app.adapter = app.adapter_builder(switch_result.current_context.name)
        self._refresh_aside()
        self._render_lines(log, self._context_switch_lines(switch_result))

    async def _open_context_picker(self) -> None:
        app = self.app
        assert isinstance(app, HexawynTUI)
        app.push_screen(
            ContextPickerScreen(self._available_contexts()),
            callback=self._switch_context,
        )

    def _requested_context_name(self, text: str) -> str | None:
        parts = text.split(maxsplit=1)
        if len(parts) == 1:
            return None
        requested_context_name = parts[1].strip()
        return requested_context_name if requested_context_name else None

    def _available_contexts(self) -> list[KubernetesClusterContext]:
        app = self.app
        assert isinstance(app, HexawynTUI)
        if app.context_service is not None:
            return app.context_service.discover()
        if app.startup_status is not None:
            return app.startup_status.contexts
        return []

    def _context_switch_lines(
        self,
        switch_result: KubernetesContextSwitchResult,
    ) -> list[tuple[str, str]]:
        current_context = switch_result.current_context
        if current_context is None:
            return [("✗ Context switch failed", "red")]

        connection_line = (
            "Connection successful" if switch_result.connected else "Connection failed"
        )
        connection_style = "green" if switch_result.connected else "yellow"
        lines = [
            ("✓ Context switched", "green"),
            ("", "dim"),
            (f"Current context: {current_context.name}", "bold"),
            (f"Namespace: {current_context.namespace}", "dim"),
            (connection_line, connection_style),
        ]
        if switch_result.connection_error and not switch_result.connected:
            lines.append((switch_result.connection_error, "dim"))
        return lines

    def _render_lines(self, log: RichLog, lines: list[tuple[str, str]]) -> None:
        for text, style in lines:
            if text:
                log.write(f"[{style}]{text}[/{style}]")
            else:
                log.write("")

    def _render_result(self, log: RichLog, result: CommandResult) -> None:
        if result.kind == "pods" and result.pods is not None:
            table = Table(show_header=True, header_style="bold #8a93a6", box=box.SIMPLE)
            table.add_column("NAME")
            table.add_column("NAMESPACE")
            table.add_column("STATUS")
            table.add_column("RESTARTS", justify="right")
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
            return

        self._render_lines(log, result.lines)

    async def _update_chips(self, chips: list[str]) -> None:
        container = self.query_one("#chips", Horizontal)
        await container.remove_children()
        for i, chip in enumerate(chips[:4]):
            await container.mount(Button(chip, id=f"chip-{i}", classes="chip"))

    async def _run_startup_scan(self) -> None:
        from dataclasses import asdict

        from hexawyn.application.service.runtime_adapter import get_runtime

        app = self.app
        assert isinstance(app, HexawynTUI)
        log = self.query_one("#conversation", RichLog)

        try:
            runtime = get_runtime()
            result = runtime.run_startup_scan(cluster_name=app.cluster_name)
        except Exception as exc:
            self.app.call_from_thread(log.write, f"[yellow]Startup scan failed: {exc}[/yellow]")
            return

        accumulated: dict[str, object] = dict(asdict(result))
        app.startup_result = accumulated

        def _update_ui() -> None:
            self._render_startup_result(log, accumulated)
            self._refresh_aside()

        self.app.call_from_thread(_update_ui)

    def _render_startup_result(self, log: RichLog, startup_result: dict[str, object]) -> None:
        log.write("[bold #3B82F6]── Startup Scan Results ──[/bold #3B82F6]")
        log.write("")

        health_score = startup_result.get("health_score", 100)
        if isinstance(health_score, int):
            if health_score >= 80:
                color = "green"
            elif health_score >= 50:
                color = "yellow"
            else:
                color = "red"
            log.write(f"  [bold]Health Score:[/bold] [{color}]{health_score}/100[/{color}]")

        narrative = str(startup_result.get("narrative_summary", ""))
        if narrative:
            log.write(f"  [dim]{narrative}[/dim]")

        top_issues = startup_result.get("top_issues", [])
        if isinstance(top_issues, list) and top_issues:
            log.write("")
            log.write("  [bold]Top Issues:[/bold]")
            for issue in top_issues:
                log.write(f"    [yellow]•[/yellow] {issue}")

        suggestions = startup_result.get("suggestions", [])
        if isinstance(suggestions, list) and suggestions:
            log.write("")
            log.write("  [bold]Suggestions:[/bold]")
            for sug in suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_color = (
                        "red"
                        if severity == "critical"
                        else "yellow"
                        if severity == "warning"
                        else "dim"
                    )
                    if label and explanation:
                        log.write(f"    [{sev_color}]→[/{sev_color}] {label}")
                        log.write(f"      [dim]{explanation}[/dim]")
                    elif label:
                        log.write(f"    [{sev_color}]→[/{sev_color}] {label}")

        degraded = startup_result.get("degraded", False)
        if degraded:
            log.write("")
            error_msg = str(startup_result.get("error", "Unknown"))
            log.write(f"  [bold yellow]⚠ DEGRADED[/bold yellow] [dim]({error_msg})[/dim]")

        log.write("")


class ProviderSetupScreen(ModalScreen[None]):
    """First-run screen: choose LLM provider and enter API key."""

    CSS = """
    ProviderSetupScreen {
        align: center middle;
        background: rgba(5, 7, 13, 0.72);
    }

    #setup-box {
        width: 58;
        height: auto;
        background: #0b0f17;
        border: round #3B82F6;
        padding: 1 2;
    }

    #setup-title {
        text-style: bold;
        color: #f2f4f8;
        margin-bottom: 1;
    }

    #setup-label {
        color: #8a93a6;
        margin-bottom: 1;
    }

    #setup-providers {
        height: 12;
        margin-bottom: 1;
    }

    Button.provider-btn {
        width: 100%;
        background: #0b0f17;
        color: #c7d0e0;
        border: none;
        margin-bottom: 0;
        padding: 0 1;
        text-align: left;
    }

    Button.provider-btn:hover {
        color: #ffffff;
    }

    #setup-key {
        margin-bottom: 1;
    }

    #setup-status {
        height: 1;
        margin-bottom: 1;
    }

    #setup-actions {
        width: 100%;
    }

    #setup-save {
        width: 100%;
        background: #0b0f17;
        color: #3ddc84;
        border: round #3B82F6;
        margin-bottom: 1;
    }

    #setup-skip {
        width: 100%;
        background: #0b0f17;
        color: #8a93a6;
        border: round #2b3850;
    }
    """

    PROVIDERS = [
        ("1", "DeepSeek", "https://api.deepseek.com"),
        ("2", "OpenAI", "https://api.openai.com/v1"),
        ("3", "Groq", "https://api.groq.com/openai/v1"),
        ("4", "Together AI", "https://api.together.xyz/v1"),
        ("5", "Mistral", "https://api.mistral.ai/v1"),
        ("6", "Google (Gemini)", "https://generativelanguage.googleapis.com/v1beta/openai"),
        ("7", "OpenRouter", "https://openrouter.ai/api/v1"),
        ("8", "xAI (Grok)", "https://api.x.ai/v1"),
        ("0", "Custom", ""),
    ]

    BINDINGS = [
        Binding("escape", "skip", "Skip", show=False),
    ]

    def compose(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def on_mount(self) -> None:
        self._selected_provider = ""
        self._selected_url = ""

    def action_skip(self) -> None:
        self.dismiss()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("provider-"):
            key = event.button.id.replace("provider-", "")
            for pk, name, url in self.PROVIDERS:
                if pk == key:
                    self._selected_provider = name
                    self._selected_url = url
                    self._highlight_provider(key)

                    key_input: Input = self.query_one("#setup-key", Input)
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def _highlight_provider(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", Button)
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "default"

    def _save_and_continue(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "Custom" and not self._selected_url:
            self._selected_url = api_key
            if not self._selected_url.startswith("http"):
                self.query_one("#setup-status", Static).update(
                    "[red]Custom provider: paste the base URL first, then the API key.[/red]"
                )
                return
            self.query_one("#setup-key", Input).value = ""
            self.query_one("#setup-key", Input).placeholder = "Paste your API key..."
            self._selected_provider = "Custom"
            return

        if not api_key:
            self.query_one("#setup-status", Static).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()


class HexawynTUI(App[None]):
    CSS = """
    Header {
        display: none;
    }

    Screen {
        background: #05070d;
    }
    """

    BINDINGS = [
        Binding("ctrl+c", "clear_input", "Cancel", show=False),
        Binding("ctrl+q", "quit", "Quit", show=False),
    ]

    def __init__(
        self,
        adapter: Any,
        expert_mode: bool = False,
        demo_mode: bool = False,
        scenario: str = "aws_eks",
        extra_chip: str | None = None,
        startup_status: KubernetesStartupStatus | None = None,
        context_service: ContextService | None = None,
        adapter_builder: Callable[[str], Any] = build_adapters,
        run_startup_scan: bool = False,
        cluster_name: str = "unknown",
        needs_setup: bool = False,
    ) -> None:
        super().__init__()
        self.adapter = adapter
        self.expert_mode = expert_mode
        self.demo_mode = demo_mode
        self.scenario = scenario
        self.extra_chip = extra_chip
        self.startup_status = startup_status
        self.context_service = context_service
        self.adapter_builder = adapter_builder
        self.run_startup_scan = run_startup_scan
        self.cluster_name = cluster_name
        self.startup_result: dict[str, object] | None = None
        self.needs_setup = needs_setup

    def on_mount(self) -> None:
        if self.needs_setup:
            self.push_screen(SessionScreen())
            self.push_screen(ProviderSetupScreen())
        else:
            self.push_screen(SessionScreen())

    def action_clear_input(self) -> None:
        if isinstance(self.screen, WelcomeScreen | SessionScreen):
            self.screen.action_clear_input()
