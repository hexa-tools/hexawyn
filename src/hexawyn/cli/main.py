import click


@click.group()
def app() -> None:
    """hexawyn — AI-powered Kubernetes diagnostic agent."""


@app.command()
@click.option("--demo", is_flag=True, help="Start in demo mode (no real cluster needed)")
@click.option(
    "--scenario",
    default="aws_eks",
    type=click.Choice(["aws_eks", "azure_aks", "gcp_gke", "openshift", "datadog"]),
    help="Demo scenario to use",
)
@click.option("--expert", is_flag=True, help="Expert mode: raw JSON, no suggestion chips")
def start(demo: bool, scenario: str, expert: bool) -> None:
    """Start the hexawyn TUI."""
    import os

    if demo:
        os.environ["HEXAWYN_DEMO_MODE"] = "true"
        os.environ["HEXAWYN_DEMO_SCENARIO"] = scenario

    from hexawyn.cli.app import HexawynApp

    app_instance = HexawynApp(expert_mode=expert)
    app_instance.run()


@app.command()
def setup() -> None:
    """Run the setup wizard manually."""
    from hexawyn.cli.app import HexawynApp

    app_instance = HexawynApp(force_setup=True)
    app_instance.run()


from hexawyn.cli.commands.cache_command import cache  # noqa: E402, I001
from hexawyn.cli.commands.cluster_command import cluster  # noqa: E402, I001
from hexawyn.cli.commands.db_command import db  # noqa: E402, I001
from hexawyn.cli.commands.quota_command import quota  # noqa: E402, I001

app.add_command(quota)
app.add_command(cluster)
app.add_command(db)
app.add_command(cache)


if __name__ == "__main__":
    app()
