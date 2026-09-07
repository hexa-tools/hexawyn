from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical, VerticalScroll
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Static


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁProviderSetupScreenǁcompose__mutmut: MutantDict = {}  # type: ignore
mutants_xǁProviderSetupScreenǁon_mount__mutmut: MutantDict = {}  # type: ignore
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut: MutantDict = {}  # type: ignore
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut: MutantDict = {}  # type: ignore
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut: MutantDict = {}  # type: ignore


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

    @_mutmut_mutated(mutants_xǁProviderSetupScreenǁcompose__mutmut)
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

    def xǁProviderSetupScreenǁcompose__mutmut_orig(self) -> ComposeResult:
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

    def xǁProviderSetupScreenǁcompose__mutmut_1(self) -> ComposeResult:
        with Vertical(id=None):
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

    def xǁProviderSetupScreenǁcompose__mutmut_2(self) -> ComposeResult:
        with Vertical(id="XXsetup-boxXX"):
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

    def xǁProviderSetupScreenǁcompose__mutmut_3(self) -> ComposeResult:
        with Vertical(id="SETUP-BOX"):
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

    def xǁProviderSetupScreenǁcompose__mutmut_4(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static(None, id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_5(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id=None)
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_6(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static(id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_7(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", )
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_8(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("XX[bold]🔑  LLM Setup[/bold]XX", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_9(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  llm setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_10(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[BOLD]🔑  LLM SETUP[/BOLD]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_11(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="XXsetup-titleXX")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_12(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="SETUP-TITLE")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_13(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static(None, id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_14(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id=None)
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_15(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static(id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_16(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", )
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_17(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("XXChoose your provider:XX", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_18(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_19(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("CHOOSE YOUR PROVIDER:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_20(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="XXsetup-labelXX")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_21(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="SETUP-LABEL")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_22(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id=None):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_23(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="XXsetup-providersXX"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_24(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="SETUP-PROVIDERS"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_25(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(None, id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_26(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=None, classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_27(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes=None)
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_28(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_29(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_30(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", )
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_31(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="XXprovider-btnXX")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_32(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="PROVIDER-BTN")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_33(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder=None, id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_34(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id=None, password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_35(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=None)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_36(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_37(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_38(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", )
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_39(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="XXPaste your API key...XX", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_40(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="paste your api key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_41(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="PASTE YOUR API KEY...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_42(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="XXsetup-keyXX", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_43(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="SETUP-KEY", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_44(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=False)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_45(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static(None, id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_46(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id=None)
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_47(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static(id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_48(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", )
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_49(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("XXXX", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_50(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="XXsetup-statusXX")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_51(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="SETUP-STATUS")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_52(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id=None):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_53(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="XXsetup-actionsXX"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_54(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="SETUP-ACTIONS"):
                yield Button("Save & Continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_55(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button(None, id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_56(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id=None, variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_57(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant=None)
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_58(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button(id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_59(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_60(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", )
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_61(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("XXSave & ContinueXX", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_62(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("save & continue", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_63(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("SAVE & CONTINUE", id="setup-save", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_64(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="XXsetup-saveXX", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_65(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="SETUP-SAVE", variant="primary")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_66(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="XXprimaryXX")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_67(self) -> ComposeResult:
        with Vertical(id="setup-box"):
            yield Static("[bold]🔑  LLM Setup[/bold]", id="setup-title")
            yield Static("Choose your provider:", id="setup-label")
            with VerticalScroll(id="setup-providers"):
                for key, name, _ in self.PROVIDERS:
                    yield Button(f"[{key}]  {name}", id=f"provider-{key}", classes="provider-btn")
            yield Input(placeholder="Paste your API key...", id="setup-key", password=True)
            yield Static("", id="setup-status")
            with Vertical(id="setup-actions"):
                yield Button("Save & Continue", id="setup-save", variant="PRIMARY")
                yield Button("Skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_68(self) -> ComposeResult:
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
                yield Button(None, id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_69(self) -> ComposeResult:
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
                yield Button("Skip for now", id=None, variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_70(self) -> ComposeResult:
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
                yield Button("Skip for now", id="setup-skip", variant=None)

    def xǁProviderSetupScreenǁcompose__mutmut_71(self) -> ComposeResult:
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
                yield Button(id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_72(self) -> ComposeResult:
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
                yield Button("Skip for now", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_73(self) -> ComposeResult:
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
                yield Button("Skip for now", id="setup-skip", )

    def xǁProviderSetupScreenǁcompose__mutmut_74(self) -> ComposeResult:
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
                yield Button("XXSkip for nowXX", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_75(self) -> ComposeResult:
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
                yield Button("skip for now", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_76(self) -> ComposeResult:
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
                yield Button("SKIP FOR NOW", id="setup-skip", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_77(self) -> ComposeResult:
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
                yield Button("Skip for now", id="XXsetup-skipXX", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_78(self) -> ComposeResult:
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
                yield Button("Skip for now", id="SETUP-SKIP", variant="default")

    def xǁProviderSetupScreenǁcompose__mutmut_79(self) -> ComposeResult:
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
                yield Button("Skip for now", id="setup-skip", variant="XXdefaultXX")

    def xǁProviderSetupScreenǁcompose__mutmut_80(self) -> ComposeResult:
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
                yield Button("Skip for now", id="setup-skip", variant="DEFAULT")

    @_mutmut_mutated(mutants_xǁProviderSetupScreenǁon_mount__mutmut)
    def on_mount(self) -> None:
        self._selected_provider = ""
        self._selected_url = ""

    def xǁProviderSetupScreenǁon_mount__mutmut_orig(self) -> None:
        self._selected_provider = ""
        self._selected_url = ""

    def xǁProviderSetupScreenǁon_mount__mutmut_1(self) -> None:
        self._selected_provider = None
        self._selected_url = ""

    def xǁProviderSetupScreenǁon_mount__mutmut_2(self) -> None:
        self._selected_provider = "XXXX"
        self._selected_url = ""

    def xǁProviderSetupScreenǁon_mount__mutmut_3(self) -> None:
        self._selected_provider = ""
        self._selected_url = None

    def xǁProviderSetupScreenǁon_mount__mutmut_4(self) -> None:
        self._selected_provider = ""
        self._selected_url = "XXXX"

    def action_skip(self) -> None:
        self.dismiss()

    @_mutmut_mutated(mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut)
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_orig(self, event: Button.Pressed) -> None:
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_1(self, event: Button.Pressed) -> None:
        if event.button.id != "setup-skip":
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_2(self, event: Button.Pressed) -> None:
        if event.button.id == "XXsetup-skipXX":
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_3(self, event: Button.Pressed) -> None:
        if event.button.id == "SETUP-SKIP":
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_4(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id != "setup-save":
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_5(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "XXsetup-saveXX":
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_6(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "SETUP-SAVE":
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_7(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id or event.button.id.startswith("provider-"):
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_8(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith(None):
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_9(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("XXprovider-XX"):
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_10(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("PROVIDER-"):
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_11(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("provider-"):
            key = None
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_12(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("provider-"):
            key = event.button.id.replace(None, "")
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_13(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("provider-"):
            key = event.button.id.replace("provider-", None)
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_14(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("provider-"):
            key = event.button.id.replace("")
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_15(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("provider-"):
            key = event.button.id.replace("provider-", )
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_16(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("provider-"):
            key = event.button.id.replace("XXprovider-XX", "")
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_17(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("provider-"):
            key = event.button.id.replace("PROVIDER-", "")
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_18(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("provider-"):
            key = event.button.id.replace("provider-", "XXXX")
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

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_19(self, event: Button.Pressed) -> None:
        if event.button.id == "setup-skip":
            self.dismiss()
            return

        if event.button.id == "setup-save":
            self._save_and_continue()
            return

        if event.button.id and event.button.id.startswith("provider-"):
            key = event.button.id.replace("provider-", "")
            for pk, name, url in self.PROVIDERS:
                if pk != key:
                    self._selected_provider = name
                    self._selected_url = url
                    self._highlight_provider(key)

                    key_input: Input = self.query_one("#setup-key", Input)
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_20(self, event: Button.Pressed) -> None:
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
                    self._selected_provider = None
                    self._selected_url = url
                    self._highlight_provider(key)

                    key_input: Input = self.query_one("#setup-key", Input)
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_21(self, event: Button.Pressed) -> None:
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
                    self._selected_url = None
                    self._highlight_provider(key)

                    key_input: Input = self.query_one("#setup-key", Input)
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_22(self, event: Button.Pressed) -> None:
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
                    self._highlight_provider(None)

                    key_input: Input = self.query_one("#setup-key", Input)
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_23(self, event: Button.Pressed) -> None:
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

                    key_input: Input = None
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_24(self, event: Button.Pressed) -> None:
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

                    key_input: Input = self.query_one(None, Input)
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_25(self, event: Button.Pressed) -> None:
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

                    key_input: Input = self.query_one("#setup-key", None)
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_26(self, event: Button.Pressed) -> None:
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

                    key_input: Input = self.query_one(Input)
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_27(self, event: Button.Pressed) -> None:
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

                    key_input: Input = self.query_one("#setup-key", )
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_28(self, event: Button.Pressed) -> None:
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

                    key_input: Input = self.query_one("XX#setup-keyXX", Input)
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_29(self, event: Button.Pressed) -> None:
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

                    key_input: Input = self.query_one("#SETUP-KEY", Input)
                    if key == "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_30(self, event: Button.Pressed) -> None:
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
                    if key != "0":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_31(self, event: Button.Pressed) -> None:
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
                    if key == "XX0XX":
                        key_input.placeholder = "Enter your API base URL first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_32(self, event: Button.Pressed) -> None:
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
                        key_input.placeholder = None
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_33(self, event: Button.Pressed) -> None:
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
                        key_input.placeholder = "XXEnter your API base URL first, then key...XX"
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_34(self, event: Button.Pressed) -> None:
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
                        key_input.placeholder = "enter your api base url first, then key..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_35(self, event: Button.Pressed) -> None:
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
                        key_input.placeholder = "ENTER YOUR API BASE URL FIRST, THEN KEY..."
                    else:
                        key_input.placeholder = f"Paste your {name} API key..."
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_36(self, event: Button.Pressed) -> None:
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
                        key_input.placeholder = None
                    break

    def xǁProviderSetupScreenǁon_button_pressed__mutmut_37(self, event: Button.Pressed) -> None:
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
                    return

    @_mutmut_mutated(mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut)
    def _highlight_provider(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", Button)
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_orig(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", Button)
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_1(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = None
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_2(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(None, Button)
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_3(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", None)
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_4(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(Button)
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_5(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", )
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_6(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", Button)
            if key != selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_7(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", Button)
            if key == selected_key:
                btn.variant = None
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_8(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", Button)
            if key == selected_key:
                btn.variant = "XXprimaryXX"
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_9(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", Button)
            if key == selected_key:
                btn.variant = "PRIMARY"
            else:
                btn.variant = "default"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_10(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", Button)
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = None

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_11(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", Button)
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "XXdefaultXX"

    def xǁProviderSetupScreenǁ_highlight_provider__mutmut_12(self, selected_key: str) -> None:
        for key, _, _ in self.PROVIDERS:
            btn = self.query_one(f"#provider-{key}", Button)
            if key == selected_key:
                btn.variant = "primary"
            else:
                btn.variant = "DEFAULT"

    @_mutmut_mutated(mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut)
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_orig(self) -> None:
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_1(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = None

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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_2(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one(None, Input).value.strip()

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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_3(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", None).value.strip()

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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_4(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one(Input).value.strip()

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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_5(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", ).value.strip()

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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_6(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("XX#setup-keyXX", Input).value.strip()

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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_7(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#SETUP-KEY", Input).value.strip()

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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_8(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if self._selected_provider:
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_9(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                None
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_10(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one(None, Static).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_11(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", None).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_12(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one(Static).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_13(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", ).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_14(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("XX#setup-statusXX", Static).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_15(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#SETUP-STATUS", Static).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_16(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "XX[red]Please select a provider first.[/red]XX"
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_17(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]please select a provider first.[/red]"
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_18(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[RED]PLEASE SELECT A PROVIDER FIRST.[/RED]"
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_19(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "Custom" or not self._selected_url:
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_20(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider != "Custom" and not self._selected_url:
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_21(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "XXCustomXX" and not self._selected_url:
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_22(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "custom" and not self._selected_url:
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_23(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "CUSTOM" and not self._selected_url:
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_24(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "Custom" and self._selected_url:
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_25(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "Custom" and not self._selected_url:
            self._selected_url = None
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_26(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "Custom" and not self._selected_url:
            self._selected_url = api_key
            if self._selected_url.startswith("http"):
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_27(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "Custom" and not self._selected_url:
            self._selected_url = api_key
            if not self._selected_url.startswith(None):
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_28(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "Custom" and not self._selected_url:
            self._selected_url = api_key
            if not self._selected_url.startswith("XXhttpXX"):
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_29(self) -> None:
        from hexawyn.infrastructure.config.config_manager import save_llm_config

        api_key = self.query_one("#setup-key", Input).value.strip()

        if not self._selected_provider:
            self.query_one("#setup-status", Static).update(
                "[red]Please select a provider first.[/red]"
            )
            return

        if self._selected_provider == "Custom" and not self._selected_url:
            self._selected_url = api_key
            if not self._selected_url.startswith("HTTP"):
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_30(self) -> None:
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
                    None
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_31(self) -> None:
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
                self.query_one(None, Static).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_32(self) -> None:
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
                self.query_one("#setup-status", None).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_33(self) -> None:
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
                self.query_one(Static).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_34(self) -> None:
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
                self.query_one("#setup-status", ).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_35(self) -> None:
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
                self.query_one("XX#setup-statusXX", Static).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_36(self) -> None:
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
                self.query_one("#SETUP-STATUS", Static).update(
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_37(self) -> None:
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
                    "XX[red]Custom provider: paste the base URL first, then the API key.[/red]XX"
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_38(self) -> None:
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
                    "[red]custom provider: paste the base url first, then the api key.[/red]"
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_39(self) -> None:
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
                    "[RED]CUSTOM PROVIDER: PASTE THE BASE URL FIRST, THEN THE API KEY.[/RED]"
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_40(self) -> None:
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
            self.query_one("#setup-key", Input).value = None
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_41(self) -> None:
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
            self.query_one(None, Input).value = ""
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_42(self) -> None:
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
            self.query_one("#setup-key", None).value = ""
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_43(self) -> None:
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
            self.query_one(Input).value = ""
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_44(self) -> None:
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
            self.query_one("#setup-key", ).value = ""
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_45(self) -> None:
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
            self.query_one("XX#setup-keyXX", Input).value = ""
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_46(self) -> None:
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
            self.query_one("#SETUP-KEY", Input).value = ""
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_47(self) -> None:
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
            self.query_one("#setup-key", Input).value = "XXXX"
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_48(self) -> None:
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
            self.query_one("#setup-key", Input).placeholder = None
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_49(self) -> None:
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
            self.query_one(None, Input).placeholder = "Paste your API key..."
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_50(self) -> None:
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
            self.query_one("#setup-key", None).placeholder = "Paste your API key..."
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_51(self) -> None:
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
            self.query_one(Input).placeholder = "Paste your API key..."
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_52(self) -> None:
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
            self.query_one("#setup-key", ).placeholder = "Paste your API key..."
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_53(self) -> None:
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
            self.query_one("XX#setup-keyXX", Input).placeholder = "Paste your API key..."
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_54(self) -> None:
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
            self.query_one("#SETUP-KEY", Input).placeholder = "Paste your API key..."
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_55(self) -> None:
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
            self.query_one("#setup-key", Input).placeholder = "XXPaste your API key...XX"
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_56(self) -> None:
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
            self.query_one("#setup-key", Input).placeholder = "paste your api key..."
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_57(self) -> None:
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
            self.query_one("#setup-key", Input).placeholder = "PASTE YOUR API KEY..."
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

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_58(self) -> None:
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
            self._selected_provider = None
            return

        if not api_key:
            self.query_one("#setup-status", Static).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_59(self) -> None:
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
            self._selected_provider = "XXCustomXX"
            return

        if not api_key:
            self.query_one("#setup-status", Static).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_60(self) -> None:
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
            self._selected_provider = "custom"
            return

        if not api_key:
            self.query_one("#setup-status", Static).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_61(self) -> None:
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
            self._selected_provider = "CUSTOM"
            return

        if not api_key:
            self.query_one("#setup-status", Static).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_62(self) -> None:
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

        if api_key:
            self.query_one("#setup-status", Static).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_63(self) -> None:
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
            self.query_one("#setup-status", Static).update(None)
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_64(self) -> None:
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
            self.query_one(None, Static).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_65(self) -> None:
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
            self.query_one("#setup-status", None).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_66(self) -> None:
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
            self.query_one(Static).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_67(self) -> None:
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
            self.query_one("#setup-status", ).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_68(self) -> None:
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
            self.query_one("XX#setup-statusXX", Static).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_69(self) -> None:
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
            self.query_one("#SETUP-STATUS", Static).update("[red]Please enter your API key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_70(self) -> None:
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
            self.query_one("#setup-status", Static).update("XX[red]Please enter your API key.[/red]XX")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_71(self) -> None:
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
            self.query_one("#setup-status", Static).update("[red]please enter your api key.[/red]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_72(self) -> None:
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
            self.query_one("#setup-status", Static).update("[RED]PLEASE ENTER YOUR API KEY.[/RED]")
            return

        save_llm_config(self._selected_provider, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_73(self) -> None:
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

        save_llm_config(None, self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_74(self) -> None:
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

        save_llm_config(self._selected_provider, None, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_75(self) -> None:
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

        save_llm_config(self._selected_provider, self._selected_url, None)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_76(self) -> None:
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

        save_llm_config(self._selected_url, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_77(self) -> None:
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

        save_llm_config(self._selected_provider, api_key)
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_78(self) -> None:
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

        save_llm_config(self._selected_provider, self._selected_url, )
        import os

        os.environ["LLM_API_KEY"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_79(self) -> None:
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

        os.environ["LLM_API_KEY"] = None
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_80(self) -> None:
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

        os.environ["XXLLM_API_KEYXX"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_81(self) -> None:
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

        os.environ["llm_api_key"] = api_key
        os.environ["LLM_BASE_URL"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_82(self) -> None:
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
        os.environ["LLM_BASE_URL"] = None

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_83(self) -> None:
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
        os.environ["XXLLM_BASE_URLXX"] = self._selected_url

        self.dismiss()

    def xǁProviderSetupScreenǁ_save_and_continue__mutmut_84(self) -> None:
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
        os.environ["llm_base_url"] = self._selected_url

        self.dismiss()

mutants_xǁProviderSetupScreenǁcompose__mutmut['_mutmut_orig'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_orig # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_1'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_1 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_2'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_2 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_3'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_3 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_4'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_4 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_5'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_5 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_6'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_6 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_7'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_7 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_8'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_8 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_9'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_9 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_10'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_10 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_11'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_11 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_12'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_12 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_13'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_13 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_14'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_14 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_15'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_15 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_16'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_16 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_17'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_17 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_18'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_18 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_19'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_19 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_20'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_20 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_21'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_21 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_22'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_22 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_23'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_23 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_24'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_24 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_25'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_25 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_26'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_26 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_27'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_27 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_28'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_28 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_29'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_29 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_30'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_30 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_31'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_31 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_32'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_32 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_33'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_33 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_34'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_34 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_35'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_35 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_36'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_36 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_37'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_37 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_38'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_38 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_39'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_39 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_40'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_40 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_41'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_41 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_42'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_42 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_43'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_43 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_44'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_44 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_45'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_45 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_46'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_46 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_47'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_47 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_48'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_48 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_49'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_49 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_50'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_50 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_51'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_51 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_52'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_52 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_53'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_53 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_54'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_54 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_55'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_55 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_56'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_56 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_57'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_57 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_58'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_58 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_59'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_59 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_60'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_60 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_61'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_61 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_62'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_62 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_63'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_63 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_64'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_64 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_65'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_65 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_66'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_66 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_67'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_67 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_68'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_68 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_69'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_69 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_70'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_70 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_71'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_71 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_72'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_72 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_73'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_73 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_74'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_74 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_75'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_75 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_76'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_76 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_77'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_77 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_78'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_78 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_79'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_79 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁcompose__mutmut['xǁProviderSetupScreenǁcompose__mutmut_80'] = ProviderSetupScreen.xǁProviderSetupScreenǁcompose__mutmut_80 # type: ignore # mutmut generated

mutants_xǁProviderSetupScreenǁon_mount__mutmut['_mutmut_orig'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_mount__mutmut_orig # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_mount__mutmut['xǁProviderSetupScreenǁon_mount__mutmut_1'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_mount__mutmut_1 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_mount__mutmut['xǁProviderSetupScreenǁon_mount__mutmut_2'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_mount__mutmut_2 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_mount__mutmut['xǁProviderSetupScreenǁon_mount__mutmut_3'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_mount__mutmut_3 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_mount__mutmut['xǁProviderSetupScreenǁon_mount__mutmut_4'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_mount__mutmut_4 # type: ignore # mutmut generated

mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['_mutmut_orig'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_1'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_2'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_3'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_4'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_4 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_5'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_5 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_6'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_6 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_7'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_7 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_8'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_8 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_9'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_9 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_10'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_10 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_11'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_11 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_12'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_12 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_13'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_13 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_14'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_14 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_15'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_15 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_16'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_16 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_17'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_17 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_18'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_18 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_19'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_19 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_20'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_20 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_21'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_21 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_22'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_22 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_23'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_23 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_24'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_24 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_25'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_25 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_26'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_26 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_27'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_27 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_28'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_28 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_29'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_29 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_30'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_30 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_31'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_31 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_32'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_32 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_33'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_33 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_34'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_34 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_35'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_35 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_36'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_36 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁon_button_pressed__mutmut['xǁProviderSetupScreenǁon_button_pressed__mutmut_37'] = ProviderSetupScreen.xǁProviderSetupScreenǁon_button_pressed__mutmut_37 # type: ignore # mutmut generated

mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['_mutmut_orig'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_orig # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_1'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_1 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_2'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_2 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_3'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_3 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_4'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_4 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_5'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_5 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_6'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_6 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_7'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_7 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_8'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_8 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_9'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_9 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_10'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_10 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_11'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_11 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_highlight_provider__mutmut['xǁProviderSetupScreenǁ_highlight_provider__mutmut_12'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_highlight_provider__mutmut_12 # type: ignore # mutmut generated

mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['_mutmut_orig'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_orig # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_1'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_1 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_2'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_2 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_3'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_3 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_4'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_4 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_5'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_5 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_6'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_6 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_7'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_7 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_8'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_8 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_9'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_9 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_10'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_10 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_11'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_11 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_12'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_12 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_13'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_13 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_14'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_14 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_15'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_15 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_16'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_16 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_17'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_17 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_18'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_18 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_19'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_19 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_20'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_20 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_21'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_21 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_22'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_22 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_23'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_23 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_24'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_24 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_25'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_25 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_26'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_26 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_27'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_27 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_28'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_28 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_29'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_29 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_30'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_30 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_31'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_31 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_32'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_32 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_33'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_33 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_34'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_34 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_35'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_35 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_36'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_36 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_37'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_37 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_38'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_38 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_39'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_39 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_40'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_40 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_41'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_41 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_42'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_42 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_43'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_43 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_44'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_44 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_45'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_45 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_46'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_46 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_47'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_47 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_48'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_48 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_49'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_49 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_50'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_50 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_51'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_51 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_52'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_52 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_53'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_53 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_54'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_54 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_55'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_55 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_56'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_56 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_57'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_57 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_58'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_58 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_59'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_59 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_60'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_60 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_61'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_61 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_62'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_62 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_63'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_63 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_64'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_64 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_65'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_65 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_66'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_66 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_67'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_67 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_68'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_68 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_69'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_69 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_70'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_70 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_71'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_71 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_72'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_72 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_73'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_73 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_74'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_74 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_75'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_75 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_76'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_76 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_77'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_77 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_78'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_78 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_79'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_79 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_80'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_80 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_81'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_81 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_82'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_82 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_83'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_83 # type: ignore # mutmut generated
mutants_xǁProviderSetupScreenǁ_save_and_continue__mutmut['xǁProviderSetupScreenǁ_save_and_continue__mutmut_84'] = ProviderSetupScreen.xǁProviderSetupScreenǁ_save_and_continue__mutmut_84 # type: ignore # mutmut generated
