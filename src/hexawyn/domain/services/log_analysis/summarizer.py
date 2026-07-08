import re

_PATTERN_LINE_RE = re.compile(r"^\[(\d+)x\]\s+(.+?)\s+—\s+e\.g\.\s+'(.+)'$")
_NO_DATA_SUMMARY = "No log data available to summarize."


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


def _severity_hint(severity: str) -> str:
    if severity == "critical":
        return "likely requires immediate investigation"
    if severity in ("high", "medium"):
        return "worth investigating"
    return "monitor for recurrence"
