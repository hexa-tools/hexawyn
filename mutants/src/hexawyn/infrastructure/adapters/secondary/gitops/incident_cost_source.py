from __future__ import annotations

from collections.abc import Mapping

from hexawyn.application.ports.driven.incident_cost_port import (
    BusinessConfigRaw,
    IncidentCostData,
)
from hexawyn.infrastructure.config.config_manager import load_config

_DEFAULT_SERVICE_NAME = "Service concerne"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut: MutantDict = {}  # type: ignore


class ConfigIncidentCostSource:
    """Reads the business financial parameters from ~/.hexawyn/config.yaml.

    Until an incident store is wired in, incident facts default to a neutral,
    zero-downtime record; the value of this source today is loading the
    ``business:`` config so the domain can compute a real, traceable estimate.
    Any unconfigured or non-numeric parameter is exposed as None.
    """

    @_mutmut_mutated(mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut)
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

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_orig(self, incident_ref: str) -> IncidentCostData:
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

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_1(self, incident_ref: str) -> IncidentCostData:
        business = None
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

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_2(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(None)
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

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_3(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=None,
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

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_4(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=None,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_5(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=None,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_6(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at=None,
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_7(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=None,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_8(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=None,
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_9(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
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

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_10(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_11(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_12(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_13(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_14(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_15(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=1,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_16(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=1,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_17(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="XXXX",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_18(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=True,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_19(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=None,
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_20(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=None,
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_21(self, incident_ref: str) -> IncidentCostData:
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
                sla_penalty_per_hour=None,
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_22(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_23(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_24(self, incident_ref: str) -> IncidentCostData:
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
                ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_25(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(None),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_26(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get(None)),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_27(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("XXrevenue_per_minuteXX")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_28(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("REVENUE_PER_MINUTE")),
                support_cost_per_hour=_as_float(business.get("support_cost_per_hour")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_29(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(None),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_30(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get(None)),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_31(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("XXsupport_cost_per_hourXX")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_32(self, incident_ref: str) -> IncidentCostData:
        business = _business_section(load_config())
        return IncidentCostData(
            business_service_name=_DEFAULT_SERVICE_NAME,
            downtime_minutes=0,
            impacted_service_count=0,
            resolved_at="",
            sla_breached=False,
            business_config=BusinessConfigRaw(
                revenue_per_minute=_as_float(business.get("revenue_per_minute")),
                support_cost_per_hour=_as_float(business.get("SUPPORT_COST_PER_HOUR")),
                sla_penalty_per_hour=_as_float(business.get("sla_penalty_per_hour")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_33(self, incident_ref: str) -> IncidentCostData:
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
                sla_penalty_per_hour=_as_float(None),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_34(self, incident_ref: str) -> IncidentCostData:
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
                sla_penalty_per_hour=_as_float(business.get(None)),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_35(self, incident_ref: str) -> IncidentCostData:
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
                sla_penalty_per_hour=_as_float(business.get("XXsla_penalty_per_hourXX")),
            ),
        )

    def xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_36(self, incident_ref: str) -> IncidentCostData:
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
                sla_penalty_per_hour=_as_float(business.get("SLA_PENALTY_PER_HOUR")),
            ),
        )

mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['_mutmut_orig'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_1'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_2'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_3'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_4'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_5'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_6'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_7'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_8'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_9'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_10'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_11'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_12'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_13'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_14'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_15'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_16'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_17'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_18'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_18 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_19'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_19 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_20'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_20 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_21'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_21 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_22'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_22 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_23'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_23 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_24'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_24 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_25'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_25 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_26'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_26 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_27'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_27 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_28'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_28 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_29'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_29 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_30'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_30 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_31'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_31 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_32'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_32 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_33'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_33 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_34'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_34 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_35'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_35 # type: ignore # mutmut generated
mutants_xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut['xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_36'] = ConfigIncidentCostSource.xǁConfigIncidentCostSourceǁfetch_incident_cost_data__mutmut_36 # type: ignore # mutmut generated
mutants_x__business_section__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__business_section__mutmut)
def _business_section(config: Mapping[str, object]) -> Mapping[str, object]:
    business = config.get("business")
    return business if isinstance(business, Mapping) else {}


def x__business_section__mutmut_orig(config: Mapping[str, object]) -> Mapping[str, object]:
    business = config.get("business")
    return business if isinstance(business, Mapping) else {}


def x__business_section__mutmut_1(config: Mapping[str, object]) -> Mapping[str, object]:
    business = None
    return business if isinstance(business, Mapping) else {}


def x__business_section__mutmut_2(config: Mapping[str, object]) -> Mapping[str, object]:
    business = config.get(None)
    return business if isinstance(business, Mapping) else {}


def x__business_section__mutmut_3(config: Mapping[str, object]) -> Mapping[str, object]:
    business = config.get("XXbusinessXX")
    return business if isinstance(business, Mapping) else {}


def x__business_section__mutmut_4(config: Mapping[str, object]) -> Mapping[str, object]:
    business = config.get("BUSINESS")
    return business if isinstance(business, Mapping) else {}

mutants_x__business_section__mutmut['_mutmut_orig'] = x__business_section__mutmut_orig # type: ignore # mutmut generated
mutants_x__business_section__mutmut['x__business_section__mutmut_1'] = x__business_section__mutmut_1 # type: ignore # mutmut generated
mutants_x__business_section__mutmut['x__business_section__mutmut_2'] = x__business_section__mutmut_2 # type: ignore # mutmut generated
mutants_x__business_section__mutmut['x__business_section__mutmut_3'] = x__business_section__mutmut_3 # type: ignore # mutmut generated
mutants_x__business_section__mutmut['x__business_section__mutmut_4'] = x__business_section__mutmut_4 # type: ignore # mutmut generated
mutants_x__as_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_float__mutmut)
def _as_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    return None


def x__as_float__mutmut_orig(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    return None


def x__as_float__mutmut_1(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(None)
    return None

mutants_x__as_float__mutmut['_mutmut_orig'] = x__as_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_1'] = x__as_float__mutmut_1 # type: ignore # mutmut generated
