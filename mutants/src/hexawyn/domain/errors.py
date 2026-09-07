

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁHexawynErrorǁ__init____mutmut: MutantDict = {}  # type: ignore
class HexawynError(Exception):
    """Base exception for all hexawyn errors."""

    @_mutmut_mutated(mutants_xǁHexawynErrorǁ__init____mutmut)
    def __init__(self, message: str, context: dict[str, str] | None = None) -> None:
        super().__init__(message)
        self.context = context or {}

    def xǁHexawynErrorǁ__init____mutmut_orig(self, message: str, context: dict[str, str] | None = None) -> None:
        super().__init__(message)
        self.context = context or {}

    def xǁHexawynErrorǁ__init____mutmut_1(self, message: str, context: dict[str, str] | None = None) -> None:
        super().__init__(None)
        self.context = context or {}

    def xǁHexawynErrorǁ__init____mutmut_2(self, message: str, context: dict[str, str] | None = None) -> None:
        super().__init__(message)
        self.context = None

    def xǁHexawynErrorǁ__init____mutmut_3(self, message: str, context: dict[str, str] | None = None) -> None:
        super().__init__(message)
        self.context = context and {}

mutants_xǁHexawynErrorǁ__init____mutmut['_mutmut_orig'] = HexawynError.xǁHexawynErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁHexawynErrorǁ__init____mutmut['xǁHexawynErrorǁ__init____mutmut_1'] = HexawynError.xǁHexawynErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁHexawynErrorǁ__init____mutmut['xǁHexawynErrorǁ__init____mutmut_2'] = HexawynError.xǁHexawynErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁHexawynErrorǁ__init____mutmut['xǁHexawynErrorǁ__init____mutmut_3'] = HexawynError.xǁHexawynErrorǁ__init____mutmut_3 # type: ignore # mutmut generated


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
mutants_xǁQuotaExceededErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


# ── Quota ────────────────────────────────────────────────
class QuotaExceededError(HexawynError):
    """Raised when the monthly investigation limit is reached.

    Carries data (used/limit); interface-specific messaging (pricing, the
    activation command) is built by the primary adapter that surfaces it.
    """

    @_mutmut_mutated(mutants_xǁQuotaExceededErrorǁ__init____mutmut)
    def __init__(self, used: int, limit: int) -> None:
        super().__init__(f"Quota exceeded: {used}/{limit}.")
        self.used = used
        self.limit = limit

    def xǁQuotaExceededErrorǁ__init____mutmut_orig(self, used: int, limit: int) -> None:
        super().__init__(f"Quota exceeded: {used}/{limit}.")
        self.used = used
        self.limit = limit

    def xǁQuotaExceededErrorǁ__init____mutmut_1(self, used: int, limit: int) -> None:
        super().__init__(None)
        self.used = used
        self.limit = limit

    def xǁQuotaExceededErrorǁ__init____mutmut_2(self, used: int, limit: int) -> None:
        super().__init__(f"Quota exceeded: {used}/{limit}.")
        self.used = None
        self.limit = limit

    def xǁQuotaExceededErrorǁ__init____mutmut_3(self, used: int, limit: int) -> None:
        super().__init__(f"Quota exceeded: {used}/{limit}.")
        self.used = used
        self.limit = None

mutants_xǁQuotaExceededErrorǁ__init____mutmut['_mutmut_orig'] = QuotaExceededError.xǁQuotaExceededErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁQuotaExceededErrorǁ__init____mutmut['xǁQuotaExceededErrorǁ__init____mutmut_1'] = QuotaExceededError.xǁQuotaExceededErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁQuotaExceededErrorǁ__init____mutmut['xǁQuotaExceededErrorǁ__init____mutmut_2'] = QuotaExceededError.xǁQuotaExceededErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁQuotaExceededErrorǁ__init____mutmut['xǁQuotaExceededErrorǁ__init____mutmut_3'] = QuotaExceededError.xǁQuotaExceededErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁPipelineNotFoundErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class PipelineNotFoundError(HexawynError):
    """Raised when the requested pipeline has no runs in the given namespace."""

    @_mutmut_mutated(mutants_xǁPipelineNotFoundErrorǁ__init____mutmut)
    def __init__(self, pipeline_name: str) -> None:
        super().__init__(
            f"Pipeline '{pipeline_name}' not found or has no runs in the requested namespace."
        )
        self.pipeline_name = pipeline_name

    def xǁPipelineNotFoundErrorǁ__init____mutmut_orig(self, pipeline_name: str) -> None:
        super().__init__(
            f"Pipeline '{pipeline_name}' not found or has no runs in the requested namespace."
        )
        self.pipeline_name = pipeline_name

    def xǁPipelineNotFoundErrorǁ__init____mutmut_1(self, pipeline_name: str) -> None:
        super().__init__(
            None
        )
        self.pipeline_name = pipeline_name

    def xǁPipelineNotFoundErrorǁ__init____mutmut_2(self, pipeline_name: str) -> None:
        super().__init__(
            f"Pipeline '{pipeline_name}' not found or has no runs in the requested namespace."
        )
        self.pipeline_name = None

