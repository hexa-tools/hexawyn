from __future__ import annotations

import re
from difflib import SequenceMatcher

from hexawyn.domain.errors import LogPatternError


def compile_pattern(pattern: str, is_regex: bool) -> re.Pattern[str]:
    """Compiles a search pattern for log-line matching.

    `is_regex=False` (default) escapes the pattern first, so a literal search
    like "version=1.2.3" or "connection refused (postgres)" never misfires as
    regex syntax. `is_regex=True` compiles as-is, raising LogPatternError on
    invalid syntax.
    """
    source = pattern if is_regex else re.escape(pattern)
    try:
        return re.compile(source)
    except re.error as exc:
        raise LogPatternError(pattern, str(exc)) from exc


def similarity_score(pattern: str, line: str) -> float:
    """Lightweight, stdlib-only "semantic-ish" similarity — NOT a vector
    embedding. Used only as a fallback when a pod has zero exact matches, to
    surface the closest near-miss line (tagged match_type="semantic")."""
    return SequenceMatcher(None, pattern.lower(), line.lower()).ratio()
