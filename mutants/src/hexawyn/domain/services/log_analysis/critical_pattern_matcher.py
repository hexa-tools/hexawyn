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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_match_critical_pattern__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_match_critical_pattern__mutmut)
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


def x_match_critical_pattern__mutmut_orig(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
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


def x_match_critical_pattern__mutmut_1(line: str, pod_name: str, timestamp: str = "XXXX") -> CriticalMatch | None:
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


def x_match_critical_pattern__mutmut_2(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(None):
                return CriticalMatch(
                    category=category,
                    pattern=pattern.pattern,
                    log_line=line,
                    timestamp=timestamp,
                    pod_name=pod_name,
                )
    return None


def x_match_critical_pattern__mutmut_3(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    category=None,
                    pattern=pattern.pattern,
                    log_line=line,
                    timestamp=timestamp,
                    pod_name=pod_name,
                )
    return None


def x_match_critical_pattern__mutmut_4(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    category=category,
                    pattern=None,
                    log_line=line,
                    timestamp=timestamp,
                    pod_name=pod_name,
                )
    return None


def x_match_critical_pattern__mutmut_5(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    category=category,
                    pattern=pattern.pattern,
                    log_line=None,
                    timestamp=timestamp,
                    pod_name=pod_name,
                )
    return None


def x_match_critical_pattern__mutmut_6(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    category=category,
                    pattern=pattern.pattern,
                    log_line=line,
                    timestamp=None,
                    pod_name=pod_name,
                )
    return None


def x_match_critical_pattern__mutmut_7(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    category=category,
                    pattern=pattern.pattern,
                    log_line=line,
                    timestamp=timestamp,
                    pod_name=None,
                )
    return None


def x_match_critical_pattern__mutmut_8(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    pattern=pattern.pattern,
                    log_line=line,
                    timestamp=timestamp,
                    pod_name=pod_name,
                )
    return None


def x_match_critical_pattern__mutmut_9(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    category=category,
                    log_line=line,
                    timestamp=timestamp,
                    pod_name=pod_name,
                )
    return None


def x_match_critical_pattern__mutmut_10(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    category=category,
                    pattern=pattern.pattern,
                    timestamp=timestamp,
                    pod_name=pod_name,
                )
    return None


def x_match_critical_pattern__mutmut_11(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    category=category,
                    pattern=pattern.pattern,
                    log_line=line,
                    pod_name=pod_name,
                )
    return None


def x_match_critical_pattern__mutmut_12(line: str, pod_name: str, timestamp: str = "") -> CriticalMatch | None:
    """Deterministic classifier for OOM / DB connection error / panic lines."""
    for category, patterns in _CATEGORY_PATTERNS:
        for pattern in patterns:
            if pattern.search(line):
                return CriticalMatch(
                    category=category,
                    pattern=pattern.pattern,
                    log_line=line,
                    timestamp=timestamp,
                    )
    return None

mutants_x_match_critical_pattern__mutmut['_mutmut_orig'] = x_match_critical_pattern__mutmut_orig # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_1'] = x_match_critical_pattern__mutmut_1 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_2'] = x_match_critical_pattern__mutmut_2 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_3'] = x_match_critical_pattern__mutmut_3 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_4'] = x_match_critical_pattern__mutmut_4 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_5'] = x_match_critical_pattern__mutmut_5 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_6'] = x_match_critical_pattern__mutmut_6 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_7'] = x_match_critical_pattern__mutmut_7 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_8'] = x_match_critical_pattern__mutmut_8 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_9'] = x_match_critical_pattern__mutmut_9 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_10'] = x_match_critical_pattern__mutmut_10 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_11'] = x_match_critical_pattern__mutmut_11 # type: ignore # mutmut generated
mutants_x_match_critical_pattern__mutmut['x_match_critical_pattern__mutmut_12'] = x_match_critical_pattern__mutmut_12 # type: ignore # mutmut generated
