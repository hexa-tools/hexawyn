# mypy: ignore-errors
"""MCP tool: compute_slo_error_budget."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.compute_slo_error_budget.command import (  # type: ignore
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.use_case.workloads.compute_slo_error_budget.compute_slo_error_budget_use_case import (  # noqa: E501
    ComputeSLOErrorBudgetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_slo_error_budget__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_slo_error_budget__mutmut)
def compute_slo_error_budget(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_slo_error_budget__mutmut_orig(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_slo_error_budget__mutmut_1(service_name: str = "XXtest-service_nameXX") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_slo_error_budget__mutmut_2(service_name: str = "TEST-SERVICE_NAME") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_slo_error_budget__mutmut_3(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = None
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_slo_error_budget__mutmut_4(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=None)
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_slo_error_budget__mutmut_5(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = None  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_slo_error_budget__mutmut_6(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(None)  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_slo_error_budget__mutmut_7(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_slo_error_budget__mutmut_8(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compute_slo_error_budget__mutmut_9(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_compute_slo_error_budget__mutmut_10(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_compute_slo_error_budget__mutmut_11(service_name: str = "test-service_name") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        use_case = ComputeSLOErrorBudgetUseCase(error_budget_port=build_error_budget_adapter())
        _ = use_case.execute(ComputeSLOErrorBudgetCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_compute_slo_error_budget__mutmut['_mutmut_orig'] = x_compute_slo_error_budget__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_1'] = x_compute_slo_error_budget__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_2'] = x_compute_slo_error_budget__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_3'] = x_compute_slo_error_budget__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_4'] = x_compute_slo_error_budget__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_5'] = x_compute_slo_error_budget__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_6'] = x_compute_slo_error_budget__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_7'] = x_compute_slo_error_budget__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_8'] = x_compute_slo_error_budget__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_9'] = x_compute_slo_error_budget__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_10'] = x_compute_slo_error_budget__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_slo_error_budget__mutmut['x_compute_slo_error_budget__mutmut_11'] = x_compute_slo_error_budget__mutmut_11 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(compute_slo_error_budget)


def x_register__mutmut_orig(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(compute_slo_error_budget)


def x_register__mutmut_1(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
