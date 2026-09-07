# mypy: ignore-errors
"""MCP tool: detect_kustomize_patch_conflicts."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_use_case import (  # noqa: E501
    DetectKustomizePatchConflictsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_kustomize_patch_conflicts__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_kustomize_patch_conflicts__mutmut)
def detect_kustomize_patch_conflicts(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_orig(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_1(overlay_path: str = "XXtestXX") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_2(overlay_path: str = "TEST") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_3(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = None
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_4(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=None
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_5(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_6(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_7(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_8(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_9(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_10(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_detect_kustomize_patch_conflicts__mutmut_11(overlay_path: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

    try:
        use_case = DetectKustomizePatchConflictsUseCase(  # type: ignore
            port=build_kustomize_patch_analysis_adapter()
        )
        _ = use_case.execute(DetectKustomizePatchConflictsCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_detect_kustomize_patch_conflicts__mutmut['_mutmut_orig'] = x_detect_kustomize_patch_conflicts__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_1'] = x_detect_kustomize_patch_conflicts__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_2'] = x_detect_kustomize_patch_conflicts__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_3'] = x_detect_kustomize_patch_conflicts__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_4'] = x_detect_kustomize_patch_conflicts__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_5'] = x_detect_kustomize_patch_conflicts__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_6'] = x_detect_kustomize_patch_conflicts__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_7'] = x_detect_kustomize_patch_conflicts__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_8'] = x_detect_kustomize_patch_conflicts__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_9'] = x_detect_kustomize_patch_conflicts__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_10'] = x_detect_kustomize_patch_conflicts__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_kustomize_patch_conflicts__mutmut['x_detect_kustomize_patch_conflicts__mutmut_11'] = x_detect_kustomize_patch_conflicts__mutmut_11 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(detect_kustomize_patch_conflicts)


def x_register__mutmut_orig(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(detect_kustomize_patch_conflicts)


def x_register__mutmut_1(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
