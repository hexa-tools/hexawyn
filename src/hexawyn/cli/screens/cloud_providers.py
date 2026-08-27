"""Cloud provider credentials modal for hexawyn TUI — triggered by /providers.

Arrow-up/down moves between cloud providers; each selection renders that
provider's credential fields. Esc closes. Save stores the credentials in
~/.hexawyn/config.yaml and re-injects them as SDK env vars.
"""

from __future__ import annotations

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Static

from hexawyn.infrastructure.config.provider_config import (
    apply_provider_env,
    clear_provider_credentials,
    credential_fields,
    get_provider_credentials,
    set_provider_credentials,
)

_PROVIDERS = ("aws", "gcp", "azure", "datadog")


class CloudProvidersScreen(ModalScreen[None]):
    """Selector + credential form for cloud providers."""

    CSS = """
    CloudProvidersScreen {
        align: center middle;
        background: rgba(5, 7, 13, 0.78);
    }

    #providers-picker {
        width: 66;
        height: auto;
        max-height: 85%;
        overflow-y: auto;
        background: #0b0f17;
        border: round #3B82F6;
        padding: 1 2;
    }

    #providers-title {
        text-style: bold;
        color: #f2f4f8;
        margin-bottom: 1;
    }

    #providers-help {
        color: #8a93a6;
        margin-bottom: 1;
    }

    #providers-list {
        height: auto;
        min-height: 6;
        margin-bottom: 1;
        border: round #2b3850;
        padding: 1 0;
    }

    Button.provider-btn {
        width: 100%;
        background: #131826;
        color: #c7d0e0;
        border: none;
        padding: 0 1;
        text-align: left;
    }

    Button.provider-btn:hover {
        color: #ffffff;
        background: #1a2030;
    }

    Button.provider-btn.-primary {
        background: #1E3A8A;
        color: #ffffff;
        border: round #3B82F6;
    }

    #providers-fields-title {
        color: #8a93a6;
        text-style: bold;
        margin-bottom: 1;
    }

    #providers-fields {
        height: auto;
        margin-bottom: 1;
    }

    .provider-label {
        color: #8a93a6;
        margin-bottom: 1;
    }

    .provider-input {
        background: #131826;
        color: #c7d0e0;
        border: round #2b3850;
        margin-bottom: 1;
        width: 100%;
    }

    .provider-input:focus {
        border: round #3B82F6;
    }

    #providers-status {
        color: #8a93a6;
        min-height: 1;
        margin-bottom: 1;
    }

    Button.providers-action {
        width: 100%;
        background: #3B82F6;
        color: #ffffff;
        border: round #3B82F6;
        margin-bottom: 1;
    }

    Button.providers-action:hover {
        background: #1E3A8A;
    }

    Button.providers-clear {
        width: 100%;
        background: #2b3850;
        color: #fca5a5;
        border: round #2b3850;
        margin-bottom: 1;
    }

    Button.providers-cancel {
        width: 100%;
        background: #0b0f17;
        color: #8a93a6;
        border: round #2b3850;
    }

    Button.providers-cancel:hover {
        border: round #3B82F6;
    }
    """

    BINDINGS = [
        Binding("up", "prev_provider", "Prev provider", show=False),
        Binding("down", "next_provider", "Next provider", show=False),
        Binding("escape", "cancel", "Cancel", show=False),
    ]

    def __init__(self) -> None:
        super().__init__()
        self._selected: str = _PROVIDERS[0]
        self._field_inputs: dict[str, Input] = {}

    def compose(self) -> ComposeResult:
        with Vertical(id="providers-picker"):
            yield Static("🔐  Cloud Provider Credentials", id="providers-title")
            yield Static(
                "Arrow ↑/↓ to switch provider · Esc to close.",
                id="providers-help",
            )
            with Vertical(id="providers-list"):
                for name in _PROVIDERS:
                    yield Button("", id=f"provider-{name}", classes="provider-btn")
            yield Static("Credentials", id="providers-fields-title")
            with Vertical(id="providers-fields"):
                pass
            yield Static("", id="providers-status")
            yield Button(" Save", id="providers-save", classes="providers-action")
            yield Horizontal(
                Button("Clear creds", id="providers-clear", classes="providers-clear"),
                Button("Cancel", id="providers-cancel", classes="providers-cancel"),
            )

    async def on_mount(self) -> None:
        self._render_providers_list()
        await self._render_fields(self._selected)
        self._render_status()
        self._focus_provider(self._selected)

    def action_cancel(self) -> None:
        self.dismiss(None)

    async def action_next_provider(self) -> None:
        await self._step_provider(1)

    async def action_prev_provider(self) -> None:
        await self._step_provider(-1)

    async def _step_provider(self, delta: int) -> None:
        index = _PROVIDERS.index(self._selected)
        next_index = (index + delta) % len(_PROVIDERS)
        await self._select_provider(_PROVIDERS[next_index])

    async def _select_provider(self, name: str) -> None:
        self._selected = name
        self._render_providers_list()
        await self._render_fields(name)
        self._focus_provider(name)

    def _focus_provider(self, name: str) -> None:
        try:
            self.query_one(f"#provider-{name}", Button).focus()
        except Exception:
            pass

    def _render_providers_list(self) -> None:
        for name in _PROVIDERS:
            creds = get_provider_credentials(name)
            marker = "✔" if creds else "·"
            detail = ", ".join(f"{key}=*****" for key in sorted(creds)) if creds else "no creds"
            button = self.query_one(f"#provider-{name}", Button)
            button.label = f"  {marker}  {name:<8}  {detail}"
            button.variant = "primary" if name == self._selected else "default"

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id or ""
        if button_id == "providers-cancel":
            self.dismiss(None)
        elif button_id == "providers-save":
            self._save()
        elif button_id == "providers-clear":
            clear_provider_credentials(self._selected)
            self._render_providers_list()
            self._render_status("Credentials cleared.")
        elif button_id and button_id.startswith("provider-"):
            await self._select_provider(button_id.removeprefix("provider-"))

    async def _render_fields(self, provider: str) -> None:
        container = self.query_one("#providers-fields", Vertical)
        await container.remove_children()
        self._field_inputs = {}
        fields = credential_fields(provider)
        if not fields:
            await container.mount(
                Static("(no credentials — uses kubeconfig)", classes="provider-label")
            )
            return
        for key, label in fields:
            await container.mount(Static(f"{label}:", classes="provider-label"))
            field_input = Input(
                placeholder=f"{label}",
                id=f"field-{key}",
                password=True,
                classes="provider-input",
            )
            self._field_inputs[key] = field_input
            await container.mount(field_input)

    def _collect_values(self) -> dict[str, str]:
        values: dict[str, str] = {}
        for key, field_input in self._field_inputs.items():
            value = field_input.value.strip()
            if value:
                values[key] = value
        return values

    def _save(self) -> None:
        values = self._collect_values()
        if not values:
            self._render_status("[red]Enter at least one credential key.[/]")
            return
        set_provider_credentials(self._selected, values)
        apply_provider_env(self._selected)
        self._render_providers_list()
        self._render_status(f"[green]✓ Credentials stored for {self._selected}.[/]")

    def _render_status(self, message: str = "") -> None:
        provider = self._selected
        status_widget = self.query_one("#providers-status", Static)
        creds = get_provider_credentials(provider)
        if message:
            status_widget.update(message)
            return
        if creds:
            keys = ", ".join(f"{key}=*****" for key in sorted(creds))
            status_widget.update(f"[green]✓ {provider}: creds set —[/] [dim]{keys}[/]")
        else:
            status_widget.update(f"[dim]{provider}: no creds set[/]")
