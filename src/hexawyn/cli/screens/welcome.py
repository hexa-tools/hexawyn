from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Input, Static

from hexawyn.cli.widgets.command_input import CommandInput


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
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
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
        from hexawyn.cli.screens.session import SessionScreen
        from hexawyn.cli.tui import HexawynTUI

        app = self.app
        assert isinstance(app, HexawynTUI)
        app.push_screen(SessionScreen(initial_command=text))