mutants_xǁPipelineNotFoundErrorǁ__init____mutmut['_mutmut_orig'] = PipelineNotFoundError.xǁPipelineNotFoundErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineNotFoundErrorǁ__init____mutmut['xǁPipelineNotFoundErrorǁ__init____mutmut_1'] = PipelineNotFoundError.xǁPipelineNotFoundErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁPipelineNotFoundErrorǁ__init____mutmut['xǁPipelineNotFoundErrorǁ__init____mutmut_2'] = PipelineNotFoundError.xǁPipelineNotFoundErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁServiceNotFoundErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class ServiceNotFoundError(HexawynError):
    """Raised when no runs are found for the requested service."""

    @_mutmut_mutated(mutants_xǁServiceNotFoundErrorǁ__init____mutmut)
    def __init__(self, service_name: str) -> None:
        super().__init__(f"No pipelines found for service '{service_name}'.")
        self.service_name = service_name

    def xǁServiceNotFoundErrorǁ__init____mutmut_orig(self, service_name: str) -> None:
        super().__init__(f"No pipelines found for service '{service_name}'.")
        self.service_name = service_name

    def xǁServiceNotFoundErrorǁ__init____mutmut_1(self, service_name: str) -> None:
        super().__init__(None)
        self.service_name = service_name

    def xǁServiceNotFoundErrorǁ__init____mutmut_2(self, service_name: str) -> None:
        super().__init__(f"No pipelines found for service '{service_name}'.")
        self.service_name = None

mutants_xǁServiceNotFoundErrorǁ__init____mutmut['_mutmut_orig'] = ServiceNotFoundError.xǁServiceNotFoundErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁServiceNotFoundErrorǁ__init____mutmut['xǁServiceNotFoundErrorǁ__init____mutmut_1'] = ServiceNotFoundError.xǁServiceNotFoundErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁServiceNotFoundErrorǁ__init____mutmut['xǁServiceNotFoundErrorǁ__init____mutmut_2'] = ServiceNotFoundError.xǁServiceNotFoundErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusUnavailableErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class PrometheusUnavailableError(HexawynError):
    """Raised when Prometheus cannot be reached or is not configured."""

    @_mutmut_mutated(mutants_xǁPrometheusUnavailableErrorǁ__init____mutmut)
    def __init__(self, url: str) -> None:
        super().__init__(
            f"Prometheus is unavailable at '{url}'. "
            "Set PROMETHEUS_URL or ensure Prometheus is reachable."
        )
        self.url = url

    def xǁPrometheusUnavailableErrorǁ__init____mutmut_orig(self, url: str) -> None:
        super().__init__(
            f"Prometheus is unavailable at '{url}'. "
            "Set PROMETHEUS_URL or ensure Prometheus is reachable."
        )
        self.url = url

    def xǁPrometheusUnavailableErrorǁ__init____mutmut_1(self, url: str) -> None:
        super().__init__(
            None
        )
        self.url = url

    def xǁPrometheusUnavailableErrorǁ__init____mutmut_2(self, url: str) -> None:
        super().__init__(
            f"Prometheus is unavailable at '{url}'. "
            "XXSet PROMETHEUS_URL or ensure Prometheus is reachable.XX"
        )
        self.url = url

    def xǁPrometheusUnavailableErrorǁ__init____mutmut_3(self, url: str) -> None:
        super().__init__(
            f"Prometheus is unavailable at '{url}'. "
            "set prometheus_url or ensure prometheus is reachable."
        )
        self.url = url

    def xǁPrometheusUnavailableErrorǁ__init____mutmut_4(self, url: str) -> None:
        super().__init__(
            f"Prometheus is unavailable at '{url}'. "
            "SET PROMETHEUS_URL OR ENSURE PROMETHEUS IS REACHABLE."
        )
        self.url = url

    def xǁPrometheusUnavailableErrorǁ__init____mutmut_5(self, url: str) -> None:
        super().__init__(
            f"Prometheus is unavailable at '{url}'. "
            "Set PROMETHEUS_URL or ensure Prometheus is reachable."
        )
        self.url = None

mutants_xǁPrometheusUnavailableErrorǁ__init____mutmut['_mutmut_orig'] = PrometheusUnavailableError.xǁPrometheusUnavailableErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusUnavailableErrorǁ__init____mutmut['xǁPrometheusUnavailableErrorǁ__init____mutmut_1'] = PrometheusUnavailableError.xǁPrometheusUnavailableErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusUnavailableErrorǁ__init____mutmut['xǁPrometheusUnavailableErrorǁ__init____mutmut_2'] = PrometheusUnavailableError.xǁPrometheusUnavailableErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusUnavailableErrorǁ__init____mutmut['xǁPrometheusUnavailableErrorǁ__init____mutmut_3'] = PrometheusUnavailableError.xǁPrometheusUnavailableErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusUnavailableErrorǁ__init____mutmut['xǁPrometheusUnavailableErrorǁ__init____mutmut_4'] = PrometheusUnavailableError.xǁPrometheusUnavailableErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusUnavailableErrorǁ__init____mutmut['xǁPrometheusUnavailableErrorǁ__init____mutmut_5'] = PrometheusUnavailableError.xǁPrometheusUnavailableErrorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class PrometheusQueryError(HexawynError):
    """Raised when Prometheus rejects a query (e.g. a PromQL syntax error, HTTP 400)."""

    @_mutmut_mutated(mutants_xǁPrometheusQueryErrorǁ__init____mutmut)
    def __init__(self, promql: str, detail: str) -> None:
        super().__init__(f"PromQL query failed: '{promql}' — {detail}")
        self.promql = promql
        self.detail = detail

    def xǁPrometheusQueryErrorǁ__init____mutmut_orig(self, promql: str, detail: str) -> None:
        super().__init__(f"PromQL query failed: '{promql}' — {detail}")
        self.promql = promql
        self.detail = detail

    def xǁPrometheusQueryErrorǁ__init____mutmut_1(self, promql: str, detail: str) -> None:
        super().__init__(None)
        self.promql = promql
        self.detail = detail

    def xǁPrometheusQueryErrorǁ__init____mutmut_2(self, promql: str, detail: str) -> None:
        super().__init__(f"PromQL query failed: '{promql}' — {detail}")
        self.promql = None
        self.detail = detail

    def xǁPrometheusQueryErrorǁ__init____mutmut_3(self, promql: str, detail: str) -> None:
        super().__init__(f"PromQL query failed: '{promql}' — {detail}")
        self.promql = promql
        self.detail = None

