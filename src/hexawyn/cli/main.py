import click
from dotenv import load_dotenv

load_dotenv()


@click.group(invoke_without_command=True)
def app() -> None:
    """hexawyn — AI-powered Kubernetes diagnostic agent."""
    if not click.get_current_context().invoked_subcommand:
        from hexawyn.cli.presentation.feedback import header

        header()
        click.echo(app.get_help(click.get_current_context()))


def _register_start(start_group: click.Group) -> None:
    """Register the `start` command (the only TUI launcher) on the CLI group."""

    @start_group.command()
    @click.option("--demo", is_flag=True, help="Start in demo mode (no real cluster needed)")
    @click.option(
        "--scenario",
        default="aws_eks",
        type=click.Choice(["aws_eks", "azure_aks", "gcp_gke", "openshift", "datadog"]),
        help="Demo scenario to use",
    )
    @click.option("--expert", is_flag=True, help="Expert mode: raw JSON, no suggestion chips")
    @click.option("--no-cloud", is_flag=True, help="Start in local/BYOK mode (no Cloud auth)")
    def start(demo: bool, scenario: str, expert: bool, no_cloud: bool) -> None:
        """Start the hexawyn TUI (Cloud auth, or local/BYOK with --no-cloud)."""
        _welcome()

        import os

        if no_cloud:
            os.environ["HEXAWYN_RUNTIME_MODE"] = "embedded"

        if demo:
            os.environ["HEXAWYN_DEMO_MODE"] = "true"
            os.environ["HEXAWYN_DEMO_SCENARIO"] = scenario
        elif not no_cloud and not _cloud_auth_ready():
            os.environ["HEXAWYN_RUNTIME_MODE"] = "embedded"

        from hexawyn.cli.app import HexawynApp

        HexawynApp(expert_mode=expert).run()


def _cloud_auth_ready() -> bool:
    """Validate an existing/entered cloud token via the Control Plane.

    Returns True when a valid cloud token is active (and stored), otherwise the
    caller falls back to local/BYOK (embedded) mode.
    """
    import httpx

    from hexawyn.adapters.secondary.auth.cloud_auth_adapter import CloudAuthAdapter
    from hexawyn.adapters.secondary.auth.config_token_store import ConfigTokenStore
    from hexawyn.adapters.secondary.auth.token_validator import HttpTokenValidator
    from hexawyn.application.service.login_service import LoginService
    from hexawyn.domain.models.auth import LoginOutcome
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    adapter = CloudAuthAdapter(
        validator=HttpTokenValidator(httpx.Client(), get_runtime_endpoint() or ""),
        store=ConfigTokenStore(),
    )
    service = LoginService(
        auth=adapter,
        prompt_token=_prompt_token,
        emit=click.echo,
        app_start=lambda: None,
    )
    outcome = service.authenticate()
    return outcome in (LoginOutcome.AUTHENTICATED, LoginOutcome.STARTED_WITH_EXISTING)


def _prompt_token() -> str | None:
    """Prompt for the Hexawyn Cloud token using hidden input."""
    click.echo("  ✨ A Cloud token unlocks AI investigations against your cluster.")
    click.echo("     Press Ctrl+C to continue in local/BYOK mode (no cloud).")
    click.echo("")
    try:
        value = click.prompt("  Hexawyn Cloud token", hide_input=True, show_default=False)
        return value if isinstance(value, str) else None
    except (click.Abort, KeyboardInterrupt):
        return None


def _welcome() -> None:
    """Render a welcoming banner for `hexa start`."""
    from hexawyn.cli.presentation.feedback import header

    header()
    click.echo("  👋 Welcome to Hexawyn — your AI-powered Kubernetes assistant.")
    click.echo("")


_register_start(app)

from hexawyn.cli.commands.auth_command import auth  # noqa: E402, I001
from hexawyn.cli.commands.cache_command import cache  # noqa: E402, I001
from hexawyn.cli.commands.claude_command import claude  # noqa: E402, I001
from hexawyn.cli.commands.cluster_command import cluster  # noqa: E402, I001
from hexawyn.cli.commands.codex_command import codex  # noqa: E402, I001
from hexawyn.cli.commands.config_command import config  # noqa: E402, I001
from hexawyn.cli.commands.cursor_command import cursor  # noqa: E402, I001
from hexawyn.cli.commands.db_command import db  # noqa: E402, I001
from hexawyn.cli.commands.deepseek_command import deepseek  # noqa: E402, I001
from hexawyn.cli.commands.gemini_command import gemini  # noqa: E402, I001
from hexawyn.cli.commands.opencode_command import opencode  # noqa: E402, I001
from hexawyn.cli.commands.quota_command import quota  # noqa: E402, I001
from hexawyn.cli.commands.schedule_command import schedule  # noqa: E402, I001
from hexawyn.cli.commands.slack_command import slack  # noqa: E402, I001
from hexawyn.cli.commands.update_command import update, update_check, version  # noqa: E402, I001
from hexawyn.cli.commands.uninstall_command import uninstall  # noqa: E402, I001

app.add_command(auth)
app.add_command(config)
app.add_command(quota)
app.add_command(cluster)
app.add_command(db)
app.add_command(cache)
app.add_command(schedule)
app.add_command(slack)
app.add_command(claude)
app.add_command(codex)
app.add_command(opencode)
app.add_command(cursor)
app.add_command(gemini)
app.add_command(deepseek)
app.add_command(update)
app.add_command(update_check)
app.add_command(version)
app.add_command(uninstall)


if __name__ == "__main__":
    app()
