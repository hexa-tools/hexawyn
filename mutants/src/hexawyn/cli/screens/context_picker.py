from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Static

from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext as KubernetesClusterContext,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁContextPickerScreenǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁContextPickerScreenǁcompose__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContextPickerScreenǁaction_focus_next_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContextPickerScreenǁaction_focus_previous_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContextPickerScreenǁ_current_context_index__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut: MutantDict = {}  # type: ignore
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut: MutantDict = {}  # type: ignore


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

    @_mutmut_mutated(mutants_xǁContextPickerScreenǁ__init____mutmut)
    def __init__(self, contexts: list[KubernetesClusterContext]) -> None:
        super().__init__()
        self._contexts = contexts
        self._focused_context_index = self._current_context_index()

    def xǁContextPickerScreenǁ__init____mutmut_orig(self, contexts: list[KubernetesClusterContext]) -> None:
        super().__init__()
        self._contexts = contexts
        self._focused_context_index = self._current_context_index()

    def xǁContextPickerScreenǁ__init____mutmut_1(self, contexts: list[KubernetesClusterContext]) -> None:
        super().__init__()
        self._contexts = None
        self._focused_context_index = self._current_context_index()

    def xǁContextPickerScreenǁ__init____mutmut_2(self, contexts: list[KubernetesClusterContext]) -> None:
        super().__init__()
        self._contexts = contexts
        self._focused_context_index = None

    @_mutmut_mutated(mutants_xǁContextPickerScreenǁcompose__mutmut)
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

    def xǁContextPickerScreenǁcompose__mutmut_orig(self) -> ComposeResult:
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

    def xǁContextPickerScreenǁcompose__mutmut_1(self) -> ComposeResult:
        with Vertical(id=None):
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

    def xǁContextPickerScreenǁcompose__mutmut_2(self) -> ComposeResult:
        with Vertical(id="XXcontext-pickerXX"):
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

    def xǁContextPickerScreenǁcompose__mutmut_3(self) -> ComposeResult:
        with Vertical(id="CONTEXT-PICKER"):
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

    def xǁContextPickerScreenǁcompose__mutmut_4(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static(None, id="context-picker-title")
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

    def xǁContextPickerScreenǁcompose__mutmut_5(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id=None)
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

    def xǁContextPickerScreenǁcompose__mutmut_6(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static(id="context-picker-title")
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

    def xǁContextPickerScreenǁcompose__mutmut_7(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", )
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

    def xǁContextPickerScreenǁcompose__mutmut_8(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("XXSwitch Kubernetes ContextXX", id="context-picker-title")
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

    def xǁContextPickerScreenǁcompose__mutmut_9(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("switch kubernetes context", id="context-picker-title")
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

    def xǁContextPickerScreenǁcompose__mutmut_10(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("SWITCH KUBERNETES CONTEXT", id="context-picker-title")
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

    def xǁContextPickerScreenǁcompose__mutmut_11(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="XXcontext-picker-titleXX")
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

    def xǁContextPickerScreenǁcompose__mutmut_12(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="CONTEXT-PICKER-TITLE")
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

    def xǁContextPickerScreenǁcompose__mutmut_13(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                None,
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

    def xǁContextPickerScreenǁcompose__mutmut_14(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id=None,
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

    def xǁContextPickerScreenǁcompose__mutmut_15(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
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

    def xǁContextPickerScreenǁcompose__mutmut_16(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
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

    def xǁContextPickerScreenǁcompose__mutmut_17(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "XXSelect a context to reconnect without restarting Hexawyn.XX",
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

    def xǁContextPickerScreenǁcompose__mutmut_18(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "select a context to reconnect without restarting hexawyn.",
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

    def xǁContextPickerScreenǁcompose__mutmut_19(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "SELECT A CONTEXT TO RECONNECT WITHOUT RESTARTING HEXAWYN.",
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

    def xǁContextPickerScreenǁcompose__mutmut_20(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="XXcontext-picker-helpXX",
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

    def xǁContextPickerScreenǁcompose__mutmut_21(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="CONTEXT-PICKER-HELP",
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

    def xǁContextPickerScreenǁcompose__mutmut_22(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="context-picker-help",
            )
            for context in self._contexts:
                current_marker = None
                classes = (
                    "context-option current-context" if context.is_current else "context-option"
                )
                yield Button(
                    f"{current_marker}{context.name}  ·  {context.namespace}",
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_23(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="context-picker-help",
            )
            for context in self._contexts:
                current_marker = "XX✓ XX" if context.is_current else "  "
                classes = (
                    "context-option current-context" if context.is_current else "context-option"
                )
                yield Button(
                    f"{current_marker}{context.name}  ·  {context.namespace}",
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_24(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="context-picker-help",
            )
            for context in self._contexts:
                current_marker = "✓ " if context.is_current else "XX  XX"
                classes = (
                    "context-option current-context" if context.is_current else "context-option"
                )
                yield Button(
                    f"{current_marker}{context.name}  ·  {context.namespace}",
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_25(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="context-picker-help",
            )
            for context in self._contexts:
                current_marker = "✓ " if context.is_current else "  "
                classes = None
                yield Button(
                    f"{current_marker}{context.name}  ·  {context.namespace}",
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_26(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="context-picker-help",
            )
            for context in self._contexts:
                current_marker = "✓ " if context.is_current else "  "
                classes = (
                    "XXcontext-option current-contextXX" if context.is_current else "context-option"
                )
                yield Button(
                    f"{current_marker}{context.name}  ·  {context.namespace}",
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_27(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="context-picker-help",
            )
            for context in self._contexts:
                current_marker = "✓ " if context.is_current else "  "
                classes = (
                    "CONTEXT-OPTION CURRENT-CONTEXT" if context.is_current else "context-option"
                )
                yield Button(
                    f"{current_marker}{context.name}  ·  {context.namespace}",
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_28(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="context-picker-help",
            )
            for context in self._contexts:
                current_marker = "✓ " if context.is_current else "  "
                classes = (
                    "context-option current-context" if context.is_current else "XXcontext-optionXX"
                )
                yield Button(
                    f"{current_marker}{context.name}  ·  {context.namespace}",
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_29(self) -> ComposeResult:
        with Vertical(id="context-picker"):
            yield Static("Switch Kubernetes Context", id="context-picker-title")
            yield Static(
                "Select a context to reconnect without restarting Hexawyn.",
                id="context-picker-help",
            )
            for context in self._contexts:
                current_marker = "✓ " if context.is_current else "  "
                classes = (
                    "context-option current-context" if context.is_current else "CONTEXT-OPTION"
                )
                yield Button(
                    f"{current_marker}{context.name}  ·  {context.namespace}",
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_30(self) -> ComposeResult:
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
                    None,
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_31(self) -> ComposeResult:
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
                    id=None,
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_32(self) -> ComposeResult:
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
                    classes=None,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_33(self) -> ComposeResult:
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
                    id=f"context-{context.name}",
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_34(self) -> ComposeResult:
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
                    classes=classes,
                )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_35(self) -> ComposeResult:
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
                    )
            yield Button("Cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_36(self) -> ComposeResult:
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
            yield Button(None, id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_37(self) -> ComposeResult:
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
            yield Button("Cancel", id=None)

    def xǁContextPickerScreenǁcompose__mutmut_38(self) -> ComposeResult:
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
            yield Button(id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_39(self) -> ComposeResult:
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
            yield Button("Cancel", )

    def xǁContextPickerScreenǁcompose__mutmut_40(self) -> ComposeResult:
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
            yield Button("XXCancelXX", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_41(self) -> ComposeResult:
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
            yield Button("cancel", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_42(self) -> ComposeResult:
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
            yield Button("CANCEL", id="context-cancel")

    def xǁContextPickerScreenǁcompose__mutmut_43(self) -> ComposeResult:
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
            yield Button("Cancel", id="XXcontext-cancelXX")

    def xǁContextPickerScreenǁcompose__mutmut_44(self) -> ComposeResult:
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
            yield Button("Cancel", id="CONTEXT-CANCEL")

    def on_mount(self) -> None:
        self._focus_context_button()

    @_mutmut_mutated(mutants_xǁContextPickerScreenǁaction_focus_next_context__mutmut)
    def action_focus_next_context(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index + 1) % len(self._contexts)
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_next_context__mutmut_orig(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index + 1) % len(self._contexts)
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_next_context__mutmut_1(self) -> None:
        if self._contexts:
            return
        self._focused_context_index = (self._focused_context_index + 1) % len(self._contexts)
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_next_context__mutmut_2(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = None
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_next_context__mutmut_3(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index + 1) / len(self._contexts)
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_next_context__mutmut_4(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index - 1) % len(self._contexts)
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_next_context__mutmut_5(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index + 2) % len(self._contexts)
        self._focus_context_button()

    @_mutmut_mutated(mutants_xǁContextPickerScreenǁaction_focus_previous_context__mutmut)
    def action_focus_previous_context(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index - 1) % len(self._contexts)
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_previous_context__mutmut_orig(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index - 1) % len(self._contexts)
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_previous_context__mutmut_1(self) -> None:
        if self._contexts:
            return
        self._focused_context_index = (self._focused_context_index - 1) % len(self._contexts)
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_previous_context__mutmut_2(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = None
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_previous_context__mutmut_3(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index - 1) / len(self._contexts)
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_previous_context__mutmut_4(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index + 1) % len(self._contexts)
        self._focus_context_button()

    def xǁContextPickerScreenǁaction_focus_previous_context__mutmut_5(self) -> None:
        if not self._contexts:
            return
        self._focused_context_index = (self._focused_context_index - 2) % len(self._contexts)
        self._focus_context_button()

    def action_cancel(self) -> None:
        self.dismiss(None)

    @_mutmut_mutated(mutants_xǁContextPickerScreenǁ_current_context_index__mutmut)
    def _current_context_index(self) -> int:
        for context_index, context in enumerate(self._contexts):
            if context.is_current:
                return context_index
        return 0

    def xǁContextPickerScreenǁ_current_context_index__mutmut_orig(self) -> int:
        for context_index, context in enumerate(self._contexts):
            if context.is_current:
                return context_index
        return 0

    def xǁContextPickerScreenǁ_current_context_index__mutmut_1(self) -> int:
        for context_index, context in enumerate(None):
            if context.is_current:
                return context_index
        return 0

    def xǁContextPickerScreenǁ_current_context_index__mutmut_2(self) -> int:
        for context_index, context in enumerate(self._contexts):
            if context.is_current:
                return context_index
        return 1

    @_mutmut_mutated(mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut)
    def _focus_context_button(self) -> None:
        if not self._contexts:
            self.query_one("#context-cancel", Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_orig(self) -> None:
        if not self._contexts:
            self.query_one("#context-cancel", Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_1(self) -> None:
        if self._contexts:
            self.query_one("#context-cancel", Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_2(self) -> None:
        if not self._contexts:
            self.query_one(None, Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_3(self) -> None:
        if not self._contexts:
            self.query_one("#context-cancel", None).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_4(self) -> None:
        if not self._contexts:
            self.query_one(Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_5(self) -> None:
        if not self._contexts:
            self.query_one("#context-cancel", ).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_6(self) -> None:
        if not self._contexts:
            self.query_one("XX#context-cancelXX", Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_7(self) -> None:
        if not self._contexts:
            self.query_one("#CONTEXT-CANCEL", Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_8(self) -> None:
        if not self._contexts:
            self.query_one("#context-cancel", Button).focus()
            return
        context = None
        self.query_one(f"#context-{context.name}", Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_9(self) -> None:
        if not self._contexts:
            self.query_one("#context-cancel", Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(None, Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_10(self) -> None:
        if not self._contexts:
            self.query_one("#context-cancel", Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", None).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_11(self) -> None:
        if not self._contexts:
            self.query_one("#context-cancel", Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(Button).focus()

    def xǁContextPickerScreenǁ_focus_context_button__mutmut_12(self) -> None:
        if not self._contexts:
            self.query_one("#context-cancel", Button).focus()
            return
        context = self._contexts[self._focused_context_index]
        self.query_one(f"#context-{context.name}", ).focus()

    @_mutmut_mutated(mutants_xǁContextPickerScreenǁon_button_pressed__mutmut)
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removeprefix("context-"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_orig(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removeprefix("context-"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_1(self, event: Button.Pressed) -> None:
        if event.button.id != "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removeprefix("context-"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_2(self, event: Button.Pressed) -> None:
        if event.button.id == "XXcontext-cancelXX":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removeprefix("context-"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_3(self, event: Button.Pressed) -> None:
        if event.button.id == "CONTEXT-CANCEL":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removeprefix("context-"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_4(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id or event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removeprefix("context-"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_5(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith(None):
            self.dismiss(event.button.id.removeprefix("context-"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_6(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("XXcontext-XX"):
            self.dismiss(event.button.id.removeprefix("context-"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_7(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("CONTEXT-"):
            self.dismiss(event.button.id.removeprefix("context-"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_8(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(None)

    def xǁContextPickerScreenǁon_button_pressed__mutmut_9(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removeprefix(None))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_10(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removesuffix("context-"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_11(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removeprefix("XXcontext-XX"))

    def xǁContextPickerScreenǁon_button_pressed__mutmut_12(self, event: Button.Pressed) -> None:
        if event.button.id == "context-cancel":
            self.dismiss(None)
            return

        if event.button.id and event.button.id.startswith("context-"):
            self.dismiss(event.button.id.removeprefix("CONTEXT-"))

    def action_clear_input(self) -> None:
        self.dismiss(None)

mutants_xǁContextPickerScreenǁ__init____mutmut['_mutmut_orig'] = ContextPickerScreen.xǁContextPickerScreenǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ__init____mutmut['xǁContextPickerScreenǁ__init____mutmut_1'] = ContextPickerScreen.xǁContextPickerScreenǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ__init____mutmut['xǁContextPickerScreenǁ__init____mutmut_2'] = ContextPickerScreen.xǁContextPickerScreenǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁContextPickerScreenǁcompose__mutmut['_mutmut_orig'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_1'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_2'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_3'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_4'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_5'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_5 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_6'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_6 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_7'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_7 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_8'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_8 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_9'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_9 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_10'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_10 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_11'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_11 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_12'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_12 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_13'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_13 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_14'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_14 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_15'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_15 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_16'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_16 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_17'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_17 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_18'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_18 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_19'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_19 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_20'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_20 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_21'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_21 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_22'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_22 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_23'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_23 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_24'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_24 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_25'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_25 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_26'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_26 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_27'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_27 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_28'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_28 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_29'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_29 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_30'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_30 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_31'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_31 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_32'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_32 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_33'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_33 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_34'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_34 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_35'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_35 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_36'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_36 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_37'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_37 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_38'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_38 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_39'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_39 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_40'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_40 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_41'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_41 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_42'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_42 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_43'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_43 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁcompose__mutmut['xǁContextPickerScreenǁcompose__mutmut_44'] = ContextPickerScreen.xǁContextPickerScreenǁcompose__mutmut_44 # type: ignore # mutmut generated

mutants_xǁContextPickerScreenǁaction_focus_next_context__mutmut['_mutmut_orig'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_next_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁaction_focus_next_context__mutmut['xǁContextPickerScreenǁaction_focus_next_context__mutmut_1'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_next_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁaction_focus_next_context__mutmut['xǁContextPickerScreenǁaction_focus_next_context__mutmut_2'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_next_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁaction_focus_next_context__mutmut['xǁContextPickerScreenǁaction_focus_next_context__mutmut_3'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_next_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁaction_focus_next_context__mutmut['xǁContextPickerScreenǁaction_focus_next_context__mutmut_4'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_next_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁaction_focus_next_context__mutmut['xǁContextPickerScreenǁaction_focus_next_context__mutmut_5'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_next_context__mutmut_5 # type: ignore # mutmut generated

mutants_xǁContextPickerScreenǁaction_focus_previous_context__mutmut['_mutmut_orig'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_previous_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁaction_focus_previous_context__mutmut['xǁContextPickerScreenǁaction_focus_previous_context__mutmut_1'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_previous_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁaction_focus_previous_context__mutmut['xǁContextPickerScreenǁaction_focus_previous_context__mutmut_2'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_previous_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁaction_focus_previous_context__mutmut['xǁContextPickerScreenǁaction_focus_previous_context__mutmut_3'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_previous_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁaction_focus_previous_context__mutmut['xǁContextPickerScreenǁaction_focus_previous_context__mutmut_4'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_previous_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁaction_focus_previous_context__mutmut['xǁContextPickerScreenǁaction_focus_previous_context__mutmut_5'] = ContextPickerScreen.xǁContextPickerScreenǁaction_focus_previous_context__mutmut_5 # type: ignore # mutmut generated

mutants_xǁContextPickerScreenǁ_current_context_index__mutmut['_mutmut_orig'] = ContextPickerScreen.xǁContextPickerScreenǁ_current_context_index__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_current_context_index__mutmut['xǁContextPickerScreenǁ_current_context_index__mutmut_1'] = ContextPickerScreen.xǁContextPickerScreenǁ_current_context_index__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_current_context_index__mutmut['xǁContextPickerScreenǁ_current_context_index__mutmut_2'] = ContextPickerScreen.xǁContextPickerScreenǁ_current_context_index__mutmut_2 # type: ignore # mutmut generated

mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['_mutmut_orig'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_1'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_2'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_3'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_4'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_5'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_5 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_6'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_6 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_7'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_7 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_8'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_8 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_9'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_9 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_10'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_10 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_11'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_11 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁ_focus_context_button__mutmut['xǁContextPickerScreenǁ_focus_context_button__mutmut_12'] = ContextPickerScreen.xǁContextPickerScreenǁ_focus_context_button__mutmut_12 # type: ignore # mutmut generated

mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['_mutmut_orig'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_1'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_2'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_3'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_4'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_4 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_5'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_5 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_6'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_6 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_7'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_7 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_8'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_8 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_9'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_9 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_10'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_10 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_11'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_11 # type: ignore # mutmut generated
mutants_xǁContextPickerScreenǁon_button_pressed__mutmut['xǁContextPickerScreenǁon_button_pressed__mutmut_12'] = ContextPickerScreen.xǁContextPickerScreenǁon_button_pressed__mutmut_12 # type: ignore # mutmut generated
