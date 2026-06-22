class HexawynError(Exception):
    """Base exception for all hexawyn errors."""

    def __init__(self, message: str, context: dict[str, str] | None = None) -> None:
        super().__init__(message)
        self.context = context or {}


# ── Cluster & connectivity ─────────────────────────────────
class ClusterUnreachableError(HexawynError):
    """Raised when the Kubernetes API server cannot be reached."""


class ResourceNotFoundError(HexawynError):
    """Raised when a requested k8s resource does not exist."""


class InsufficientPermissionsError(HexawynError):
    """Raised when RBAC prevents the requested operation."""


class AdapterTimeoutError(HexawynError):
    """Raised when an adapter call exceeds the configured timeout."""


# ── Observability ──────────────────────────────────────────
class MetricsUnavailableError(HexawynError):
    """Raised when Prometheus / CloudWatch / Datadog metrics are unavailable."""


class TracesUnavailableError(HexawynError):
    """Raised when OTel / APM traces cannot be retrieved."""


# ── Investigation ──────────────────────────────────────────
class InvestigationError(HexawynError):
    """Raised when the LangGraph investigation pipeline fails."""


class InsufficientDataError(HexawynError):
    """Raised when there is not enough data to produce a reliable answer."""


class AmbiguousResultError(HexawynError):
    """Raised when the LLM produces a result that cannot be verified."""


# ── Semantic layer ─────────────────────────────────────────
class CheckerNodeError(HexawynError):
    """Raised when the deterministic checker node itself fails."""


class SemanticLayerError(HexawynError):
    """Raised when embedding or VSS search fails."""


# ── Safety ────────────────────────────────────────────────
class MutationGuardTriggeredError(HexawynError):
    """Raised when a destructive operation is blocked by the mutation guard."""


# ── Infrastructure ─────────────────────────────────────────
class DuckDBUnavailableError(HexawynError):
    """Raised when DuckDB cannot be initialized or queried."""


class SchemaMigrationError(HexawynError):
    """Raised when a DuckDB schema migration fails."""


class EncryptionError(HexawynError):
    """Raised when DuckDB encryption key derivation or decryption fails."""
