import re

_NOISE_PATTERNS = (
    re.compile(r"GET\s+/health(z)?\b", re.IGNORECASE),
    re.compile(r"GET\s+/ready(z)?\b", re.IGNORECASE),
    re.compile(r"GET\s+/live(z)?\b", re.IGNORECASE),
    re.compile(r"readiness probe (succeeded|passed)", re.IGNORECASE),
    re.compile(r"liveness probe (succeeded|passed)", re.IGNORECASE),
    re.compile(r"health ?check", re.IGNORECASE),
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_noise__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_noise__mutmut)
def is_noise(line: str) -> bool:
    """Deterministic classifier for health-check/informational noise lines."""
    return any(pattern.search(line) for pattern in _NOISE_PATTERNS)


def x_is_noise__mutmut_orig(line: str) -> bool:
    """Deterministic classifier for health-check/informational noise lines."""
    return any(pattern.search(line) for pattern in _NOISE_PATTERNS)


def x_is_noise__mutmut_1(line: str) -> bool:
    """Deterministic classifier for health-check/informational noise lines."""
    return any(None)


def x_is_noise__mutmut_2(line: str) -> bool:
    """Deterministic classifier for health-check/informational noise lines."""
    return any(pattern.search(None) for pattern in _NOISE_PATTERNS)

mutants_x_is_noise__mutmut['_mutmut_orig'] = x_is_noise__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_noise__mutmut['x_is_noise__mutmut_1'] = x_is_noise__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_noise__mutmut['x_is_noise__mutmut_2'] = x_is_noise__mutmut_2 # type: ignore # mutmut generated
