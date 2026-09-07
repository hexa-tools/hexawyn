from typing import Any

from hexawyn.application.service.startup_scan_service import is_error_narrative


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_format_suggestion_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_suggestion_lines__mutmut)
def format_suggestion_lines(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_orig(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_1(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = None

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_2(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "XX[dim]─────────────────────────────[/dim]XX",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_3(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[DIM]─────────────────────────────[/DIM]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_4(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "XXXX",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_5(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "XX[bold]Suggestions[/bold]XX",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_6(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_7(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[BOLD]SUGGESTIONS[/BOLD]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_8(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "XXXX",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_9(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(None)
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_10(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append(None)

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_11(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("XXXX")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_12(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_13(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = None
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_14(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get(None, [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_15(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", None)
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_16(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get([])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_17(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", )
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_18(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("XXsuggestionsXX", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_19(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("SUGGESTIONS", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_20(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = None
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_21(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(None)
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_22(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get(None, ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_23(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", None))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_24(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get(""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_25(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_26(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("XXlabelXX", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_27(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("LABEL", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_28(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", "XXXX"))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_29(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = None
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_30(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(None)
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_31(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get(None, ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_32(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", None))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_33(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get(""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_34(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_35(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("XXexplanationXX", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_36(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("EXPLANATION", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_37(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", "XXXX"))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_38(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = None
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_39(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(None)
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_40(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get(None, "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_41(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", None))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_42(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_43(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", ))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_44(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("XXseverityXX", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_45(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("SEVERITY", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_46(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "XXinfoXX"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_47(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "INFO"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_48(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = None
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_49(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "XX\U0001f534XX"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_50(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001F534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_51(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity != "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_52(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "XXcriticalXX"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_53(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "CRITICAL"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_54(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "XX\U0001f7e1XX"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_55(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001F7E1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_56(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity != "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_57(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "XXwarningXX"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_58(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "WARNING"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_59(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "XX\u26aaXX"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_60(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26AA"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_61(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label or explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_62(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(None)
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_63(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(None)
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_64(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(None)

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_65(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = None
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_66(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(None)
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_67(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get(None, ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_68(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", None))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_69(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get(""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_70(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_71(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("XXnarrative_summaryXX", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_72(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("NARRATIVE_SUMMARY", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_73(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", "XXXX"))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_74(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative or not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_75(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_76(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(None):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_77(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append(None)
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_78(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("XXXX")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_79(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(None)

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_80(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines and len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_81(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_82(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) < 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_83(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 6:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:4])

    return lines


def x_format_suggestion_lines__mutmut_84(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(None)

    return lines


def x_format_suggestion_lines__mutmut_85(  # noqa: C901
    app: Any,
    suggestions: list[str],
) -> list[str]:
    lines: list[str] = [
        "[dim]─────────────────────────────[/dim]",
        "",
        "[bold]Suggestions[/bold]",
        "",
    ]

    if app.ai_suggestion:
        lines.append(f"[bold #3B82F6]\U0001f4a1 {app.ai_suggestion}[/bold #3B82F6]")
        lines.append("")

    if app.startup_result is not None:
        startup_suggestions = app.startup_result.get("suggestions", [])
        if isinstance(startup_suggestions, list):
            for sug in startup_suggestions:
                if isinstance(sug, dict):
                    label = str(sug.get("label", ""))
                    explanation = str(sug.get("explanation", ""))
                    severity = str(sug.get("severity", "info"))
                    sev_icon = (
                        "\U0001f534"
                        if severity == "critical"
                        else "\U0001f7e1"
                        if severity == "warning"
                        else "\u26aa"
                    )
                    if label and explanation:
                        lines.append(f"{sev_icon} {label}")
                        lines.append(f"   [dim]{explanation}[/dim]")
                    elif label:
                        lines.append(f"{sev_icon} {label}")

        narrative = str(app.startup_result.get("narrative_summary", ""))
        if narrative and not is_error_narrative(narrative):
            lines.append("")
            lines.append(f"[dim italic]{narrative}[/dim italic]")

    if not lines or len(lines) <= 5:  # noqa: PLR2004
        if suggestions:
            lines.extend(f"\u2022 {s}" for s in suggestions[:5])

    return lines

mutants_x_format_suggestion_lines__mutmut['_mutmut_orig'] = x_format_suggestion_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_1'] = x_format_suggestion_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_2'] = x_format_suggestion_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_3'] = x_format_suggestion_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_4'] = x_format_suggestion_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_5'] = x_format_suggestion_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_6'] = x_format_suggestion_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_7'] = x_format_suggestion_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_8'] = x_format_suggestion_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_9'] = x_format_suggestion_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_10'] = x_format_suggestion_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_11'] = x_format_suggestion_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_12'] = x_format_suggestion_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_13'] = x_format_suggestion_lines__mutmut_13 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_14'] = x_format_suggestion_lines__mutmut_14 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_15'] = x_format_suggestion_lines__mutmut_15 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_16'] = x_format_suggestion_lines__mutmut_16 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_17'] = x_format_suggestion_lines__mutmut_17 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_18'] = x_format_suggestion_lines__mutmut_18 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_19'] = x_format_suggestion_lines__mutmut_19 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_20'] = x_format_suggestion_lines__mutmut_20 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_21'] = x_format_suggestion_lines__mutmut_21 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_22'] = x_format_suggestion_lines__mutmut_22 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_23'] = x_format_suggestion_lines__mutmut_23 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_24'] = x_format_suggestion_lines__mutmut_24 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_25'] = x_format_suggestion_lines__mutmut_25 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_26'] = x_format_suggestion_lines__mutmut_26 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_27'] = x_format_suggestion_lines__mutmut_27 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_28'] = x_format_suggestion_lines__mutmut_28 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_29'] = x_format_suggestion_lines__mutmut_29 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_30'] = x_format_suggestion_lines__mutmut_30 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_31'] = x_format_suggestion_lines__mutmut_31 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_32'] = x_format_suggestion_lines__mutmut_32 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_33'] = x_format_suggestion_lines__mutmut_33 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_34'] = x_format_suggestion_lines__mutmut_34 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_35'] = x_format_suggestion_lines__mutmut_35 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_36'] = x_format_suggestion_lines__mutmut_36 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_37'] = x_format_suggestion_lines__mutmut_37 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_38'] = x_format_suggestion_lines__mutmut_38 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_39'] = x_format_suggestion_lines__mutmut_39 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_40'] = x_format_suggestion_lines__mutmut_40 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_41'] = x_format_suggestion_lines__mutmut_41 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_42'] = x_format_suggestion_lines__mutmut_42 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_43'] = x_format_suggestion_lines__mutmut_43 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_44'] = x_format_suggestion_lines__mutmut_44 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_45'] = x_format_suggestion_lines__mutmut_45 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_46'] = x_format_suggestion_lines__mutmut_46 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_47'] = x_format_suggestion_lines__mutmut_47 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_48'] = x_format_suggestion_lines__mutmut_48 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_49'] = x_format_suggestion_lines__mutmut_49 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_50'] = x_format_suggestion_lines__mutmut_50 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_51'] = x_format_suggestion_lines__mutmut_51 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_52'] = x_format_suggestion_lines__mutmut_52 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_53'] = x_format_suggestion_lines__mutmut_53 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_54'] = x_format_suggestion_lines__mutmut_54 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_55'] = x_format_suggestion_lines__mutmut_55 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_56'] = x_format_suggestion_lines__mutmut_56 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_57'] = x_format_suggestion_lines__mutmut_57 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_58'] = x_format_suggestion_lines__mutmut_58 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_59'] = x_format_suggestion_lines__mutmut_59 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_60'] = x_format_suggestion_lines__mutmut_60 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_61'] = x_format_suggestion_lines__mutmut_61 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_62'] = x_format_suggestion_lines__mutmut_62 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_63'] = x_format_suggestion_lines__mutmut_63 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_64'] = x_format_suggestion_lines__mutmut_64 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_65'] = x_format_suggestion_lines__mutmut_65 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_66'] = x_format_suggestion_lines__mutmut_66 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_67'] = x_format_suggestion_lines__mutmut_67 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_68'] = x_format_suggestion_lines__mutmut_68 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_69'] = x_format_suggestion_lines__mutmut_69 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_70'] = x_format_suggestion_lines__mutmut_70 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_71'] = x_format_suggestion_lines__mutmut_71 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_72'] = x_format_suggestion_lines__mutmut_72 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_73'] = x_format_suggestion_lines__mutmut_73 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_74'] = x_format_suggestion_lines__mutmut_74 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_75'] = x_format_suggestion_lines__mutmut_75 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_76'] = x_format_suggestion_lines__mutmut_76 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_77'] = x_format_suggestion_lines__mutmut_77 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_78'] = x_format_suggestion_lines__mutmut_78 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_79'] = x_format_suggestion_lines__mutmut_79 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_80'] = x_format_suggestion_lines__mutmut_80 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_81'] = x_format_suggestion_lines__mutmut_81 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_82'] = x_format_suggestion_lines__mutmut_82 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_83'] = x_format_suggestion_lines__mutmut_83 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_84'] = x_format_suggestion_lines__mutmut_84 # type: ignore # mutmut generated
mutants_x_format_suggestion_lines__mutmut['x_format_suggestion_lines__mutmut_85'] = x_format_suggestion_lines__mutmut_85 # type: ignore # mutmut generated
