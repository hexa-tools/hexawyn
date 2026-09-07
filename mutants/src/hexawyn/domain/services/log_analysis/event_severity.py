SEVERITY_ORDER: dict[str, int] = {"critical": 3, "high": 2, "medium": 1, "info": 0}

_SEVERITY_KEYWORDS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("critical", ("panic", "fatal", "oomkilled", "segmentation fault")),
    ("high", ("error",)),
    ("medium", ("warn",)),
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_event_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_event_severity__mutmut)
def classify_event_severity(line: str) -> str:
    """Deterministic severity classifier for a single log line."""
    lower = line.lower()
    for severity, keywords in _SEVERITY_KEYWORDS:
        if any(keyword in lower for keyword in keywords):
            return severity
    return "info"


def x_classify_event_severity__mutmut_orig(line: str) -> str:
    """Deterministic severity classifier for a single log line."""
    lower = line.lower()
    for severity, keywords in _SEVERITY_KEYWORDS:
        if any(keyword in lower for keyword in keywords):
            return severity
    return "info"


def x_classify_event_severity__mutmut_1(line: str) -> str:
    """Deterministic severity classifier for a single log line."""
    lower = None
    for severity, keywords in _SEVERITY_KEYWORDS:
        if any(keyword in lower for keyword in keywords):
            return severity
    return "info"


def x_classify_event_severity__mutmut_2(line: str) -> str:
    """Deterministic severity classifier for a single log line."""
    lower = line.upper()
    for severity, keywords in _SEVERITY_KEYWORDS:
        if any(keyword in lower for keyword in keywords):
            return severity
    return "info"


def x_classify_event_severity__mutmut_3(line: str) -> str:
    """Deterministic severity classifier for a single log line."""
    lower = line.lower()
    for severity, keywords in _SEVERITY_KEYWORDS:
        if any(None):
            return severity
    return "info"


def x_classify_event_severity__mutmut_4(line: str) -> str:
    """Deterministic severity classifier for a single log line."""
    lower = line.lower()
    for severity, keywords in _SEVERITY_KEYWORDS:
        if any(keyword not in lower for keyword in keywords):
            return severity
    return "info"


def x_classify_event_severity__mutmut_5(line: str) -> str:
    """Deterministic severity classifier for a single log line."""
    lower = line.lower()
    for severity, keywords in _SEVERITY_KEYWORDS:
        if any(keyword in lower for keyword in keywords):
            return severity
    return "XXinfoXX"


def x_classify_event_severity__mutmut_6(line: str) -> str:
    """Deterministic severity classifier for a single log line."""
    lower = line.lower()
    for severity, keywords in _SEVERITY_KEYWORDS:
        if any(keyword in lower for keyword in keywords):
            return severity
    return "INFO"

mutants_x_classify_event_severity__mutmut['_mutmut_orig'] = x_classify_event_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_event_severity__mutmut['x_classify_event_severity__mutmut_1'] = x_classify_event_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_event_severity__mutmut['x_classify_event_severity__mutmut_2'] = x_classify_event_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_event_severity__mutmut['x_classify_event_severity__mutmut_3'] = x_classify_event_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_event_severity__mutmut['x_classify_event_severity__mutmut_4'] = x_classify_event_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_event_severity__mutmut['x_classify_event_severity__mutmut_5'] = x_classify_event_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_event_severity__mutmut['x_classify_event_severity__mutmut_6'] = x_classify_event_severity__mutmut_6 # type: ignore # mutmut generated
