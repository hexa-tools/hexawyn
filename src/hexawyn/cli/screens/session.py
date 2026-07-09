import asyncio
from dataclasses import asdict as _asdict
from typing import Any

from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Input, RichLog, Static

from hexawyn.application.use_case.chat_cli.chat_cli_response import ChatCliResponse
from hexawyn.cli.command_router import route_command
from hexawyn.cli.presentation.asides import (
    crashloop_finding_count,
    failed_pod_count,
    kubectl_current_context,
    mapping_int,
    namespace_count,
    pending_pod_count,
    restarting_finding_count,
    running_pod_count,
    safe_findings,
    safe_health_score,
    safe_metrics,
    safe_pods,
    safe_suggestions,
)
from hexawyn.cli.presentation.constants import _LOGO_BANNER, _POD_STATUS_COLORS
from hexawyn.cli.presentation.formatting import (
    app_version,
    compact_project_directory,
    connection_line,
    context_line,
    missing_context_lines,
    startup_lines,
    startup_status_from_switch,
)
from hexawyn.cli.screens.context_picker import ContextPickerScreen
from hexawyn.cli.widgets.command_input import CommandInput
from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext as KubernetesClusterContext,
)
from hexawyn.infrastructure.config.kubernetes_context import (
    KubernetesContextSwitchResult,
)


