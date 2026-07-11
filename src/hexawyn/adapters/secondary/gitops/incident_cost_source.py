from __future__ import annotations

from collections.abc import Mapping

from hexawyn.application.ports.driven.incident_cost_port import (
    BusinessConfigRaw,
    IncidentCostData,
)
from hexawyn.infrastructure.config.config_manager import load_config

_DEFAULT_SERVICE_NAME = "Service concerne"


class ConfigIncidentCostSource:
    """Reads the business financial parameters from ~/.hexawyn/config.yaml.

    Until an incident store is wired in, incident facts default to a neutral,
    zero-downtime record; the value of this source today is loading the
    ``business:`` config so the domain can compute a real, traceable estimate.
    Any unconfigured or non-numeric parameter is exposed as None.
    """

    def fetch_incident_cost_data(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )


def _business_section(config: Mapping[str, object]) -> Mapping[str, object]:
    business = config.get("business")
    return business if isinstance(business, Mapping) else {}


def _as_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    return None
