"""MCP tool: analyze_incident_cost — Analyze incident financial impact."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.analyze_incident_cost.analyze_incident_cost_use_case import (  # noqa: E501
    AnalyzeIncidentCostUseCase,
)
from hexawyn.application.use_case.finops.analyze_incident_cost.command import (
    AnalyzeIncidentCostCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_analyze_incident_cost__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analyze_incident_cost__mutmut)
def analyze_incident_cost(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_orig(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_1(incident_ref: str = "XXyesterdayXX") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_2(incident_ref: str = "YESTERDAY") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_3(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = None
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_4(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=None)
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_5(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = None  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_6(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=None)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_7(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = None
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_8(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(None)
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_9(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=None))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_10(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = None
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_11(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "XXbusiness_service_nameXX": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_12(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "BUSINESS_SERVICE_NAME": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_13(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "XXdowntime_minutesXX": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_14(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "DOWNTIME_MINUTES": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_15(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "XXrevenue_impact_eurXX": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_16(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "REVENUE_IMPACT_EUR": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_17(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "XXtotal_cost_eurXX": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_18(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "TOTAL_COST_EUR": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_19(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_20(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "ERROR": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_21(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"XXbusiness_service_nameXX": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_22(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"BUSINESS_SERVICE_NAME": "", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_23(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "XXXX", "downtime_minutes": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_24(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "XXdowntime_minutesXX": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_25(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "DOWNTIME_MINUTES": 0, "error": str(exc)}


def x_analyze_incident_cost__mutmut_26(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 1, "error": str(exc)}


def x_analyze_incident_cost__mutmut_27(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "XXerrorXX": str(exc)}


def x_analyze_incident_cost__mutmut_28(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "ERROR": str(exc)}


def x_analyze_incident_cost__mutmut_29(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(None)}

mutants_x_analyze_incident_cost__mutmut['_mutmut_orig'] = x_analyze_incident_cost__mutmut_orig # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_1'] = x_analyze_incident_cost__mutmut_1 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_2'] = x_analyze_incident_cost__mutmut_2 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_3'] = x_analyze_incident_cost__mutmut_3 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_4'] = x_analyze_incident_cost__mutmut_4 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_5'] = x_analyze_incident_cost__mutmut_5 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_6'] = x_analyze_incident_cost__mutmut_6 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_7'] = x_analyze_incident_cost__mutmut_7 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_8'] = x_analyze_incident_cost__mutmut_8 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_9'] = x_analyze_incident_cost__mutmut_9 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_10'] = x_analyze_incident_cost__mutmut_10 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_11'] = x_analyze_incident_cost__mutmut_11 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_12'] = x_analyze_incident_cost__mutmut_12 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_13'] = x_analyze_incident_cost__mutmut_13 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_14'] = x_analyze_incident_cost__mutmut_14 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_15'] = x_analyze_incident_cost__mutmut_15 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_16'] = x_analyze_incident_cost__mutmut_16 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_17'] = x_analyze_incident_cost__mutmut_17 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_18'] = x_analyze_incident_cost__mutmut_18 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_19'] = x_analyze_incident_cost__mutmut_19 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_20'] = x_analyze_incident_cost__mutmut_20 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_21'] = x_analyze_incident_cost__mutmut_21 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_22'] = x_analyze_incident_cost__mutmut_22 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_23'] = x_analyze_incident_cost__mutmut_23 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_24'] = x_analyze_incident_cost__mutmut_24 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_25'] = x_analyze_incident_cost__mutmut_25 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_26'] = x_analyze_incident_cost__mutmut_26 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_27'] = x_analyze_incident_cost__mutmut_27 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_28'] = x_analyze_incident_cost__mutmut_28 # type: ignore # mutmut generated
mutants_x_analyze_incident_cost__mutmut['x_analyze_incident_cost__mutmut_29'] = x_analyze_incident_cost__mutmut_29 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_incident_cost)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(analyze_incident_cost)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
