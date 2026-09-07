from __future__ import annotations

from hexawyn.domain.models.helm_values_diff import DiffSeverity

_SECRET_TOKENS = ("secret", "password", "passwd", "token", "privatekey", "apikey", "credential")
_CRITICAL_TOKENS = ("image.tag", "image.repository", "rbac", "secret")
_WARNING_TOKENS = (
    "replicacount",
    "replicas",
    "resources.limits",
    "resources.requests",
    "featureflags",
    "feature_flags",
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_severity__mutmut)
def classify_severity(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_orig(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_1(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = None
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_2(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.upper()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_3(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) and _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_4(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(None) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_5(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(None, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_6(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, None):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_7(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(_CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_8(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, ):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_9(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "XXcriticalXX"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_10(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "CRITICAL"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_11(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(None, _WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_12(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, None):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_13(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(_WARNING_TOKENS):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_14(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, ):
        return "warning"
    return "informational"


def x_classify_severity__mutmut_15(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "XXwarningXX"
    return "informational"


def x_classify_severity__mutmut_16(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "WARNING"
    return "informational"


def x_classify_severity__mutmut_17(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "XXinformationalXX"


def x_classify_severity__mutmut_18(key_path: str) -> DiffSeverity:
    """Authoritative severity matrix for Helm values differences.

    critical  → image tag/repository, RBAC, any secret-bearing key
    warning   → replica count, resource limits/requests, feature flags
    info      → everything else (logging level, labels, annotations, ...)

    This matrix is the single source of truth the checker/semantic layer
    verifies the LLM output against.
    """
    normalized = key_path.lower()
    if is_secret_key(key_path) or _contains(normalized, _CRITICAL_TOKENS):
        return "critical"
    if _contains(normalized, _WARNING_TOKENS):
        return "warning"
    return "INFORMATIONAL"

mutants_x_classify_severity__mutmut['_mutmut_orig'] = x_classify_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_1'] = x_classify_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_2'] = x_classify_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_3'] = x_classify_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_4'] = x_classify_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_5'] = x_classify_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_6'] = x_classify_severity__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_7'] = x_classify_severity__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_8'] = x_classify_severity__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_9'] = x_classify_severity__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_10'] = x_classify_severity__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_11'] = x_classify_severity__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_12'] = x_classify_severity__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_13'] = x_classify_severity__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_14'] = x_classify_severity__mutmut_14 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_15'] = x_classify_severity__mutmut_15 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_16'] = x_classify_severity__mutmut_16 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_17'] = x_classify_severity__mutmut_17 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_18'] = x_classify_severity__mutmut_18 # type: ignore # mutmut generated
mutants_x_is_secret_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_secret_key__mutmut)
def is_secret_key(key_path: str) -> bool:
    """True when the key path names a secret-bearing value that must be redacted."""
    normalized = key_path.lower()
    return any(token in normalized for token in _SECRET_TOKENS)


def x_is_secret_key__mutmut_orig(key_path: str) -> bool:
    """True when the key path names a secret-bearing value that must be redacted."""
    normalized = key_path.lower()
    return any(token in normalized for token in _SECRET_TOKENS)


def x_is_secret_key__mutmut_1(key_path: str) -> bool:
    """True when the key path names a secret-bearing value that must be redacted."""
    normalized = None
    return any(token in normalized for token in _SECRET_TOKENS)


def x_is_secret_key__mutmut_2(key_path: str) -> bool:
    """True when the key path names a secret-bearing value that must be redacted."""
    normalized = key_path.upper()
    return any(token in normalized for token in _SECRET_TOKENS)


def x_is_secret_key__mutmut_3(key_path: str) -> bool:
    """True when the key path names a secret-bearing value that must be redacted."""
    normalized = key_path.lower()
    return any(None)


def x_is_secret_key__mutmut_4(key_path: str) -> bool:
    """True when the key path names a secret-bearing value that must be redacted."""
    normalized = key_path.lower()
    return any(token not in normalized for token in _SECRET_TOKENS)

mutants_x_is_secret_key__mutmut['_mutmut_orig'] = x_is_secret_key__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_secret_key__mutmut['x_is_secret_key__mutmut_1'] = x_is_secret_key__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_secret_key__mutmut['x_is_secret_key__mutmut_2'] = x_is_secret_key__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_secret_key__mutmut['x_is_secret_key__mutmut_3'] = x_is_secret_key__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_secret_key__mutmut['x_is_secret_key__mutmut_4'] = x_is_secret_key__mutmut_4 # type: ignore # mutmut generated
mutants_x__contains__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__contains__mutmut)
def _contains(normalized_path: str, tokens: tuple[str, ...]) -> bool:
    return any(token in normalized_path for token in tokens)


def x__contains__mutmut_orig(normalized_path: str, tokens: tuple[str, ...]) -> bool:
    return any(token in normalized_path for token in tokens)


def x__contains__mutmut_1(normalized_path: str, tokens: tuple[str, ...]) -> bool:
    return any(None)


def x__contains__mutmut_2(normalized_path: str, tokens: tuple[str, ...]) -> bool:
    return any(token not in normalized_path for token in tokens)

mutants_x__contains__mutmut['_mutmut_orig'] = x__contains__mutmut_orig # type: ignore # mutmut generated
mutants_x__contains__mutmut['x__contains__mutmut_1'] = x__contains__mutmut_1 # type: ignore # mutmut generated
mutants_x__contains__mutmut['x__contains__mutmut_2'] = x__contains__mutmut_2 # type: ignore # mutmut generated
