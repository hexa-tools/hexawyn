"""MCP tool: compare_service_cost."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.compare_service_cost.command import (
    CompareServiceCostCommand,
)
from hexawyn.application.use_case.finops.compare_service_cost.compare_service_cost_use_case import (
    CompareUseCaseCostUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compare_service_cost__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compare_service_cost__mutmut)
def compare_service_cost(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_orig(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_1(
    service_name: str,
    cpu_price_per_core_hour: float = 1.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_2(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 1.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_3(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = None
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_4(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=None)
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_5(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = None
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_6(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            None
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_7(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=None,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_8(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=None,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_9(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=None,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_10(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_11(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_12(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_13(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"XXerrorXX": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_14(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"ERROR": None}
    except Exception as exc:
        return {"error": str(exc)}


def x_compare_service_cost__mutmut_15(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_compare_service_cost__mutmut_16(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_compare_service_cost__mutmut_17(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        use_case = CompareUseCaseCostUseCase(cost_port=build_service_cost_adapter())
        _ = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_compare_service_cost__mutmut['_mutmut_orig'] = x_compare_service_cost__mutmut_orig # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_1'] = x_compare_service_cost__mutmut_1 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_2'] = x_compare_service_cost__mutmut_2 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_3'] = x_compare_service_cost__mutmut_3 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_4'] = x_compare_service_cost__mutmut_4 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_5'] = x_compare_service_cost__mutmut_5 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_6'] = x_compare_service_cost__mutmut_6 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_7'] = x_compare_service_cost__mutmut_7 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_8'] = x_compare_service_cost__mutmut_8 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_9'] = x_compare_service_cost__mutmut_9 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_10'] = x_compare_service_cost__mutmut_10 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_11'] = x_compare_service_cost__mutmut_11 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_12'] = x_compare_service_cost__mutmut_12 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_13'] = x_compare_service_cost__mutmut_13 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_14'] = x_compare_service_cost__mutmut_14 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_15'] = x_compare_service_cost__mutmut_15 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_16'] = x_compare_service_cost__mutmut_16 # type: ignore # mutmut generated
mutants_x_compare_service_cost__mutmut['x_compare_service_cost__mutmut_17'] = x_compare_service_cost__mutmut_17 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(compare_service_cost)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(compare_service_cost)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
