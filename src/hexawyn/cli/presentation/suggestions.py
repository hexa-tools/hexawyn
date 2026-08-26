from typing import Any

from hexawyn.application.service.startup_scan_service import is_error_narrative


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
