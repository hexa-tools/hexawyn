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
from hexawyn.cli.presentation.feedback import fail, ok, spinner, success


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_mcp_client_group__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_mcp_client_group__mutmut)
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


def x_build_mcp_client_group__mutmut_orig(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_1(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = None
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_2(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=None,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_3(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=None,
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_4(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_5(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_6(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(None)
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_7(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(None, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_8(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, None))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_9(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_10(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, ))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_11(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(None)
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_12(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(None, display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_13(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, None))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_14(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(display_name))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_15(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, ))
    group.add_command(_status_command(client, display_name))
    return group


def x_build_mcp_client_group__mutmut_16(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(None)
    return group


def x_build_mcp_client_group__mutmut_17(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(None, display_name))
    return group


def x_build_mcp_client_group__mutmut_18(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, None))
    return group


def x_build_mcp_client_group__mutmut_19(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(display_name))
    return group


def x_build_mcp_client_group__mutmut_20(client: str, display_name: str) -> click.Group:
    """Build a thin `hexa <client>` click group for a coding agent."""
    group = click.Group(
        name=client,
        help=f"Configure {display_name} to use the Hexawyn MCP server.",
    )
    group.add_command(_install_command(client, display_name))
    group.add_command(_uninstall_command(client, display_name))
    group.add_command(_status_command(client, ))
    return group

mutants_x_build_mcp_client_group__mutmut['_mutmut_orig'] = x_build_mcp_client_group__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_1'] = x_build_mcp_client_group__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_2'] = x_build_mcp_client_group__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_3'] = x_build_mcp_client_group__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_4'] = x_build_mcp_client_group__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_5'] = x_build_mcp_client_group__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_6'] = x_build_mcp_client_group__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_7'] = x_build_mcp_client_group__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_8'] = x_build_mcp_client_group__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_9'] = x_build_mcp_client_group__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_10'] = x_build_mcp_client_group__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_11'] = x_build_mcp_client_group__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_12'] = x_build_mcp_client_group__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_13'] = x_build_mcp_client_group__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_14'] = x_build_mcp_client_group__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_15'] = x_build_mcp_client_group__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_16'] = x_build_mcp_client_group__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_17'] = x_build_mcp_client_group__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_18'] = x_build_mcp_client_group__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_19'] = x_build_mcp_client_group__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_mcp_client_group__mutmut['x_build_mcp_client_group__mutmut_20'] = x_build_mcp_client_group__mutmut_20 # type: ignore # mutmut generated


def _install_command(client: str, display_name: str) -> click.Command:
    @click.command(name="install", help="Configure Hexawyn as an MCP server (idempotent).")
    def install() -> None:
        integration = get_integration(client)
        if not integration.is_available():
            fail(f"{display_name} not detected. Install {display_name} first.")
            raise SystemExit(1)
        ok(f"{display_name} detected")
        with spinner(f"Registering Hexawyn MCP server with {display_name}"):
            result = integration.install()
        if not result.success:
            fail(result.message)
            raise SystemExit(1)
        if result.already_configured:
            ok("Hexawyn MCP already configured")
        else:
            ok("Hexawyn MCP configured")
        with spinner("Verifying configuration"):
            pass
        ok("Configuration verified")
        success(f"{display_name} is ready to use Hexawyn")
        click.echo("")
        click.echo(f"  Server: {MCP_SERVER_NAME}")
        click.echo(f"  Transport: {MCP_TRANSPORT}")
        click.echo(f"  Command: {' '.join(mcp_stdio_command())}")
        click.echo("")
        click.echo("  Restart your coding agent to load the tools.")

    return install


def _uninstall_command(client: str, display_name: str) -> click.Command:
    @click.command(name="uninstall", help="Remove the Hexawyn MCP server from the client.")
    def uninstall() -> None:
        integration = get_integration(client)
        if not integration.is_available():
            fail(f"{display_name} not detected. Nothing to uninstall.")
            raise SystemExit(1)
        with spinner(f"Removing Hexawyn MCP server from {display_name}"):
            result = integration.uninstall()
        if not result.success:
            fail(result.message)
            raise SystemExit(1)
        if result.message == "not configured":
            ok(f"Hexawyn MCP is not configured for {display_name} — nothing to remove.")
        else:
            ok(f"Hexawyn MCP removed from {display_name}.")
            success(f"{display_name} cleaned up")

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
            fail(current.error)
            raise SystemExit(1)
        if current.configured:
            click.echo("Status: ✓ Configured")
            click.echo(f"  Server: {MCP_SERVER_NAME}")
            click.echo(f"  Transport: {current.transport}")
            if current.command:
                click.echo(f"  Command: {current.command}")
            if current.endpoint:
                click.echo(f"  Endpoint: {current.endpoint}")
            return
        _print_not_configured(client)

    return status
mutants_x__print_not_configured__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__print_not_configured__mutmut)
def _print_not_configured(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("")
    click.echo("Run:")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_orig(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("")
    click.echo("Run:")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_1(client: str) -> None:
    click.echo(None)
    click.echo("")
    click.echo("Run:")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_2(client: str) -> None:
    click.echo("XXStatus: ✗ Not configuredXX")
    click.echo("")
    click.echo("Run:")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_3(client: str) -> None:
    click.echo("status: ✗ not configured")
    click.echo("")
    click.echo("Run:")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_4(client: str) -> None:
    click.echo("STATUS: ✗ NOT CONFIGURED")
    click.echo("")
    click.echo("Run:")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_5(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo(None)
    click.echo("Run:")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_6(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("XXXX")
    click.echo("Run:")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_7(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("")
    click.echo(None)
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_8(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("")
    click.echo("XXRun:XX")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_9(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("")
    click.echo("run:")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_10(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("")
    click.echo("RUN:")
    click.echo("")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_11(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("")
    click.echo("Run:")
    click.echo(None)
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_12(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("")
    click.echo("Run:")
    click.echo("XXXX")
    click.echo(f"  hexa {client} install")


def x__print_not_configured__mutmut_13(client: str) -> None:
    click.echo("Status: ✗ Not configured")
    click.echo("")
    click.echo("Run:")
    click.echo("")
    click.echo(None)

mutants_x__print_not_configured__mutmut['_mutmut_orig'] = x__print_not_configured__mutmut_orig # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_1'] = x__print_not_configured__mutmut_1 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_2'] = x__print_not_configured__mutmut_2 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_3'] = x__print_not_configured__mutmut_3 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_4'] = x__print_not_configured__mutmut_4 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_5'] = x__print_not_configured__mutmut_5 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_6'] = x__print_not_configured__mutmut_6 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_7'] = x__print_not_configured__mutmut_7 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_8'] = x__print_not_configured__mutmut_8 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_9'] = x__print_not_configured__mutmut_9 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_10'] = x__print_not_configured__mutmut_10 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_11'] = x__print_not_configured__mutmut_11 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_12'] = x__print_not_configured__mutmut_12 # type: ignore # mutmut generated
mutants_x__print_not_configured__mutmut['x__print_not_configured__mutmut_13'] = x__print_not_configured__mutmut_13 # type: ignore # mutmut generated
