from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical, VerticalScroll
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Static


class ProviderSetupScreen(ModalScreen[None]):
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