mutants_xǁPrometheusQueryErrorǁ__init____mutmut['_mutmut_orig'] = PrometheusQueryError.xǁPrometheusQueryErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusQueryErrorǁ__init____mutmut['xǁPrometheusQueryErrorǁ__init____mutmut_1'] = PrometheusQueryError.xǁPrometheusQueryErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryErrorǁ__init____mutmut['xǁPrometheusQueryErrorǁ__init____mutmut_2'] = PrometheusQueryError.xǁPrometheusQueryErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusQueryErrorǁ__init____mutmut['xǁPrometheusQueryErrorǁ__init____mutmut_3'] = PrometheusQueryError.xǁPrometheusQueryErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁLabelSelectorErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class LabelSelectorError(HexawynError):
    """Raised when a label selector string is malformed (e.g. missing '=')."""

    @_mutmut_mutated(mutants_xǁLabelSelectorErrorǁ__init____mutmut)
    def __init__(self, selector: str, detail: str) -> None:
        super().__init__(f"Invalid label selector '{selector}': {detail}")
        self.selector = selector
        self.detail = detail

    def xǁLabelSelectorErrorǁ__init____mutmut_orig(self, selector: str, detail: str) -> None:
        super().__init__(f"Invalid label selector '{selector}': {detail}")
        self.selector = selector
        self.detail = detail

    def xǁLabelSelectorErrorǁ__init____mutmut_1(self, selector: str, detail: str) -> None:
        super().__init__(None)
        self.selector = selector
        self.detail = detail

    def xǁLabelSelectorErrorǁ__init____mutmut_2(self, selector: str, detail: str) -> None:
        super().__init__(f"Invalid label selector '{selector}': {detail}")
        self.selector = None
        self.detail = detail

    def xǁLabelSelectorErrorǁ__init____mutmut_3(self, selector: str, detail: str) -> None:
        super().__init__(f"Invalid label selector '{selector}': {detail}")
        self.selector = selector
        self.detail = None

mutants_xǁLabelSelectorErrorǁ__init____mutmut['_mutmut_orig'] = LabelSelectorError.xǁLabelSelectorErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁLabelSelectorErrorǁ__init____mutmut['xǁLabelSelectorErrorǁ__init____mutmut_1'] = LabelSelectorError.xǁLabelSelectorErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁLabelSelectorErrorǁ__init____mutmut['xǁLabelSelectorErrorǁ__init____mutmut_2'] = LabelSelectorError.xǁLabelSelectorErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁLabelSelectorErrorǁ__init____mutmut['xǁLabelSelectorErrorǁ__init____mutmut_3'] = LabelSelectorError.xǁLabelSelectorErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁLogPatternErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class LogPatternError(HexawynError):
    """Raised when a log search pattern is invalid (e.g. malformed regex)."""

    @_mutmut_mutated(mutants_xǁLogPatternErrorǁ__init____mutmut)
    def __init__(self, pattern: str, detail: str) -> None:
        super().__init__(f"Invalid log search pattern '{pattern}': {detail}")
        self.pattern = pattern
        self.detail = detail

    def xǁLogPatternErrorǁ__init____mutmut_orig(self, pattern: str, detail: str) -> None:
        super().__init__(f"Invalid log search pattern '{pattern}': {detail}")
        self.pattern = pattern
        self.detail = detail

    def xǁLogPatternErrorǁ__init____mutmut_1(self, pattern: str, detail: str) -> None:
        super().__init__(None)
        self.pattern = pattern
        self.detail = detail

    def xǁLogPatternErrorǁ__init____mutmut_2(self, pattern: str, detail: str) -> None:
        super().__init__(f"Invalid log search pattern '{pattern}': {detail}")
        self.pattern = None
        self.detail = detail

    def xǁLogPatternErrorǁ__init____mutmut_3(self, pattern: str, detail: str) -> None:
        super().__init__(f"Invalid log search pattern '{pattern}': {detail}")
        self.pattern = pattern
        self.detail = None

