"""MCP tool: metric_correlation — Correlate error/latency spikes between services."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.metric_correlation.command import (
    MetricCorrelationCommand,
)
from hexawyn.application.use_case.observability.metric_correlation.metric_correlation_use_case import (  # noqa: E501
    MetricCorrelationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_metric_correlation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_metric_correlation__mutmut)
def metric_correlation(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_orig(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_1(
    primary_service: str, correlated_service: str, time_window_minutes: int = 31
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_2(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = None
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_3(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = None
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_4(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            None
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_5(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=None).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_6(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=None,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_7(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=None,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_8(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=None,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_9(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_10(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_11(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_12(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "XXprimary_serviceXX": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_13(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "PRIMARY_SERVICE": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_14(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "XXcorrelated_serviceXX": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_15(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "CORRELATED_SERVICE": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_16(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "XXstatusXX": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_17(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "STATUS": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_18(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "XXcoefficientXX": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_19(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "COEFFICIENT": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_20(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "XXlag_indexXX": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_21(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "LAG_INDEX": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_22(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "XXhypothesisXX": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_23(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "HYPOTHESIS": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_24(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "XXdata_point_countXX": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_25(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "DATA_POINT_COUNT": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_26(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_27(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_28(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXprimary_serviceXX": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_29(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"PRIMARY_SERVICE": primary_service, "error": str(exc)}


def x_metric_correlation__mutmut_30(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "XXerrorXX": str(exc)}


def x_metric_correlation__mutmut_31(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "ERROR": str(exc)}


def x_metric_correlation__mutmut_32(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(port=a).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(None)}

mutants_x_metric_correlation__mutmut['_mutmut_orig'] = x_metric_correlation__mutmut_orig # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_1'] = x_metric_correlation__mutmut_1 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_2'] = x_metric_correlation__mutmut_2 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_3'] = x_metric_correlation__mutmut_3 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_4'] = x_metric_correlation__mutmut_4 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_5'] = x_metric_correlation__mutmut_5 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_6'] = x_metric_correlation__mutmut_6 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_7'] = x_metric_correlation__mutmut_7 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_8'] = x_metric_correlation__mutmut_8 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_9'] = x_metric_correlation__mutmut_9 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_10'] = x_metric_correlation__mutmut_10 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_11'] = x_metric_correlation__mutmut_11 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_12'] = x_metric_correlation__mutmut_12 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_13'] = x_metric_correlation__mutmut_13 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_14'] = x_metric_correlation__mutmut_14 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_15'] = x_metric_correlation__mutmut_15 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_16'] = x_metric_correlation__mutmut_16 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_17'] = x_metric_correlation__mutmut_17 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_18'] = x_metric_correlation__mutmut_18 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_19'] = x_metric_correlation__mutmut_19 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_20'] = x_metric_correlation__mutmut_20 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_21'] = x_metric_correlation__mutmut_21 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_22'] = x_metric_correlation__mutmut_22 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_23'] = x_metric_correlation__mutmut_23 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_24'] = x_metric_correlation__mutmut_24 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_25'] = x_metric_correlation__mutmut_25 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_26'] = x_metric_correlation__mutmut_26 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_27'] = x_metric_correlation__mutmut_27 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_28'] = x_metric_correlation__mutmut_28 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_29'] = x_metric_correlation__mutmut_29 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_30'] = x_metric_correlation__mutmut_30 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_31'] = x_metric_correlation__mutmut_31 # type: ignore # mutmut generated
mutants_x_metric_correlation__mutmut['x_metric_correlation__mutmut_32'] = x_metric_correlation__mutmut_32 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(metric_correlation)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(metric_correlation)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
