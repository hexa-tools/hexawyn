from __future__ import annotations

from hexawyn.domain.models.incident_triage import IncidentTriageReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_format_report_as_markdown__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_report_as_markdown__mutmut)
def format_report_as_markdown(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_orig(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_1(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = None

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_2(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            None
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_3(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n" - "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_4(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "XX\n**Insufficient data** — no events, logs, pod restarts, or pipeline XX"
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_5(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_6(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**INSUFFICIENT DATA** — NO EVENTS, LOGS, POD RESTARTS, OR PIPELINE "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_7(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "XXruns were found for this window.\n\nChecked:\nXX"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_8(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nchecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_9(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "RUNS WERE FOUND FOR THIS WINDOW.\n\nCHECKED:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_10(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(None)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_11(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "XX\nXX".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_12(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(None)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_13(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "XX\n\nXX".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_14(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(None)
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_15(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(None))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_16(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(None)
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_17(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(None))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_18(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(None)
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_19(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(None))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_20(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(None)
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_21(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(None))
    return "\n\n".join(sections)


def x_format_report_as_markdown__mutmut_22(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(None)


def x_format_report_as_markdown__mutmut_23(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "XX\n\nXX".join(sections)

mutants_x_format_report_as_markdown__mutmut['_mutmut_orig'] = x_format_report_as_markdown__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_1'] = x_format_report_as_markdown__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_2'] = x_format_report_as_markdown__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_3'] = x_format_report_as_markdown__mutmut_3 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_4'] = x_format_report_as_markdown__mutmut_4 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_5'] = x_format_report_as_markdown__mutmut_5 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_6'] = x_format_report_as_markdown__mutmut_6 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_7'] = x_format_report_as_markdown__mutmut_7 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_8'] = x_format_report_as_markdown__mutmut_8 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_9'] = x_format_report_as_markdown__mutmut_9 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_10'] = x_format_report_as_markdown__mutmut_10 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_11'] = x_format_report_as_markdown__mutmut_11 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_12'] = x_format_report_as_markdown__mutmut_12 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_13'] = x_format_report_as_markdown__mutmut_13 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_14'] = x_format_report_as_markdown__mutmut_14 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_15'] = x_format_report_as_markdown__mutmut_15 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_16'] = x_format_report_as_markdown__mutmut_16 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_17'] = x_format_report_as_markdown__mutmut_17 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_18'] = x_format_report_as_markdown__mutmut_18 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_19'] = x_format_report_as_markdown__mutmut_19 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_20'] = x_format_report_as_markdown__mutmut_20 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_21'] = x_format_report_as_markdown__mutmut_21 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_22'] = x_format_report_as_markdown__mutmut_22 # type: ignore # mutmut generated
mutants_x_format_report_as_markdown__mutmut['x_format_report_as_markdown__mutmut_23'] = x_format_report_as_markdown__mutmut_23 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__timeline_section__mutmut)
def _timeline_section(report: IncidentTriageReport) -> str:
    lines = [
        "## Timeline",
        "| Timestamp | Source | Object | Reason | Message |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_orig(report: IncidentTriageReport) -> str:
    lines = [
        "## Timeline",
        "| Timestamp | Source | Object | Reason | Message |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_1(report: IncidentTriageReport) -> str:
    lines = None
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_2(report: IncidentTriageReport) -> str:
    lines = [
        "XX## TimelineXX",
        "| Timestamp | Source | Object | Reason | Message |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_3(report: IncidentTriageReport) -> str:
    lines = [
        "## timeline",
        "| Timestamp | Source | Object | Reason | Message |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_4(report: IncidentTriageReport) -> str:
    lines = [
        "## TIMELINE",
        "| Timestamp | Source | Object | Reason | Message |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_5(report: IncidentTriageReport) -> str:
    lines = [
        "## Timeline",
        "XX| Timestamp | Source | Object | Reason | Message |XX",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_6(report: IncidentTriageReport) -> str:
    lines = [
        "## Timeline",
        "| timestamp | source | object | reason | message |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_7(report: IncidentTriageReport) -> str:
    lines = [
        "## Timeline",
        "| TIMESTAMP | SOURCE | OBJECT | REASON | MESSAGE |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_8(report: IncidentTriageReport) -> str:
    lines = [
        "## Timeline",
        "| Timestamp | Source | Object | Reason | Message |",
        "XX|---|---|---|---|---|XX",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_9(report: IncidentTriageReport) -> str:
    lines = [
        "## Timeline",
        "| Timestamp | Source | Object | Reason | Message |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            None  # noqa: E501
        )
    return "\n".join(lines)


def x__timeline_section__mutmut_10(report: IncidentTriageReport) -> str:
    lines = [
        "## Timeline",
        "| Timestamp | Source | Object | Reason | Message |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "\n".join(None)


def x__timeline_section__mutmut_11(report: IncidentTriageReport) -> str:
    lines = [
        "## Timeline",
        "| Timestamp | Source | Object | Reason | Message |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"  # noqa: E501
        )
    return "XX\nXX".join(lines)

mutants_x__timeline_section__mutmut['_mutmut_orig'] = x__timeline_section__mutmut_orig # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_1'] = x__timeline_section__mutmut_1 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_2'] = x__timeline_section__mutmut_2 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_3'] = x__timeline_section__mutmut_3 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_4'] = x__timeline_section__mutmut_4 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_5'] = x__timeline_section__mutmut_5 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_6'] = x__timeline_section__mutmut_6 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_7'] = x__timeline_section__mutmut_7 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_8'] = x__timeline_section__mutmut_8 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_9'] = x__timeline_section__mutmut_9 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_10'] = x__timeline_section__mutmut_10 # type: ignore # mutmut generated
mutants_x__timeline_section__mutmut['x__timeline_section__mutmut_11'] = x__timeline_section__mutmut_11 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__impact_section__mutmut)
def _impact_section(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_orig(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_1(report: IncidentTriageReport) -> str:
    lines = None
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_2(report: IncidentTriageReport) -> str:
    lines = ["XX## Impact AssessmentXX"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_3(report: IncidentTriageReport) -> str:
    lines = ["## impact assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_4(report: IncidentTriageReport) -> str:
    lines = ["## IMPACT ASSESSMENT"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_5(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(None)
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_6(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) and 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_7(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(None) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_8(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {'XX, XX'.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_9(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'XXnoneXX'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_10(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'NONE'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_11(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(None)
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_12(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact and 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_13(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'XXunknownXX'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_14(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'UNKNOWN'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_15(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(None)
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_16(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(None)
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_17(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(None)
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_18(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(None)
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_19(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append(None)
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_20(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("XX- **Cross-namespace correlation:**XX")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_21(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_22(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **CROSS-NAMESPACE CORRELATION:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def x__impact_section__mutmut_23(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(None)
    return "\n".join(lines)


def x__impact_section__mutmut_24(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(None)


def x__impact_section__mutmut_25(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "XX\nXX".join(lines)

mutants_x__impact_section__mutmut['_mutmut_orig'] = x__impact_section__mutmut_orig # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_1'] = x__impact_section__mutmut_1 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_2'] = x__impact_section__mutmut_2 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_3'] = x__impact_section__mutmut_3 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_4'] = x__impact_section__mutmut_4 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_5'] = x__impact_section__mutmut_5 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_6'] = x__impact_section__mutmut_6 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_7'] = x__impact_section__mutmut_7 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_8'] = x__impact_section__mutmut_8 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_9'] = x__impact_section__mutmut_9 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_10'] = x__impact_section__mutmut_10 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_11'] = x__impact_section__mutmut_11 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_12'] = x__impact_section__mutmut_12 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_13'] = x__impact_section__mutmut_13 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_14'] = x__impact_section__mutmut_14 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_15'] = x__impact_section__mutmut_15 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_16'] = x__impact_section__mutmut_16 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_17'] = x__impact_section__mutmut_17 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_18'] = x__impact_section__mutmut_18 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_19'] = x__impact_section__mutmut_19 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_20'] = x__impact_section__mutmut_20 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_21'] = x__impact_section__mutmut_21 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_22'] = x__impact_section__mutmut_22 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_23'] = x__impact_section__mutmut_23 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_24'] = x__impact_section__mutmut_24 # type: ignore # mutmut generated
mutants_x__impact_section__mutmut['x__impact_section__mutmut_25'] = x__impact_section__mutmut_25 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__root_cause_section__mutmut)
def _root_cause_section(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_orig(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_1(report: IncidentTriageReport) -> str:
    lines = None
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_2(report: IncidentTriageReport) -> str:
    lines = ["XX## Root CauseXX"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_3(report: IncidentTriageReport) -> str:
    lines = ["## root cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_4(report: IncidentTriageReport) -> str:
    lines = ["## ROOT CAUSE"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_5(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_6(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append(None)
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_7(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("XXNo root cause identified.XX")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_8(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("no root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_9(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("NO ROOT CAUSE IDENTIFIED.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_10(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(None)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_11(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "XX\nXX".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_12(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(None, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_13(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=None):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_14(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_15(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, ):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_16(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=2):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_17(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            None
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def x__root_cause_section__mutmut_18(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(None)
    return "\n".join(lines)


def x__root_cause_section__mutmut_19(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(None)


def x__root_cause_section__mutmut_20(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "XX\nXX".join(lines)

mutants_x__root_cause_section__mutmut['_mutmut_orig'] = x__root_cause_section__mutmut_orig # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_1'] = x__root_cause_section__mutmut_1 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_2'] = x__root_cause_section__mutmut_2 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_3'] = x__root_cause_section__mutmut_3 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_4'] = x__root_cause_section__mutmut_4 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_5'] = x__root_cause_section__mutmut_5 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_6'] = x__root_cause_section__mutmut_6 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_7'] = x__root_cause_section__mutmut_7 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_8'] = x__root_cause_section__mutmut_8 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_9'] = x__root_cause_section__mutmut_9 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_10'] = x__root_cause_section__mutmut_10 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_11'] = x__root_cause_section__mutmut_11 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_12'] = x__root_cause_section__mutmut_12 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_13'] = x__root_cause_section__mutmut_13 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_14'] = x__root_cause_section__mutmut_14 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_15'] = x__root_cause_section__mutmut_15 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_16'] = x__root_cause_section__mutmut_16 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_17'] = x__root_cause_section__mutmut_17 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_18'] = x__root_cause_section__mutmut_18 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_19'] = x__root_cause_section__mutmut_19 # type: ignore # mutmut generated
mutants_x__root_cause_section__mutmut['x__root_cause_section__mutmut_20'] = x__root_cause_section__mutmut_20 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__remediation_section__mutmut)
def _remediation_section(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_orig(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_1(report: IncidentTriageReport) -> str:
    lines = None
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_2(report: IncidentTriageReport) -> str:
    lines = ["XX## Remediation StepsXX"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_3(report: IncidentTriageReport) -> str:
    lines = ["## remediation steps"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_4(report: IncidentTriageReport) -> str:
    lines = ["## REMEDIATION STEPS"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_5(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_6(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append(None)
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_7(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("XXNo remediation steps available.XX")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_8(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("no remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_9(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("NO REMEDIATION STEPS AVAILABLE.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_10(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(None)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_11(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "XX\nXX".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)


def x__remediation_section__mutmut_12(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(None)
    return "\n".join(lines)


def x__remediation_section__mutmut_13(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(None)


def x__remediation_section__mutmut_14(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "XX\nXX".join(lines)

mutants_x__remediation_section__mutmut['_mutmut_orig'] = x__remediation_section__mutmut_orig # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_1'] = x__remediation_section__mutmut_1 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_2'] = x__remediation_section__mutmut_2 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_3'] = x__remediation_section__mutmut_3 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_4'] = x__remediation_section__mutmut_4 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_5'] = x__remediation_section__mutmut_5 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_6'] = x__remediation_section__mutmut_6 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_7'] = x__remediation_section__mutmut_7 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_8'] = x__remediation_section__mutmut_8 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_9'] = x__remediation_section__mutmut_9 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_10'] = x__remediation_section__mutmut_10 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_11'] = x__remediation_section__mutmut_11 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_12'] = x__remediation_section__mutmut_12 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_13'] = x__remediation_section__mutmut_13 # type: ignore # mutmut generated
mutants_x__remediation_section__mutmut['x__remediation_section__mutmut_14'] = x__remediation_section__mutmut_14 # type: ignore # mutmut generated
