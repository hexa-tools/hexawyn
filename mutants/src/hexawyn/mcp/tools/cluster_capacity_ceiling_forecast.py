"""MCP tool: cluster_capacity_ceiling_forecast — Forecast cluster capacity ceiling."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_use_case import (  # noqa: E501
    ClusterCapacityCeilingForecastUseCase,
)
from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.command import (
    ClusterCapacityCeilingForecastCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_cluster_capacity_ceiling_forecast__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_cluster_capacity_ceiling_forecast__mutmut)
def cluster_capacity_ceiling_forecast() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = None
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=None,
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=None,
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = None
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(None)
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "XXcpuXX": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "CPU": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "XXmemoryXX": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "MEMORY": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "XXcritical_resourceXX": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "CRITICAL_RESOURCE": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "XXautoscaler_enabledXX": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "AUTOSCALER_ENABLED": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "XXrecommendationXX": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "RECOMMENDATION": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "XXconfidenceXX": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "CONFIDENCE": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "XXwindow_days_usedXX": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "WINDOW_DAYS_USED": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXcpuXX": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "CPU": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "XXmemoryXX": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "MEMORY": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "XXcritical_resourceXX": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "CRITICAL_RESOURCE": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "XXXX",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "XXautoscaler_enabledXX": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "AUTOSCALER_ENABLED": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": True,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "XXrecommendationXX": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_35() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "RECOMMENDATION": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_36() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "XXXX",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_37() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "XXconfidenceXX": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_38() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "CONFIDENCE": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_39() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "XXXX",
            "window_days_used": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_40() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "XXwindow_days_usedXX": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_41() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "WINDOW_DAYS_USED": 0,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_42() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 1,
            "error": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_43() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "XXerrorXX": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_44() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "ERROR": str(exc),
        }


def x_cluster_capacity_ceiling_forecast__mutmut_45() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(None),
        }

mutants_x_cluster_capacity_ceiling_forecast__mutmut['_mutmut_orig'] = x_cluster_capacity_ceiling_forecast__mutmut_orig # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_1'] = x_cluster_capacity_ceiling_forecast__mutmut_1 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_2'] = x_cluster_capacity_ceiling_forecast__mutmut_2 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_3'] = x_cluster_capacity_ceiling_forecast__mutmut_3 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_4'] = x_cluster_capacity_ceiling_forecast__mutmut_4 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_5'] = x_cluster_capacity_ceiling_forecast__mutmut_5 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_6'] = x_cluster_capacity_ceiling_forecast__mutmut_6 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_7'] = x_cluster_capacity_ceiling_forecast__mutmut_7 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_8'] = x_cluster_capacity_ceiling_forecast__mutmut_8 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_9'] = x_cluster_capacity_ceiling_forecast__mutmut_9 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_10'] = x_cluster_capacity_ceiling_forecast__mutmut_10 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_11'] = x_cluster_capacity_ceiling_forecast__mutmut_11 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_12'] = x_cluster_capacity_ceiling_forecast__mutmut_12 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_13'] = x_cluster_capacity_ceiling_forecast__mutmut_13 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_14'] = x_cluster_capacity_ceiling_forecast__mutmut_14 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_15'] = x_cluster_capacity_ceiling_forecast__mutmut_15 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_16'] = x_cluster_capacity_ceiling_forecast__mutmut_16 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_17'] = x_cluster_capacity_ceiling_forecast__mutmut_17 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_18'] = x_cluster_capacity_ceiling_forecast__mutmut_18 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_19'] = x_cluster_capacity_ceiling_forecast__mutmut_19 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_20'] = x_cluster_capacity_ceiling_forecast__mutmut_20 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_21'] = x_cluster_capacity_ceiling_forecast__mutmut_21 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_22'] = x_cluster_capacity_ceiling_forecast__mutmut_22 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_23'] = x_cluster_capacity_ceiling_forecast__mutmut_23 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_24'] = x_cluster_capacity_ceiling_forecast__mutmut_24 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_25'] = x_cluster_capacity_ceiling_forecast__mutmut_25 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_26'] = x_cluster_capacity_ceiling_forecast__mutmut_26 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_27'] = x_cluster_capacity_ceiling_forecast__mutmut_27 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_28'] = x_cluster_capacity_ceiling_forecast__mutmut_28 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_29'] = x_cluster_capacity_ceiling_forecast__mutmut_29 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_30'] = x_cluster_capacity_ceiling_forecast__mutmut_30 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_31'] = x_cluster_capacity_ceiling_forecast__mutmut_31 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_32'] = x_cluster_capacity_ceiling_forecast__mutmut_32 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_33'] = x_cluster_capacity_ceiling_forecast__mutmut_33 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_34'] = x_cluster_capacity_ceiling_forecast__mutmut_34 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_35'] = x_cluster_capacity_ceiling_forecast__mutmut_35 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_36'] = x_cluster_capacity_ceiling_forecast__mutmut_36 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_37'] = x_cluster_capacity_ceiling_forecast__mutmut_37 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_38'] = x_cluster_capacity_ceiling_forecast__mutmut_38 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_39'] = x_cluster_capacity_ceiling_forecast__mutmut_39 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_40'] = x_cluster_capacity_ceiling_forecast__mutmut_40 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_41'] = x_cluster_capacity_ceiling_forecast__mutmut_41 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_42'] = x_cluster_capacity_ceiling_forecast__mutmut_42 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_43'] = x_cluster_capacity_ceiling_forecast__mutmut_43 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_44'] = x_cluster_capacity_ceiling_forecast__mutmut_44 # type: ignore # mutmut generated
mutants_x_cluster_capacity_ceiling_forecast__mutmut['x_cluster_capacity_ceiling_forecast__mutmut_45'] = x_cluster_capacity_ceiling_forecast__mutmut_45 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(cluster_capacity_ceiling_forecast)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(cluster_capacity_ceiling_forecast)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
