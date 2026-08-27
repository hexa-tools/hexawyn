"""hexa login — Hexawyn Cloud authentication for the CLI.

The Control Plane owns GitHub OAuth, account signup and token issuance. The
CLI is a thin authenticated client: it resolves/validates a token, persists
it, and then starts the canonical Hexawyn application. It remains an optional
path — OSS/BYOK usage never requires it.
"""

from __future__ import annotations

import click
import httpx

from hexawyn.application.service.login_service import LoginService
from hexawyn.domain.models.auth import LoginOutcome

_SUCCESS_OUTCOMES = (
    LoginOutcome.STARTED_WITH_EXISTING,
    LoginOutcome.AUTHENTICATED,
    LoginOutcome.CANCELLED,
)


@click.command()
def login() -> None:
    """Authenticate against Hexawyn Cloud and start Hexawyn."""
    service = _build_service()
    outcome = service.authenticate()
    if outcome not in _SUCCESS_OUTCOMES:
        raise SystemExit(1)


def _build_service() -> LoginService:
    """Wire the CloudAuthPort implementation for the login command."""
    from hexawyn.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.cli.app import HexawynApp
    from hexawyn.infrastructure.config.config_manager import get_cloud_url

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(client=httpx.Client(), base_url=get_cloud_url()),
        store=ConfigTokenStore(),
    )
    return LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=HexawynApp().run,
    )


def _prompt_token() -> str | None:
    try:
        value = click.prompt("Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except click.Abort:
        return None
