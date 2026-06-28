import click

from hexawyn.infrastructure.memory.duckdb_cache_adapter import DuckDBCacheAdapter


def _get_adapter() -> DuckDBCacheAdapter:
    return DuckDBCacheAdapter()


@click.group()
def cache() -> None:
    """Manage local investigation cache (RGPD-compliant)."""


@cache.command()
def stats() -> None:
    """Show cache statistics."""
    adapter = _get_adapter()
    s = adapter.stats()
    try:
        click.echo(f"Total entries : {s['total']}")
        click.echo(f"Valid         : {s['valid']}")
        click.echo(f"Expired       : {s['expired']}")
    finally:
        adapter.close()


@cache.command()
def clear() -> None:
    """Delete all cached investigations (right to erasure)."""
    adapter = _get_adapter()
    previous = adapter.stats()
    adapter.clear()
    try:
        click.echo(f"Cache cleared ({previous['total']} entries removed)")
    finally:
        adapter.close()


@cache.command()
@click.option("--cluster", required=True, help="Cluster name")
@click.option("--namespace", required=True, help="Namespace")
@click.option("--resource", required=True, help="Resource name (e.g., pod name)")
def invalidate(cluster: str, namespace: str, resource: str) -> None:
    """Invalidate cache entries for a specific resource."""
    adapter = _get_adapter()
    count = adapter.invalidate_by_resource(cluster, namespace, resource)
    try:
        click.echo(f"Invalidated {count} entries for {cluster}/{namespace}/{resource}")
    finally:
        adapter.close()
