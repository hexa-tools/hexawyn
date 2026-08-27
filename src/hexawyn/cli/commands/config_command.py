"""hexa config — manage CLI-set cloud provider credentials."""

from __future__ import annotations

import click

from hexawyn.cli.presentation.feedback import fail, ok
from hexawyn.infrastructure.config.provider_config import (
    apply_provider_env,
    clear_provider_credentials,
    list_provider_credentials,
    set_provider_credentials,
)
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


@click.group()
def config() -> None:
    """Manage hexawyn configuration (cloud provider credentials)."""


@config.command("providers")
def providers() -> None:
    """List installed cloud providers and their credential status."""
    installed = detect_installed_providers()
    stored = list_provider_credentials()

    click.echo("Installed cloud providers:")
    for provider in sorted(installed):
        status = "creds set" if provider in stored else "no creds"
        flag = "👤" if provider in stored else "—"
        click.echo(f"  {flag} {provider:<10} ({status})")

    if not stored:
        click.echo("")
        click.echo(
            "  No credentials stored yet. Use: hexa config provider set <name> key=value ..."
        )


@config.group("provider")
def provider_group() -> None:
    """Manage credentials for a single cloud provider."""


@provider_group.command("set")
@click.argument("name")
@click.argument("values", nargs=-1)
def set_credentials(name: str, values: tuple[str, ...]) -> None:
    """Store cloud provider credentials.

    NAME is the provider (aws, gcp, azure, datadog). VALUES are key=value
    pairs, e.g. `access_key=AKIA ... secret_key=... region=eu-west-3`.
    """
    parsed: dict[str, str] = {}
    for raw in values:
        if "=" not in raw:
            fail(f"Invalid credential '{raw}' — expected key=value")
            raise click.exceptions.Exit(code=1)
        key, _, value = raw.partition("=")
        parsed[key.strip()] = value.strip()

    set_provider_credentials(name, parsed)
    applied = apply_provider_env(name)

    ok(f"Credentials stored for {name}")
    if applied:
        click.echo("  Env (this session):")
        for env_name in sorted(applied):
            click.echo(f"    {env_name} = {'*' * 6}")


@provider_group.command("list")
def list_credentials() -> None:
    """Show which providers have stored credentials (values redacted)."""
    stored = list_provider_credentials()
    if not stored:
        click.echo("No cloud provider credentials stored.")
        return
    for name, creds in sorted(stored.items()):
        redacted = ", ".join(f"{key}={'*' * 5}" for key in sorted(creds))
        click.echo(f"  {name:<10} {redacted}")


@provider_group.command("clear")
@click.argument("name")
def clear_credentials(name: str) -> None:
    """Remove stored credentials for a provider."""
    clear_provider_credentials(name)
    ok(f"Credentials cleared for {name}")
