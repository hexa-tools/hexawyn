"""RuntimeQuotaSource — quota mirror backed by the control plane.

The control plane (hexa-cloud) is the source of truth for the investigation
quota. The CLI is only a read mirror: it shows what the control plane reports
and falls back to the local DuckDB store only when the control plane is
unreachable (limit == -1 sentinel from HttpRuntimeAdapter) or running in
embedded/stub mode.

Slack alerts quota is not exposed by the control plane — it stays local.
"""

from __future__ import annotations

from hexawyn.application.ports.driven.plan_port import PlanPort
from hexawyn.application.ports.driven.runtime_port import QuotaCheckResult, RuntimePort
from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort

_CP_UNAVAILABLE_LIMIT = -1


def _get_current_investigation_quota() -> object:
    from hexawyn.infrastructure.config.quota_manager import (  # noqa: hexa-lazy-import
        _get_current_investigation_quota,
    )

    return _get_current_investigation_quota()


def _get_current_slack_quota() -> object:
    from hexawyn.infrastructure.config.quota_manager import (  # noqa: hexa-lazy-import
        _get_current_slack_quota,
    )

    return _get_current_slack_quota()


class RuntimeQuotaSource(UsageMeterPort, PlanPort):
    """Reads investigation quota from the control plane, falling back locally."""

    def __init__(self, runtime: RuntimePort) -> None:
        self._runtime = runtime
        self._plan: PlanPort | None = None

    def _local_plan(self) -> PlanPort:
        if self._plan is None:
            from hexawyn.adapters.secondary.pricing_plan_adapter import (  # noqa: hexa-lazy-import
                PricingPlanAdapter,
            )

            self._plan = PricingPlanAdapter()
        return self._plan

    def _cp_quota(self) -> QuotaCheckResult | None:
        try:
            result = self._runtime.check_quota()
        except Exception:
            return None
        if not isinstance(result, dict):
            return None
        if result.get("limit", _CP_UNAVAILABLE_LIMIT) == _CP_UNAVAILABLE_LIMIT:
            return None
        return result

    # ── UsageMeterPort ───────────────────────────────────────
    def get_usage(self, resource: str) -> int:
        if resource == "investigations":
            cp = self._cp_quota()
            if cp is not None:
                return int(cp["used"])
            return int(getattr(_get_current_investigation_quota(), "count", 0))
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── PlanPort ─────────────────────────────────────────────
    def get_limit(self, resource: str) -> int | None:
        if resource == "investigations":
            cp = self._cp_quota()
            if cp is not None:
                return int(cp["limit"])
            return int(getattr(_get_current_investigation_quota(), "limit", 0))
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "limit", 0))
        return self._local_plan().get_limit(resource)

    def is_available(self, feature: str) -> bool:
        return self._local_plan().is_available(feature)

    def tier_required_for(self, feature: str) -> str | None:
        return self._local_plan().tier_required_for(feature)