mutants_xǁLogPatternErrorǁ__init____mutmut['_mutmut_orig'] = LogPatternError.xǁLogPatternErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁLogPatternErrorǁ__init____mutmut['xǁLogPatternErrorǁ__init____mutmut_1'] = LogPatternError.xǁLogPatternErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁLogPatternErrorǁ__init____mutmut['xǁLogPatternErrorǁ__init____mutmut_2'] = LogPatternError.xǁLogPatternErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁLogPatternErrorǁ__init____mutmut['xǁLogPatternErrorǁ__init____mutmut_3'] = LogPatternError.xǁLogPatternErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackQuotaExceededErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class SlackQuotaExceededError(HexawynError):
    """Raised when the monthly Slack alert limit is reached.

    Carries data (used/limit); interface-specific messaging is built by the
    primary adapter that surfaces it.
    """

    @_mutmut_mutated(mutants_xǁSlackQuotaExceededErrorǁ__init____mutmut)
    def __init__(self, used: int, limit: int) -> None:
        super().__init__(f"Slack alert quota exceeded: {used}/{limit}.")
        self.used = used
        self.limit = limit

    def xǁSlackQuotaExceededErrorǁ__init____mutmut_orig(self, used: int, limit: int) -> None:
        super().__init__(f"Slack alert quota exceeded: {used}/{limit}.")
        self.used = used
        self.limit = limit

    def xǁSlackQuotaExceededErrorǁ__init____mutmut_1(self, used: int, limit: int) -> None:
        super().__init__(None)
        self.used = used
        self.limit = limit

    def xǁSlackQuotaExceededErrorǁ__init____mutmut_2(self, used: int, limit: int) -> None:
        super().__init__(f"Slack alert quota exceeded: {used}/{limit}.")
        self.used = None
        self.limit = limit

    def xǁSlackQuotaExceededErrorǁ__init____mutmut_3(self, used: int, limit: int) -> None:
        super().__init__(f"Slack alert quota exceeded: {used}/{limit}.")
        self.used = used
        self.limit = None

mutants_xǁSlackQuotaExceededErrorǁ__init____mutmut['_mutmut_orig'] = SlackQuotaExceededError.xǁSlackQuotaExceededErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackQuotaExceededErrorǁ__init____mutmut['xǁSlackQuotaExceededErrorǁ__init____mutmut_1'] = SlackQuotaExceededError.xǁSlackQuotaExceededErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackQuotaExceededErrorǁ__init____mutmut['xǁSlackQuotaExceededErrorǁ__init____mutmut_2'] = SlackQuotaExceededError.xǁSlackQuotaExceededErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackQuotaExceededErrorǁ__init____mutmut['xǁSlackQuotaExceededErrorǁ__init____mutmut_3'] = SlackQuotaExceededError.xǁSlackQuotaExceededErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁComponentNotInstalledErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


