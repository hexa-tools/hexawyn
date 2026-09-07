from hexawyn.infrastructure.license.license_reader import read_license_state


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_format_license_aside_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_license_aside_lines__mutmut)
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


def x_format_license_aside_lines__mutmut_orig() -> list[str]:
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


def x_format_license_aside_lines__mutmut_1() -> list[str]:
    state_info = None

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


def x_format_license_aside_lines__mutmut_2() -> list[str]:
    state_info = read_license_state()

    if state_info.state != "missing":
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


def x_format_license_aside_lines__mutmut_3() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "XXmissingXX":
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


def x_format_license_aside_lines__mutmut_4() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "MISSING":
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


def x_format_license_aside_lines__mutmut_5() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["XXXX", "[dim]License: not configured[/dim]"]
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


def x_format_license_aside_lines__mutmut_6() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "XX[dim]License: not configured[/dim]XX"]
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


def x_format_license_aside_lines__mutmut_7() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]license: not configured[/dim]"]
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


def x_format_license_aside_lines__mutmut_8() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[DIM]LICENSE: NOT CONFIGURED[/DIM]"]
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


def x_format_license_aside_lines__mutmut_9() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state != "invalid":
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


def x_format_license_aside_lines__mutmut_10() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "XXinvalidXX":
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


def x_format_license_aside_lines__mutmut_11() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "INVALID":
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


def x_format_license_aside_lines__mutmut_12() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["XXXX", "[dim]License: invalid[/dim]"]

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


def x_format_license_aside_lines__mutmut_13() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "XX[dim]License: invalid[/dim]XX"]

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


def x_format_license_aside_lines__mutmut_14() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]license: invalid[/dim]"]

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


def x_format_license_aside_lines__mutmut_15() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[DIM]LICENSE: INVALID[/DIM]"]

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


def x_format_license_aside_lines__mutmut_16() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]License: invalid[/dim]"]

    expiry_display: str
    if state_info.state != "expired":
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


def x_format_license_aside_lines__mutmut_17() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]License: invalid[/dim]"]

    expiry_display: str
    if state_info.state == "XXexpiredXX":
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


def x_format_license_aside_lines__mutmut_18() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]License: invalid[/dim]"]

    expiry_display: str
    if state_info.state == "EXPIRED":
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


def x_format_license_aside_lines__mutmut_19() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]License: invalid[/dim]"]

    expiry_display: str
    if state_info.state == "expired":
        expiry_display = None
    elif state_info.days_remaining > 0:
        expiry_display = f"{state_info.expiry_date} ({state_info.days_remaining}d)"
    else:
        expiry_display = state_info.expiry_date

    return [
        "",
        f"[bold green]License: {state_info.plan.title()}[/]",
        f"[dim]Expires: {expiry_display}[/dim]",
    ]


def x_format_license_aside_lines__mutmut_20() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]License: invalid[/dim]"]

    expiry_display: str
    if state_info.state == "expired":
        expiry_display = "XX[red]expired[/]XX"
    elif state_info.days_remaining > 0:
        expiry_display = f"{state_info.expiry_date} ({state_info.days_remaining}d)"
    else:
        expiry_display = state_info.expiry_date

    return [
        "",
        f"[bold green]License: {state_info.plan.title()}[/]",
        f"[dim]Expires: {expiry_display}[/dim]",
    ]


def x_format_license_aside_lines__mutmut_21() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]License: invalid[/dim]"]

    expiry_display: str
    if state_info.state == "expired":
        expiry_display = "[RED]EXPIRED[/]"
    elif state_info.days_remaining > 0:
        expiry_display = f"{state_info.expiry_date} ({state_info.days_remaining}d)"
    else:
        expiry_display = state_info.expiry_date

    return [
        "",
        f"[bold green]License: {state_info.plan.title()}[/]",
        f"[dim]Expires: {expiry_display}[/dim]",
    ]


def x_format_license_aside_lines__mutmut_22() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]License: invalid[/dim]"]

    expiry_display: str
    if state_info.state == "expired":
        expiry_display = "[red]expired[/]"
    elif state_info.days_remaining >= 0:
        expiry_display = f"{state_info.expiry_date} ({state_info.days_remaining}d)"
    else:
        expiry_display = state_info.expiry_date

    return [
        "",
        f"[bold green]License: {state_info.plan.title()}[/]",
        f"[dim]Expires: {expiry_display}[/dim]",
    ]


def x_format_license_aside_lines__mutmut_23() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]License: invalid[/dim]"]

    expiry_display: str
    if state_info.state == "expired":
        expiry_display = "[red]expired[/]"
    elif state_info.days_remaining > 1:
        expiry_display = f"{state_info.expiry_date} ({state_info.days_remaining}d)"
    else:
        expiry_display = state_info.expiry_date

    return [
        "",
        f"[bold green]License: {state_info.plan.title()}[/]",
        f"[dim]Expires: {expiry_display}[/dim]",
    ]


