from hexawyn.application.ports.driven.plan_port import PlanPort


class PricingPlanAdapter(PlanPort):
    """Plan feature gating — NO hardcoded per-tier limits (Option A neutral).

    The control plane owns tier limits. This public client does not fabricate
    numbers: an unknown limit means the feature is available (fail-open),
    consistent with the project's "never invent data, never block when there
    is nothing to enforce" principle.
    """

    def get_limit(self, resource: str) -> int | None:
        return None  # neutral / unknown — the control plane is the authority

    def is_available(self, feature: str) -> bool:
        return True

    def tier_required_for(self, feature: str) -> str | None:
        return None
