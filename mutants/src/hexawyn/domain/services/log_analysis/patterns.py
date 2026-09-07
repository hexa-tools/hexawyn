import re

from hexawyn.domain.models.analyze_pod_logs import (
    ConnectionIssue,
    ConnectionIssueCategory,
    PodLogLine,
)

_TIMEOUT_PATTERNS = (
    re.compile(r"connection timeout", re.IGNORECASE),
    re.compile(r"timed out connecting", re.IGNORECASE),
    re.compile(r"i/o timeout", re.IGNORECASE),
)
_REFUSED_PATTERNS = (
    re.compile(r"connection refused", re.IGNORECASE),
    re.compile(r"upstream connect error", re.IGNORECASE),
    re.compile(r"dial tcp.*refused", re.IGNORECASE),
)
_CONFIDENCE_BASE = 0.5
_CONFIDENCE_STEP = 0.05


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_categorize_connection_issues__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_categorize_connection_issues__mutmut)
def categorize_connection_issues(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_orig(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_1(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = None
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_2(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = None

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_3(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(None, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_4(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, None):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_5(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(_TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_6(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, ):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_7(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = None
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_8(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) - 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_9(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(None, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_10(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, None) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_11(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_12(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, ) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_13(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 1) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_14(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 2
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_15(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(None, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_16(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, None):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_17(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(_REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_18(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, ):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_19(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = None

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_20(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) - 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_21(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(None, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_22(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, None) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_23(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_24(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, ) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_25(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 1) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_26(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 2

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_27(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = None
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_28(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues(None, timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_29(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", None)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_30(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues(timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_31(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", )
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_32(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("XXconnection_timeoutXX", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_33(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("CONNECTION_TIMEOUT", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_34(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = None
    return timeouts, refused


def x_categorize_connection_issues__mutmut_35(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues(None, refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_36(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", None)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_37(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues(refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_38(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", )
    return timeouts, refused


def x_categorize_connection_issues__mutmut_39(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("XXconnection_refusedXX", refused_counts)
    return timeouts, refused


def x_categorize_connection_issues__mutmut_40(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("CONNECTION_REFUSED", refused_counts)
    return timeouts, refused

mutants_x_categorize_connection_issues__mutmut['_mutmut_orig'] = x_categorize_connection_issues__mutmut_orig # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_1'] = x_categorize_connection_issues__mutmut_1 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_2'] = x_categorize_connection_issues__mutmut_2 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_3'] = x_categorize_connection_issues__mutmut_3 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_4'] = x_categorize_connection_issues__mutmut_4 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_5'] = x_categorize_connection_issues__mutmut_5 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_6'] = x_categorize_connection_issues__mutmut_6 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_7'] = x_categorize_connection_issues__mutmut_7 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_8'] = x_categorize_connection_issues__mutmut_8 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_9'] = x_categorize_connection_issues__mutmut_9 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_10'] = x_categorize_connection_issues__mutmut_10 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_11'] = x_categorize_connection_issues__mutmut_11 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_12'] = x_categorize_connection_issues__mutmut_12 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_13'] = x_categorize_connection_issues__mutmut_13 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_14'] = x_categorize_connection_issues__mutmut_14 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_15'] = x_categorize_connection_issues__mutmut_15 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_16'] = x_categorize_connection_issues__mutmut_16 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_17'] = x_categorize_connection_issues__mutmut_17 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_18'] = x_categorize_connection_issues__mutmut_18 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_19'] = x_categorize_connection_issues__mutmut_19 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_20'] = x_categorize_connection_issues__mutmut_20 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_21'] = x_categorize_connection_issues__mutmut_21 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_22'] = x_categorize_connection_issues__mutmut_22 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_23'] = x_categorize_connection_issues__mutmut_23 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_24'] = x_categorize_connection_issues__mutmut_24 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_25'] = x_categorize_connection_issues__mutmut_25 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_26'] = x_categorize_connection_issues__mutmut_26 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_27'] = x_categorize_connection_issues__mutmut_27 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_28'] = x_categorize_connection_issues__mutmut_28 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_29'] = x_categorize_connection_issues__mutmut_29 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_30'] = x_categorize_connection_issues__mutmut_30 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_31'] = x_categorize_connection_issues__mutmut_31 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_32'] = x_categorize_connection_issues__mutmut_32 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_33'] = x_categorize_connection_issues__mutmut_33 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_34'] = x_categorize_connection_issues__mutmut_34 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_35'] = x_categorize_connection_issues__mutmut_35 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_36'] = x_categorize_connection_issues__mutmut_36 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_37'] = x_categorize_connection_issues__mutmut_37 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_38'] = x_categorize_connection_issues__mutmut_38 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_39'] = x_categorize_connection_issues__mutmut_39 # type: ignore # mutmut generated
mutants_x_categorize_connection_issues__mutmut['x_categorize_connection_issues__mutmut_40'] = x_categorize_connection_issues__mutmut_40 # type: ignore # mutmut generated
mutants_x__matches_any__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__matches_any__mutmut)
def _matches_any(message: str, patterns: tuple[re.Pattern[str], ...]) -> bool:
    return any(pattern.search(message) for pattern in patterns)


def x__matches_any__mutmut_orig(message: str, patterns: tuple[re.Pattern[str], ...]) -> bool:
    return any(pattern.search(message) for pattern in patterns)


def x__matches_any__mutmut_1(message: str, patterns: tuple[re.Pattern[str], ...]) -> bool:
    return any(None)


def x__matches_any__mutmut_2(message: str, patterns: tuple[re.Pattern[str], ...]) -> bool:
    return any(pattern.search(None) for pattern in patterns)

mutants_x__matches_any__mutmut['_mutmut_orig'] = x__matches_any__mutmut_orig # type: ignore # mutmut generated
mutants_x__matches_any__mutmut['x__matches_any__mutmut_1'] = x__matches_any__mutmut_1 # type: ignore # mutmut generated
mutants_x__matches_any__mutmut['x__matches_any__mutmut_2'] = x__matches_any__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_issues__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_issues__mutmut)
def _build_issues(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=category,
            message_sample=message,
            count=count,
            confidence=_confidence(count),
        )
        for message, count in counts.items()
    ]


def x__build_issues__mutmut_orig(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=category,
            message_sample=message,
            count=count,
            confidence=_confidence(count),
        )
        for message, count in counts.items()
    ]


def x__build_issues__mutmut_1(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=None,
            message_sample=message,
            count=count,
            confidence=_confidence(count),
        )
        for message, count in counts.items()
    ]


def x__build_issues__mutmut_2(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=category,
            message_sample=None,
            count=count,
            confidence=_confidence(count),
        )
        for message, count in counts.items()
    ]


def x__build_issues__mutmut_3(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=category,
            message_sample=message,
            count=None,
            confidence=_confidence(count),
        )
        for message, count in counts.items()
    ]


def x__build_issues__mutmut_4(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=category,
            message_sample=message,
            count=count,
            confidence=None,
        )
        for message, count in counts.items()
    ]


def x__build_issues__mutmut_5(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            message_sample=message,
            count=count,
            confidence=_confidence(count),
        )
        for message, count in counts.items()
    ]


def x__build_issues__mutmut_6(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=category,
            count=count,
            confidence=_confidence(count),
        )
        for message, count in counts.items()
    ]


def x__build_issues__mutmut_7(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=category,
            message_sample=message,
            confidence=_confidence(count),
        )
        for message, count in counts.items()
    ]


def x__build_issues__mutmut_8(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=category,
            message_sample=message,
            count=count,
            )
        for message, count in counts.items()
    ]


def x__build_issues__mutmut_9(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=category,
            message_sample=message,
            count=count,
            confidence=_confidence(None),
        )
        for message, count in counts.items()
    ]

mutants_x__build_issues__mutmut['_mutmut_orig'] = x__build_issues__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_issues__mutmut['x__build_issues__mutmut_1'] = x__build_issues__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_issues__mutmut['x__build_issues__mutmut_2'] = x__build_issues__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_issues__mutmut['x__build_issues__mutmut_3'] = x__build_issues__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_issues__mutmut['x__build_issues__mutmut_4'] = x__build_issues__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_issues__mutmut['x__build_issues__mutmut_5'] = x__build_issues__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_issues__mutmut['x__build_issues__mutmut_6'] = x__build_issues__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_issues__mutmut['x__build_issues__mutmut_7'] = x__build_issues__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_issues__mutmut['x__build_issues__mutmut_8'] = x__build_issues__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_issues__mutmut['x__build_issues__mutmut_9'] = x__build_issues__mutmut_9 # type: ignore # mutmut generated
mutants_x__confidence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__confidence__mutmut)
def _confidence(count: int) -> float:
    return min(1.0, _CONFIDENCE_BASE + _CONFIDENCE_STEP * count)


def x__confidence__mutmut_orig(count: int) -> float:
    return min(1.0, _CONFIDENCE_BASE + _CONFIDENCE_STEP * count)


def x__confidence__mutmut_1(count: int) -> float:
    return min(None, _CONFIDENCE_BASE + _CONFIDENCE_STEP * count)


def x__confidence__mutmut_2(count: int) -> float:
    return min(1.0, None)


def x__confidence__mutmut_3(count: int) -> float:
    return min(_CONFIDENCE_BASE + _CONFIDENCE_STEP * count)


def x__confidence__mutmut_4(count: int) -> float:
    return min(1.0, )


def x__confidence__mutmut_5(count: int) -> float:
    return min(2.0, _CONFIDENCE_BASE + _CONFIDENCE_STEP * count)


def x__confidence__mutmut_6(count: int) -> float:
    return min(1.0, _CONFIDENCE_BASE - _CONFIDENCE_STEP * count)


def x__confidence__mutmut_7(count: int) -> float:
    return min(1.0, _CONFIDENCE_BASE + _CONFIDENCE_STEP / count)

mutants_x__confidence__mutmut['_mutmut_orig'] = x__confidence__mutmut_orig # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_1'] = x__confidence__mutmut_1 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_2'] = x__confidence__mutmut_2 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_3'] = x__confidence__mutmut_3 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_4'] = x__confidence__mutmut_4 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_5'] = x__confidence__mutmut_5 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_6'] = x__confidence__mutmut_6 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_7'] = x__confidence__mutmut_7 # type: ignore # mutmut generated