class SessionScreen(Screen[None]):
    CSS = """
    SessionScreen {
        layout: horizontal;
        background: #05070d;
    }

    #main-col {
        width: 1fr;
        height: 100%;
        padding: 0 2 1 2;
    }

    #conversation {
        height: 1fr;
        background: #05070d;
        scrollbar-size: 0 0;
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
        self._history: list[dict[str, str]] = []

    def _tui_app(self) -> Any:
        from hexawyn.cli.tui import HexawynTUI

        app = self.app
        assert isinstance(app, HexawynTUI)
        return app

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="main-col"):
                yield RichLog(id="conversation", wrap=True, markup=True)
                yield Static("", id="status-bar")
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
                yield Static(compact_project_directory(), id="aside-project")
                yield Static(
                    f"hexa[bold #3B82F6]wyn[/bold #3B82F6] [dim]{app_version()}[/dim]",
                    id="aside-brand",
                )

    async def on_mount(self) -> None:
        self.query_one("#cmd-input", CommandInput).focus()
        self._refresh_aside()

        app = self._tui_app()
        log = self.query_one("#conversation", RichLog)
        log.write("\n".join(line.format(version=app_version()) for line in _LOGO_BANNER))
        log.write("")
        for startup_line in startup_lines(app.startup_status):
            log.write(startup_line)
        if app.startup_status is not None:
            log.write("")
        log.write(context_line(app.adapter))

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
        self.query_one("#aside-body", Static).update("\n".join(self._aside_lines()))

    def _aside_lines(self) -> list[str]:
        app = self._tui_app()
        ctx = app.adapter.get_cluster_context()
        pods = safe_pods(app.adapter)
        metrics = safe_metrics(app.adapter)
        findings = safe_findings(app.adapter)
        suggestions = safe_suggestions(app.adapter)

        cluster_name = str(ctx.get("name", "unknown"))
        namespace = str(ctx.get("namespace", "default"))
        pod_count = mapping_int(metrics, "pod_count", len(pods))
        node_count = mapping_int(metrics, "node_count", 0)
        kubectl_ctx = kubectl_current_context()

        lines = [
            "[bold]HEXAWYN[/bold]",
            "",
            connection_line(app.startup_status),
            "",
            f"Cluster: [bold]{cluster_name}[/bold]",
            f"Context: [dim]{kubectl_ctx}[/dim]",
            f"Namespaces: [bold]{namespace_count(pods, namespace)}[/bold]",
            f"Nodes: [bold]{node_count}[/bold]",
            f"Pods: [bold]{pod_count}[/bold]",
        ]

        if app.startup_result is not None:
            health_score = app.startup_result.get("health_score", 100)
            if isinstance(health_score, int) and health_score > 0:
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
                adapter_score = safe_health_score(app.adapter)
                lines.append(f"Health Score: [bold]{adapter_score}/100[/bold]")
        else:
            lines.append("")
            lines.append(f"Health Score: [bold]{safe_health_score(app.adapter)}/100[/bold]")

        lines.extend(
            [
                "",
                f"🟢 Running Pods      {running_pod_count(pods)}",
                f"🟡 Pending Pods       {pending_pod_count(pods)}",
                f"🔴 Failed Pods        {failed_pod_count(pods)}",
                "",
            ]
        )
        lines.extend(self._finding_warning_lines(findings))
        lines.extend(self._suggestion_lines(app, suggestions))

        return lines

    def _finding_warning_lines(self, findings: list[Any]) -> list[str]:
        lines: list[str] = []
        cl_count = crashloop_finding_count(findings)
        r_count = restarting_finding_count(findings)
        if cl_count:
            lines.append(f"⚠ {cl_count} CrashLoopBackOff detected")
        if r_count:
            lines.append(f"⚠ {r_count} pods with high restart count")
        if not lines:
            lines.append("[green]No active warnings[/green]")
        return lines

    def _suggestion_lines(self, app: Any, suggestions: list[str]) -> list[str]:
        lines: list[str] = [
            "[dim]─────────────────────────────[/dim]",
            "",
            "[bold]Suggestions[/bold]",
            "",
        ]

        if app.ai_suggestion:
            lines.append(f"[bold #3B82F6]💡 {app.ai_suggestion}[/bold #3B82F6]")
            lines.append("")

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
            if suggestions:
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
        if not text:
            return
        cmd_input = event.input
        if hasattr(cmd_input, "remember"):
            cmd_input.remember(text)
        cmd_input.action_delete_left_all()
        asyncio.create_task(self._handle_command(text))

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id and event.button.id.startswith("chip-"):
            await self._handle_command(str(event.button.label))

    async def _show_spinner(self, log: RichLog, stages: list[str]) -> None:
        icons = ["🎯", "📡", "🔍", "📝"]
        status = self.query_one("#status-bar", Static)
        try:
            for i, stage in enumerate(stages):
                icon = icons[i] if i < len(icons) else "⏳"
                status.update(f"[dim #5b6472]  {icon} {stage}...[/dim #5b6472]")
                await asyncio.sleep(0.3)
                if i < len(stages) - 1:
                    status.update(f"[dim #3B82F6]  ✓ {stage}[/dim #3B82F6]")
                    await asyncio.sleep(0.3)
        except asyncio.CancelledError:
            pass
        finally:
            status.update("")

    async def _handle_command(self, text: str) -> None:
        app = self._tui_app()
        log = self.query_one("#conversation", RichLog)

        user_msg = Text(text, style="bold #c7d0e0")
        panel = Panel(
            user_msg,
            border_style="#3B82F6",
            box=box.ROUNDED,
            padding=(0, 2),
        )
        log.write(panel, expand=True)
        log.write("")

        if text.strip() == "/setup":
            self._render_setup_info(log)
            return

        if self._is_context_command(text.strip()):
            await self._handle_context_command(text.strip(), log)
            return

        if self._is_stack_command(text.strip()):
            self._handle_stack_command(text.strip(), log)
            return

        stages = ["Planning", "Fetching pods", "Diagnosing", "Formatting"]
        spinner_task = asyncio.create_task(self._show_spinner(log, stages))

        loop = asyncio.get_running_loop()
        history_with_context = list(self._history)
        findings = safe_findings(app.adapter)
        if findings:
            finding_lines = [
                f"{f.get('type', 'issue')}: {f.get('resource', 'unknown')} "
                f"in {f.get('namespace', '?')} — {f.get('message', '')}"
                for f in findings[:5]
            ]
            history_with_context.insert(
                0,
                {
                    "role": "system",
                    "content": (
                        "IMPORTANT — The cluster dashboard detected these issues at startup. "
                        "You MUST investigate them using appropriate tools (describe_pod, "
                        "analyze_pod_logs, detect_crashloop, etc.) before giving a diagnosis: "
                        + "; ".join(finding_lines)
                    ),
                },
            )
        result: ChatCliResponse = await loop.run_in_executor(
            None, route_command, text, app.adapter, history_with_context
        )

        spinner_task.cancel()
        try:
            await spinner_task
        except asyncio.CancelledError:
            pass

        log.write("")

        if app.expert_mode:
            log.write(f"[dim]{result!r}[/dim]")
            return

        self._render_result(log, result)
        answer_text = "\n".join(line[0] for line in result.lines if line[0].strip())
        self._history.append({"role": "user", "content": text})
        self._history.append({"role": "assistant", "content": answer_text[:2000]})
        if result.suggestions:
            await self._update_chips(result.suggestions)
        self._refresh_aside()

    def _is_context_command(self, text: str) -> bool:
        command_name = text.split(maxsplit=1)[0] if text else ""
        return command_name in {"/context", "/ctx"}

    def _is_stack_command(self, text: str) -> bool:
        command_name = text.split(maxsplit=1)[0] if text else ""
        return command_name == "/stack"

    def _handle_stack_command(self, text: str, log: RichLog) -> None:
        from hexawyn.cli.presentation.stack_view import run_stack_command

        app = self._tui_app()
        context_name = app.cluster_name or "default"
        self._render_lines(log, run_stack_command(text, context_name))

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
        app = self._tui_app()
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

        app = self._tui_app()
        log = self.query_one("#conversation", RichLog)
        if app.context_service is None:
            self._render_lines(log, [("Kubernetes context switching is unavailable.", "yellow")])
            return

        switch_result = app.context_service.switch_context(context_name)
        if not switch_result.switched or switch_result.current_context is None:
            self._render_lines(log, missing_context_lines(switch_result.contexts))
            return

        app.startup_status = startup_status_from_switch(switch_result)
        app.adapter = app.adapter_builder(switch_result.current_context.name)
        app.cluster_name = switch_result.current_context.name
        self._refresh_aside()
        self._render_lines(log, self._context_switch_lines(switch_result))
        log.write(context_line(app.adapter))

    async def _open_context_picker(self) -> None:
        app = self._tui_app()
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
        app = self._tui_app()
        if app.context_service is not None:
            return app.context_service.discover()  # type: ignore[no-any-return]
        if app.startup_status is not None:
            return app.startup_status.contexts  # type: ignore[no-any-return]
        return []

    def _context_switch_lines(
        self,
        switch_result: KubernetesContextSwitchResult,
    ) -> list[tuple[str, str]]:
        current_context = switch_result.current_context
        if current_context is None:
            return [("✗ Context switch failed", "red")]

        conn_result = "Connection successful" if switch_result.connected else "Connection failed"
        conn_style = "green" if switch_result.connected else "yellow"
        lines = [
            ("✓ Context switched", "green"),
            ("", "dim"),
            (f"Current context: {current_context.name}", "bold"),
            (f"Namespace: {current_context.namespace}", "dim"),
            (conn_result, conn_style),
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

    def _render_result(self, log: RichLog, result: ChatCliResponse) -> None:
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
        from hexawyn.application.service.runtime_adapter import get_runtime

        app = self._tui_app()
        log = self.query_one("#conversation", RichLog)

        try:
            runtime = get_runtime()
            result = runtime.run_startup_scan(cluster_name=app.cluster_name)
        except Exception as exc:
            self.app.call_from_thread(log.write, f"[yellow]Startup scan failed: {exc}[/yellow]")
            return

        accumulated: dict[str, object] = dict(_asdict(result))
        if (
            str(accumulated.get("narrative_summary", ""))
            != "Startup scan not available via HTTP runtime."
        ):
            app.startup_result = accumulated

        def _update_ui() -> None:
            self._refresh_aside()

        self.app.call_from_thread(_update_ui)
