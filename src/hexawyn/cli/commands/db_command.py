import click

from hexawyn.cli.presentation.formatting import format_size
from hexawyn.infrastructure.memory.duckdb_client import (
    _DB_SIZE_WARNING_THRESHOLD,
    DB_PATH,
    _load_sql,
    get_connection,
    get_db_size_bytes,
    purge_expired_incidents,
    purge_older_than,
)


@click.group()
def db() -> None:
    """Manage the local DuckDB storage (~/.hexawyn/memory.duckdb)."""


@db.command()
def size() -> None:
    """Show the current DuckDB file size."""
    size_bytes = get_db_size_bytes(DB_PATH)
    formatted = format_size(size_bytes)
    threshold_str = format_size(_DB_SIZE_WARNING_THRESHOLD)

    click.echo(f"Database: {DB_PATH}")
    click.echo(f"Size    : {formatted}")

    if size_bytes > _DB_SIZE_WARNING_THRESHOLD:
        click.echo(f"\n\u26a0\ufe0f  Database exceeds {threshold_str} warning threshold.")
        click.echo("   Run 'hexa db purge' to clean expired incidents.")
    elif size_bytes > 0:
        click.echo(f"Warning threshold: {threshold_str}")


@db.command()
@click.option(
    "--older-than",
    type=int,
    default=None,
    help="Purge incidents older than N days (default: purge only expired)",
)
@click.option("--dry-run", is_flag=True, help="Show what would be deleted without deleting")
def purge(older_than: int | None, dry_run: bool) -> None:
    """Purge expired or old incidents from DuckDB."""
    try:
        conn = get_connection()
    except Exception as exc:
        click.echo(f"\u274c Cannot connect to DuckDB: {exc}")
        return

    try:
        if older_than is not None:
            if dry_run:
                before = conn.execute(
                    _load_sql("count_older_than.sql"),
                    [older_than],
                ).fetchone()
                count = before[0] if before else 0
                click.echo(
                    f"Would delete {count} incident(s) older than {older_than} days (dry run)."
                )
            else:
                deleted = purge_older_than(conn, days=older_than)
                click.echo(f"Deleted {deleted} incident(s) older than {older_than} days.")
        else:
            if dry_run:
                before = conn.execute(_load_sql("count_expired.sql")).fetchone()
                count = before[0] if before else 0
                click.echo(f"Would delete {count} expired incident(s) (dry run).")
            else:
                deleted = purge_expired_incidents(conn)
                click.echo(f"Deleted {deleted} expired incident(s).")

        remaining = conn.execute(_load_sql("count_incidents.sql")).fetchone()
        remaining_count = remaining[0] if remaining else 0
        click.echo(f"Remaining: {remaining_count} incident(s).")

    finally:
        conn.close()
