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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


def _get_current_slack_quota() -> object:
    from hexawyn.infrastructure.config.quota_manager import (  # noqa: hexa-lazy-import
        _get_current_slack_quota,
    )

    return _get_current_slack_quota()
mutants_xǁRuntimeQuotaSourceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeQuotaSourceǁ_local_plan__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeQuotaSourceǁis_available__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeQuotaSourceǁtier_required_for__mutmut: MutantDict = {}  # type: ignore


class RuntimeQuotaSource(UsageMeterPort, PlanPort):
    """Reads investigation quota from the control plane (or cache, or neutral)."""

    @_mutmut_mutated(mutants_xǁRuntimeQuotaSourceǁ__init____mutmut)
    def __init__(self, runtime: RuntimePort) -> None:
        self._runtime = runtime
        self._plan: PlanPort | None = None

    def xǁRuntimeQuotaSourceǁ__init____mutmut_orig(self, runtime: RuntimePort) -> None:
        self._runtime = runtime
        self._plan: PlanPort | None = None

    def xǁRuntimeQuotaSourceǁ__init____mutmut_1(self, runtime: RuntimePort) -> None:
        self._runtime = None
        self._plan: PlanPort | None = None

    def xǁRuntimeQuotaSourceǁ__init____mutmut_2(self, runtime: RuntimePort) -> None:
        self._runtime = runtime
        self._plan: PlanPort | None = ""

    @_mutmut_mutated(mutants_xǁRuntimeQuotaSourceǁ_local_plan__mutmut)
    def _local_plan(self) -> PlanPort:
        if self._plan is None:
            from hexawyn.infrastructure.adapters.secondary.pricing_plan_adapter import (  # noqa: hexa-lazy-import
                PricingPlanAdapter,
            )

            self._plan = PricingPlanAdapter()
        return self._plan

    def xǁRuntimeQuotaSourceǁ_local_plan__mutmut_orig(self) -> PlanPort:
        if self._plan is None:
            from hexawyn.infrastructure.adapters.secondary.pricing_plan_adapter import (  # noqa: hexa-lazy-import
                PricingPlanAdapter,
            )

            self._plan = PricingPlanAdapter()
        return self._plan

    def xǁRuntimeQuotaSourceǁ_local_plan__mutmut_1(self) -> PlanPort:
        if self._plan is not None:
            from hexawyn.infrastructure.adapters.secondary.pricing_plan_adapter import (  # noqa: hexa-lazy-import
                PricingPlanAdapter,
            )

            self._plan = PricingPlanAdapter()
        return self._plan

    def xǁRuntimeQuotaSourceǁ_local_plan__mutmut_2(self) -> PlanPort:
        if self._plan is None:
            from hexawyn.infrastructure.adapters.secondary.pricing_plan_adapter import (  # noqa: hexa-lazy-import
                PricingPlanAdapter,
            )

            self._plan = None
        return self._plan

    @_mutmut_mutated(mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut)
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

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_orig(self) -> QuotaCheckResult | None:
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

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_1(self) -> QuotaCheckResult | None:
        """Control-plane quota, or ``None`` when unreachable / unverifiable."""
        try:
            result = None
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

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_2(self) -> QuotaCheckResult | None:
        """Control-plane quota, or ``None`` when unreachable / unverifiable."""
        try:
            result = self._runtime.check_quota()
        except Exception:
            return None
        if isinstance(result, dict):
            return None
        if result.get("limit", _CP_UNAVAILABLE_LIMIT) == _CP_UNAVAILABLE_LIMIT:
            return None
        return QuotaCheckResult(
            allowed=bool(result.get("allowed", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_3(self) -> QuotaCheckResult | None:
        """Control-plane quota, or ``None`` when unreachable / unverifiable."""
        try:
            result = self._runtime.check_quota()
        except Exception:
            return None
        if not isinstance(result, dict):
            return None
        if result.get(None, _CP_UNAVAILABLE_LIMIT) == _CP_UNAVAILABLE_LIMIT:
            return None
        return QuotaCheckResult(
            allowed=bool(result.get("allowed", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_4(self) -> QuotaCheckResult | None:
        """Control-plane quota, or ``None`` when unreachable / unverifiable."""
        try:
            result = self._runtime.check_quota()
        except Exception:
            return None
        if not isinstance(result, dict):
            return None
        if result.get("limit", None) == _CP_UNAVAILABLE_LIMIT:
            return None
        return QuotaCheckResult(
            allowed=bool(result.get("allowed", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_5(self) -> QuotaCheckResult | None:
        """Control-plane quota, or ``None`` when unreachable / unverifiable."""
        try:
            result = self._runtime.check_quota()
        except Exception:
            return None
        if not isinstance(result, dict):
            return None
        if result.get(_CP_UNAVAILABLE_LIMIT) == _CP_UNAVAILABLE_LIMIT:
            return None
        return QuotaCheckResult(
            allowed=bool(result.get("allowed", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_6(self) -> QuotaCheckResult | None:
        """Control-plane quota, or ``None`` when unreachable / unverifiable."""
        try:
            result = self._runtime.check_quota()
        except Exception:
            return None
        if not isinstance(result, dict):
            return None
        if result.get("limit", ) == _CP_UNAVAILABLE_LIMIT:
            return None
        return QuotaCheckResult(
            allowed=bool(result.get("allowed", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_7(self) -> QuotaCheckResult | None:
        """Control-plane quota, or ``None`` when unreachable / unverifiable."""
        try:
            result = self._runtime.check_quota()
        except Exception:
            return None
        if not isinstance(result, dict):
            return None
        if result.get("XXlimitXX", _CP_UNAVAILABLE_LIMIT) == _CP_UNAVAILABLE_LIMIT:
            return None
        return QuotaCheckResult(
            allowed=bool(result.get("allowed", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_8(self) -> QuotaCheckResult | None:
        """Control-plane quota, or ``None`` when unreachable / unverifiable."""
        try:
            result = self._runtime.check_quota()
        except Exception:
            return None
        if not isinstance(result, dict):
            return None
        if result.get("LIMIT", _CP_UNAVAILABLE_LIMIT) == _CP_UNAVAILABLE_LIMIT:
            return None
        return QuotaCheckResult(
            allowed=bool(result.get("allowed", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_9(self) -> QuotaCheckResult | None:
        """Control-plane quota, or ``None`` when unreachable / unverifiable."""
        try:
            result = self._runtime.check_quota()
        except Exception:
            return None
        if not isinstance(result, dict):
            return None
        if result.get("limit", _CP_UNAVAILABLE_LIMIT) != _CP_UNAVAILABLE_LIMIT:
            return None
        return QuotaCheckResult(
            allowed=bool(result.get("allowed", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_10(self) -> QuotaCheckResult | None:
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
            allowed=None,
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_11(self) -> QuotaCheckResult | None:
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
            used=None,
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_12(self) -> QuotaCheckResult | None:
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
            limit=None,
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_13(self) -> QuotaCheckResult | None:
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
            remaining=None,
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_14(self) -> QuotaCheckResult | None:
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
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_15(self) -> QuotaCheckResult | None:
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
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_16(self) -> QuotaCheckResult | None:
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
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_17(self) -> QuotaCheckResult | None:
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
            )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_18(self) -> QuotaCheckResult | None:
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
            allowed=bool(None),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_19(self) -> QuotaCheckResult | None:
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
            allowed=bool(result.get(None, True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_20(self) -> QuotaCheckResult | None:
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
            allowed=bool(result.get("allowed", None)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_21(self) -> QuotaCheckResult | None:
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
            allowed=bool(result.get(True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_22(self) -> QuotaCheckResult | None:
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
            allowed=bool(result.get("allowed", )),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_23(self) -> QuotaCheckResult | None:
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
            allowed=bool(result.get("XXallowedXX", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_24(self) -> QuotaCheckResult | None:
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
            allowed=bool(result.get("ALLOWED", True)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_25(self) -> QuotaCheckResult | None:
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
            allowed=bool(result.get("allowed", False)),
            used=int(result.get("used", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_26(self) -> QuotaCheckResult | None:
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
            used=int(None),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_27(self) -> QuotaCheckResult | None:
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
            used=int(result.get(None, 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_28(self) -> QuotaCheckResult | None:
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
            used=int(result.get("used", None)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_29(self) -> QuotaCheckResult | None:
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
            used=int(result.get(0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_30(self) -> QuotaCheckResult | None:
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
            used=int(result.get("used", )),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_31(self) -> QuotaCheckResult | None:
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
            used=int(result.get("XXusedXX", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_32(self) -> QuotaCheckResult | None:
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
            used=int(result.get("USED", 0)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_33(self) -> QuotaCheckResult | None:
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
            used=int(result.get("used", 1)),
            limit=int(result.get("limit", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_34(self) -> QuotaCheckResult | None:
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
            limit=int(None),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_35(self) -> QuotaCheckResult | None:
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
            limit=int(result.get(None, _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_36(self) -> QuotaCheckResult | None:
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
            limit=int(result.get("limit", None)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_37(self) -> QuotaCheckResult | None:
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
            limit=int(result.get(_CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_38(self) -> QuotaCheckResult | None:
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
            limit=int(result.get("limit", )),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_39(self) -> QuotaCheckResult | None:
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
            limit=int(result.get("XXlimitXX", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_40(self) -> QuotaCheckResult | None:
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
            limit=int(result.get("LIMIT", _CP_UNAVAILABLE_LIMIT)),
            remaining=int(result.get("remaining", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_41(self) -> QuotaCheckResult | None:
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
            remaining=int(None),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_42(self) -> QuotaCheckResult | None:
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
            remaining=int(result.get(None, _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_43(self) -> QuotaCheckResult | None:
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
            remaining=int(result.get("remaining", None)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_44(self) -> QuotaCheckResult | None:
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
            remaining=int(result.get(_CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_45(self) -> QuotaCheckResult | None:
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
            remaining=int(result.get("remaining", )),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_46(self) -> QuotaCheckResult | None:
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
            remaining=int(result.get("XXremainingXX", _CP_UNAVAILABLE_LIMIT)),
        )

    def xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_47(self) -> QuotaCheckResult | None:
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
            remaining=int(result.get("REMAINING", _CP_UNAVAILABLE_LIMIT)),
        )

    @_mutmut_mutated(mutants_xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut)
    def _resolve_quota(self) -> QuotaCheckResult | None:
        """CP first, then encrypted cache, then ``None`` (neutral/unknown)."""
        cp = self._cp_quota()
        if cp is not None:
            quota_cache.save_quota(cp)
            return cp
        return quota_cache.load_quota()

    def xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_orig(self) -> QuotaCheckResult | None:
        """CP first, then encrypted cache, then ``None`` (neutral/unknown)."""
        cp = self._cp_quota()
        if cp is not None:
            quota_cache.save_quota(cp)
            return cp
        return quota_cache.load_quota()

    def xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_1(self) -> QuotaCheckResult | None:
        """CP first, then encrypted cache, then ``None`` (neutral/unknown)."""
        cp = None
        if cp is not None:
            quota_cache.save_quota(cp)
            return cp
        return quota_cache.load_quota()

    def xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_2(self) -> QuotaCheckResult | None:
        """CP first, then encrypted cache, then ``None`` (neutral/unknown)."""
        cp = self._cp_quota()
        if cp is None:
            quota_cache.save_quota(cp)
            return cp
        return quota_cache.load_quota()

    def xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_3(self) -> QuotaCheckResult | None:
        """CP first, then encrypted cache, then ``None`` (neutral/unknown)."""
        cp = self._cp_quota()
        if cp is not None:
            quota_cache.save_quota(None)
            return cp
        return quota_cache.load_quota()

    # ── UsageMeterPort ───────────────────────────────────────
    @_mutmut_mutated(mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut)
    def get_usage(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_orig(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_1(self, resource: str) -> int:
        if resource != "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_2(self, resource: str) -> int:
        if resource == "XXinvestigationsXX":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_3(self, resource: str) -> int:
        if resource == "INVESTIGATIONS":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_4(self, resource: str) -> int:
        if resource == "investigations":
            quota = None
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_5(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_6(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(None)
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_7(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["XXusedXX"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_8(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["USED"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_9(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 1  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_10(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource != "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_11(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "XXslack_alertsXX":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_12(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "SLACK_ALERTS":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_13(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(None)
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_14(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(None, "count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_15(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), None, 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_16(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", None))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_17(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr("count", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_18(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_19(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", ))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_20(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "XXcountXX", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_21(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "COUNT", 0))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_22(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 1))
        return 0

    # ── UsageMeterPort ───────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_usage__mutmut_23(self, resource: str) -> int:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["used"])
            return 0  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return int(getattr(_get_current_slack_quota(), "count", 0))
        return 1

    # ── PlanPort ─────────────────────────────────────────────
    @_mutmut_mutated(mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut)
    def get_limit(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_orig(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_1(self, resource: str) -> int | None:
        if resource != "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_2(self, resource: str) -> int | None:
        if resource == "XXinvestigationsXX":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_3(self, resource: str) -> int | None:
        if resource == "INVESTIGATIONS":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_4(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = None
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_5(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_6(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(None)
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_7(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["XXlimitXX"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_8(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["LIMIT"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_9(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource != "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_10(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "XXslack_alertsXX":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_11(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "SLACK_ALERTS":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(resource)

    # ── PlanPort ─────────────────────────────────────────────
    def xǁRuntimeQuotaSourceǁget_limit__mutmut_12(self, resource: str) -> int | None:
        if resource == "investigations":
            quota = self._resolve_quota()
            if quota is not None:
                return int(quota["limit"])
            return None  # neutral / unknown — never a fabricated number
        if resource == "slack_alerts":
            return _CP_UNAVAILABLE_LIMIT  # counted locally, no hardcoded limit
        return self._local_plan().get_limit(None)

    @_mutmut_mutated(mutants_xǁRuntimeQuotaSourceǁis_available__mutmut)
    def is_available(self, feature: str) -> bool:
        return self._local_plan().is_available(feature)

    def xǁRuntimeQuotaSourceǁis_available__mutmut_orig(self, feature: str) -> bool:
        return self._local_plan().is_available(feature)

    def xǁRuntimeQuotaSourceǁis_available__mutmut_1(self, feature: str) -> bool:
        return self._local_plan().is_available(None)

    @_mutmut_mutated(mutants_xǁRuntimeQuotaSourceǁtier_required_for__mutmut)
    def tier_required_for(self, feature: str) -> str | None:
        return self._local_plan().tier_required_for(feature)

    def xǁRuntimeQuotaSourceǁtier_required_for__mutmut_orig(self, feature: str) -> str | None:
        return self._local_plan().tier_required_for(feature)

    def xǁRuntimeQuotaSourceǁtier_required_for__mutmut_1(self, feature: str) -> str | None:
        return self._local_plan().tier_required_for(None)

mutants_xǁRuntimeQuotaSourceǁ__init____mutmut['_mutmut_orig'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ__init____mutmut['xǁRuntimeQuotaSourceǁ__init____mutmut_1'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ__init____mutmut['xǁRuntimeQuotaSourceǁ__init____mutmut_2'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁRuntimeQuotaSourceǁ_local_plan__mutmut['_mutmut_orig'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_local_plan__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_local_plan__mutmut['xǁRuntimeQuotaSourceǁ_local_plan__mutmut_1'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_local_plan__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_local_plan__mutmut['xǁRuntimeQuotaSourceǁ_local_plan__mutmut_2'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_local_plan__mutmut_2 # type: ignore # mutmut generated

mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['_mutmut_orig'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_1'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_2'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_3'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_4'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_5'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_6'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_7'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_8'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_9'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_10'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_11'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_12'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_13'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_14'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_15'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_16'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_17'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_18'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_19'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_20'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_21'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_22'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_23'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_24'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_25'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_26'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_27'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_28'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_29'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_30'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_31'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_32'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_33'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_34'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_35'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_36'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_37'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_38'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_39'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_40'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_41'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_42'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_43'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_44'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_45'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_46'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_cp_quota__mutmut['xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_47'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_cp_quota__mutmut_47 # type: ignore # mutmut generated

mutants_xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut['_mutmut_orig'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut['xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_1'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut['xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_2'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut['xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_3'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁ_resolve_quota__mutmut_3 # type: ignore # mutmut generated

mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['_mutmut_orig'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_1'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_2'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_3'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_4'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_5'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_6'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_7'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_8'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_9'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_10'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_11'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_12'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_13'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_14'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_15'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_16'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_17'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_18'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_19'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_20'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_21'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_22'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_usage__mutmut['xǁRuntimeQuotaSourceǁget_usage__mutmut_23'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_usage__mutmut_23 # type: ignore # mutmut generated

mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['_mutmut_orig'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_1'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_2'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_3'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_4'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_5'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_6'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_7'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_8'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_9'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_10'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_11'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁget_limit__mutmut['xǁRuntimeQuotaSourceǁget_limit__mutmut_12'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁget_limit__mutmut_12 # type: ignore # mutmut generated

mutants_xǁRuntimeQuotaSourceǁis_available__mutmut['_mutmut_orig'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁis_available__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁis_available__mutmut['xǁRuntimeQuotaSourceǁis_available__mutmut_1'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁis_available__mutmut_1 # type: ignore # mutmut generated

mutants_xǁRuntimeQuotaSourceǁtier_required_for__mutmut['_mutmut_orig'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁtier_required_for__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeQuotaSourceǁtier_required_for__mutmut['xǁRuntimeQuotaSourceǁtier_required_for__mutmut_1'] = RuntimeQuotaSource.xǁRuntimeQuotaSourceǁtier_required_for__mutmut_1 # type: ignore # mutmut generated
