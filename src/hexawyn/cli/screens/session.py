import asyncio
from dataclasses import asdict as _asdict
from typing import Any

from rich import box
from rich.panel import Panel
from rich.text import Text
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Input, RichLog, Static

from hexawyn.application.use_case.chat_cli.chat_cli_response import ChatCliResponse
from hexawyn.cli.command_router import route_command
from hexawyn.cli.presentation.aside_builder import build_aside_lines
from hexawyn.cli.presentation.asides import (
    safe_findings,
)
from hexawyn.cli.presentation.command_router import (
    extract_requested_context,
)
from hexawyn.cli.presentation.command_router import (
    is_context_command as _is_context_command,
)
from hexawyn.cli.presentation.command_router import (
    is_setup_command as _is_setup_command,
)
from hexawyn.cli.presentation.command_router import (
    is_stack_command as _is_stack_command,
)
from hexawyn.cli.presentation.command_router import (
    is_token_command as _is_token_command,
)
from hexawyn.cli.presentation.constants import _LOGO_BANNER
from hexawyn.cli.presentation.context_display import format_context_switch_lines
from hexawyn.cli.presentation.formatting import (
    app_version,
    compact_project_directory,
    context_line,
    missing_context_lines,
    startup_lines,
    startup_status_from_switch,
)
from hexawyn.cli.presentation.license_display import (
    format_license_aside_lines,
    format_license_footer_hint,
)
from hexawyn.cli.presentation.response_renderer import render_lines, render_result
from hexawyn.cli.presentation.setup_info import render_setup_info
from hexawyn.cli.presentation.startup_scan import is_valid_startup_result
from hexawyn.cli.screens.context_picker import ContextPickerScreen
from hexawyn.cli.widgets.command_input import CommandInput
from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext as KubernetesClusterContext,
)


