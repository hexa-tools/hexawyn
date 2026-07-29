"""Token activation modal screen for hexawyn TUI — triggered by /token."""

import asyncio
from pathlib import Path

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Static


def _format_expiry(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def _get_current_plan() -> str | None:
    """Read current license plan from ~/.hexawyn/license.key if it exists."""
    from hexawyn.infrastructure.license.license_reader import read_license_state

    state = read_license_state()
    if state.state in ("missing", "invalid"):
        return None
    return state.plan


class TokenInputScreen(ModalScreen[str | None]):
    CSS = """
    TokenInputScreen {
        align: center middle;
        background: rgba(5, 7, 13, 0.72);
    }

    #token-picker {
        width: 62;
        height: auto;
        background: #0b0f17;
        border: round #3B82F6;
        padding: 1 2;
    }

    #token-picker-title {
        text-style: bold;
        color: #f2f4f8;
        margin-bottom: 1;
    }

    #token-picker-help {
        color: #8a93a6;
        margin-bottom: 1;
    }

    #token-input {
        background: #131826;
        color: #c7d0e0;
        border: round #2b3850;
        margin-bottom: 1;
        width: 100%;
    }

    #token-input:focus {
        border: round #3B82F6;
    }

    #token-status {
        color: #8a93a6;
        min-height: 1;
        margin-bottom: 1;
    }

    Button.token-action {
        width: 100%;
        background: #3B82F6;
        color: #ffffff;
        border: round #3B82F6;
        margin-bottom: 1;
    }

    Button.token-action:hover {
        background: #1E3A8A;
    }

    #token-cancel {
        width: 100%;
        background: #0b0f17;
        color: #8a93a6;
        border: round #2b3850;
    }

    #token-cancel:hover {
        border: round #3B82F6;
    }
    """

    BINDINGS = [
        Binding("escape", "cancel", "Cancel", show=False),
    ]

    def compose(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "hexawyn License"
            help_text = (
                f"[green]✓ Currently activated — Plan: [bold]{current_plan}[/bold][/]\n"
                "Paste a new token to replace, or Esc to cancel."
            )

        with Vertical(id="token-picker"):
            yield Static(title, id="token-picker-title")
            yield Static(help_text, id="token-picker-help")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def action_cancel(self) -> None:
        self.dismiss(None)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one("#token-status", Static).update(
                    "[bold red]Please enter your token first.[/]"
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    async def _do_activate(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = get_machine_id()
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.post(
                    "https://api.hexawyn.com/api/v1/license/activate",
                    json={
                        "api_key": token,
                        "machine_id": machine_id,
                        "client_version": "1.0.0",
                    },
                )
        except Exception as exc:
            status.update(f"[bold red]Connection failed: {exc}[/]")
            return

        if response.status_code != 200:  # noqa: PLR2004
            detail = "Unknown error"
            try:
                detail = response.json().get("detail", detail)
            except Exception:
                pass
            status.update(f"[bold red]Activation failed: {detail}[/]")
            return

        data = response.json()
        jwt_token = data.get("token", "")
        plan = data.get("plan", "unknown")
        expires_at = data.get("expires_at", "")

        license_dir = Path.home() / ".hexawyn"
        license_dir.mkdir(parents=True, exist_ok=True)
        (license_dir / "license.key").write_text(jwt_token)

        from hexawyn.infrastructure.config.config_manager import load_config, save_config

        cfg = load_config()
        cfg["hexawyn_token"] = token
        cfg["hexawyn_token_prefix"] = token[: min(len(token), 16)]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])
