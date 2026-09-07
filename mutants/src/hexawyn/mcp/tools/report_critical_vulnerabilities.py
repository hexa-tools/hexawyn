"""MCP tool: report_critical_vulnerabilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.report_critical_vulnerabilities.command import (
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.use_case.security.report_critical_vulnerabilities.report_critical_vulnerabilities_use_case import (  # noqa: E501
    ReportCriticalVulnerabilitiesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_report_critical_vulnerabilities__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_report_critical_vulnerabilities__mutmut)
def report_critical_vulnerabilities() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_critical_vulnerabilities__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_critical_vulnerabilities__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = None
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_critical_vulnerabilities__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=None)
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_critical_vulnerabilities__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = None  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_critical_vulnerabilities__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = ReportCriticalVulnerabilitiesUseCase(service=None)  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_critical_vulnerabilities__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_critical_vulnerabilities__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_critical_vulnerabilities__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_critical_vulnerabilities__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_report_critical_vulnerabilities__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_report_critical_vulnerabilities__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_report_critical_vulnerabilities__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        service = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_report_critical_vulnerabilities__mutmut['_mutmut_orig'] = x_report_critical_vulnerabilities__mutmut_orig # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_1'] = x_report_critical_vulnerabilities__mutmut_1 # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_2'] = x_report_critical_vulnerabilities__mutmut_2 # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_3'] = x_report_critical_vulnerabilities__mutmut_3 # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_4'] = x_report_critical_vulnerabilities__mutmut_4 # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_5'] = x_report_critical_vulnerabilities__mutmut_5 # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_6'] = x_report_critical_vulnerabilities__mutmut_6 # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_7'] = x_report_critical_vulnerabilities__mutmut_7 # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_8'] = x_report_critical_vulnerabilities__mutmut_8 # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_9'] = x_report_critical_vulnerabilities__mutmut_9 # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_10'] = x_report_critical_vulnerabilities__mutmut_10 # type: ignore # mutmut generated
mutants_x_report_critical_vulnerabilities__mutmut['x_report_critical_vulnerabilities__mutmut_11'] = x_report_critical_vulnerabilities__mutmut_11 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(report_critical_vulnerabilities)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(report_critical_vulnerabilities)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
