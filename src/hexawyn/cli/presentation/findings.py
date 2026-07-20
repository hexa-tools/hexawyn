from hexawyn.cli.presentation.asides import crashloop_finding_count, restarting_finding_count


def is_error_narrative(text: str) -> bool:
    skip = [
        "not available",
        "unavailable",
        "install hexawyn",
        "is down",
        "no node",
        "no pods",
        "0 pods",
        "Runtime not available",
        "startup scan requires",
        "empty and inactive",
    ]
    text_lower = text.lower()
    return any(p.lower() in text_lower for p in skip)


def format_finding_warnings(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(findings)
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append("[green]No active warnings[/green]")
    return lines
