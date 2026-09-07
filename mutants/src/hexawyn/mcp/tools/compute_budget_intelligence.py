"""MCP tool: compute_budget_intelligence — Compute budget intelligence."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.compute_budget_intelligence.command import (
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.use_case.finops.compute_budget_intelligence.compute_budget_intelligence_use_case import (  # noqa: E501
    ComputeBudgetIntelligenceUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_budget_intelligence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_budget_intelligence__mutmut)
def compute_budget_intelligence(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_orig(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_1(period: str = "XXcurrentXX") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_2(period: str = "CURRENT") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_3(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = None
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_4(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=None
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_5(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = None  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_6(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=None)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_7(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = None
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_8(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(None)
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_9(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=None))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_10(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"XXperiod_labelXX": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_11(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"PERIOD_LABEL": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_12(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "XXerrorXX": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_13(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "ERROR": None}
    except Exception as exc:
        return {"period_label": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_14(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"XXperiod_labelXX": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_15(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"PERIOD_LABEL": period, "error": str(exc)}


def x_compute_budget_intelligence__mutmut_16(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "XXerrorXX": str(exc)}


def x_compute_budget_intelligence__mutmut_17(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "ERROR": str(exc)}


def x_compute_budget_intelligence__mutmut_18(period: str = "current") -> dict[str, object]:
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        service = ComputeBudgetIntelligenceUseCase(
            budget_intelligence_port=build_budget_intelligence_adapter()
        )
        use_case = ComputeBudgetIntelligenceUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        return {"period_label": period, "error": None}
    except Exception as exc:
        return {"period_label": period, "error": str(None)}

mutants_x_compute_budget_intelligence__mutmut['_mutmut_orig'] = x_compute_budget_intelligence__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_1'] = x_compute_budget_intelligence__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_2'] = x_compute_budget_intelligence__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_3'] = x_compute_budget_intelligence__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_4'] = x_compute_budget_intelligence__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_5'] = x_compute_budget_intelligence__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_6'] = x_compute_budget_intelligence__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_7'] = x_compute_budget_intelligence__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_8'] = x_compute_budget_intelligence__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_9'] = x_compute_budget_intelligence__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_10'] = x_compute_budget_intelligence__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_11'] = x_compute_budget_intelligence__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_12'] = x_compute_budget_intelligence__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_13'] = x_compute_budget_intelligence__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_14'] = x_compute_budget_intelligence__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_15'] = x_compute_budget_intelligence__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_16'] = x_compute_budget_intelligence__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_17'] = x_compute_budget_intelligence__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_18'] = x_compute_budget_intelligence__mutmut_18 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_budget_intelligence)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(compute_budget_intelligence)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
