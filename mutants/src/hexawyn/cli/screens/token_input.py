"""Token activation modal screen for hexawyn TUI — triggered by /token."""

import asyncio
from pathlib import Path

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Static


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__format_expiry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__format_expiry__mutmut)
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


def x__format_expiry__mutmut_orig(expires_at: str) -> str:
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


def x__format_expiry__mutmut_1(expires_at: str) -> str:
    if expires_at:
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


def x__format_expiry__mutmut_2(expires_at: str) -> str:
    if not expires_at:
        return "XXunknownXX"
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


def x__format_expiry__mutmut_3(expires_at: str) -> str:
    if not expires_at:
        return "UNKNOWN"
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


def x__format_expiry__mutmut_4(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = None
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_5(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(None, tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_6(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=None)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_7(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_8(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), )
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_9(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(None), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_10(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = None
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_11(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(None)
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_12(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace(None, "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_13(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", None))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_14(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_15(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", ))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_16(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("XXZXX", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_17(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_18(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "XX+00:00XX"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_19(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = None
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_20(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt + datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_21(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(None)).days
        return f"{dt.strftime('%d %b %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_22(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime(None)} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_23(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('XX%d %b %YXX')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_24(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%d %b %y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def x__format_expiry__mutmut_25(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        from datetime import UTC, datetime

        if expires_at.isdigit():
            dt = datetime.fromtimestamp(int(expires_at), tz=UTC)
        else:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{dt.strftime('%D %B %Y')} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at

mutants_x__format_expiry__mutmut['_mutmut_orig'] = x__format_expiry__mutmut_orig # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_1'] = x__format_expiry__mutmut_1 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_2'] = x__format_expiry__mutmut_2 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_3'] = x__format_expiry__mutmut_3 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_4'] = x__format_expiry__mutmut_4 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_5'] = x__format_expiry__mutmut_5 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_6'] = x__format_expiry__mutmut_6 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_7'] = x__format_expiry__mutmut_7 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_8'] = x__format_expiry__mutmut_8 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_9'] = x__format_expiry__mutmut_9 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_10'] = x__format_expiry__mutmut_10 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_11'] = x__format_expiry__mutmut_11 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_12'] = x__format_expiry__mutmut_12 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_13'] = x__format_expiry__mutmut_13 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_14'] = x__format_expiry__mutmut_14 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_15'] = x__format_expiry__mutmut_15 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_16'] = x__format_expiry__mutmut_16 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_17'] = x__format_expiry__mutmut_17 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_18'] = x__format_expiry__mutmut_18 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_19'] = x__format_expiry__mutmut_19 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_20'] = x__format_expiry__mutmut_20 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_21'] = x__format_expiry__mutmut_21 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_22'] = x__format_expiry__mutmut_22 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_23'] = x__format_expiry__mutmut_23 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_24'] = x__format_expiry__mutmut_24 # type: ignore # mutmut generated
mutants_x__format_expiry__mutmut['x__format_expiry__mutmut_25'] = x__format_expiry__mutmut_25 # type: ignore # mutmut generated
mutants_x__get_current_plan__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_current_plan__mutmut)
def _get_current_plan() -> str | None:
    """Read current license plan from ~/.hexawyn/license.key if it exists."""
    from hexawyn.infrastructure.license.license_reader import read_license_state

    state = read_license_state()
    if state.state in ("missing", "invalid"):
        return None
    return state.plan


def x__get_current_plan__mutmut_orig() -> str | None:
    """Read current license plan from ~/.hexawyn/license.key if it exists."""
    from hexawyn.infrastructure.license.license_reader import read_license_state

    state = read_license_state()
    if state.state in ("missing", "invalid"):
        return None
    return state.plan


def x__get_current_plan__mutmut_1() -> str | None:
    """Read current license plan from ~/.hexawyn/license.key if it exists."""
    from hexawyn.infrastructure.license.license_reader import read_license_state

    state = None
    if state.state in ("missing", "invalid"):
        return None
    return state.plan


def x__get_current_plan__mutmut_2() -> str | None:
    """Read current license plan from ~/.hexawyn/license.key if it exists."""
    from hexawyn.infrastructure.license.license_reader import read_license_state

    state = read_license_state()
    if state.state not in ("missing", "invalid"):
        return None
    return state.plan


def x__get_current_plan__mutmut_3() -> str | None:
    """Read current license plan from ~/.hexawyn/license.key if it exists."""
    from hexawyn.infrastructure.license.license_reader import read_license_state

    state = read_license_state()
    if state.state in ("XXmissingXX", "invalid"):
        return None
    return state.plan


def x__get_current_plan__mutmut_4() -> str | None:
    """Read current license plan from ~/.hexawyn/license.key if it exists."""
    from hexawyn.infrastructure.license.license_reader import read_license_state

    state = read_license_state()
    if state.state in ("MISSING", "invalid"):
        return None
    return state.plan


def x__get_current_plan__mutmut_5() -> str | None:
    """Read current license plan from ~/.hexawyn/license.key if it exists."""
    from hexawyn.infrastructure.license.license_reader import read_license_state

    state = read_license_state()
    if state.state in ("missing", "XXinvalidXX"):
        return None
    return state.plan


def x__get_current_plan__mutmut_6() -> str | None:
    """Read current license plan from ~/.hexawyn/license.key if it exists."""
    from hexawyn.infrastructure.license.license_reader import read_license_state

    state = read_license_state()
    if state.state in ("missing", "INVALID"):
        return None
    return state.plan

mutants_x__get_current_plan__mutmut['_mutmut_orig'] = x__get_current_plan__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_current_plan__mutmut['x__get_current_plan__mutmut_1'] = x__get_current_plan__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_current_plan__mutmut['x__get_current_plan__mutmut_2'] = x__get_current_plan__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_current_plan__mutmut['x__get_current_plan__mutmut_3'] = x__get_current_plan__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_current_plan__mutmut['x__get_current_plan__mutmut_4'] = x__get_current_plan__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_current_plan__mutmut['x__get_current_plan__mutmut_5'] = x__get_current_plan__mutmut_5 # type: ignore # mutmut generated
mutants_x__get_current_plan__mutmut['x__get_current_plan__mutmut_6'] = x__get_current_plan__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTokenInputScreenǁ_do_activate__mutmut: MutantDict = {}  # type: ignore


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

    @_mutmut_mutated(mutants_xǁTokenInputScreenǁcompose__mutmut)
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

    def xǁTokenInputScreenǁcompose__mutmut_orig(self) -> ComposeResult:
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

    def xǁTokenInputScreenǁcompose__mutmut_1(self) -> ComposeResult:
        current_plan = None
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

    def xǁTokenInputScreenǁcompose__mutmut_2(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = None
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

    def xǁTokenInputScreenǁcompose__mutmut_3(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "XXActivate hexawyn LicenseXX"
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

    def xǁTokenInputScreenǁcompose__mutmut_4(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "activate hexawyn license"
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

    def xǁTokenInputScreenǁcompose__mutmut_5(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "ACTIVATE HEXAWYN LICENSE"
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

    def xǁTokenInputScreenǁcompose__mutmut_6(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = None

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

    def xǁTokenInputScreenǁcompose__mutmut_7(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "XXPaste your hexawyn API key received by email after subscribing.XX"

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

    def xǁTokenInputScreenǁcompose__mutmut_8(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "paste your hexawyn api key received by email after subscribing."

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

    def xǁTokenInputScreenǁcompose__mutmut_9(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "PASTE YOUR HEXAWYN API KEY RECEIVED BY EMAIL AFTER SUBSCRIBING."

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

    def xǁTokenInputScreenǁcompose__mutmut_10(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = None
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

    def xǁTokenInputScreenǁcompose__mutmut_11(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "XXhexawyn LicenseXX"
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

    def xǁTokenInputScreenǁcompose__mutmut_12(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "hexawyn license"
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

    def xǁTokenInputScreenǁcompose__mutmut_13(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "HEXAWYN LICENSE"
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

    def xǁTokenInputScreenǁcompose__mutmut_14(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "hexawyn License"
            help_text = None

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

    def xǁTokenInputScreenǁcompose__mutmut_15(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "hexawyn License"
            help_text = (
                f"[green]✓ Currently activated — Plan: [bold]{current_plan}[/bold][/]\n"
                "XXPaste a new token to replace, or Esc to cancel.XX"
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

    def xǁTokenInputScreenǁcompose__mutmut_16(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "hexawyn License"
            help_text = (
                f"[green]✓ Currently activated — Plan: [bold]{current_plan}[/bold][/]\n"
                "paste a new token to replace, or esc to cancel."
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

    def xǁTokenInputScreenǁcompose__mutmut_17(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "hexawyn License"
            help_text = (
                f"[green]✓ Currently activated — Plan: [bold]{current_plan}[/bold][/]\n"
                "PASTE A NEW TOKEN TO REPLACE, OR ESC TO CANCEL."
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

    def xǁTokenInputScreenǁcompose__mutmut_18(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "hexawyn License"
            help_text = (
                f"[green]✓ Currently activated — Plan: [bold]{current_plan}[/bold][/]\n"
                "Paste a new token to replace, or Esc to cancel."
            )

        with Vertical(id=None):
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

    def xǁTokenInputScreenǁcompose__mutmut_19(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "hexawyn License"
            help_text = (
                f"[green]✓ Currently activated — Plan: [bold]{current_plan}[/bold][/]\n"
                "Paste a new token to replace, or Esc to cancel."
            )

        with Vertical(id="XXtoken-pickerXX"):
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

    def xǁTokenInputScreenǁcompose__mutmut_20(self) -> ComposeResult:
        current_plan = _get_current_plan()
        title = "Activate hexawyn License"
        help_text = "Paste your hexawyn API key received by email after subscribing."

        if current_plan:
            title = "hexawyn License"
            help_text = (
                f"[green]✓ Currently activated — Plan: [bold]{current_plan}[/bold][/]\n"
                "Paste a new token to replace, or Esc to cancel."
            )

        with Vertical(id="TOKEN-PICKER"):
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

    def xǁTokenInputScreenǁcompose__mutmut_21(self) -> ComposeResult:
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
            yield Static(None, id="token-picker-title")
            yield Static(help_text, id="token-picker-help")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_22(self) -> ComposeResult:
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
            yield Static(title, id=None)
            yield Static(help_text, id="token-picker-help")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_23(self) -> ComposeResult:
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
            yield Static(id="token-picker-title")
            yield Static(help_text, id="token-picker-help")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_24(self) -> ComposeResult:
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
            yield Static(title, )
            yield Static(help_text, id="token-picker-help")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_25(self) -> ComposeResult:
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
            yield Static(title, id="XXtoken-picker-titleXX")
            yield Static(help_text, id="token-picker-help")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_26(self) -> ComposeResult:
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
            yield Static(title, id="TOKEN-PICKER-TITLE")
            yield Static(help_text, id="token-picker-help")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_27(self) -> ComposeResult:
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
            yield Static(None, id="token-picker-help")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_28(self) -> ComposeResult:
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
            yield Static(help_text, id=None)
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_29(self) -> ComposeResult:
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
            yield Static(id="token-picker-help")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_30(self) -> ComposeResult:
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
            yield Static(help_text, )
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_31(self) -> ComposeResult:
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
            yield Static(help_text, id="XXtoken-picker-helpXX")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_32(self) -> ComposeResult:
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
            yield Static(help_text, id="TOKEN-PICKER-HELP")
            yield Input(
                placeholder="Paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_33(self) -> ComposeResult:
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
                placeholder=None,
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_34(self) -> ComposeResult:
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
                id=None,
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_35(self) -> ComposeResult:
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
                password=None,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_36(self) -> ComposeResult:
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
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_37(self) -> ComposeResult:
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
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_38(self) -> ComposeResult:
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
                )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_39(self) -> ComposeResult:
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
                placeholder="XXPaste your token here...XX",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_40(self) -> ComposeResult:
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
                placeholder="paste your token here...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_41(self) -> ComposeResult:
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
                placeholder="PASTE YOUR TOKEN HERE...",
                id="token-input",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_42(self) -> ComposeResult:
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
                id="XXtoken-inputXX",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_43(self) -> ComposeResult:
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
                id="TOKEN-INPUT",
                password=True,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_44(self) -> ComposeResult:
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
                password=False,
            )
            yield Static("", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_45(self) -> ComposeResult:
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
            yield Static(None, id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_46(self) -> ComposeResult:
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
            yield Static("", id=None)
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_47(self) -> ComposeResult:
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
            yield Static(id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_48(self) -> ComposeResult:
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
            yield Static("", )
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_49(self) -> ComposeResult:
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
            yield Static("XXXX", id="token-status")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_50(self) -> ComposeResult:
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
            yield Static("", id="XXtoken-statusXX")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_51(self) -> ComposeResult:
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
            yield Static("", id="TOKEN-STATUS")
            yield Button(" Activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_52(self) -> ComposeResult:
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
            yield Button(None, id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_53(self) -> ComposeResult:
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
            yield Button(" Activate", id=None, classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_54(self) -> ComposeResult:
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
            yield Button(" Activate", id="token-activate", classes=None)
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_55(self) -> ComposeResult:
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
            yield Button(id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_56(self) -> ComposeResult:
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
            yield Button(" Activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_57(self) -> ComposeResult:
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
            yield Button(" Activate", id="token-activate", )
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_58(self) -> ComposeResult:
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
            yield Button("XX ActivateXX", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_59(self) -> ComposeResult:
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
            yield Button(" activate", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_60(self) -> ComposeResult:
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
            yield Button(" ACTIVATE", id="token-activate", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_61(self) -> ComposeResult:
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
            yield Button(" Activate", id="XXtoken-activateXX", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_62(self) -> ComposeResult:
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
            yield Button(" Activate", id="TOKEN-ACTIVATE", classes="token-action")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_63(self) -> ComposeResult:
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
            yield Button(" Activate", id="token-activate", classes="XXtoken-actionXX")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_64(self) -> ComposeResult:
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
            yield Button(" Activate", id="token-activate", classes="TOKEN-ACTION")
            yield Button("Cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_65(self) -> ComposeResult:
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
            yield Button(None, id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_66(self) -> ComposeResult:
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
            yield Button("Cancel", id=None)

    def xǁTokenInputScreenǁcompose__mutmut_67(self) -> ComposeResult:
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
            yield Button(id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_68(self) -> ComposeResult:
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
            yield Button("Cancel", )

    def xǁTokenInputScreenǁcompose__mutmut_69(self) -> ComposeResult:
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
            yield Button("XXCancelXX", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_70(self) -> ComposeResult:
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
            yield Button("cancel", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_71(self) -> ComposeResult:
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
            yield Button("CANCEL", id="token-cancel")

    def xǁTokenInputScreenǁcompose__mutmut_72(self) -> ComposeResult:
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
            yield Button("Cancel", id="XXtoken-cancelXX")

    def xǁTokenInputScreenǁcompose__mutmut_73(self) -> ComposeResult:
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
            yield Button("Cancel", id="TOKEN-CANCEL")

    def action_cancel(self) -> None:
        self.dismiss(None)

    @_mutmut_mutated(mutants_xǁTokenInputScreenǁon_button_pressed__mutmut)
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_orig(self, event: Button.Pressed) -> None:
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_1(self, event: Button.Pressed) -> None:
        if event.button.id != "token-cancel":
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_2(self, event: Button.Pressed) -> None:
        if event.button.id == "XXtoken-cancelXX":
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_3(self, event: Button.Pressed) -> None:
        if event.button.id == "TOKEN-CANCEL":
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_4(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id != "token-activate":
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_5(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "XXtoken-activateXX":
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_6(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "TOKEN-ACTIVATE":
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_7(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = None
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_8(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one(None, Input).value.strip()
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_9(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", None).value.strip()
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_10(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one(Input).value.strip()
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_11(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", ).value.strip()
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_12(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("XX#token-inputXX", Input).value.strip()
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_13(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#TOKEN-INPUT", Input).value.strip()
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_14(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if token:
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

    def xǁTokenInputScreenǁon_button_pressed__mutmut_15(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one("#token-status", Static).update(
                    None
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_16(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one(None, Static).update(
                    "[bold red]Please enter your token first.[/]"
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_17(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one("#token-status", None).update(
                    "[bold red]Please enter your token first.[/]"
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_18(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one(Static).update(
                    "[bold red]Please enter your token first.[/]"
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_19(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one("#token-status", ).update(
                    "[bold red]Please enter your token first.[/]"
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_20(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one("XX#token-statusXX", Static).update(
                    "[bold red]Please enter your token first.[/]"
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_21(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one("#TOKEN-STATUS", Static).update(
                    "[bold red]Please enter your token first.[/]"
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_22(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one("#token-status", Static).update(
                    "XX[bold red]Please enter your token first.[/]XX"
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_23(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one("#token-status", Static).update(
                    "[bold red]please enter your token first.[/]"
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_24(self, event: Button.Pressed) -> None:
        if event.button.id == "token-cancel":
            self.dismiss(None)
            return

        if event.button.id == "token-activate":
            token = self.query_one("#token-input", Input).value.strip()
            if not token:
                self.query_one("#token-status", Static).update(
                    "[BOLD RED]PLEASE ENTER YOUR TOKEN FIRST.[/]"
                )
                return
            if not token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_25(self, event: Button.Pressed) -> None:
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
            if token.startswith("hxw_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_26(self, event: Button.Pressed) -> None:
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
            if not token.startswith(None):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_27(self, event: Button.Pressed) -> None:
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
            if not token.startswith("XXhxw_XX"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_28(self, event: Button.Pressed) -> None:
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
            if not token.startswith("HXW_"):
                self.query_one("#token-status", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_29(self, event: Button.Pressed) -> None:
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
                    None
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_30(self, event: Button.Pressed) -> None:
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
                self.query_one(None, Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_31(self, event: Button.Pressed) -> None:
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
                self.query_one("#token-status", None).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_32(self, event: Button.Pressed) -> None:
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
                self.query_one(Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_33(self, event: Button.Pressed) -> None:
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
                self.query_one("#token-status", ).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_34(self, event: Button.Pressed) -> None:
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
                self.query_one("XX#token-statusXX", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_35(self, event: Button.Pressed) -> None:
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
                self.query_one("#TOKEN-STATUS", Static).update(
                    "[bold red]Invalid token format. Token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_36(self, event: Button.Pressed) -> None:
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
                    "XX[bold red]Invalid token format. Token must start with 'hxw_'.[/]XX"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_37(self, event: Button.Pressed) -> None:
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
                    "[bold red]invalid token format. token must start with 'hxw_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_38(self, event: Button.Pressed) -> None:
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
                    "[BOLD RED]INVALID TOKEN FORMAT. TOKEN MUST START WITH 'HXW_'.[/]"
                )
                return
            asyncio.ensure_future(self._do_activate(token))

    def xǁTokenInputScreenǁon_button_pressed__mutmut_39(self, event: Button.Pressed) -> None:
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
            asyncio.ensure_future(None)

    def xǁTokenInputScreenǁon_button_pressed__mutmut_40(self, event: Button.Pressed) -> None:
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
            asyncio.ensure_future(self._do_activate(None))

    @_mutmut_mutated(mutants_xǁTokenInputScreenǁ_do_activate__mutmut)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_orig(self, token: str) -> None:
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_1(self, token: str) -> None:
        import httpx

        status = None
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_2(self, token: str) -> None:
        import httpx

        status = self.query_one(None, Static)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_3(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", None)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_4(self, token: str) -> None:
        import httpx

        status = self.query_one(Static)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_5(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", )
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_6(self, token: str) -> None:
        import httpx

        status = self.query_one("XX#token-statusXX", Static)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_7(self, token: str) -> None:
        import httpx

        status = self.query_one("#TOKEN-STATUS", Static)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_8(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update(None)

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_9(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("XX[dim]Contacting hexa-cloud...[/]XX")

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_10(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]contacting hexa-cloud...[/]")

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_11(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[DIM]CONTACTING HEXA-CLOUD...[/]")

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_12(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = None
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_13(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = get_machine_id()
            async with httpx.AsyncClient(timeout=None) as client:
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_14(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = get_machine_id()
            async with httpx.AsyncClient(timeout=11) as client:
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_15(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = get_machine_id()
            async with httpx.AsyncClient(timeout=10) as client:
                response = None
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_16(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = get_machine_id()
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.post(
                    None,
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_17(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = get_machine_id()
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.post(
                    "https://api.hexawyn.com/api/v1/license/activate",
                    json=None,
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_18(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = get_machine_id()
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.post(
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_19(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = get_machine_id()
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.post(
                    "https://api.hexawyn.com/api/v1/license/activate",
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_20(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = get_machine_id()
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.post(
                    "XXhttps://api.hexawyn.com/api/v1/license/activateXX",
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_21(self, token: str) -> None:
        import httpx

        status = self.query_one("#token-status", Static)
        status.update("[dim]Contacting hexa-cloud...[/]")

        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id

            machine_id = get_machine_id()
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.post(
                    "HTTPS://API.HEXAWYN.COM/API/V1/LICENSE/ACTIVATE",
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_22(self, token: str) -> None:
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
                        "XXapi_keyXX": token,
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_23(self, token: str) -> None:
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
                        "API_KEY": token,
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_24(self, token: str) -> None:
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
                        "XXmachine_idXX": machine_id,
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_25(self, token: str) -> None:
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
                        "MACHINE_ID": machine_id,
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_26(self, token: str) -> None:
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
                        "XXclient_versionXX": "1.0.0",
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_27(self, token: str) -> None:
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
                        "CLIENT_VERSION": "1.0.0",
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_28(self, token: str) -> None:
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
                        "client_version": "XX1.0.0XX",
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_29(self, token: str) -> None:
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
            status.update(None)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_30(self, token: str) -> None:
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

        if response.status_code == 200:  # noqa: PLR2004
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_31(self, token: str) -> None:
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

        if response.status_code != 201:  # noqa: PLR2004
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_32(self, token: str) -> None:
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
            detail = None
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_33(self, token: str) -> None:
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
            detail = "XXUnknown errorXX"
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_34(self, token: str) -> None:
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
            detail = "unknown error"
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_35(self, token: str) -> None:
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
            detail = "UNKNOWN ERROR"
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_36(self, token: str) -> None:
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
                detail = None
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_37(self, token: str) -> None:
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
                detail = response.json().get(None, detail)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_38(self, token: str) -> None:
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
                detail = response.json().get("detail", None)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_39(self, token: str) -> None:
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
                detail = response.json().get(detail)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_40(self, token: str) -> None:
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
                detail = response.json().get("detail", )
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_41(self, token: str) -> None:
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
                detail = response.json().get("XXdetailXX", detail)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_42(self, token: str) -> None:
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
                detail = response.json().get("DETAIL", detail)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_43(self, token: str) -> None:
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
            status.update(None)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_44(self, token: str) -> None:
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

        data = None
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_45(self, token: str) -> None:
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
        jwt_token = None
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_46(self, token: str) -> None:
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
        jwt_token = data.get(None, "")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_47(self, token: str) -> None:
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
        jwt_token = data.get("token", None)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_48(self, token: str) -> None:
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
        jwt_token = data.get("")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_49(self, token: str) -> None:
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
        jwt_token = data.get("token", )
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_50(self, token: str) -> None:
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
        jwt_token = data.get("XXtokenXX", "")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_51(self, token: str) -> None:
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
        jwt_token = data.get("TOKEN", "")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_52(self, token: str) -> None:
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
        jwt_token = data.get("token", "XXXX")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_53(self, token: str) -> None:
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
        plan = None
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_54(self, token: str) -> None:
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
        plan = data.get(None, "unknown")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_55(self, token: str) -> None:
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
        plan = data.get("plan", None)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_56(self, token: str) -> None:
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
        plan = data.get("unknown")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_57(self, token: str) -> None:
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
        plan = data.get("plan", )
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_58(self, token: str) -> None:
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
        plan = data.get("XXplanXX", "unknown")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_59(self, token: str) -> None:
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
        plan = data.get("PLAN", "unknown")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_60(self, token: str) -> None:
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
        plan = data.get("plan", "XXunknownXX")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_61(self, token: str) -> None:
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
        plan = data.get("plan", "UNKNOWN")
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_62(self, token: str) -> None:
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
        expires_at = None

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_63(self, token: str) -> None:
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
        expires_at = data.get(None, "")

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_64(self, token: str) -> None:
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
        expires_at = data.get("expires_at", None)

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_65(self, token: str) -> None:
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
        expires_at = data.get("")

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_66(self, token: str) -> None:
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
        expires_at = data.get("expires_at", )

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_67(self, token: str) -> None:
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
        expires_at = data.get("XXexpires_atXX", "")

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_68(self, token: str) -> None:
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
        expires_at = data.get("EXPIRES_AT", "")

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_69(self, token: str) -> None:
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
        expires_at = data.get("expires_at", "XXXX")

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_70(self, token: str) -> None:
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

        license_dir = None
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_71(self, token: str) -> None:
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

        license_dir = Path.home() * ".hexawyn"
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_72(self, token: str) -> None:
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

        license_dir = Path.home() / "XX.hexawynXX"
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_73(self, token: str) -> None:
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

        license_dir = Path.home() / ".HEXAWYN"
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_74(self, token: str) -> None:
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
        license_dir.mkdir(parents=None, exist_ok=True)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_75(self, token: str) -> None:
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
        license_dir.mkdir(parents=True, exist_ok=None)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_76(self, token: str) -> None:
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
        license_dir.mkdir(exist_ok=True)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_77(self, token: str) -> None:
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
        license_dir.mkdir(parents=True, )
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_78(self, token: str) -> None:
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
        license_dir.mkdir(parents=False, exist_ok=True)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_79(self, token: str) -> None:
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
        license_dir.mkdir(parents=True, exist_ok=False)
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_80(self, token: str) -> None:
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
        (license_dir / "license.key").write_text(None)

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_81(self, token: str) -> None:
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
        (license_dir * "license.key").write_text(jwt_token)

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_82(self, token: str) -> None:
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
        (license_dir / "XXlicense.keyXX").write_text(jwt_token)

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_83(self, token: str) -> None:
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
        (license_dir / "LICENSE.KEY").write_text(jwt_token)

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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_84(self, token: str) -> None:
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

        cfg = None
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

    async def xǁTokenInputScreenǁ_do_activate__mutmut_85(self, token: str) -> None:
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
        cfg["hexawyn_token"] = None
        cfg["hexawyn_token_prefix"] = token[: min(len(token), 16)]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_86(self, token: str) -> None:
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
        cfg["XXhexawyn_tokenXX"] = token
        cfg["hexawyn_token_prefix"] = token[: min(len(token), 16)]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_87(self, token: str) -> None:
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
        cfg["HEXAWYN_TOKEN"] = token
        cfg["hexawyn_token_prefix"] = token[: min(len(token), 16)]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_88(self, token: str) -> None:
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
        cfg["hexawyn_token_prefix"] = None
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_89(self, token: str) -> None:
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
        cfg["XXhexawyn_token_prefixXX"] = token[: min(len(token), 16)]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_90(self, token: str) -> None:
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
        cfg["HEXAWYN_TOKEN_PREFIX"] = token[: min(len(token), 16)]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_91(self, token: str) -> None:
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
        cfg["hexawyn_token_prefix"] = token[: min(None, 16)]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_92(self, token: str) -> None:
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
        cfg["hexawyn_token_prefix"] = token[: min(len(token), None)]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_93(self, token: str) -> None:
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
        cfg["hexawyn_token_prefix"] = token[: min(16)]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_94(self, token: str) -> None:
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
        cfg["hexawyn_token_prefix"] = token[: min(len(token), )]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_95(self, token: str) -> None:
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
        cfg["hexawyn_token_prefix"] = token[: min(len(token), 17)]
        save_config(cfg)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_96(self, token: str) -> None:
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
        save_config(None)

        status.update(
            f"[bold green]✓ License activated — Plan: {plan}[/]\n"
            f"[dim]Expires: {_format_expiry(expires_at)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_97(self, token: str) -> None:
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
            None
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_98(self, token: str) -> None:
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
            f"[dim]Expires: {_format_expiry(None)}[/]"
        )

        import asyncio

        await asyncio.sleep(1)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_99(self, token: str) -> None:
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

        await asyncio.sleep(None)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_100(self, token: str) -> None:
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

        await asyncio.sleep(2)
        self.dismiss(token[:16])

    async def xǁTokenInputScreenǁ_do_activate__mutmut_101(self, token: str) -> None:
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
        self.dismiss(None)

    async def xǁTokenInputScreenǁ_do_activate__mutmut_102(self, token: str) -> None:
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
        self.dismiss(token[:17])

mutants_xǁTokenInputScreenǁcompose__mutmut['_mutmut_orig'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_1'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_2'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_3'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_4'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_5'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_6'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_7'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_8'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_9'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_10'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_11'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_12'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_13'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_14'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_15'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_16'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_17'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_18'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_19'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_20'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_21'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_22'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_23'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_24'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_25'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_26'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_27'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_28'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_29'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_30'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_31'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_32'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_33'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_34'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_35'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_36'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_37'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_38'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_38 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_39'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_39 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_40'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_40 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_41'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_41 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_42'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_42 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_43'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_43 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_44'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_44 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_45'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_45 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_46'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_46 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_47'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_47 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_48'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_48 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_49'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_49 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_50'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_50 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_51'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_51 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_52'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_52 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_53'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_53 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_54'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_54 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_55'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_55 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_56'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_56 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_57'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_57 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_58'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_58 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_59'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_59 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_60'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_60 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_61'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_61 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_62'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_62 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_63'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_63 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_64'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_64 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_65'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_65 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_66'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_66 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_67'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_67 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_68'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_68 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_69'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_69 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_70'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_70 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_71'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_71 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_72'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_72 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁcompose__mutmut['xǁTokenInputScreenǁcompose__mutmut_73'] = TokenInputScreen.xǁTokenInputScreenǁcompose__mutmut_73 # type: ignore # mutmut generated

mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['_mutmut_orig'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_1'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_2'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_3'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_4'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_5'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_6'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_7'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_8'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_9'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_10'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_11'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_12'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_13'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_14'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_15'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_16'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_17'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_18'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_19'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_20'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_21'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_22'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_23'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_24'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_25'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_26'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_27'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_28'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_29'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_30'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_31'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_32'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_33'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_34'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_35'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_36'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_37'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_38'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_38 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_39'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_39 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁon_button_pressed__mutmut['xǁTokenInputScreenǁon_button_pressed__mutmut_40'] = TokenInputScreen.xǁTokenInputScreenǁon_button_pressed__mutmut_40 # type: ignore # mutmut generated

mutants_xǁTokenInputScreenǁ_do_activate__mutmut['_mutmut_orig'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_1'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_2'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_3'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_4'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_5'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_6'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_7'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_8'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_9'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_10'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_11'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_12'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_13'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_14'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_15'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_16'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_17'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_18'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_19'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_20'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_21'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_22'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_23'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_24'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_25'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_26'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_27'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_28'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_29'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_30'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_31'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_32'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_33'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_34'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_35'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_36'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_37'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_38'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_39'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_40'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_40 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_41'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_41 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_42'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_42 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_43'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_43 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_44'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_44 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_45'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_45 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_46'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_46 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_47'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_47 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_48'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_48 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_49'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_49 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_50'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_50 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_51'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_51 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_52'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_52 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_53'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_53 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_54'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_54 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_55'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_55 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_56'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_56 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_57'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_57 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_58'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_58 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_59'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_59 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_60'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_60 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_61'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_61 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_62'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_62 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_63'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_63 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_64'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_64 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_65'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_65 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_66'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_66 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_67'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_67 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_68'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_68 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_69'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_69 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_70'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_70 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_71'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_71 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_72'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_72 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_73'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_73 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_74'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_74 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_75'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_75 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_76'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_76 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_77'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_77 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_78'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_78 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_79'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_79 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_80'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_80 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_81'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_81 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_82'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_82 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_83'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_83 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_84'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_84 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_85'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_85 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_86'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_86 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_87'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_87 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_88'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_88 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_89'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_89 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_90'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_90 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_91'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_91 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_92'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_92 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_93'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_93 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_94'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_94 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_95'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_95 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_96'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_96 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_97'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_97 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_98'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_98 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_99'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_99 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_100'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_100 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_101'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_101 # type: ignore # mutmut generated
mutants_xǁTokenInputScreenǁ_do_activate__mutmut['xǁTokenInputScreenǁ_do_activate__mutmut_102'] = TokenInputScreen.xǁTokenInputScreenǁ_do_activate__mutmut_102 # type: ignore # mutmut generated
