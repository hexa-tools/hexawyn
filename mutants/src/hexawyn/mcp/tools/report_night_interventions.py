"""MCP tool: report_night_interventions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.report_night_interventions.command import (
    ReportNightInterventionsCommand,
)
from hexawyn.application.use_case.workloads.report_night_interventions.report_night_interventions_use_case import (  # noqa: E501
    ReportNightInterventionsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_report_night_interventions__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_report_night_interventions__mutmut)
def report_night_interventions() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_night_interventions__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_night_interventions__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = None
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_night_interventions__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=None)
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_night_interventions__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = None  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_night_interventions__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = ReportNightInterventionsUseCase(service=None)  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_night_interventions__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_night_interventions__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_night_interventions__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_night_interventions__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_night_interventions__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_report_night_interventions__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_report_night_interventions__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        service = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        use_case = ReportNightInterventionsUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_report_night_interventions__mutmut['_mutmut_orig'] = x_report_night_interventions__mutmut_orig # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_1'] = x_report_night_interventions__mutmut_1 # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_2'] = x_report_night_interventions__mutmut_2 # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_3'] = x_report_night_interventions__mutmut_3 # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_4'] = x_report_night_interventions__mutmut_4 # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_5'] = x_report_night_interventions__mutmut_5 # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_6'] = x_report_night_interventions__mutmut_6 # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_7'] = x_report_night_interventions__mutmut_7 # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_8'] = x_report_night_interventions__mutmut_8 # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_9'] = x_report_night_interventions__mutmut_9 # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_10'] = x_report_night_interventions__mutmut_10 # type: ignore # mutmut generated
mutants_x_report_night_interventions__mutmut['x_report_night_interventions__mutmut_11'] = x_report_night_interventions__mutmut_11 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(report_night_interventions)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(report_night_interventions)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
