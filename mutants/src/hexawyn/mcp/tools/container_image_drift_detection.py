"""MCP tool: container_image_drift_detection."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.detect_container_image_drift.command import (
    DetectContainerImageDriftCommand,
)
from hexawyn.application.use_case.security.detect_container_image_drift.detect_container_image_drift_use_case import (  # noqa: E501
    DetectContainerImageDriftUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_container_image_drift__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_container_image_drift__mutmut)
def detect_container_image_drift(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = DetectContainerImageDriftUseCase(port=build_helm_drift_adapter())  # type: ignore
        use_case.execute(DetectContainerImageDriftCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_container_image_drift__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = DetectContainerImageDriftUseCase(port=build_helm_drift_adapter())  # type: ignore
        use_case.execute(DetectContainerImageDriftCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_container_image_drift__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = None  # type: ignore
        use_case.execute(DetectContainerImageDriftCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_container_image_drift__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = DetectContainerImageDriftUseCase(port=None)  # type: ignore
        use_case.execute(DetectContainerImageDriftCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_container_image_drift__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = DetectContainerImageDriftUseCase(port=build_helm_drift_adapter())  # type: ignore
        use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_container_image_drift__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = DetectContainerImageDriftUseCase(port=build_helm_drift_adapter())  # type: ignore
        use_case.execute(DetectContainerImageDriftCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_container_image_drift__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = DetectContainerImageDriftUseCase(port=build_helm_drift_adapter())  # type: ignore
        use_case.execute(DetectContainerImageDriftCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_container_image_drift__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = DetectContainerImageDriftUseCase(port=build_helm_drift_adapter())  # type: ignore
        use_case.execute(DetectContainerImageDriftCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_detect_container_image_drift__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = DetectContainerImageDriftUseCase(port=build_helm_drift_adapter())  # type: ignore
        use_case.execute(DetectContainerImageDriftCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_detect_container_image_drift__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_drift_adapter

    try:
        use_case = DetectContainerImageDriftUseCase(port=build_helm_drift_adapter())  # type: ignore
        use_case.execute(DetectContainerImageDriftCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_detect_container_image_drift__mutmut['_mutmut_orig'] = x_detect_container_image_drift__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_container_image_drift__mutmut['x_detect_container_image_drift__mutmut_1'] = x_detect_container_image_drift__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_container_image_drift__mutmut['x_detect_container_image_drift__mutmut_2'] = x_detect_container_image_drift__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_container_image_drift__mutmut['x_detect_container_image_drift__mutmut_3'] = x_detect_container_image_drift__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_container_image_drift__mutmut['x_detect_container_image_drift__mutmut_4'] = x_detect_container_image_drift__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_container_image_drift__mutmut['x_detect_container_image_drift__mutmut_5'] = x_detect_container_image_drift__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_container_image_drift__mutmut['x_detect_container_image_drift__mutmut_6'] = x_detect_container_image_drift__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_container_image_drift__mutmut['x_detect_container_image_drift__mutmut_7'] = x_detect_container_image_drift__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_container_image_drift__mutmut['x_detect_container_image_drift__mutmut_8'] = x_detect_container_image_drift__mutmut_8 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_container_image_drift)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(detect_container_image_drift)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
