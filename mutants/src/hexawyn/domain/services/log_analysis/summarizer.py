import re

_PATTERN_LINE_RE = re.compile(r"^\[(\d+)x\]\s+(.+?)\s+—\s+e\.g\.\s+'(.+)'$")
_NO_DATA_SUMMARY = "No log data available to summarize."


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_generate_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_generate_summary__mutmut)
def generate_summary(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if not reduced_lines:
        return _NO_DATA_SUMMARY, True

    match = _PATTERN_LINE_RE.match(reduced_lines[0])
    if match:
        count, pattern, sample = match.groups()
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(severity)}.",
            False,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        False,
    )


def x_generate_summary__mutmut_orig(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if not reduced_lines:
        return _NO_DATA_SUMMARY, True

    match = _PATTERN_LINE_RE.match(reduced_lines[0])
    if match:
        count, pattern, sample = match.groups()
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(severity)}.",
            False,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        False,
    )


def x_generate_summary__mutmut_1(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if reduced_lines:
        return _NO_DATA_SUMMARY, True

    match = _PATTERN_LINE_RE.match(reduced_lines[0])
    if match:
        count, pattern, sample = match.groups()
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(severity)}.",
            False,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        False,
    )


def x_generate_summary__mutmut_2(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if not reduced_lines:
        return _NO_DATA_SUMMARY, False

    match = _PATTERN_LINE_RE.match(reduced_lines[0])
    if match:
        count, pattern, sample = match.groups()
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(severity)}.",
            False,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        False,
    )


def x_generate_summary__mutmut_3(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if not reduced_lines:
        return _NO_DATA_SUMMARY, True

    match = None
    if match:
        count, pattern, sample = match.groups()
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(severity)}.",
            False,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        False,
    )


def x_generate_summary__mutmut_4(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if not reduced_lines:
        return _NO_DATA_SUMMARY, True

    match = _PATTERN_LINE_RE.match(None)
    if match:
        count, pattern, sample = match.groups()
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(severity)}.",
            False,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        False,
    )


def x_generate_summary__mutmut_5(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if not reduced_lines:
        return _NO_DATA_SUMMARY, True

    match = _PATTERN_LINE_RE.match(reduced_lines[1])
    if match:
        count, pattern, sample = match.groups()
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(severity)}.",
            False,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        False,
    )


def x_generate_summary__mutmut_6(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if not reduced_lines:
        return _NO_DATA_SUMMARY, True

    match = _PATTERN_LINE_RE.match(reduced_lines[0])
    if match:
        count, pattern, sample = None
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(severity)}.",
            False,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        False,
    )


def x_generate_summary__mutmut_7(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if not reduced_lines:
        return _NO_DATA_SUMMARY, True

    match = _PATTERN_LINE_RE.match(reduced_lines[0])
    if match:
        count, pattern, sample = match.groups()
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(None)}.",
            False,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        False,
    )


def x_generate_summary__mutmut_8(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if not reduced_lines:
        return _NO_DATA_SUMMARY, True

    match = _PATTERN_LINE_RE.match(reduced_lines[0])
    if match:
        count, pattern, sample = match.groups()
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(severity)}.",
            True,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        False,
    )


def x_generate_summary__mutmut_9(reduced_lines: list[str], severity: str) -> tuple[str, bool]:
    """Deterministic, template-based natural-language summary.

    Stands in for a real LLM-backed summarizer — this repo makes no
    outbound LLM call (see docs/use-cases/58-hybrid-log-analysis.md).
    This function is the isolated seam where a real Anthropic/local-model
    adapter would plug in later, behind the same (reduced_lines, severity)
    -> (summary, degraded) contract.

    Returns (summary, degraded). degraded=True means there was nothing to
    summarize (empty reduced input) — the pattern-only output should be
    used and a warning surfaced.
    """
    if not reduced_lines:
        return _NO_DATA_SUMMARY, True

    match = _PATTERN_LINE_RE.match(reduced_lines[0])
    if match:
        count, pattern, sample = match.groups()
        return (
            f"Recurring '{pattern}' pattern detected {count} times "
            f"(e.g. {sample!r}) — {_severity_hint(severity)}.",
            False,
        )

    return (
        f"No recurring error patterns detected across {len(reduced_lines)} sampled "
        f"lines — no anomalies found.",
        True,
    )

