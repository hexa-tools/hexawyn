import re

from hexawyn.domain.models.watch_pod_logs import CriticalMatch, CriticalPatternCategory

_OOM_PATTERNS = (
    re.compile(r"oomkilled", re.IGNORECASE),
    re.compile(r"out of memory", re.IGNORECASE),
    re.compile(r"memory limit exceeded", re.IGNORECASE),
)
_DB_CONNECTION_PATTERNS = (
    re.compile(r"connection refused", re.IGNORECASE),
    re.compile(r"connection timeout", re.IGNORECASE),
    re.compile(r"could not connect to", re.IGNORECASE),
)
_PANIC_PATTERNS = (
    re.compile(r"panic:", re.IGNORECASE),
    re.compile(r"fatal error", re.IGNORECASE),
    re.compile(r"segmentation fault", re.IGNORECASE),
    re.compile(r"traceback \(most recent call last\)", re.IGNORECASE),
)

_CATEGORY_PATTERNS: tuple[tuple[CriticalPatternCategory, tuple[re.Pattern[str], ...]], ...] = (
    ("oom", _OOM_PATTERNS),
    ("db_connection_error", _DB_CONNECTION_PATTERNS),
    ("panic", _PANIC_PATTERNS),
)


def match_critical_pattern(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    category=category,
                    pattern=pattern.pattern,
                    log_line=line,
                    timestamp=timestamp,
                    pod_name=pod_name,
                )
    return None
