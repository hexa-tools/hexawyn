import asyncio
import platform
import subprocess
import tempfile
from dataclasses import asdict as _asdict
from typing import Any

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import Input, LoadingIndicator, Static

from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_response import ChatCliResponse
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
    missing_context_lines,
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
from hexawyn.cli.widgets.markdown_log import MarkdownLog
from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext as KubernetesClusterContext,
)


class SessionScreen(Screen[None]):
    CSS_PATH = "session.tcss"
    BINDINGS = [
        Binding("ctrl+b", "manage_subscription", "Manage subscription"),
        Binding("ctrl+y", "copy_response", "Copy last response"),
        Binding("ctrl+e", "export_response", "Export to editor"),
    ]

    def __init__(self, initial_command: str | None = None) -> None:
        super().__init__()
        self.initial_command = initial_command
        self._history: list[dict[str, str]] = []
        self._refresh_task: asyncio.Task[None] | None = None
        self._last_response: str = ""
        self._boot_ready: bool = False

    def _tui_app(self) -> Any:
        from hexawyn.cli.tui import HexawynTUI

        app = self.app
        assert isinstance(app, HexawynTUI)
        return app

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="main-col"):
                with VerticalScroll(id="conversation-scroll"):
                    yield Static("", id="logo-banner", markup=True)
                    yield LoadingIndicator(id="boot-loader")
                    yield MarkdownLog(id="conversation")
                    yield Static("", id="agentic-steps", markup=True)
                yield Static("", id="status-bar")
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
        self._show_aside_skeleton()
        self.run_worker(self._prime_aside, thread=True)
        self.run_worker(self._auto_hide_loader, thread=True)
        self._refresh_footer()

        app = self._tui_app()
        self.query_one("#logo-banner", Static).update(
            "\n".join(line.format(version=app_version()) for line in _LOGO_BANNER)
        )
        log = self.query_one("#conversation", MarkdownLog)
        log.write("")

        if app.run_startup_scan:
            self.run_worker(self._run_startup_scan, thread=True)  # type: ignore[arg-type]

        if self.initial_command:
            await self._handle_command(self.initial_command)

        self._start_background_license_refresh()

    def _auto_hide_loader(self) -> None:
        """Guarantee the boot loader disappears even if priming never completes.

        Safety net: hides the loading indicator after a grace period so the
        UI never remains stuck on a spinner when the cluster is unreachable.
        """
        import time as _time

        deadline = _time.monotonic() + 5.0
        while _time.monotonic() < deadline:
            if self._boot_ready:
                return
            _time.sleep(0.25)

        def _hide() -> None:
            self._mark_boot_ready()

        self.app.call_from_thread(_hide)

    def _show_aside_skeleton(self) -> None:
        """Populate the aside structure immediately without slow cluster reads.

        The right column renders its labels right away (the cluster polling,
        which can take a couple of seconds, happens in the _prime_aside worker
        that overwrites these placeholders).
        """
        from hexawyn.cli.presentation.aside_builder import build_aside_skeleton

        try:
            skeleton = build_aside_skeleton(self._tui_app())
            self.query_one("#aside-body", Static).update("\n".join(skeleton))
        except Exception:
            pass

    def _prime_aside(self) -> None:
        """Build the aside lines off the render thread so startup is instant.

        The heavy cluster reads (build_aside_lines) run on a worker; the result
        is applied back on the Textual event loop via call_from_thread. If the
        screen was replaced meanwhile, the update is skipped.
        """
        try:
            lines = self._aside_lines()

            def _apply() -> None:
                try:
                    body = self.query_one("#aside-body", Static)
                    body.update("\n".join(lines))
                    self._refresh_quota_bar()
                    self._refresh_footer()
                    self._mark_boot_ready()
                except Exception:
                    pass

            self.app.call_from_thread(_apply)
        except Exception:
            pass

    def _mark_boot_ready(self) -> None:
        """Hide the boot loader once the aside has been primed."""
        self._boot_ready = True
        try:
            loader = self.query_one("#boot-loader", LoadingIndicator)
            loader.visible = False
            loader.display = False
        except Exception:
            pass

    def _start_background_license_refresh(self) -> None:
        async def _periodic_refresh() -> None:
            try:
                await asyncio.sleep(300)
            except asyncio.CancelledError:
                return
            while True:
                from hexawyn.infrastructure.license.license_reader import refresh_license

                refresh_license()
                self._refresh_aside()
                try:
                    await asyncio.sleep(6 * 3600)
                except asyncio.CancelledError:
                    return

        self._refresh_task = asyncio.create_task(_periodic_refresh())

    def _refresh_aside(self) -> None:
        """Refresh the aside off the render thread so the UI never freezes.

        The heavy cluster reads (build_aside_lines) run on a worker; the result
        is applied back via call_from_thread by _prime_aside. Falls back to a
        synchronous rebuild when run_worker is unavailable (e.g. unit tests).
        """
        try:
            self.run_worker(self._prime_aside, thread=True)
        except Exception:
            self._rebuild_aside_sync()

    def _rebuild_aside_sync(self) -> None:
        try:
            self.query_one("#aside-body", Static).update("\n".join(self._aside_lines()))
            self._refresh_quota_bar()
            self._refresh_footer()
        except Exception:
            pass

    def _aside_lines(self) -> list[str]:
        return build_aside_lines(self._tui_app())

    def _refresh_quota_bar(self) -> None:
        try:
            from hexawyn.adapters.secondary.runtime_quota_source import (
                RuntimeQuotaSource,
            )
            from hexawyn.application.service.runtime_adapter import get_runtime
            from hexawyn.application.use_case.cluster.get_quota_usage.command import (
                GetQuotaUsageCommand,
            )
            from hexawyn.application.use_case.cluster.get_quota_usage.get_quota_usage_use_case import (  # noqa: E501
                GetQuotaUsageUseCase,
            )
            from hexawyn.cli.widgets.quota_bar import _quota_bar

            quota_source = RuntimeQuotaSource(runtime=get_runtime())
            use_case = GetQuotaUsageUseCase(
                plan_port=quota_source,
                usage_meter=quota_source,
            )
            response = use_case.execute(GetQuotaUsageCommand())

            lines: list[str] = ["", "[bold]Quota[/bold]", "\u2500" * 18]
            for quota in response.quotas:
                if quota.state.value == "unlimited":
                    continue
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
            "[bold]Ctrl+C[/bold] cancel   [bold]Ctrl+Y[/bold] copy   "
            "[dim]click-drag select[/dim]   [bold]Ctrl+Q[/bold] quit   "
            f"{ctrl_b}"
        )

    def _license_aside_lines(self) -> list[str]:
        return format_license_aside_lines()

    def action_manage_subscription(self) -> None:
        import webbrowser

        from hexawyn.infrastructure.config.config_manager import load_config

        config = load_config()
        subscription_key = config.get("hexawyn_token")
        if subscription_key:
            webbrowser.open(f"https://hexawyn.com/account/manage?key={subscription_key}")
        else:
            webbrowser.open("https://hexawyn.com/account/manage")
        self.notify("Opening account page...", title="Subscription")

    def action_clear_input(self) -> None:
        cmd_input = self.query_one("#cmd-input", CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def on_unmount(self) -> None:
        if self._refresh_task:
            self._refresh_task.cancel()

    async def on_input_changed(self, event: Input.Changed) -> None:
        pass

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return
        cmd_input = event.input
        if hasattr(cmd_input, "remember"):
            cmd_input.remember(text)
        cmd_input.action_delete_left_all()
        asyncio.create_task(self._handle_command(text))

    async def _show_spinner(self, log: MarkdownLog, stages: list[str]) -> None:
        spinner_chars = ["⬡", "⬢", "⬡", "⬢"]
        status = self.query_one("#status-bar", Static)
        try:
            for i, stage in enumerate(stages):
                for char in spinner_chars:
                    status.update(f"[bold #3B82F6]  {char}[/] [dim #8a93a6]{stage}...[/]")
                    await asyncio.sleep(0.15)
                if i < len(stages) - 1:
                    status.update(f"[bold #22c55e]  ✓[/] [dim #5b6472]{stage}[/]")
                    await asyncio.sleep(0.4)
        except asyncio.CancelledError:
            pass
        finally:
            status.update("")

    async def _handle_command(self, text: str) -> None:  # noqa: C901, PLR0912, PLR0915
        app = self._tui_app()
        log = self.query_one("#conversation", MarkdownLog)

        log.write(f"\n> **{text}**\n")

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

        status = self.query_one("#status-bar", Static)
        steps_widget = self.query_one("#agentic-steps", Static)
        seen_steps: list[str] = []

        def _steps_markup(char: str) -> str:
            line = " · ".join(seen_steps) if seen_steps else "Thinking"
            return f"[bold #3B82F6]  {char}[/] [dim #8a93a6]{line}...[/]"

        def _on_progress(_node_name: str, label: str) -> None:
            if label not in seen_steps:
                seen_steps.append(label)
            line = " · ".join(seen_steps)
            self.app.call_from_thread(
                status.update, f"[bold #3B82F6]  ⬡[/] [dim #8a93a6]{line}...[/]"
            )
            self.app.call_from_thread(
                steps_widget.update,
                f"[dim #8a93a6]{_steps_markup('⬡')}[/]",
            )

        async def _continuous_spinner() -> None:
            chars = ["⬡", "⬢", "⬡", "⬢"]
            i = 0
            try:
                while True:
                    line = " · ".join(seen_steps) if seen_steps else "Thinking"
                    status.update(f"[bold #3B82F6]  {chars[i % 4]}[/] [dim #8a93a6]{line}...[/]")
                    steps_widget.update(f"[dim #8a93a6]{_steps_markup(chars[i % 4])}[/]")
                    i += 1
                    await asyncio.sleep(0.3)
            except asyncio.CancelledError:
                pass

        spinner_task = asyncio.create_task(_continuous_spinner())

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
            None,
            lambda: route_command(
                text, app.adapter, history_with_context, on_progress=_on_progress
            ),
        )

        spinner_task.cancel()
        try:
            await spinner_task
        except asyncio.CancelledError:
            pass

        steps_widget.update("")

        if seen_steps:
            status.update(f"[bold #22c55e]  ✓[/] [dim #5b6472]{' · '.join(seen_steps)}[/]")
        else:
            status.update("")

        if app.expert_mode:
            log.write(f"[dim]{result!r}[/dim]")
            return

        render_result(log, result)
        if result.duration_ms:
            seconds = result.duration_ms / 1000
            status.update(f"[dim #5b6472]{seconds:.1f}s[/]")
        answer_text = "\n".join(line[0] for line in result.lines if line[0].strip())
        self._last_response = answer_text
        self._history.append({"role": "user", "content": text})
        self._history.append({"role": "assistant", "content": answer_text[:2000]})
        self._refresh_aside()

    def _copy_to_clipboard(self, text: str) -> str:
        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
                return "✓ Copied to clipboard"
            if system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return "✓ Copied to clipboard"
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
                return "✗ Install xclip or wl-clipboard to enable copy"
            return f"✗ Copy not supported on {system}"
        except Exception as exc:
            return f"✗ Copy failed: {exc}"

    def action_copy_response(self) -> None:
        if not self._last_response:
            self.query_one("#status-bar", Static).update("[dim #8a93a6]Nothing to copy yet.[/]")  # noqa: E501
            return
        result = self._copy_to_clipboard(self._last_response)
        self.query_one("#status-bar", Static).update(f"[dim #8a93a6]{result}[/]")

    def action_export_response(self) -> None:
        if not self._last_response:
            self.query_one("#status-bar", Static).update("[dim #8a93a6]Nothing to export yet.[/]")  # noqa: E501
            return
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".txt", delete=False, encoding="utf-8"
            ) as f:  # noqa: E501
                f.write(self._last_response)
                path = f.name
            system = platform.system()
            if system == "Darwin":
                subprocess.Popen(["open", path])
            elif system == "Linux":
                subprocess.Popen(["xdg-open", path])
            self.query_one("#status-bar", Static).update("[dim #8a93a6]✓ Opened in editor[/]")  # noqa: E501
        except Exception as exc:
            self.query_one("#status-bar", Static).update(f"[dim #8a93a6]✗ Export failed: {exc}[/]")  # noqa: E501

    def _handle_stack_command(self, text: str, log: MarkdownLog) -> None:
        from hexawyn.cli.presentation.stack_view import run_stack_command

        app = self._tui_app()
        context_name = app.cluster_name or "default"
        render_lines(log, run_stack_command(text, context_name))

    async def _handle_context_command(self, text: str, log: MarkdownLog) -> None:
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
        log = self.query_one("#conversation", MarkdownLog)
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
            log = self.query_one("#conversation", MarkdownLog)
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

    async def _run_startup_scan(self) -> None:
        from hexawyn.application.service.runtime_adapter import get_runtime

        app = self._tui_app()
        log = self.query_one("#conversation", MarkdownLog)

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
