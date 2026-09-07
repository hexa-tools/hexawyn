from hexawyn.cli.presentation.asides import crashloop_finding_count, restarting_finding_count


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_format_finding_warnings__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_finding_warnings__mutmut)
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


def x_format_finding_warnings__mutmut_orig(findings: list[dict[str, object]]) -> list[str]:
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


def x_format_finding_warnings__mutmut_1(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = None
    cl_count = crashloop_finding_count(findings)
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append("[green]No active warnings[/green]")
    return lines


def x_format_finding_warnings__mutmut_2(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = None
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append("[green]No active warnings[/green]")
    return lines


def x_format_finding_warnings__mutmut_3(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(None)
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append("[green]No active warnings[/green]")
    return lines


def x_format_finding_warnings__mutmut_4(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(findings)
    r_count = None
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append("[green]No active warnings[/green]")
    return lines


def x_format_finding_warnings__mutmut_5(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(findings)
    r_count = restarting_finding_count(None)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append("[green]No active warnings[/green]")
    return lines


def x_format_finding_warnings__mutmut_6(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(findings)
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(None)
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append("[green]No active warnings[/green]")
    return lines


def x_format_finding_warnings__mutmut_7(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(findings)
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(None)
    if not lines:
        lines.append("[green]No active warnings[/green]")
    return lines


def x_format_finding_warnings__mutmut_8(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(findings)
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if lines:
        lines.append("[green]No active warnings[/green]")
    return lines


def x_format_finding_warnings__mutmut_9(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(findings)
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append(None)
    return lines


def x_format_finding_warnings__mutmut_10(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(findings)
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append("XX[green]No active warnings[/green]XX")
    return lines


def x_format_finding_warnings__mutmut_11(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(findings)
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append("[green]no active warnings[/green]")
    return lines


def x_format_finding_warnings__mutmut_12(findings: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    cl_count = crashloop_finding_count(findings)
    r_count = restarting_finding_count(findings)
    if cl_count:
        lines.append(f"\u26a0 {cl_count} CrashLoopBackOff detected")
    if r_count:
        lines.append(f"\u26a0 {r_count} pods with high restart count")
    if not lines:
        lines.append("[GREEN]NO ACTIVE WARNINGS[/GREEN]")
    return lines

mutants_x_format_finding_warnings__mutmut['_mutmut_orig'] = x_format_finding_warnings__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_1'] = x_format_finding_warnings__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_2'] = x_format_finding_warnings__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_3'] = x_format_finding_warnings__mutmut_3 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_4'] = x_format_finding_warnings__mutmut_4 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_5'] = x_format_finding_warnings__mutmut_5 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_6'] = x_format_finding_warnings__mutmut_6 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_7'] = x_format_finding_warnings__mutmut_7 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_8'] = x_format_finding_warnings__mutmut_8 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_9'] = x_format_finding_warnings__mutmut_9 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_10'] = x_format_finding_warnings__mutmut_10 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_11'] = x_format_finding_warnings__mutmut_11 # type: ignore # mutmut generated
mutants_x_format_finding_warnings__mutmut['x_format_finding_warnings__mutmut_12'] = x_format_finding_warnings__mutmut_12 # type: ignore # mutmut generated
