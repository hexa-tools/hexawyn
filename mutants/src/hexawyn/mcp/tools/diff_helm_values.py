# mypy: ignore-errors
"""MCP tool: diff_helm_values."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.diff_helm_values.command import DiffHelmValuesCommand
from hexawyn.application.use_case.gitops.diff_helm_values.diff_helm_values_use_case import (
    DiffHelmValuesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_diff_helm_values__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_diff_helm_values__mutmut)
def diff_helm_values(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_orig(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_1(  # type: ignore
    release="XXtestXX",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_2(  # type: ignore
    release="TEST",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_3(  # type: ignore
    release="test",
    source_namespace="XXtest-source_namespaceXX",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_4(  # type: ignore
    release="test",
    source_namespace="TEST-SOURCE_NAMESPACE",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_5(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="XXtest-target_namespaceXX",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_6(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="TEST-TARGET_NAMESPACE",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_7(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = None
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_8(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=None)
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_9(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_10(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_11(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_12(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_diff_helm_values__mutmut_13(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_diff_helm_values__mutmut_14(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_diff_helm_values__mutmut_15(  # type: ignore
    release="test",
    source_namespace="test-source_namespace",
    target_namespace="test-target_namespace",
) -> dict[str, object]:
    from hexawyn.mcp.server import build_helm_values_diff_adapter

    try:
        use_case = DiffHelmValuesUseCase(helm_values_port=build_helm_values_diff_adapter())
        _ = use_case.execute(DiffHelmValuesCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_diff_helm_values__mutmut['_mutmut_orig'] = x_diff_helm_values__mutmut_orig # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_1'] = x_diff_helm_values__mutmut_1 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_2'] = x_diff_helm_values__mutmut_2 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_3'] = x_diff_helm_values__mutmut_3 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_4'] = x_diff_helm_values__mutmut_4 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_5'] = x_diff_helm_values__mutmut_5 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_6'] = x_diff_helm_values__mutmut_6 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_7'] = x_diff_helm_values__mutmut_7 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_8'] = x_diff_helm_values__mutmut_8 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_9'] = x_diff_helm_values__mutmut_9 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_10'] = x_diff_helm_values__mutmut_10 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_11'] = x_diff_helm_values__mutmut_11 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_12'] = x_diff_helm_values__mutmut_12 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_13'] = x_diff_helm_values__mutmut_13 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_14'] = x_diff_helm_values__mutmut_14 # type: ignore # mutmut generated
mutants_x_diff_helm_values__mutmut['x_diff_helm_values__mutmut_15'] = x_diff_helm_values__mutmut_15 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(diff_helm_values)


def x_register__mutmut_orig(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(diff_helm_values)


def x_register__mutmut_1(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