class SessionScreen(Screen[None]):
    CSS_PATH = "session.tcss"
    BINDINGS = [
        Binding("ctrl+b", "manage_subscription", "Manage subscription"),
    ]

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
                    yield Static("", id="footer-hints")
            with Vertical(id="aside"):
                with VerticalScroll(id="aside-content"):
                    yield Static("", id="aside-body")
                yield Static("", id="quota-bar")
                yield Static(compact_project_directory(), id="aside-project")
                yield Static(
                    f"hexa[bold #3B82F6]wyn[/bold #3B82F6] [dim]{app_version()}[/dim]",
                    id="aside-brand",
                )

    async def on_mount(self) -> None:
        self.query_one("#cmd-input", CommandInput).focus()
        self._refresh_aside()
        self._refresh_footer()

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
        self._refresh_quota_bar()
        self._refresh_footer()

    def _aside_lines(self) -> list[str]:
        return build_aside_lines(self._tui_app())

    def _refresh_quota_bar(self) -> None:
        try:
            from hexawyn.adapters.secondary.pricing_plan_adapter import (
                PricingPlanAdapter,
            )
            from hexawyn.adapters.secondary.usage_meter_adapter import (
                UsageMeterAdapter,
            )
            from hexawyn.application.ports.driving.get_quota_usage.get_quota_usage_command import (
                GetQuotaUsageCommand,
            )
            from hexawyn.application.service.get_quota_usage_service import (
                GetQuotaUsageService,
            )
            from hexawyn.application.use_case.get_quota_usage.get_quota_usage_use_case import (
                GetQuotaUsageUseCase,
            )
            from hexawyn.cli.widgets.quota_bar import _quota_bar
            from hexawyn.infrastructure.config.quota_manager import (
                _get_current_investigation_quota,
                _get_current_slack_quota,
            )

            plan = PricingPlanAdapter()
            meter = UsageMeterAdapter()

            try:
                inv = _get_current_investigation_quota()
                slack = _get_current_slack_quota()
                meter.set_usage("investigations", inv.count)
                meter.set_usage("slack_alerts", slack.count)
            except Exception:
                pass

            service = GetQuotaUsageService(plan_port=plan, usage_meter=meter)
            use_case = GetQuotaUsageUseCase(service=service)
            response = use_case.execute(GetQuotaUsageCommand())

            lines: list[str] = ["", "[bold]Quota[/bold]", "\u2500" * 18]
            for quota in response.quotas:
                lines.append(_quota_bar(quota))

            self.query_one("#quota-bar", Static).update("\n".join(lines))
        except Exception as exc:
            self.query_one("#quota-bar", Static).update(f"[dim]Quota unavailable — {exc}[/dim]")

    def _refresh_footer(self) -> None:
        from hexawyn.infrastructure.license.license_reader import read_license_state

        state_info = read_license_state()
        ctrl_b = format_license_footer_hint(state_info.state)

        self.query_one("#footer-hints", Static).update(
            "[bold]Enter[/bold] send   [bold]↑↓[/bold] history   "
            "[bold]Ctrl+C[/bold] cancel   [bold]Ctrl+Q[/bold] quit   "
            f"{ctrl_b}"
        )

    def _license_aside_lines(self) -> list[str]:
        return format_license_aside_lines()

    def action_manage_subscription(self) -> None:
        import webbrowser

        from hexawyn.infrastructure.config.config_manager import load_config

        config = load_config()
        token = config.get("hexawyn_token")
        if token:
            webbrowser.open(f"https://hexawyn.com/account/manage?key={token}")
        else:
            webbrowser.open("https://hexawyn.com/account/manage")
        self.notify("Opening account page...", title="Subscription")

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

        if _is_setup_command(text.strip()):
            render_setup_info(log)
            return

        if _is_token_command(text.strip()):
            await self._open_token_input()
            return

        if _is_context_command(text.strip()):
            await self._handle_context_command(text.strip(), log)
            return

        if _is_stack_command(text.strip()):
            self._handle_stack_command(text.strip(), log)
            return

        if text.strip() == "/refresh":
            from hexawyn.infrastructure.license.license_reader import refresh_license

            if refresh_license():
                log.write("[green]✓ License refreshed successfully.[/]")
            else:
                log.write("[yellow]⚠ Could not refresh license. Run /token to re-activate.[/]")
            self._refresh_aside()
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

        render_result(log, result)
        answer_text = "\n".join(line[0] for line in result.lines if line[0].strip())
        self._history.append({"role": "user", "content": text})
        self._history.append({"role": "assistant", "content": answer_text[:2000]})
        if result.suggestions:
            await self._update_chips(result.suggestions)
        self._refresh_aside()

    def _handle_stack_command(self, text: str, log: RichLog) -> None:
        from hexawyn.cli.presentation.stack_view import run_stack_command

        app = self._tui_app()
        context_name = app.cluster_name or "default"
        render_lines(log, run_stack_command(text, context_name))

    async def _handle_context_command(self, text: str, log: RichLog) -> None:
        app = self._tui_app()
        if app.context_service is None:
            render_lines(log, [("Kubernetes context switching is unavailable.", "yellow")])
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
            render_lines(log, [("Kubernetes context switching is unavailable.", "yellow")])
            return

        switch_result = app.context_service.switch_context(context_name)
        if not switch_result.switched or switch_result.current_context is None:
            render_lines(log, missing_context_lines(switch_result.contexts))
            return

        app.startup_status = startup_status_from_switch(switch_result)
        app.adapter = app.adapter_builder(switch_result.current_context.name)
        app.cluster_name = switch_result.current_context.name
        self._refresh_aside()
        render_lines(log, format_context_switch_lines(switch_result))
        log.write(context_line(app.adapter))

    async def _open_context_picker(self) -> None:
        app = self._tui_app()
        app.push_screen(
            ContextPickerScreen(self._available_contexts()),
            callback=self._switch_context,
        )

    async def _open_token_input(self) -> None:
        from hexawyn.cli.screens.token_input import TokenInputScreen

        app = self._tui_app()

        def _on_done(prefix: str | None) -> None:
            log = self.query_one("#conversation", RichLog)
            if prefix:
                log.write(f"[green]✓ License activated — token: [bold]{prefix}...[/][/green]")
            self._refresh_aside()

        app.push_screen(TokenInputScreen(), callback=_on_done)

    def _requested_context_name(self, text: str) -> str | None:
        return extract_requested_context(text)

    def _available_contexts(self) -> list[KubernetesClusterContext]:
        app = self._tui_app()
        if app.context_service is not None:
            return app.context_service.discover()  # type: ignore[no-any-return]
        if app.startup_status is not None:
            return app.startup_status.contexts  # type: ignore[no-any-return]
        return []

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
        if is_valid_startup_result(accumulated):
            app.startup_result = accumulated

        def _update_ui() -> None:
            self._refresh_aside()

        self.app.call_from_thread(_update_ui)
