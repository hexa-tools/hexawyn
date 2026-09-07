# mypy: ignore-errors
"""MCP tool: generate_sla_report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.generate_sla_report.command import (  # type: ignore
    GenerateSLAReportCommand,
)
from hexawyn.application.use_case.workloads.generate_sla_report.generate_sla_report_use_case import (  # noqa: E501  # type: ignore  # type: ignore
    GenerateSLAReportUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_generate_sla_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_generate_sla_report__mutmut)
def generate_sla_report(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_orig(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_1(quarter: str = "XXtestXX") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_2(quarter: str = "TEST") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_3(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = None
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_4(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=None)
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_5(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_6(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_7(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=None))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_8(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_9(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_generate_sla_report__mutmut_10(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_generate_sla_report__mutmut_11(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_generate_sla_report__mutmut_12(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_generate_sla_report__mutmut['_mutmut_orig'] = x_generate_sla_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_1'] = x_generate_sla_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_2'] = x_generate_sla_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_3'] = x_generate_sla_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_4'] = x_generate_sla_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_5'] = x_generate_sla_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_6'] = x_generate_sla_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_7'] = x_generate_sla_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_8'] = x_generate_sla_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_9'] = x_generate_sla_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_10'] = x_generate_sla_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_11'] = x_generate_sla_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_generate_sla_report__mutmut['x_generate_sla_report__mutmut_12'] = x_generate_sla_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(generate_sla_report)


def x_register__mutmut_orig(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(generate_sla_report)


def x_register__mutmut_1(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
