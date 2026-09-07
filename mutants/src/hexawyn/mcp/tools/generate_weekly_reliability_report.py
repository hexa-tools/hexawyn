"""MCP tool: generate_weekly_reliability_report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.generate_weekly_reliability_report_use_case import (  # noqa: E501
    GenerateWeeklyReliabilityReportUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_generate_weekly_reliability_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_generate_weekly_reliability_report__mutmut)
def generate_weekly_reliability_report() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=build_reliability_report_adapter()
        )
        _ = use_case.execute(GenerateWeeklyReliabilityReportCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_weekly_reliability_report__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=build_reliability_report_adapter()
        )
        _ = use_case.execute(GenerateWeeklyReliabilityReportCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_weekly_reliability_report__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = None
        _ = use_case.execute(GenerateWeeklyReliabilityReportCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_weekly_reliability_report__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=None
        )
        _ = use_case.execute(GenerateWeeklyReliabilityReportCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_weekly_reliability_report__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=build_reliability_report_adapter()
        )
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_weekly_reliability_report__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=build_reliability_report_adapter()
        )
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_weekly_reliability_report__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=build_reliability_report_adapter()
        )
        _ = use_case.execute(GenerateWeeklyReliabilityReportCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_weekly_reliability_report__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=build_reliability_report_adapter()
        )
        _ = use_case.execute(GenerateWeeklyReliabilityReportCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_weekly_reliability_report__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=build_reliability_report_adapter()
        )
        _ = use_case.execute(GenerateWeeklyReliabilityReportCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_generate_weekly_reliability_report__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=build_reliability_report_adapter()
        )
        _ = use_case.execute(GenerateWeeklyReliabilityReportCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_generate_weekly_reliability_report__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=build_reliability_report_adapter()
        )
        _ = use_case.execute(GenerateWeeklyReliabilityReportCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_generate_weekly_reliability_report__mutmut['_mutmut_orig'] = x_generate_weekly_reliability_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_generate_weekly_reliability_report__mutmut['x_generate_weekly_reliability_report__mutmut_1'] = x_generate_weekly_reliability_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_generate_weekly_reliability_report__mutmut['x_generate_weekly_reliability_report__mutmut_2'] = x_generate_weekly_reliability_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_generate_weekly_reliability_report__mutmut['x_generate_weekly_reliability_report__mutmut_3'] = x_generate_weekly_reliability_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_generate_weekly_reliability_report__mutmut['x_generate_weekly_reliability_report__mutmut_4'] = x_generate_weekly_reliability_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_generate_weekly_reliability_report__mutmut['x_generate_weekly_reliability_report__mutmut_5'] = x_generate_weekly_reliability_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_generate_weekly_reliability_report__mutmut['x_generate_weekly_reliability_report__mutmut_6'] = x_generate_weekly_reliability_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_generate_weekly_reliability_report__mutmut['x_generate_weekly_reliability_report__mutmut_7'] = x_generate_weekly_reliability_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_generate_weekly_reliability_report__mutmut['x_generate_weekly_reliability_report__mutmut_8'] = x_generate_weekly_reliability_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_generate_weekly_reliability_report__mutmut['x_generate_weekly_reliability_report__mutmut_9'] = x_generate_weekly_reliability_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(generate_weekly_reliability_report)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(generate_weekly_reliability_report)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