mutants_x_generate_summary__mutmut['_mutmut_orig'] = x_generate_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x_generate_summary__mutmut['x_generate_summary__mutmut_1'] = x_generate_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x_generate_summary__mutmut['x_generate_summary__mutmut_2'] = x_generate_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x_generate_summary__mutmut['x_generate_summary__mutmut_3'] = x_generate_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x_generate_summary__mutmut['x_generate_summary__mutmut_4'] = x_generate_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x_generate_summary__mutmut['x_generate_summary__mutmut_5'] = x_generate_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x_generate_summary__mutmut['x_generate_summary__mutmut_6'] = x_generate_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x_generate_summary__mutmut['x_generate_summary__mutmut_7'] = x_generate_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x_generate_summary__mutmut['x_generate_summary__mutmut_8'] = x_generate_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x_generate_summary__mutmut['x_generate_summary__mutmut_9'] = x_generate_summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__severity_hint__mutmut)
def _severity_hint(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("high", "medium"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_orig(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("high", "medium"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_1(severity: str) -> str:
    if severity != "critical":
        return "likely requires immediate investigation"
    if severity in ("high", "medium"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_2(severity: str) -> str:
    if severity == "XXcriticalXX":
        return "likely requires immediate investigation"
    if severity in ("high", "medium"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_3(severity: str) -> str:
    if severity == "CRITICAL":
        return "likely requires immediate investigation"
    if severity in ("high", "medium"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_4(severity: str) -> str:
    if severity == "critical":
        return "XXlikely requires immediate investigationXX"
    if severity in ("high", "medium"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_5(severity: str) -> str:
    if severity == "critical":
        return "LIKELY REQUIRES IMMEDIATE INVESTIGATION"
    if severity in ("high", "medium"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_6(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity not in ("high", "medium"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_7(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("XXhighXX", "medium"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_8(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("HIGH", "medium"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_9(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("high", "XXmediumXX"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_10(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("high", "MEDIUM"):
        return "worth investigating"
    return "monitor for recurrence"


def x__severity_hint__mutmut_11(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("high", "medium"):
        return "XXworth investigatingXX"
    return "monitor for recurrence"


def x__severity_hint__mutmut_12(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("high", "medium"):
        return "WORTH INVESTIGATING"
    return "monitor for recurrence"


def x__severity_hint__mutmut_13(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("high", "medium"):
        return "worth investigating"
    return "XXmonitor for recurrenceXX"


def x__severity_hint__mutmut_14(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("high", "medium"):
        return "worth investigating"
    return "MONITOR FOR RECURRENCE"

mutants_x__severity_hint__mutmut['_mutmut_orig'] = x__severity_hint__mutmut_orig # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_1'] = x__severity_hint__mutmut_1 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_2'] = x__severity_hint__mutmut_2 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_3'] = x__severity_hint__mutmut_3 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_4'] = x__severity_hint__mutmut_4 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_5'] = x__severity_hint__mutmut_5 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_6'] = x__severity_hint__mutmut_6 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_7'] = x__severity_hint__mutmut_7 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_8'] = x__severity_hint__mutmut_8 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_9'] = x__severity_hint__mutmut_9 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_10'] = x__severity_hint__mutmut_10 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_11'] = x__severity_hint__mutmut_11 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_12'] = x__severity_hint__mutmut_12 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_13'] = x__severity_hint__mutmut_13 # type: ignore # mutmut generated
mutants_x__severity_hint__mutmut['x__severity_hint__mutmut_14'] = x__severity_hint__mutmut_14 # type: ignore # mutmut generated
