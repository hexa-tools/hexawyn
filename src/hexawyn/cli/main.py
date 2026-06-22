import click

from hexawyn.infrastructure.config.config_manager import get_api_key


@click.group()
def app() -> None:
    """hexawyn — AI-powered Kubernetes diagnostic agent."""


@app.command()
@click.option(
    "--demo", is_flag=True, help="Start in demo mode (no real cluster needed)"
)
@click.option(
    "--scenario",
    default="aws_eks",
    type=click.Choice(["aws_eks", "azure_aks", "gcp_gke", "openshift", "datadog"]),
    help="Demo scenario to use",
)
@click.option(
    "--expert", is_flag=True, help="Expert mode: raw JSON, no suggestion chips"
)
def start(demo: bool, scenario: str, expert: bool) -> None:
    """Start the hexawyn TUI."""
    import os

    if demo:
        os.environ["HEXAWYN_DEMO_MODE"] = "true"
        os.environ["HEXAWYN_DEMO_SCENARIO"] = scenario

    # Check API key before launching TUI
    if not get_api_key():
        click.echo("⚠️  No Anthropic API key found.")
        click.echo("Set ANTHROPIC_API_KEY env var or run 'hexa setup'")
        return

    from hexawyn.cli.app import HexawynApp

    app_instance = HexawynApp(expert_mode=expert)
    app_instance.run()


@app.command()
def setup() -> None:
    """Run the setup wizard manually."""
    from hexawyn.cli.app import HexawynApp

    app_instance = HexawynApp(force_setup=True)
    app_instance.run()


from hexawyn.cli.commands.quota_command import quota  # noqa: E402

app.add_command(quota)


if __name__ == "__main__":
    app()
