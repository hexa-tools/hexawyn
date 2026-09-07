"""MCP tool: error_attribution — Identify which downstream service causes gateway errors."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.error_attribution.command import (
    ErrorAttributionCommand,
)
from hexawyn.application.use_case.observability.error_attribution.error_attribution_use_case import (  # noqa: E501
    ErrorAttributionUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_error_attribution__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_error_attribution__mutmut)
def error_attribution(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_orig(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_1(gateway: str, time_window_minutes: int = 31) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_2(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = None
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_3(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = None
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_4(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            None  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_5(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=None).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_6(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=None, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_7(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=None)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_8(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_9(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, )  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_10(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "XXgatewayXX": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_11(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "GATEWAY": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_12(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "XXtotal_errorsXX": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_13(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "TOTAL_ERRORS": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_14(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "XXattributionXX": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_15(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "ATTRIBUTION": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_16(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "XXpareto_culpritXX": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_17(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "PARETO_CULPRIT": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_18(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_19(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(exc)}


def x_error_attribution__mutmut_20(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXgatewayXX": gateway, "error": str(exc)}


def x_error_attribution__mutmut_21(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"GATEWAY": gateway, "error": str(exc)}


def x_error_attribution__mutmut_22(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "XXerrorXX": str(exc)}


def x_error_attribution__mutmut_23(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "ERROR": str(exc)}


def x_error_attribution__mutmut_24(gateway: str, time_window_minutes: int = 30) -> dict[str, object]:
    from hexawyn.mcp.server import build_error_attribution_adapter

    try:
        a = build_error_attribution_adapter()
        r = ErrorAttributionUseCase(port=a).execute(
            ErrorAttributionCommand(gateway=gateway, time_window_minutes=time_window_minutes)  # type: ignore
        )
        return {
            "gateway": r.gateway,
            "total_errors": r.total_errors,
            "attribution": r.attribution,
            "pareto_culprit": r.pareto_culprit,
            "error": r.error,
        }
    except Exception as exc:
        return {"gateway": gateway, "error": str(None)}

mutants_x_error_attribution__mutmut['_mutmut_orig'] = x_error_attribution__mutmut_orig # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_1'] = x_error_attribution__mutmut_1 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_2'] = x_error_attribution__mutmut_2 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_3'] = x_error_attribution__mutmut_3 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_4'] = x_error_attribution__mutmut_4 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_5'] = x_error_attribution__mutmut_5 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_6'] = x_error_attribution__mutmut_6 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_7'] = x_error_attribution__mutmut_7 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_8'] = x_error_attribution__mutmut_8 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_9'] = x_error_attribution__mutmut_9 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_10'] = x_error_attribution__mutmut_10 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_11'] = x_error_attribution__mutmut_11 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_12'] = x_error_attribution__mutmut_12 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_13'] = x_error_attribution__mutmut_13 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_14'] = x_error_attribution__mutmut_14 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_15'] = x_error_attribution__mutmut_15 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_16'] = x_error_attribution__mutmut_16 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_17'] = x_error_attribution__mutmut_17 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_18'] = x_error_attribution__mutmut_18 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_19'] = x_error_attribution__mutmut_19 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_20'] = x_error_attribution__mutmut_20 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_21'] = x_error_attribution__mutmut_21 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_22'] = x_error_attribution__mutmut_22 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_23'] = x_error_attribution__mutmut_23 # type: ignore # mutmut generated
mutants_x_error_attribution__mutmut['x_error_attribution__mutmut_24'] = x_error_attribution__mutmut_24 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(error_attribution)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(error_attribution)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