# ── Optional components ─────────────────────────────────────
class ComponentNotInstalledError(HexawynError):
    """Raised when a single named optional component is absent.

    Describes the absence of ONE named component (e.g. Tekton, Argo Rollouts,
    Cert-Manager, KEDA, KubeArchive, helm, kustomize). This is distinct from
    GitOpsEngineNotFoundError / PolicyEngineNotFoundError, which express "no
    engine among several candidates was detected" (an OR over a set), not the
    absence of a specific named component.
    """

    @_mutmut_mutated(mutants_xǁComponentNotInstalledErrorǁ__init____mutmut)
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

    def xǁComponentNotInstalledErrorǁ__init____mutmut_orig(
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

    def xǁComponentNotInstalledErrorǁ__init____mutmut_1(
        self,
        component_name: str,
        install_url: str | None = None,
        context: dict[str, str] | None = None,
    ) -> None:
        suffix = None
        super().__init__(
            f"{component_name} is not installed in this cluster. Install it first{suffix}",
            context=context,
        )
        self.component_name = component_name
        self.install_url = install_url

    def xǁComponentNotInstalledErrorǁ__init____mutmut_2(
        self,
        component_name: str,
        install_url: str | None = None,
        context: dict[str, str] | None = None,
    ) -> None:
        suffix = f": {install_url}" if install_url else "XX.XX"
        super().__init__(
            f"{component_name} is not installed in this cluster. Install it first{suffix}",
            context=context,
        )
        self.component_name = component_name
        self.install_url = install_url

    def xǁComponentNotInstalledErrorǁ__init____mutmut_3(
        self,
        component_name: str,
        install_url: str | None = None,
        context: dict[str, str] | None = None,
    ) -> None:
        suffix = f": {install_url}" if install_url else "."
        super().__init__(
            None,
            context=context,
        )
        self.component_name = component_name
        self.install_url = install_url

    def xǁComponentNotInstalledErrorǁ__init____mutmut_4(
        self,
        component_name: str,
        install_url: str | None = None,
        context: dict[str, str] | None = None,
    ) -> None:
        suffix = f": {install_url}" if install_url else "."
        super().__init__(
            f"{component_name} is not installed in this cluster. Install it first{suffix}",
            context=None,
        )
        self.component_name = component_name
        self.install_url = install_url

    def xǁComponentNotInstalledErrorǁ__init____mutmut_5(
        self,
        component_name: str,
        install_url: str | None = None,
        context: dict[str, str] | None = None,
    ) -> None:
        suffix = f": {install_url}" if install_url else "."
        super().__init__(
            context=context,
        )
        self.component_name = component_name
        self.install_url = install_url

    def xǁComponentNotInstalledErrorǁ__init____mutmut_6(
        self,
        component_name: str,
        install_url: str | None = None,
        context: dict[str, str] | None = None,
    ) -> None:
        suffix = f": {install_url}" if install_url else "."
        super().__init__(
            f"{component_name} is not installed in this cluster. Install it first{suffix}",
            )
        self.component_name = component_name
        self.install_url = install_url

    def xǁComponentNotInstalledErrorǁ__init____mutmut_7(
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
        self.component_name = None
        self.install_url = install_url

    def xǁComponentNotInstalledErrorǁ__init____mutmut_8(
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
        self.install_url = None

mutants_xǁComponentNotInstalledErrorǁ__init____mutmut['_mutmut_orig'] = ComponentNotInstalledError.xǁComponentNotInstalledErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁComponentNotInstalledErrorǁ__init____mutmut['xǁComponentNotInstalledErrorǁ__init____mutmut_1'] = ComponentNotInstalledError.xǁComponentNotInstalledErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁComponentNotInstalledErrorǁ__init____mutmut['xǁComponentNotInstalledErrorǁ__init____mutmut_2'] = ComponentNotInstalledError.xǁComponentNotInstalledErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁComponentNotInstalledErrorǁ__init____mutmut['xǁComponentNotInstalledErrorǁ__init____mutmut_3'] = ComponentNotInstalledError.xǁComponentNotInstalledErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁComponentNotInstalledErrorǁ__init____mutmut['xǁComponentNotInstalledErrorǁ__init____mutmut_4'] = ComponentNotInstalledError.xǁComponentNotInstalledErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁComponentNotInstalledErrorǁ__init____mutmut['xǁComponentNotInstalledErrorǁ__init____mutmut_5'] = ComponentNotInstalledError.xǁComponentNotInstalledErrorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁComponentNotInstalledErrorǁ__init____mutmut['xǁComponentNotInstalledErrorǁ__init____mutmut_6'] = ComponentNotInstalledError.xǁComponentNotInstalledErrorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁComponentNotInstalledErrorǁ__init____mutmut['xǁComponentNotInstalledErrorǁ__init____mutmut_7'] = ComponentNotInstalledError.xǁComponentNotInstalledErrorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁComponentNotInstalledErrorǁ__init____mutmut['xǁComponentNotInstalledErrorǁ__init____mutmut_8'] = ComponentNotInstalledError.xǁComponentNotInstalledErrorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


# ── KubeArchive ───────────────────────────────────────────
class HistoricalDataWindowExpiredError(HexawynError):
    """Raised when the requested timestamp predates KubeArchive's data retention window."""

    @_mutmut_mutated(mutants_xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut)
    def __init__(self, queried_timestamp: str, retention_window: str) -> None:
        super().__init__(
            f"Requested timestamp {queried_timestamp} is outside the retention window ({retention_window}). "  # noqa: E501
            "KubeArchive only retains data within the configured retention period."
        )
        self.queried_timestamp = queried_timestamp
        self.retention_window = retention_window

    def xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_orig(self, queried_timestamp: str, retention_window: str) -> None:
        super().__init__(
            f"Requested timestamp {queried_timestamp} is outside the retention window ({retention_window}). "  # noqa: E501
            "KubeArchive only retains data within the configured retention period."
        )
        self.queried_timestamp = queried_timestamp
        self.retention_window = retention_window

    def xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_1(self, queried_timestamp: str, retention_window: str) -> None:
        super().__init__(
            None
        )
        self.queried_timestamp = queried_timestamp
        self.retention_window = retention_window

    def xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_2(self, queried_timestamp: str, retention_window: str) -> None:
        super().__init__(
            f"Requested timestamp {queried_timestamp} is outside the retention window ({retention_window}). "  # noqa: E501
            "XXKubeArchive only retains data within the configured retention period.XX"
        )
        self.queried_timestamp = queried_timestamp
        self.retention_window = retention_window

    def xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_3(self, queried_timestamp: str, retention_window: str) -> None:
        super().__init__(
            f"Requested timestamp {queried_timestamp} is outside the retention window ({retention_window}). "  # noqa: E501
            "kubearchive only retains data within the configured retention period."
        )
        self.queried_timestamp = queried_timestamp
        self.retention_window = retention_window

    def xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_4(self, queried_timestamp: str, retention_window: str) -> None:
        super().__init__(
            f"Requested timestamp {queried_timestamp} is outside the retention window ({retention_window}). "  # noqa: E501
            "KUBEARCHIVE ONLY RETAINS DATA WITHIN THE CONFIGURED RETENTION PERIOD."
        )
        self.queried_timestamp = queried_timestamp
        self.retention_window = retention_window

    def xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_5(self, queried_timestamp: str, retention_window: str) -> None:
        super().__init__(
            f"Requested timestamp {queried_timestamp} is outside the retention window ({retention_window}). "  # noqa: E501
            "KubeArchive only retains data within the configured retention period."
        )
        self.queried_timestamp = None
        self.retention_window = retention_window

    def xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_6(self, queried_timestamp: str, retention_window: str) -> None:
        super().__init__(
            f"Requested timestamp {queried_timestamp} is outside the retention window ({retention_window}). "  # noqa: E501
            "KubeArchive only retains data within the configured retention period."
        )
        self.queried_timestamp = queried_timestamp
        self.retention_window = None

mutants_xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut['_mutmut_orig'] = HistoricalDataWindowExpiredError.xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut['xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_1'] = HistoricalDataWindowExpiredError.xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut['xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_2'] = HistoricalDataWindowExpiredError.xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut['xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_3'] = HistoricalDataWindowExpiredError.xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut['xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_4'] = HistoricalDataWindowExpiredError.xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut['xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_5'] = HistoricalDataWindowExpiredError.xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut['xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_6'] = HistoricalDataWindowExpiredError.xǁHistoricalDataWindowExpiredErrorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitOpsEngineNotFoundErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


# ── GitOps ─────────────────────────────────────────────
class GitOpsEngineNotFoundError(HexawynError):
    """Raised when no GitOps engine (Flux CD or Argo CD) is detected in the cluster."""

    @_mutmut_mutated(mutants_xǁGitOpsEngineNotFoundErrorǁ__init____mutmut)
    def __init__(self) -> None:
        super().__init__(
            "No GitOps engine detected in this cluster. "
            "Install Flux CD (https://fluxcd.io) or Argo CD (https://argo-cd.readthedocs.io) first."
        )

    def xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_orig(self) -> None:
        super().__init__(
            "No GitOps engine detected in this cluster. "
            "Install Flux CD (https://fluxcd.io) or Argo CD (https://argo-cd.readthedocs.io) first."
        )

    def xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_1(self) -> None:
        super().__init__(
            None
        )

    def xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_2(self) -> None:
        super().__init__(
            "XXNo GitOps engine detected in this cluster. XX"
            "Install Flux CD (https://fluxcd.io) or Argo CD (https://argo-cd.readthedocs.io) first."
        )

    def xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_3(self) -> None:
        super().__init__(
            "no gitops engine detected in this cluster. "
            "Install Flux CD (https://fluxcd.io) or Argo CD (https://argo-cd.readthedocs.io) first."
        )

    def xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_4(self) -> None:
        super().__init__(
            "NO GITOPS ENGINE DETECTED IN THIS CLUSTER. "
            "Install Flux CD (https://fluxcd.io) or Argo CD (https://argo-cd.readthedocs.io) first."
        )

    def xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_5(self) -> None:
        super().__init__(
            "No GitOps engine detected in this cluster. "
            "XXInstall Flux CD (https://fluxcd.io) or Argo CD (https://argo-cd.readthedocs.io) first.XX"
        )

    def xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_6(self) -> None:
        super().__init__(
            "No GitOps engine detected in this cluster. "
            "install flux cd (https://fluxcd.io) or argo cd (https://argo-cd.readthedocs.io) first."
        )

    def xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_7(self) -> None:
        super().__init__(
            "No GitOps engine detected in this cluster. "
            "INSTALL FLUX CD (HTTPS://FLUXCD.IO) OR ARGO CD (HTTPS://ARGO-CD.READTHEDOCS.IO) FIRST."
        )

mutants_xǁGitOpsEngineNotFoundErrorǁ__init____mutmut['_mutmut_orig'] = GitOpsEngineNotFoundError.xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsEngineNotFoundErrorǁ__init____mutmut['xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_1'] = GitOpsEngineNotFoundError.xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsEngineNotFoundErrorǁ__init____mutmut['xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_2'] = GitOpsEngineNotFoundError.xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsEngineNotFoundErrorǁ__init____mutmut['xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_3'] = GitOpsEngineNotFoundError.xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitOpsEngineNotFoundErrorǁ__init____mutmut['xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_4'] = GitOpsEngineNotFoundError.xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitOpsEngineNotFoundErrorǁ__init____mutmut['xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_5'] = GitOpsEngineNotFoundError.xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitOpsEngineNotFoundErrorǁ__init____mutmut['xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_6'] = GitOpsEngineNotFoundError.xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitOpsEngineNotFoundErrorǁ__init____mutmut['xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_7'] = GitOpsEngineNotFoundError.xǁGitOpsEngineNotFoundErrorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁPolicyEngineNotFoundErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


# ── Policy Engines ────────────────────────────────────────
class PolicyEngineNotFoundError(HexawynError):
    """Raised when no policy engine (Kyverno or OPA/Gatekeeper) is detected."""

    @_mutmut_mutated(mutants_xǁPolicyEngineNotFoundErrorǁ__init____mutmut)
    def __init__(self) -> None:
        super().__init__(
            "No policy engine detected in this cluster. "
            "Install Kyverno (https://kyverno.io) or OPA Gatekeeper (https://open-policy-agent.github.io/gatekeeper) first."  # noqa: E501
        )

    def xǁPolicyEngineNotFoundErrorǁ__init____mutmut_orig(self) -> None:
        super().__init__(
            "No policy engine detected in this cluster. "
            "Install Kyverno (https://kyverno.io) or OPA Gatekeeper (https://open-policy-agent.github.io/gatekeeper) first."  # noqa: E501
        )

    def xǁPolicyEngineNotFoundErrorǁ__init____mutmut_1(self) -> None:
        super().__init__(
            None  # noqa: E501
        )

    def xǁPolicyEngineNotFoundErrorǁ__init____mutmut_2(self) -> None:
        super().__init__(
            "XXNo policy engine detected in this cluster. XX"
            "Install Kyverno (https://kyverno.io) or OPA Gatekeeper (https://open-policy-agent.github.io/gatekeeper) first."  # noqa: E501
        )

    def xǁPolicyEngineNotFoundErrorǁ__init____mutmut_3(self) -> None:
        super().__init__(
            "no policy engine detected in this cluster. "
            "Install Kyverno (https://kyverno.io) or OPA Gatekeeper (https://open-policy-agent.github.io/gatekeeper) first."  # noqa: E501
        )

    def xǁPolicyEngineNotFoundErrorǁ__init____mutmut_4(self) -> None:
        super().__init__(
            "NO POLICY ENGINE DETECTED IN THIS CLUSTER. "
            "Install Kyverno (https://kyverno.io) or OPA Gatekeeper (https://open-policy-agent.github.io/gatekeeper) first."  # noqa: E501
        )

    def xǁPolicyEngineNotFoundErrorǁ__init____mutmut_5(self) -> None:
        super().__init__(
            "No policy engine detected in this cluster. "
            "XXInstall Kyverno (https://kyverno.io) or OPA Gatekeeper (https://open-policy-agent.github.io/gatekeeper) first.XX"  # noqa: E501
        )

    def xǁPolicyEngineNotFoundErrorǁ__init____mutmut_6(self) -> None:
        super().__init__(
            "No policy engine detected in this cluster. "
            "install kyverno (https://kyverno.io) or opa gatekeeper (https://open-policy-agent.github.io/gatekeeper) first."  # noqa: E501
        )

    def xǁPolicyEngineNotFoundErrorǁ__init____mutmut_7(self) -> None:
        super().__init__(
            "No policy engine detected in this cluster. "
            "INSTALL KYVERNO (HTTPS://KYVERNO.IO) OR OPA GATEKEEPER (HTTPS://OPEN-POLICY-AGENT.GITHUB.IO/GATEKEEPER) FIRST."  # noqa: E501
        )

mutants_xǁPolicyEngineNotFoundErrorǁ__init____mutmut['_mutmut_orig'] = PolicyEngineNotFoundError.xǁPolicyEngineNotFoundErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyEngineNotFoundErrorǁ__init____mutmut['xǁPolicyEngineNotFoundErrorǁ__init____mutmut_1'] = PolicyEngineNotFoundError.xǁPolicyEngineNotFoundErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyEngineNotFoundErrorǁ__init____mutmut['xǁPolicyEngineNotFoundErrorǁ__init____mutmut_2'] = PolicyEngineNotFoundError.xǁPolicyEngineNotFoundErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyEngineNotFoundErrorǁ__init____mutmut['xǁPolicyEngineNotFoundErrorǁ__init____mutmut_3'] = PolicyEngineNotFoundError.xǁPolicyEngineNotFoundErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyEngineNotFoundErrorǁ__init____mutmut['xǁPolicyEngineNotFoundErrorǁ__init____mutmut_4'] = PolicyEngineNotFoundError.xǁPolicyEngineNotFoundErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁPolicyEngineNotFoundErrorǁ__init____mutmut['xǁPolicyEngineNotFoundErrorǁ__init____mutmut_5'] = PolicyEngineNotFoundError.xǁPolicyEngineNotFoundErrorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁPolicyEngineNotFoundErrorǁ__init____mutmut['xǁPolicyEngineNotFoundErrorǁ__init____mutmut_6'] = PolicyEngineNotFoundError.xǁPolicyEngineNotFoundErrorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁPolicyEngineNotFoundErrorǁ__init____mutmut['xǁPolicyEngineNotFoundErrorǁ__init____mutmut_7'] = PolicyEngineNotFoundError.xǁPolicyEngineNotFoundErrorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁManifestRenderErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


# ── Configuration Drift Detection ───────────────────────────
class ManifestRenderError(HexawynError):
    """Raised when rendering a Helm release or Kustomize overlay genuinely
    fails (malformed chart/path/YAML, command error) — distinct from
    "release doesn't exist", which is a normal `source_exists() -> False`."""

    @_mutmut_mutated(mutants_xǁManifestRenderErrorǁ__init____mutmut)
    def __init__(self, source: str, detail: str) -> None:
        super().__init__(f"Failed to render manifests for {source!r}: {detail}")
        self.source = source
        self.detail = detail

    def xǁManifestRenderErrorǁ__init____mutmut_orig(self, source: str, detail: str) -> None:
        super().__init__(f"Failed to render manifests for {source!r}: {detail}")
        self.source = source
        self.detail = detail

    def xǁManifestRenderErrorǁ__init____mutmut_1(self, source: str, detail: str) -> None:
        super().__init__(None)
        self.source = source
        self.detail = detail

    def xǁManifestRenderErrorǁ__init____mutmut_2(self, source: str, detail: str) -> None:
        super().__init__(f"Failed to render manifests for {source!r}: {detail}")
        self.source = None
        self.detail = detail

    def xǁManifestRenderErrorǁ__init____mutmut_3(self, source: str, detail: str) -> None:
        super().__init__(f"Failed to render manifests for {source!r}: {detail}")
        self.source = source
        self.detail = None

mutants_xǁManifestRenderErrorǁ__init____mutmut['_mutmut_orig'] = ManifestRenderError.xǁManifestRenderErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁManifestRenderErrorǁ__init____mutmut['xǁManifestRenderErrorǁ__init____mutmut_1'] = ManifestRenderError.xǁManifestRenderErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁManifestRenderErrorǁ__init____mutmut['xǁManifestRenderErrorǁ__init____mutmut_2'] = ManifestRenderError.xǁManifestRenderErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁManifestRenderErrorǁ__init____mutmut['xǁManifestRenderErrorǁ__init____mutmut_3'] = ManifestRenderError.xǁManifestRenderErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class ClusterOperatorCRDNotFoundError(HexawynError):
    """Raised when the ClusterOperator CRD is absent (e.g. vanilla Kubernetes).

    ClusterOperators are an OpenShift-only resource served by the
    config.openshift.io/v1 API group.
    """

    @_mutmut_mutated(mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut)
    def __init__(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "ClusterOperator CRD not found. This resource is OpenShift-only "
            "(config.openshift.io/v1). Run this tool against an OpenShift cluster.",
            context=context,
        )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_orig(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "ClusterOperator CRD not found. This resource is OpenShift-only "
            "(config.openshift.io/v1). Run this tool against an OpenShift cluster.",
            context=context,
        )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_1(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            None,
            context=context,
        )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_2(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "ClusterOperator CRD not found. This resource is OpenShift-only "
            "(config.openshift.io/v1). Run this tool against an OpenShift cluster.",
            context=None,
        )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_3(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            context=context,
        )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_4(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "ClusterOperator CRD not found. This resource is OpenShift-only "
            "(config.openshift.io/v1). Run this tool against an OpenShift cluster.",
            )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_5(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "XXClusterOperator CRD not found. This resource is OpenShift-only XX"
            "(config.openshift.io/v1). Run this tool against an OpenShift cluster.",
            context=context,
        )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_6(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "clusteroperator crd not found. this resource is openshift-only "
            "(config.openshift.io/v1). Run this tool against an OpenShift cluster.",
            context=context,
        )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_7(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "CLUSTEROPERATOR CRD NOT FOUND. THIS RESOURCE IS OPENSHIFT-ONLY "
            "(config.openshift.io/v1). Run this tool against an OpenShift cluster.",
            context=context,
        )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_8(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "ClusterOperator CRD not found. This resource is OpenShift-only "
            "XX(config.openshift.io/v1). Run this tool against an OpenShift cluster.XX",
            context=context,
        )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_9(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "ClusterOperator CRD not found. This resource is OpenShift-only "
            "(config.openshift.io/v1). run this tool against an openshift cluster.",
            context=context,
        )

    def xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_10(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "ClusterOperator CRD not found. This resource is OpenShift-only "
            "(CONFIG.OPENSHIFT.IO/V1). RUN THIS TOOL AGAINST AN OPENSHIFT CLUSTER.",
            context=context,
        )

mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['_mutmut_orig'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_1'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_2'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_3'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_4'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_5'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_6'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_7'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_8'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_9'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut['xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_10'] = ClusterOperatorCRDNotFoundError.xǁClusterOperatorCRDNotFoundErrorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class MachineConfigPoolCRDNotFoundError(HexawynError):
    """Raised when the MachineConfigPool CRD is absent (e.g. vanilla Kubernetes).

    MachineConfigPools are an OpenShift-only resource served by the
    machineconfiguration.openshift.io/v1 API group.
    """

    @_mutmut_mutated(mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut)
    def __init__(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "OpenShift cluster.",
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_orig(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "OpenShift cluster.",
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_1(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            None,
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_2(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "OpenShift cluster.",
            context=None,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_3(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_4(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "OpenShift cluster.",
            )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_5(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "XXMachineConfigPool CRD not found. This resource is OpenShift-only XX"
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "OpenShift cluster.",
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_6(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "machineconfigpool crd not found. this resource is openshift-only "
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "OpenShift cluster.",
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_7(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MACHINECONFIGPOOL CRD NOT FOUND. THIS RESOURCE IS OPENSHIFT-ONLY "
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "OpenShift cluster.",
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_8(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "XX(machineconfiguration.openshift.io/v1). Run this tool against an XX"
            "OpenShift cluster.",
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_9(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "(machineconfiguration.openshift.io/v1). run this tool against an "
            "OpenShift cluster.",
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_10(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "(MACHINECONFIGURATION.OPENSHIFT.IO/V1). RUN THIS TOOL AGAINST AN "
            "OpenShift cluster.",
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_11(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "XXOpenShift cluster.XX",
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_12(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "openshift cluster.",
            context=context,
        )

    def xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_13(self, context: dict[str, str] | None = None) -> None:
        super().__init__(
            "MachineConfigPool CRD not found. This resource is OpenShift-only "
            "(machineconfiguration.openshift.io/v1). Run this tool against an "
            "OPENSHIFT CLUSTER.",
            context=context,
        )

mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['_mutmut_orig'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_1'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_2'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_3'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_4'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_5'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_6'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_7'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_8'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_9'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_10'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_11'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_12'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut['xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_13'] = MachineConfigPoolCRDNotFoundError.xǁMachineConfigPoolCRDNotFoundErrorǁ__init____mutmut_13 # type: ignore # mutmut generated
