from hexawyn.cli.widgets.markdown_log import MarkdownLog
from hexawyn.infrastructure.config.config_manager import get_llm_config


def render_setup_info(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")
