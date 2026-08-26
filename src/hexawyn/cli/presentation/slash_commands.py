def is_context_command(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name in {"/context", "/ctx"}


def is_token_command(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name == "/token"


def is_stack_command(text: str) -> bool:
    command_name = text.split(maxsplit=1)[0] if text else ""
    return command_name == "/stack"


def is_refresh_command(text: str) -> bool:
    return text.strip() == "/refresh"


def is_setup_command(text: str) -> bool:
    return text.strip() == "/setup"


def extract_requested_context(text: str) -> str | None:
    if not text.strip():
        return None
    parts = text.strip().split(maxsplit=1)
    if len(parts) < 2:  # noqa: PLR2004
        return None
    requested_name = parts[1].strip()
    return requested_name if requested_name else None
