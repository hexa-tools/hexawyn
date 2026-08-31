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
    """Raised when the monthly investigation limit is reached.

    Carries data (used/limit); interface-specific messaging (pricing, the
    activation command) is built by the primary adapter that surfaces it.
    """

    def __init__(self, used: int, limit: int) -> None:
        super().__init__(f"Quota exceeded: {used}/{limit}.")
        self.used = used
        self.limit = limit


class PipelineNotFoundError(HexawynError):
    """Raised when the requested pipeline has no runs in the given namespace."""

    def __init__(self, pipeline_name: str) -> None:
        super().__init__(
            f"Pipeline '{pipeline_name}' not found or has no runs in the requested namespace."
        )
        self.pipeline_name = pipeline_name


class ServiceNotFoundError(HexawynError):
    """Raised when no runs are found for the requested service."""

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


class PrometheusQueryError(HexawynError):
    """Raised when Prometheus rejects a query (e.g. a PromQL syntax error, HTTP 400)."""

    def __init__(self, promql: str, detail: str) -> None:
        super().__init__(f"PromQL query failed: '{promql}' — {detail}")
        self.promql = promql
        self.detail = detail


class LabelSelectorError(HexawynError):
    """Raised when a label selector string is malformed (e.g. missing '=')."""

    def __init__(self, selector: str, detail: str) -> None:
        super().__init__(f"Invalid label selector '{selector}': {detail}")
        self.selector = selector
        self.detail = detail


class LogPatternError(HexawynError):
    """Raised when a log search pattern is invalid (e.g. malformed regex)."""

    def __init__(self, pattern: str, detail: str) -> None:
        super().__init__(f"Invalid log search pattern '{pattern}': {detail}")
        self.pattern = pattern
        self.detail = detail


class SlackQuotaExceededError(HexawynError):
    """Raised when the monthly Slack alert limit is reached.

    Carries data (used/limit); interface-specific messaging is built by the
    primary adapter that surfaces it.
    """

    def __init__(self, used: int, limit: int) -> None:
        super().__init__(f"Slack alert quota exceeded: {used}/{limit}.")
        self.used = used
        self.limit = limit


# ── Optional components ─────────────────────────────────────
class ComponentNotInstalledError(HexawynError):
    """Raised when a single named optional component is absent.

    Describes the absence of ONE named component (e.g. Tekton, Argo Rollouts,
    Cert-Manager, KEDA, KubeArchive, helm, kustomize). This is distinct from
    GitOpsEngineNotFoundError / PolicyEngineNotFoundError, which express "no
    engine among several candidates was detected" (an OR over a set), not the
    absence of a specific named component.
    """

    def __init__(
        self,
        component_name: str,
        install_url: str | None = None,
        context: dict[str, str] | None = None,
    ) -> None:
        suffix = f": {install_url}" if install_url else "."
        super().__init__(
            f"{component_name} is not installed in this cluster. Install it first{suffix}",
            context=context,
        )
        self.component_name = component_name
        self.install_url = install_url


# ── KubeArchive ───────────────────────────────────────────
class HistoricalDataWindowExpiredError(HexawynError):
    """Raised when the requested timestamp predates KubeArchive's data retention window."""

    def __init__(self, queried_timestamp: str, retention_window: str) -> None:
        super().__init__(
            f"Requested timestamp {queried_timestamp} is outside the retention window ({retention_window}). "  # noqa: E501
            "KubeArchive only retains data within the configured retention period."
        )
        self.queried_timestamp = queried_timestamp
        self.retention_window = retention_window


# ── GitOps ─────────────────────────────────────────────
class GitOpsEngineNotFoundError(HexawynError):
    """Raised when no GitOps engine (Flux CD or Argo CD) is detected in the cluster."""

    def __init__(self) -> None:
        super().__init__(
            "No GitOps engine detected in this cluster. "
            "Install Flux CD (https://fluxcd.io) or Argo CD (https://argo-cd.readthedocs.io) first."
        )


# ── Policy Engines ────────────────────────────────────────
class PolicyEngineNotFoundError(HexawynError):
    """Raised when no policy engine (Kyverno or OPA/Gatekeeper) is detected."""

    def __init__(self) -> None:
        super().__init__(
            "No policy engine detected in this cluster. "
            "Install Kyverno (https://kyverno.io) or OPA Gatekeeper (https://open-policy-agent.github.io/gatekeeper) first."  # noqa: E501
        )


# ── Configuration Drift Detection ───────────────────────────
class ManifestRenderError(HexawynError):
    """Raised when rendering a Helm release or Kustomize overlay genuinely
    fails (malformed chart/path/YAML, command error) — distinct from
    "release doesn't exist", which is a normal `source_exists() -> False`."""

    def __init__(self, source: str, detail: str) -> None:
        super().__init__(f"Failed to render manifests for {source!r}: {detail}")
        self.source = source
        self.detail = detail


class ClusterOperatorCRDNotFoundError(HexawynError):
    """Raised when the ClusterOperator CRD is absent (e.g. vanilla Kubernetes).

    ClusterOperators are an OpenShift-only resource served by the
    config.openshift.io/v1 API group.
    """

    def __init__(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "ClusterOperator CRD not found. This resource is OpenShift-only "
            "(config.openshift.io/v1). Run this tool against an OpenShift cluster.",
            context=context,
        )


class MachineConfigPoolCRDNotFoundError(HexawynError):
    """Raised when the MachineConfigPool CRD is absent (e.g. vanilla Kubernetes).

    MachineConfigPools are an OpenShift-only resource served by the
    machineconfiguration.openshift.io/v1 API group.
    """

    def __init__(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "OpenShift cluster.",
            context=context,
        )
