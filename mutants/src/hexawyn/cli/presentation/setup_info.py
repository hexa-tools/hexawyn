from hexawyn.cli.widgets.markdown_log import MarkdownLog
from hexawyn.infrastructure.config.config_manager import get_llm_config


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_render_setup_info__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_render_setup_info__mutmut)
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


def x_render_setup_info__mutmut_orig(log: MarkdownLog) -> None:
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


def x_render_setup_info__mutmut_1(log: MarkdownLog) -> None:
    cfg = None
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


def x_render_setup_info__mutmut_2(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = None
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


def x_render_setup_info__mutmut_3(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get(None, "Not configured")
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


def x_render_setup_info__mutmut_4(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", None)
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


def x_render_setup_info__mutmut_5(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("Not configured")
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


def x_render_setup_info__mutmut_6(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", )
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


def x_render_setup_info__mutmut_7(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("XXproviderXX", "Not configured")
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


def x_render_setup_info__mutmut_8(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("PROVIDER", "Not configured")
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


def x_render_setup_info__mutmut_9(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "XXNot configuredXX")
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


def x_render_setup_info__mutmut_10(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "not configured")
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


def x_render_setup_info__mutmut_11(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "NOT CONFIGURED")
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


def x_render_setup_info__mutmut_12(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = None
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


def x_render_setup_info__mutmut_13(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get(None, "N/A")
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


def x_render_setup_info__mutmut_14(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", None)
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


def x_render_setup_info__mutmut_15(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("N/A")
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


def x_render_setup_info__mutmut_16(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", )
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


def x_render_setup_info__mutmut_17(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("XXbase_urlXX", "N/A")
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


def x_render_setup_info__mutmut_18(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("BASE_URL", "N/A")
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


def x_render_setup_info__mutmut_19(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "XXN/AXX")
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


def x_render_setup_info__mutmut_20(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "n/a")
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


def x_render_setup_info__mutmut_21(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = None

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


def x_render_setup_info__mutmut_22(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(None)

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


def x_render_setup_info__mutmut_23(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get(None))

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


def x_render_setup_info__mutmut_24(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("XXapi_keyXX"))

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


def x_render_setup_info__mutmut_25(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("API_KEY"))

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


def x_render_setup_info__mutmut_26(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write(None)
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_27(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("XX[bold]LLM Configuration[/bold]XX")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_28(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]llm configuration[/bold]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_29(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[BOLD]LLM CONFIGURATION[/BOLD]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_30(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write(None)
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_31(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("XXXX")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_32(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("")
    log.write(None)
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_33(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(None)
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_34(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(None)
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_35(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'XX[green]✓ configured[/green]XX' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_36(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[GREEN]✓ CONFIGURED[/GREEN]' if has_key else '[red]✗ missing[/red]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_37(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else 'XX[red]✗ missing[/red]XX'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_38(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[RED]✗ MISSING[/RED]'}")
    log.write("")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_39(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write(None)

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_40(log: MarkdownLog) -> None:
    cfg = get_llm_config()
    provider = cfg.get("provider", "Not configured")
    base_url = cfg.get("base_url", "N/A")
    has_key = bool(cfg.get("api_key"))

    log.write("[bold]LLM Configuration[/bold]")
    log.write("")
    log.write(f"Provider: [bold]{provider}[/bold]")
    log.write(f"Base URL: [dim]{base_url}[/dim]")
    log.write(f"API Key: {'[green]✓ configured[/green]' if has_key else '[red]✗ missing[/red]'}")
    log.write("XXXX")

    if not has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_41(log: MarkdownLog) -> None:
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

    if has_key:
        log.write("[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_42(log: MarkdownLog) -> None:
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
        log.write(None)
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_43(log: MarkdownLog) -> None:
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
        log.write("XX[yellow]Run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]XX")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_44(log: MarkdownLog) -> None:
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
        log.write("[yellow]run [bold]hexa setup[/bold] from your terminal to configure.[/yellow]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_45(log: MarkdownLog) -> None:
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
        log.write("[YELLOW]RUN [BOLD]HEXA SETUP[/BOLD] FROM YOUR TERMINAL TO CONFIGURE.[/YELLOW]")
    else:
        log.write("[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_46(log: MarkdownLog) -> None:
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
        log.write(None)


def x_render_setup_info__mutmut_47(log: MarkdownLog) -> None:
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
        log.write("XX[dim]To change provider, exit and run [bold]hexa setup[/bold].[/dim]XX")


def x_render_setup_info__mutmut_48(log: MarkdownLog) -> None:
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
        log.write("[dim]to change provider, exit and run [bold]hexa setup[/bold].[/dim]")


def x_render_setup_info__mutmut_49(log: MarkdownLog) -> None:
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
        log.write("[DIM]TO CHANGE PROVIDER, EXIT AND RUN [BOLD]HEXA SETUP[/BOLD].[/DIM]")

mutants_x_render_setup_info__mutmut['_mutmut_orig'] = x_render_setup_info__mutmut_orig # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_1'] = x_render_setup_info__mutmut_1 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_2'] = x_render_setup_info__mutmut_2 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_3'] = x_render_setup_info__mutmut_3 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_4'] = x_render_setup_info__mutmut_4 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_5'] = x_render_setup_info__mutmut_5 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_6'] = x_render_setup_info__mutmut_6 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_7'] = x_render_setup_info__mutmut_7 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_8'] = x_render_setup_info__mutmut_8 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_9'] = x_render_setup_info__mutmut_9 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_10'] = x_render_setup_info__mutmut_10 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_11'] = x_render_setup_info__mutmut_11 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_12'] = x_render_setup_info__mutmut_12 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_13'] = x_render_setup_info__mutmut_13 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_14'] = x_render_setup_info__mutmut_14 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_15'] = x_render_setup_info__mutmut_15 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_16'] = x_render_setup_info__mutmut_16 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_17'] = x_render_setup_info__mutmut_17 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_18'] = x_render_setup_info__mutmut_18 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_19'] = x_render_setup_info__mutmut_19 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_20'] = x_render_setup_info__mutmut_20 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_21'] = x_render_setup_info__mutmut_21 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_22'] = x_render_setup_info__mutmut_22 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_23'] = x_render_setup_info__mutmut_23 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_24'] = x_render_setup_info__mutmut_24 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_25'] = x_render_setup_info__mutmut_25 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_26'] = x_render_setup_info__mutmut_26 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_27'] = x_render_setup_info__mutmut_27 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_28'] = x_render_setup_info__mutmut_28 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_29'] = x_render_setup_info__mutmut_29 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_30'] = x_render_setup_info__mutmut_30 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_31'] = x_render_setup_info__mutmut_31 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_32'] = x_render_setup_info__mutmut_32 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_33'] = x_render_setup_info__mutmut_33 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_34'] = x_render_setup_info__mutmut_34 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_35'] = x_render_setup_info__mutmut_35 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_36'] = x_render_setup_info__mutmut_36 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_37'] = x_render_setup_info__mutmut_37 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_38'] = x_render_setup_info__mutmut_38 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_39'] = x_render_setup_info__mutmut_39 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_40'] = x_render_setup_info__mutmut_40 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_41'] = x_render_setup_info__mutmut_41 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_42'] = x_render_setup_info__mutmut_42 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_43'] = x_render_setup_info__mutmut_43 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_44'] = x_render_setup_info__mutmut_44 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_45'] = x_render_setup_info__mutmut_45 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_46'] = x_render_setup_info__mutmut_46 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_47'] = x_render_setup_info__mutmut_47 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_48'] = x_render_setup_info__mutmut_48 # type: ignore # mutmut generated
mutants_x_render_setup_info__mutmut['x_render_setup_info__mutmut_49'] = x_render_setup_info__mutmut_49 # type: ignore # mutmut generated
