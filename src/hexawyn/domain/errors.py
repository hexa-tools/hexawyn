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


# ── Quota ────────────────────────────────────────────────
class QuotaExceededError(HexawynError):
    """
    Raised when the monthly investigation limit is reached.
    Limits by tier:
    - Free    : 50/month
    - Dev     : 200/month
    - Startup : 500/month
    - Scale-up: unlimited
    - Enterprise: unlimited
    """

    def __init__(self, used: int, limit: int) -> None:
        super().__init__(
            f"You've used {used}/{limit} investigations this month.\n"
            f"Resets on the 1st of next month.\n"
            f"Upgrade your plan: https://hexawyn.com/pricing\n"
            f"Activate: hexa license activate <YOUR-KEY>"
        )
        self.used = used
        self.limit = limit


class PipelineNotFoundError(HexawynError):
    """Raised when the requested pipeline has no TaskRuns in the given namespace."""

    def __init__(self, pipeline_name: str) -> None:
        super().__init__(
            f"Pipeline '{pipeline_name}' not found or has no TaskRuns in the requested namespace."
        )
        self.pipeline_name = pipeline_name


class ServiceNotFoundError(HexawynError):
    """Raised when no PipelineRuns are found for the requested service."""

    def __init__(self, service_name: str) -> None:
        super().__init__(f"No pipelines found for service '{service_name}'.")
        self.service_name = service_name


class PrometheusUnavailableError(HexawynError):
    """Raised when Prometheus cannot be reached or is not configured."""

    def __init__(self, url: str) -> None:
        super().__init__(
            f"Prometheus is unavailable at '{url}'. "
            "Set PROMETHEUS_URL or ensure Prometheus is reachable."
        )
        self.url = url


class TektonNotInstalledError(HexawynError):
    """Raised when Tekton CRDs are not installed in the cluster."""

    def __init__(self) -> None:
        super().__init__("Tekton is not installed in this cluster. Install Tekton Pipelines first.")


class SlackQuotaExceededError(HexawynError):
    """
    Raised when the monthly Slack alert limit is reached.
    Limits by tier:
    - Free    : 5/month
    - Dev     : 50/month
    - Startup : unlimited
    - Scale-up: unlimited
    - Enterprise: unlimited
    """

    def __init__(self, used: int, limit: int) -> None:
        super().__init__(
            f"You've used {used}/{limit} Slack alerts this month.\n"
            f"Resets on the 1st of next month.\n"
            f"Upgrade your plan: https://hexawyn.com/pricing"
        )
        self.used = used
        self.limit = limit


# ── KubeArchive ───────────────────────────────────────────
class KubeArchiveUnavailableError(HexawynError):
    """Raised when KubeArchive is not installed or unreachable in the cluster."""

    def __init__(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "KubeArchive is not available in this cluster. "
            "Install KubeArchive first: https://kubearchive.org/docs/installation",
            context=context,
        )


class HistoricalDataWindowExpiredError(HexawynError):
    """Raised when the requested timestamp predates KubeArchive's data retention window."""

    def __init__(self, queried_timestamp: str, retention_window: str) -> None:
        super().__init__(
            f"Requested timestamp {queried_timestamp} is outside the retention window ({retention_window}). "
            "KubeArchive only retains data within the configured retention period."
        )
        self.queried_timestamp = queried_timestamp
        self.retention_window = retention_window
