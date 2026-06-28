from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Static

from hexawyn.infrastructure.config.kubernetes_context import (
    ClusterContext as KubernetesClusterContext,
)


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
