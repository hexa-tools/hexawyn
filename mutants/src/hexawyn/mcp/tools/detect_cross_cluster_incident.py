"""MCP tool: detect_cross_cluster_incident."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.command import (
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.detect_cross_cluster_incident_use_case import (  # noqa: E501
    DetectCrossClusterIncidentUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_cross_cluster_incident__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_cross_cluster_incident__mutmut)
def detect_cross_cluster_incident() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_cross_cluster_incident__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_cross_cluster_incident__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = None
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_cross_cluster_incident__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=None
        )
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_cross_cluster_incident__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = None  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_cross_cluster_incident__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = DetectCrossClusterIncidentUseCase(service=None)  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_cross_cluster_incident__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_cross_cluster_incident__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = use_case.execute(None)
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_cross_cluster_incident__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_cross_cluster_incident__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_cross_cluster_incident__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_detect_cross_cluster_incident__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_detect_cross_cluster_incident__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_cross_cluster_incident_adapter

    try:
        service = DetectCrossClusterIncidentUseCase(
            incident_port=build_cross_cluster_incident_adapter()
        )
        use_case = DetectCrossClusterIncidentUseCase(service=service)  # type: ignore
        _ = use_case.execute(DetectCrossClusterIncidentCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_detect_cross_cluster_incident__mutmut['_mutmut_orig'] = x_detect_cross_cluster_incident__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_1'] = x_detect_cross_cluster_incident__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_2'] = x_detect_cross_cluster_incident__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_3'] = x_detect_cross_cluster_incident__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_4'] = x_detect_cross_cluster_incident__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_5'] = x_detect_cross_cluster_incident__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_6'] = x_detect_cross_cluster_incident__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_7'] = x_detect_cross_cluster_incident__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_8'] = x_detect_cross_cluster_incident__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_9'] = x_detect_cross_cluster_incident__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_10'] = x_detect_cross_cluster_incident__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_cross_cluster_incident__mutmut['x_detect_cross_cluster_incident__mutmut_11'] = x_detect_cross_cluster_incident__mutmut_11 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_cross_cluster_incident)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(detect_cross_cluster_incident)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