def x_format_license_aside_lines__mutmut_24() -> list[str]:
    state_info = read_license_state()

    if state_info.state == "missing":
        return ["", "[dim]License: not configured[/dim]"]
    if state_info.state == "invalid":
        return ["", "[dim]License: invalid[/dim]"]

    expiry_display: str
    if state_info.state == "expired":
        expiry_display = "[red]expired[/]"
    elif state_info.days_remaining > 0:
        expiry_display = None
    else:
        expiry_display = state_info.expiry_date

    return [
        "",
        f"[bold green]License: {state_info.plan.title()}[/]",
        f"[dim]Expires: {expiry_display}[/dim]",
    ]


def x_format_license_aside_lines__mutmut_25() -> list[str]:
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
        expiry_display = None

    return [
        "",
        f"[bold green]License: {state_info.plan.title()}[/]",
        f"[dim]Expires: {expiry_display}[/dim]",
    ]


def x_format_license_aside_lines__mutmut_26() -> list[str]:
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
        "XXXX",
        f"[bold green]License: {state_info.plan.title()}[/]",
        f"[dim]Expires: {expiry_display}[/dim]",
    ]

mutants_x_format_license_aside_lines__mutmut['_mutmut_orig'] = x_format_license_aside_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_1'] = x_format_license_aside_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_2'] = x_format_license_aside_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_3'] = x_format_license_aside_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_4'] = x_format_license_aside_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_5'] = x_format_license_aside_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_6'] = x_format_license_aside_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_7'] = x_format_license_aside_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_8'] = x_format_license_aside_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_9'] = x_format_license_aside_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_10'] = x_format_license_aside_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_11'] = x_format_license_aside_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_12'] = x_format_license_aside_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_13'] = x_format_license_aside_lines__mutmut_13 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_14'] = x_format_license_aside_lines__mutmut_14 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_15'] = x_format_license_aside_lines__mutmut_15 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_16'] = x_format_license_aside_lines__mutmut_16 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_17'] = x_format_license_aside_lines__mutmut_17 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_18'] = x_format_license_aside_lines__mutmut_18 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_19'] = x_format_license_aside_lines__mutmut_19 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_20'] = x_format_license_aside_lines__mutmut_20 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_21'] = x_format_license_aside_lines__mutmut_21 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_22'] = x_format_license_aside_lines__mutmut_22 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_23'] = x_format_license_aside_lines__mutmut_23 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_24'] = x_format_license_aside_lines__mutmut_24 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_25'] = x_format_license_aside_lines__mutmut_25 # type: ignore # mutmut generated
mutants_x_format_license_aside_lines__mutmut['x_format_license_aside_lines__mutmut_26'] = x_format_license_aside_lines__mutmut_26 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_license_footer_hint__mutmut)
def format_license_footer_hint(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_orig(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_1(state: str) -> str:
    if state != "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_2(state: str) -> str:
    if state == "XXexpiredXX":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_3(state: str) -> str:
    if state == "EXPIRED":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_4(state: str) -> str:
    if state == "expired":
        return "XX[bold #f97316]Ctrl+B[#f97316] upgrade[/]XX"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_5(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]ctrl+b[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_6(state: str) -> str:
    if state == "expired":
        return "[BOLD #F97316]CTRL+B[#F97316] UPGRADE[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_7(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state != "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_8(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "XXwarningXX":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_9(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "WARNING":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_10(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "XX[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]XX"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_11(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]ctrl+b[/] [dim]upgrade[/dim]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_12(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[BOLD #F97316]CTRL+B[/] [DIM]UPGRADE[/DIM]"
    return "[bold]Ctrl+B[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_13(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "XX[bold]Ctrl+B[/bold] [dim]manage[/dim]XX"


def x_format_license_footer_hint__mutmut_14(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[bold]ctrl+b[/bold] [dim]manage[/dim]"


def x_format_license_footer_hint__mutmut_15(state: str) -> str:
    if state == "expired":
        return "[bold #f97316]Ctrl+B[#f97316] upgrade[/]"
    if state == "warning":
        return "[bold #f97316]Ctrl+B[/] [dim]upgrade[/dim]"
    return "[BOLD]CTRL+B[/BOLD] [DIM]MANAGE[/DIM]"

mutants_x_format_license_footer_hint__mutmut['_mutmut_orig'] = x_format_license_footer_hint__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_1'] = x_format_license_footer_hint__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_2'] = x_format_license_footer_hint__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_3'] = x_format_license_footer_hint__mutmut_3 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_4'] = x_format_license_footer_hint__mutmut_4 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_5'] = x_format_license_footer_hint__mutmut_5 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_6'] = x_format_license_footer_hint__mutmut_6 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_7'] = x_format_license_footer_hint__mutmut_7 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_8'] = x_format_license_footer_hint__mutmut_8 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_9'] = x_format_license_footer_hint__mutmut_9 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_10'] = x_format_license_footer_hint__mutmut_10 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_11'] = x_format_license_footer_hint__mutmut_11 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_12'] = x_format_license_footer_hint__mutmut_12 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_13'] = x_format_license_footer_hint__mutmut_13 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_14'] = x_format_license_footer_hint__mutmut_14 # type: ignore # mutmut generated
mutants_x_format_license_footer_hint__mutmut['x_format_license_footer_hint__mutmut_15'] = x_format_license_footer_hint__mutmut_15 # type: ignore # mutmut generated
