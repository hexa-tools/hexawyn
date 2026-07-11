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


def is_secret_key(key_path: str) -> bool:
    """True when the key path names a secret-bearing value that must be redacted."""
    normalized = key_path.lower()
    return any(token in normalized for token in _SECRET_TOKENS)


def _contains(normalized_path: str, tokens: tuple[str, ...]) -> bool:
    return any(token in normalized_path for token in tokens)
