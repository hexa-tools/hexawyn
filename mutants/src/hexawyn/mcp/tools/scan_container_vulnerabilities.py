"""MCP tool: scan_container_vulnerabilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.scan_container_vulnerabilities.command import (
    ScanContainerVulnerabilitiesCommand,
)
from hexawyn.application.use_case.security.scan_container_vulnerabilities.scan_container_vulnerabilities_use_case import (  # noqa: E501
    ScanContainerVulnerabilitiesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_scan_container_vulnerabilities__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_scan_container_vulnerabilities__mutmut)
def scan_container_vulnerabilities() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=build_image_inventory_adapter())  # type: ignore
        _ = use_case.execute(ScanContainerVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_scan_container_vulnerabilities__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=build_image_inventory_adapter())  # type: ignore
        _ = use_case.execute(ScanContainerVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_scan_container_vulnerabilities__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = None  # type: ignore
        _ = use_case.execute(ScanContainerVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_scan_container_vulnerabilities__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=None)  # type: ignore
        _ = use_case.execute(ScanContainerVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_scan_container_vulnerabilities__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=build_image_inventory_adapter())  # type: ignore
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_scan_container_vulnerabilities__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=build_image_inventory_adapter())  # type: ignore
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_scan_container_vulnerabilities__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=build_image_inventory_adapter())  # type: ignore
        _ = use_case.execute(ScanContainerVulnerabilitiesCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_scan_container_vulnerabilities__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=build_image_inventory_adapter())  # type: ignore
        _ = use_case.execute(ScanContainerVulnerabilitiesCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_scan_container_vulnerabilities__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=build_image_inventory_adapter())  # type: ignore
        _ = use_case.execute(ScanContainerVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_scan_container_vulnerabilities__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=build_image_inventory_adapter())  # type: ignore
        _ = use_case.execute(ScanContainerVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_scan_container_vulnerabilities__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_image_inventory_adapter

    try:
        use_case = ScanContainerVulnerabilitiesUseCase(port=build_image_inventory_adapter())  # type: ignore
        _ = use_case.execute(ScanContainerVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_scan_container_vulnerabilities__mutmut['_mutmut_orig'] = x_scan_container_vulnerabilities__mutmut_orig # type: ignore # mutmut generated
mutants_x_scan_container_vulnerabilities__mutmut['x_scan_container_vulnerabilities__mutmut_1'] = x_scan_container_vulnerabilities__mutmut_1 # type: ignore # mutmut generated
mutants_x_scan_container_vulnerabilities__mutmut['x_scan_container_vulnerabilities__mutmut_2'] = x_scan_container_vulnerabilities__mutmut_2 # type: ignore # mutmut generated
mutants_x_scan_container_vulnerabilities__mutmut['x_scan_container_vulnerabilities__mutmut_3'] = x_scan_container_vulnerabilities__mutmut_3 # type: ignore # mutmut generated
mutants_x_scan_container_vulnerabilities__mutmut['x_scan_container_vulnerabilities__mutmut_4'] = x_scan_container_vulnerabilities__mutmut_4 # type: ignore # mutmut generated
mutants_x_scan_container_vulnerabilities__mutmut['x_scan_container_vulnerabilities__mutmut_5'] = x_scan_container_vulnerabilities__mutmut_5 # type: ignore # mutmut generated
mutants_x_scan_container_vulnerabilities__mutmut['x_scan_container_vulnerabilities__mutmut_6'] = x_scan_container_vulnerabilities__mutmut_6 # type: ignore # mutmut generated
mutants_x_scan_container_vulnerabilities__mutmut['x_scan_container_vulnerabilities__mutmut_7'] = x_scan_container_vulnerabilities__mutmut_7 # type: ignore # mutmut generated
mutants_x_scan_container_vulnerabilities__mutmut['x_scan_container_vulnerabilities__mutmut_8'] = x_scan_container_vulnerabilities__mutmut_8 # type: ignore # mutmut generated
mutants_x_scan_container_vulnerabilities__mutmut['x_scan_container_vulnerabilities__mutmut_9'] = x_scan_container_vulnerabilities__mutmut_9 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(scan_container_vulnerabilities)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(scan_container_vulnerabilities)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
