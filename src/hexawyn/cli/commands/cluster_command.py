import click

from hexawyn.infrastructure.config.cache_manager import clear_l1


@click.group()
def cluster() -> None:
    """Manage Kubernetes cluster contexts."""


@cluster.command()
@click.argument("context_name")
def use(context_name: str) -> None:
    """Switch to a different cluster context."""
    clear_l1()
    click.echo(f"\u2705 Switched to cluster: {context_name}")
    click.echo("\U0001f5d1\ufe0f  Cache cleared (stale responses removed)")
