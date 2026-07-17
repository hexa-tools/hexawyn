from hexawyn.application.ports.driven.plan_port import PlanPort
from hexawyn.domain.models.quota import (
    UNLIMITED,
    LicenseTier,
    get_billing_api_limit,
    get_cluster_limit,
    get_investigation_limit,
    get_slack_channel_limit,
    get_slack_limit,
    get_user_limit,
)

_RESOURCE_LIMIT_MAP: dict[str, object] = {
    "investigations": get_investigation_limit,
    "slack_alerts": get_slack_limit,
    "slack_channels": get_slack_channel_limit,
    "clusters": get_cluster_limit,
    "users": get_user_limit,
    "billing_api": get_billing_api_limit,
}


def _resolve_tier() -> LicenseTier:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        return get_license_tier()
    except ImportError:
        return LicenseTier.STARTER


class PricingPlanAdapter(PlanPort):
    def __init__(self, tier: LicenseTier | None = None) -> None:
        self._tier = tier if tier is not None else _resolve_tier()

    def get_limit(self, resource: str) -> int | None:
        limit_fn = _RESOURCE_LIMIT_MAP.get(resource)
        if limit_fn is None:
            return None
        result = limit_fn(self._tier)  # type: ignore[operator]
        return None if result == UNLIMITED else int(result)

    def is_available(self, feature: str) -> bool:
        limit = self.get_limit(feature)
        if limit is None:
            return True
        return limit > 0

    def tier_required_for(self, feature: str) -> str | None:
        limit = self.get_limit(feature)
        if limit is not None and limit > 0:
            return None
        return None
