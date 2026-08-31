"""RuntimeQuotaSource — quota mirror backed by the control plane.

The control plane (hexa-cloud) is the source of truth for the investigation
quota. The CLI is a read mirror: it reports what the control plane returns,
then the last-known encrypted cache, then an honest NEUTRAL state when neither
is available.

Trust model (Option A — neutral):
- No hardcoded per-tier limit grid lives in this public client.
- CP reachable            -> use CP used/limit, persist an encrypted 0o600 cache.
- CP unreachable + cache  -> use the cached last-known server values.
- CP unreachable, no cache -> NEUTRAL ("quota unknown locally"). We never
  fabricate a limit and never block: the control plane is the real gate and
  re-enforces on the next sync. *This is a deliberate, documented business
  risk*: a totally-offline, never-synced install is locally unconstrained.

Slack alert quota is not exposed by the control plane: it stays local, but is
COUNTED WITHOUT a hardcoded limit (unlimited locally). A follow-up should
expose the real server-side slack quota.
"""

from __future__ import annotations

from hexawyn.application.ports.driven.plan_port import PlanPort
from hexawyn.application.ports.driven.runtime_port import QuotaCheckResult, RuntimePort
from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort
from hexawyn.infrastructure.config import quota_cache

_CP_UNAVAILABLE_LIMIT = -1


def _get_current_slack_quota() -> object:
    from hexawyn.infrastructure.config.quota_manager import (  # noqa: hexa-lazy-import
        _get_current_slack_quota,
    )

    return _get_current_slack_quota()


class RuntimeQuotaSource(UsageMeterPort, PlanPort):
    """Reads investigation quota from the control plane (or cache, or neutral)."""

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
        """Control-plane quota, or ``None`` when unreachable / unverifiable."""
        try:
            result = self._runtime.check_quota()
        except Exception:
            return None
        if not isinstance(result, dict):
            return None
        if result.get("limit", _CP_UNAVAILABLE_LIMIT) == _CP_UNAVAILABLE_LIMIT:
            return None
        return QuotaCheckResult(
            allowed=bool(result.get("allowed", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def _resolve_quota(self) -> QuotaCheckResult | None:
        """CP first, then encrypted cache, then ``None`` (neutral/unknown)."""
        cp = self._cp_quota()
        if cp is not None:
            quota_cache.save_quota(cp)
            return cp
        return quota_cache.load_quota()

    # ── UsageMeterPort ───────────────────────────────────────
    def get_usage(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── PlanPort ─────────────────────────────────────────────
    def get_limit(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    def is_available(self, feature: str) -> bool:
        return self._local_plan().is_available(feature)

    def tier_required_for(self, feature: str) -> str | None:
        return self._local_plan().tier_required_for(feature)
