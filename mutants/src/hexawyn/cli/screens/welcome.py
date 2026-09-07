from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Input, Static

from hexawyn.cli.widgets.command_input import CommandInput


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁWelcomeScreenǁcompose__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWelcomeScreenǁon_mount__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWelcomeScreenǁaction_clear_input__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWelcomeScreenǁon_input_submitted__mutmut: MutantDict = {}  # type: ignore


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

    @_mutmut_mutated(mutants_xǁWelcomeScreenǁcompose__mutmut)
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

    def xǁWelcomeScreenǁcompose__mutmut_orig(self) -> ComposeResult:
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

    def xǁWelcomeScreenǁcompose__mutmut_1(self) -> ComposeResult:
        with Vertical(id=None):
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

    def xǁWelcomeScreenǁcompose__mutmut_2(self) -> ComposeResult:
        with Vertical(id="XXwelcome-rootXX"):
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

    def xǁWelcomeScreenǁcompose__mutmut_3(self) -> ComposeResult:
        with Vertical(id="WELCOME-ROOT"):
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

    def xǁWelcomeScreenǁcompose__mutmut_4(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static(None, id="welcome-logo")
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

    def xǁWelcomeScreenǁcompose__mutmut_5(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id=None)
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

    def xǁWelcomeScreenǁcompose__mutmut_6(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static(id="welcome-logo")
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

    def xǁWelcomeScreenǁcompose__mutmut_7(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", )
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

    def xǁWelcomeScreenǁcompose__mutmut_8(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("XXhexa[bold #3B82F6]wyn[/bold #3B82F6]XX", id="welcome-logo")
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

    def xǁWelcomeScreenǁcompose__mutmut_9(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3b82f6]wyn[/bold #3b82f6]", id="welcome-logo")
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

    def xǁWelcomeScreenǁcompose__mutmut_10(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("HEXA[BOLD #3B82F6]WYN[/BOLD #3B82F6]", id="welcome-logo")
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

    def xǁWelcomeScreenǁcompose__mutmut_11(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="XXwelcome-logoXX")
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

    def xǁWelcomeScreenǁcompose__mutmut_12(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="WELCOME-LOGO")
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

    def xǁWelcomeScreenǁcompose__mutmut_13(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id=None):
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

    def xǁWelcomeScreenǁcompose__mutmut_14(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="XXwelcome-panelXX"):
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

    def xǁWelcomeScreenǁcompose__mutmut_15(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="WELCOME-PANEL"):
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

    def xǁWelcomeScreenǁcompose__mutmut_16(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder=None,
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

    def xǁWelcomeScreenǁcompose__mutmut_17(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id=None,
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

    def xǁWelcomeScreenǁcompose__mutmut_18(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
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

    def xǁWelcomeScreenǁcompose__mutmut_19(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
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

    def xǁWelcomeScreenǁcompose__mutmut_20(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='XXAsk anything... "What is happening in payments?"XX',
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

    def xǁWelcomeScreenǁcompose__mutmut_21(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='ask anything... "what is happening in payments?"',
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

    def xǁWelcomeScreenǁcompose__mutmut_22(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='ASK ANYTHING... "WHAT IS HAPPENING IN PAYMENTS?"',
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

    def xǁWelcomeScreenǁcompose__mutmut_23(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id="XXwelcome-inputXX",
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

    def xǁWelcomeScreenǁcompose__mutmut_24(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id="WELCOME-INPUT",
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

    def xǁWelcomeScreenǁcompose__mutmut_25(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id="welcome-input",
                )
                yield Static(
                    None,
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

    def xǁWelcomeScreenǁcompose__mutmut_26(self) -> ComposeResult:
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
                    id=None,
                )
            yield Static(
                "tab agents   ctrl+p commands",
                id="welcome-shortcuts",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_27(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id="welcome-input",
                )
                yield Static(
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

    def xǁWelcomeScreenǁcompose__mutmut_28(self) -> ComposeResult:
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
                    )
            yield Static(
                "tab agents   ctrl+p commands",
                id="welcome-shortcuts",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_29(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id="welcome-input",
                )
                yield Static(
                    "XX[bold #3B82F6]Build[/bold #3B82F6] · Hexawyn Kubernetes · XX"
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

    def xǁWelcomeScreenǁcompose__mutmut_30(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id="welcome-input",
                )
                yield Static(
                    "[bold #3b82f6]build[/bold #3b82f6] · hexawyn kubernetes · "
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

    def xǁWelcomeScreenǁcompose__mutmut_31(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id="welcome-input",
                )
                yield Static(
                    "[BOLD #3B82F6]BUILD[/BOLD #3B82F6] · HEXAWYN KUBERNETES · "
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

    def xǁWelcomeScreenǁcompose__mutmut_32(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id="welcome-input",
                )
                yield Static(
                    "[bold #3B82F6]Build[/bold #3B82F6] · Hexawyn Kubernetes · "
                    "XX[bold #f5a623]high[/bold #f5a623]XX",
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

    def xǁWelcomeScreenǁcompose__mutmut_33(self) -> ComposeResult:
        with Vertical(id="welcome-root"):
            yield Static("hexa[bold #3B82F6]wyn[/bold #3B82F6]", id="welcome-logo")
            with Vertical(id="welcome-panel"):
                yield CommandInput(
                    placeholder='Ask anything... "What is happening in payments?"',
                    id="welcome-input",
                )
                yield Static(
                    "[bold #3B82F6]Build[/bold #3B82F6] · Hexawyn Kubernetes · "
                    "[BOLD #F5A623]HIGH[/BOLD #F5A623]",
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

    def xǁWelcomeScreenǁcompose__mutmut_34(self) -> ComposeResult:
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
                    id="XXwelcome-modeXX",
                )
            yield Static(
                "tab agents   ctrl+p commands",
                id="welcome-shortcuts",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_35(self) -> ComposeResult:
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
                    id="WELCOME-MODE",
                )
            yield Static(
                "tab agents   ctrl+p commands",
                id="welcome-shortcuts",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_36(self) -> ComposeResult:
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
                None,
                id="welcome-shortcuts",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_37(self) -> ComposeResult:
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
                id=None,
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_38(self) -> ComposeResult:
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
                id="welcome-shortcuts",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_39(self) -> ComposeResult:
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
                )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_40(self) -> ComposeResult:
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
                "XXtab agents   ctrl+p commandsXX",
                id="welcome-shortcuts",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_41(self) -> ComposeResult:
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
                "TAB AGENTS   CTRL+P COMMANDS",
                id="welcome-shortcuts",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_42(self) -> ComposeResult:
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
                id="XXwelcome-shortcutsXX",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_43(self) -> ComposeResult:
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
                id="WELCOME-SHORTCUTS",
            )
            yield Static(
                "[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_44(self) -> ComposeResult:
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
                None,  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_45(self) -> ComposeResult:
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
                id=None,
            )

    def xǁWelcomeScreenǁcompose__mutmut_46(self) -> ComposeResult:
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
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_47(self) -> ComposeResult:
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
                )

    def xǁWelcomeScreenǁcompose__mutmut_48(self) -> ComposeResult:
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
                "XX[yellow]●[/yellow] Tip Run [bold]hexa debug config[/bold] to troubleshoot configurationXX",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_49(self) -> ComposeResult:
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
                "[yellow]●[/yellow] tip run [bold]hexa debug config[/bold] to troubleshoot configuration",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_50(self) -> ComposeResult:
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
                "[YELLOW]●[/YELLOW] TIP RUN [BOLD]HEXA DEBUG CONFIG[/BOLD] TO TROUBLESHOOT CONFIGURATION",  # noqa: E501
                id="welcome-tip",
            )

    def xǁWelcomeScreenǁcompose__mutmut_51(self) -> ComposeResult:
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
                id="XXwelcome-tipXX",
            )

    def xǁWelcomeScreenǁcompose__mutmut_52(self) -> ComposeResult:
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
                id="WELCOME-TIP",
            )

    @_mutmut_mutated(mutants_xǁWelcomeScreenǁon_mount__mutmut)
    def on_mount(self) -> None:
        self.query_one("#welcome-input", CommandInput).focus()

    def xǁWelcomeScreenǁon_mount__mutmut_orig(self) -> None:
        self.query_one("#welcome-input", CommandInput).focus()

    def xǁWelcomeScreenǁon_mount__mutmut_1(self) -> None:
        self.query_one(None, CommandInput).focus()

    def xǁWelcomeScreenǁon_mount__mutmut_2(self) -> None:
        self.query_one("#welcome-input", None).focus()

    def xǁWelcomeScreenǁon_mount__mutmut_3(self) -> None:
        self.query_one(CommandInput).focus()

    def xǁWelcomeScreenǁon_mount__mutmut_4(self) -> None:
        self.query_one("#welcome-input", ).focus()

    def xǁWelcomeScreenǁon_mount__mutmut_5(self) -> None:
        self.query_one("XX#welcome-inputXX", CommandInput).focus()

    def xǁWelcomeScreenǁon_mount__mutmut_6(self) -> None:
        self.query_one("#WELCOME-INPUT", CommandInput).focus()

    @_mutmut_mutated(mutants_xǁWelcomeScreenǁaction_clear_input__mutmut)
    def action_clear_input(self) -> None:
        cmd_input = self.query_one("#welcome-input", CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def xǁWelcomeScreenǁaction_clear_input__mutmut_orig(self) -> None:
        cmd_input = self.query_one("#welcome-input", CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def xǁWelcomeScreenǁaction_clear_input__mutmut_1(self) -> None:
        cmd_input = None
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def xǁWelcomeScreenǁaction_clear_input__mutmut_2(self) -> None:
        cmd_input = self.query_one(None, CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def xǁWelcomeScreenǁaction_clear_input__mutmut_3(self) -> None:
        cmd_input = self.query_one("#welcome-input", None)
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def xǁWelcomeScreenǁaction_clear_input__mutmut_4(self) -> None:
        cmd_input = self.query_one(CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def xǁWelcomeScreenǁaction_clear_input__mutmut_5(self) -> None:
        cmd_input = self.query_one("#welcome-input", )
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def xǁWelcomeScreenǁaction_clear_input__mutmut_6(self) -> None:
        cmd_input = self.query_one("XX#welcome-inputXX", CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def xǁWelcomeScreenǁaction_clear_input__mutmut_7(self) -> None:
        cmd_input = self.query_one("#WELCOME-INPUT", CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = ""
        else:
            self.app.exit()

    def xǁWelcomeScreenǁaction_clear_input__mutmut_8(self) -> None:
        cmd_input = self.query_one("#welcome-input", CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = None
        else:
            self.app.exit()

    def xǁWelcomeScreenǁaction_clear_input__mutmut_9(self) -> None:
        cmd_input = self.query_one("#welcome-input", CommandInput)
        if cmd_input.value.strip():
            cmd_input.value = "XXXX"
        else:
            self.app.exit()

    @_mutmut_mutated(mutants_xǁWelcomeScreenǁon_input_submitted__mutmut)
    def on_input_submitted(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return
        from hexawyn.cli.screens.session import SessionScreen
        from hexawyn.cli.tui import HexawynTUI

        app = self.app
        assert isinstance(app, HexawynTUI)
        app.push_screen(SessionScreen(initial_command=text))

    def xǁWelcomeScreenǁon_input_submitted__mutmut_orig(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return
        from hexawyn.cli.screens.session import SessionScreen
        from hexawyn.cli.tui import HexawynTUI

        app = self.app
        assert isinstance(app, HexawynTUI)
        app.push_screen(SessionScreen(initial_command=text))

    def xǁWelcomeScreenǁon_input_submitted__mutmut_1(self, event: Input.Submitted) -> None:
        text = None
        if not text:
            return
        from hexawyn.cli.screens.session import SessionScreen
        from hexawyn.cli.tui import HexawynTUI

        app = self.app
        assert isinstance(app, HexawynTUI)
        app.push_screen(SessionScreen(initial_command=text))

    def xǁWelcomeScreenǁon_input_submitted__mutmut_2(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if text:
            return
        from hexawyn.cli.screens.session import SessionScreen
        from hexawyn.cli.tui import HexawynTUI

        app = self.app
        assert isinstance(app, HexawynTUI)
        app.push_screen(SessionScreen(initial_command=text))

    def xǁWelcomeScreenǁon_input_submitted__mutmut_3(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return
        from hexawyn.cli.screens.session import SessionScreen
        from hexawyn.cli.tui import HexawynTUI

        app = None
        assert isinstance(app, HexawynTUI)
        app.push_screen(SessionScreen(initial_command=text))

    def xǁWelcomeScreenǁon_input_submitted__mutmut_4(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return
        from hexawyn.cli.screens.session import SessionScreen
        from hexawyn.cli.tui import HexawynTUI

        app = self.app
        assert isinstance(app, HexawynTUI)
        app.push_screen(None)

    def xǁWelcomeScreenǁon_input_submitted__mutmut_5(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        if not text:
            return
        from hexawyn.cli.screens.session import SessionScreen
        from hexawyn.cli.tui import HexawynTUI

        app = self.app
        assert isinstance(app, HexawynTUI)
        app.push_screen(SessionScreen(initial_command=None))

mutants_xǁWelcomeScreenǁcompose__mutmut['_mutmut_orig'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_1'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_2'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_3'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_4'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_5'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_6'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_7'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_8'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_9'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_10'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_11'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_12'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_13'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_14'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_15'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_16'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_17'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_18'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_19'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_20'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_21'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_22'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_23'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_24'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_25'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_26'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_26 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_27'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_27 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_28'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_28 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_29'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_29 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_30'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_30 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_31'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_31 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_32'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_32 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_33'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_33 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_34'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_34 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_35'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_35 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_36'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_36 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_37'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_37 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_38'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_38 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_39'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_39 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_40'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_40 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_41'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_41 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_42'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_42 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_43'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_43 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_44'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_44 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_45'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_45 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_46'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_46 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_47'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_47 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_48'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_48 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_49'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_49 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_50'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_50 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_51'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_51 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁcompose__mutmut['xǁWelcomeScreenǁcompose__mutmut_52'] = WelcomeScreen.xǁWelcomeScreenǁcompose__mutmut_52 # type: ignore # mutmut generated

mutants_xǁWelcomeScreenǁon_mount__mutmut['_mutmut_orig'] = WelcomeScreen.xǁWelcomeScreenǁon_mount__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_mount__mutmut['xǁWelcomeScreenǁon_mount__mutmut_1'] = WelcomeScreen.xǁWelcomeScreenǁon_mount__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_mount__mutmut['xǁWelcomeScreenǁon_mount__mutmut_2'] = WelcomeScreen.xǁWelcomeScreenǁon_mount__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_mount__mutmut['xǁWelcomeScreenǁon_mount__mutmut_3'] = WelcomeScreen.xǁWelcomeScreenǁon_mount__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_mount__mutmut['xǁWelcomeScreenǁon_mount__mutmut_4'] = WelcomeScreen.xǁWelcomeScreenǁon_mount__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_mount__mutmut['xǁWelcomeScreenǁon_mount__mutmut_5'] = WelcomeScreen.xǁWelcomeScreenǁon_mount__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_mount__mutmut['xǁWelcomeScreenǁon_mount__mutmut_6'] = WelcomeScreen.xǁWelcomeScreenǁon_mount__mutmut_6 # type: ignore # mutmut generated

mutants_xǁWelcomeScreenǁaction_clear_input__mutmut['_mutmut_orig'] = WelcomeScreen.xǁWelcomeScreenǁaction_clear_input__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁaction_clear_input__mutmut['xǁWelcomeScreenǁaction_clear_input__mutmut_1'] = WelcomeScreen.xǁWelcomeScreenǁaction_clear_input__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁaction_clear_input__mutmut['xǁWelcomeScreenǁaction_clear_input__mutmut_2'] = WelcomeScreen.xǁWelcomeScreenǁaction_clear_input__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁaction_clear_input__mutmut['xǁWelcomeScreenǁaction_clear_input__mutmut_3'] = WelcomeScreen.xǁWelcomeScreenǁaction_clear_input__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁaction_clear_input__mutmut['xǁWelcomeScreenǁaction_clear_input__mutmut_4'] = WelcomeScreen.xǁWelcomeScreenǁaction_clear_input__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁaction_clear_input__mutmut['xǁWelcomeScreenǁaction_clear_input__mutmut_5'] = WelcomeScreen.xǁWelcomeScreenǁaction_clear_input__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁaction_clear_input__mutmut['xǁWelcomeScreenǁaction_clear_input__mutmut_6'] = WelcomeScreen.xǁWelcomeScreenǁaction_clear_input__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁaction_clear_input__mutmut['xǁWelcomeScreenǁaction_clear_input__mutmut_7'] = WelcomeScreen.xǁWelcomeScreenǁaction_clear_input__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁaction_clear_input__mutmut['xǁWelcomeScreenǁaction_clear_input__mutmut_8'] = WelcomeScreen.xǁWelcomeScreenǁaction_clear_input__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁaction_clear_input__mutmut['xǁWelcomeScreenǁaction_clear_input__mutmut_9'] = WelcomeScreen.xǁWelcomeScreenǁaction_clear_input__mutmut_9 # type: ignore # mutmut generated

mutants_xǁWelcomeScreenǁon_input_submitted__mutmut['_mutmut_orig'] = WelcomeScreen.xǁWelcomeScreenǁon_input_submitted__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_input_submitted__mutmut['xǁWelcomeScreenǁon_input_submitted__mutmut_1'] = WelcomeScreen.xǁWelcomeScreenǁon_input_submitted__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_input_submitted__mutmut['xǁWelcomeScreenǁon_input_submitted__mutmut_2'] = WelcomeScreen.xǁWelcomeScreenǁon_input_submitted__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_input_submitted__mutmut['xǁWelcomeScreenǁon_input_submitted__mutmut_3'] = WelcomeScreen.xǁWelcomeScreenǁon_input_submitted__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_input_submitted__mutmut['xǁWelcomeScreenǁon_input_submitted__mutmut_4'] = WelcomeScreen.xǁWelcomeScreenǁon_input_submitted__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWelcomeScreenǁon_input_submitted__mutmut['xǁWelcomeScreenǁon_input_submitted__mutmut_5'] = WelcomeScreen.xǁWelcomeScreenǁon_input_submitted__mutmut_5 # type: ignore # mutmut generated
