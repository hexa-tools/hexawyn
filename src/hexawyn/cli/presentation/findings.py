from hexawyn.cli.presentation.asides import crashloop_finding_count, restarting_finding_count


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
