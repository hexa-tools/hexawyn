from hexawyn.infrastructure.license.license_reader import read_license_state


def format_license_aside_lines() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]License: invalid[/dim]"]

    expiry_display: str
    if state_info.state == "expired":
        expiry_display = "[red]expired[/]"
    elif state_info.days_remaining > 0:
        expiry_display = f"{state_info.expiry_date} ({state_info.days_remaining}d)"
    else:
        expiry_display = state_info.expiry_date

    return [
        "",
        f"[bold green]License: {state_info.plan.title()}[/]",
        f"[dim]Expires: {expiry_display}[/dim]",
    ]


def format_license_footer_hint(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"
