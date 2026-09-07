"""MCP tool: report_unauthorized_access."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.report_unauthorized_access.command import (
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.use_case.security.report_unauthorized_access.report_unauthorized_access_use_case import (  # noqa: E501
    ReportUnauthorizedAccessUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_report_unauthorized_access__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_report_unauthorized_access__mutmut)
def report_unauthorized_access() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_unauthorized_access__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_unauthorized_access__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = None
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_unauthorized_access__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=None)
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_unauthorized_access__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = None  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_unauthorized_access__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=None)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_unauthorized_access__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_unauthorized_access__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_unauthorized_access__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_unauthorized_access__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_unauthorized_access__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_report_unauthorized_access__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_report_unauthorized_access__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_report_unauthorized_access__mutmut['_mutmut_orig'] = x_report_unauthorized_access__mutmut_orig # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_1'] = x_report_unauthorized_access__mutmut_1 # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_2'] = x_report_unauthorized_access__mutmut_2 # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_3'] = x_report_unauthorized_access__mutmut_3 # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_4'] = x_report_unauthorized_access__mutmut_4 # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_5'] = x_report_unauthorized_access__mutmut_5 # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_6'] = x_report_unauthorized_access__mutmut_6 # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_7'] = x_report_unauthorized_access__mutmut_7 # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_8'] = x_report_unauthorized_access__mutmut_8 # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_9'] = x_report_unauthorized_access__mutmut_9 # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_10'] = x_report_unauthorized_access__mutmut_10 # type: ignore # mutmut generated
mutants_x_report_unauthorized_access__mutmut['x_report_unauthorized_access__mutmut_11'] = x_report_unauthorized_access__mutmut_11 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(report_unauthorized_access)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(report_unauthorized_access)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
