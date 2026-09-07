from hexawyn.application.ports.driven.plan_port import PlanPort


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPricingPlanAdapterǁis_available__mutmut: MutantDict = {}  # type: ignore


class PricingPlanAdapter(PlanPort):
    """Plan feature gating — NO hardcoded per-tier limits (Option A neutral).

    The control plane owns tier limits. This public client does not fabricate
    numbers: an unknown limit means the feature is available (fail-open),
    consistent with the project's "never invent data, never block when there
    is nothing to enforce" principle.
    """

    def get_limit(self, resource: str) -> int | None:
        return None  # neutral / unknown — the control plane is the authority

    @_mutmut_mutated(mutants_xǁPricingPlanAdapterǁis_available__mutmut)
    def is_available(self, feature: str) -> bool:
        return True

    def xǁPricingPlanAdapterǁis_available__mutmut_orig(self, feature: str) -> bool:
        return True

    def xǁPricingPlanAdapterǁis_available__mutmut_1(self, feature: str) -> bool:
        return False

    def tier_required_for(self, feature: str) -> str | None:
        return None

mutants_xǁPricingPlanAdapterǁis_available__mutmut['_mutmut_orig'] = PricingPlanAdapter.xǁPricingPlanAdapterǁis_available__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPricingPlanAdapterǁis_available__mutmut['xǁPricingPlanAdapterǁis_available__mutmut_1'] = PricingPlanAdapter.xǁPricingPlanAdapterǁis_available__mutmut_1 # type: ignore # mutmut generated
