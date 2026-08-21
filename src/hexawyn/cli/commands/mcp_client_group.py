"""Shared click group builder for coding-agent MCP integrations.

Each coding agent (Claude Code, Codex, OpenCode, Cursor, Gemini CLI) gets its
own top-level `hexa <client>` group with install/uninstall/status. This builder
keeps those command files thin: the Click layer only translates input/output
into calls to the integration registry.
"""

from __future__ import annotations

import click

from hexawyn.cli.integrations.mcp.base import MCP_SERVER_NAME, MCP_TRANSPORT
from hexawyn.cli.integrations.mcp.command import mcp_stdio_command
from hexawyn.cli.integrations.mcp.registry import get_integration


def build_mcp_client_group(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def _install_command(client: str, display_name: str) -> click.Command:
    @click.command(name="install", help="Configure Hexawyn as an MCP server (idempotent).")
    def install() -> None:
        integration = get_integration(client)
        if not integration.is_available():
            _fail(f"{display_name} not detected. Install {display_name} first.")
            raise SystemExit(1)
        click.echo(f"✓ {display_name} detected")
        result = integration.install()
        if not result.success:
            _fail(result.message)
            raise SystemExit(1)
        if result.already_configured:
            click.echo("✓ Hexawyn MCP already configured")
        else:
            click.echo("✓ Hexawyn MCP configured")
        click.echo("✓ Configuration verified")
        click.echo("")
        click.echo(f"Server: {MCP_SERVER_NAME}")
        click.echo(f"Transport: {MCP_TRANSPORT}")
        click.echo(f"Command: {' '.join(mcp_stdio_command())}")

    return install


def _uninstall_command(client: str, display_name: str) -> click.Command:
    @click.command(name="uninstall", help="Remove the Hexawyn MCP server from the client.")
    def uninstall() -> None:
        integration = get_integration(client)
        if not integration.is_available():
            _fail(f"{display_name} not detected. Nothing to uninstall.")
            raise SystemExit(1)
        result = integration.uninstall()
        if not result.success:
            _fail(result.message)
            raise SystemExit(1)
        if result.message == "not configured":
            click.echo(f"✓ Hexawyn MCP is not configured for {display_name} — nothing to remove.")
        else:
            click.echo(f"✓ Hexawyn MCP removed from {display_name}.")

    return uninstall


def _status_command(client: str, display_name: str) -> click.Command:
    @click.command(name="status", help="Show whether Hexawyn is configured as an MCP server.")
    def status() -> None:
        integration = get_integration(client)
        click.echo(f"Hexawyn MCP — {display_name}")
        click.echo("")
        if not integration.is_available():
            _print_not_configured(client)
            return
        current = integration.status()
        if current.error:
            _fail(current.error)
            raise SystemExit(1)
        if current.configured:
            click.echo("Status: ✓ Configured")
            click.echo(f"Server: {MCP_SERVER_NAME}")
            click.echo(f"Transport: {current.transport}")
            if current.command:
                click.echo(f"Command: {current.command}")
            if current.endpoint:
                click.echo(f"Endpoint: {current.endpoint}")
            return
        _print_not_configured(client)

    return status


def _fail(message: str) -> None:
    click.echo(f"❌ {message}", err=True)


def _print_not_configured(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("")
    click.echo("Run:")
    click.echo("")
    click.echo(f"  hexa {client} install")
