"""RED → GREEN — MCP tool: compute_optimization_roi."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.optimization_roi_port import (
    OptimizationRoiPort,
    SprintRoiData,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _data(
    has_baseline: bool = True,
    metrics: list[dict[str, object]] | None = None,
) -> SprintRoiData:
    return SprintRoiData(
        has_baseline=has_baseline,
        baseline_monthly_eur=500.0,
        current_monthly_eur=150.0,
        optimizations=[
            {
                "name": "right-size",
                "category": "right_sizing",
                "monthly_saving_eur": 350.0,
                "description": "1.0 → 0.3 cores",
            }
        ],
        performance_metrics=metrics if metrics is not None else [],
    )


def _port(data: SprintRoiData) -> MagicMock:
    port = MagicMock(spec=OptimizationRoiPort)
    port.get_sprint_roi_data.return_value = data
    return port


class TestComputeOptimizationRoiTool:
    def test_returns_savings_and_optimizations(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_optimization_roi_adapter",
            return_value=_port(_data()),
        ):
            from hexawyn.mcp.tools.compute_optimization_roi import compute_optimization_roi

            result = compute_optimization_roi(sprint_id="sprint-42")

        assert result["baseline_monthly_eur"] == 500.0
        assert result["monthly_saving_eur"] == 350.0
        assert result["annual_saving_eur"] == 4200.0
        assert result["savings_pct"] == 70.0
        assert result["top_optimization"]["name"] == "right-size"
        assert result["error"] is None

    def test_trade_off_flagged(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_optimization_roi_adapter",
            return_value=_port(
                _data(metrics=[{"metric": "p99_latency_ms", "before": 95.0, "after": 130.0}])
            ),
        ):
            from hexawyn.mcp.tools.compute_optimization_roi import compute_optimization_roi

            result = compute_optimization_roi(sprint_id="sprint-42")

        assert result["has_regression"] is True
        assert result["warning"] != ""

    def test_no_baseline_returns_guidance(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_optimization_roi_adapter",
            return_value=_port(_data(has_baseline=False)),
        ):
            from hexawyn.mcp.tools.compute_optimization_roi import compute_optimization_roi

            result = compute_optimization_roi(sprint_id="sprint-42")

        assert result["has_baseline"] is False
        assert "baseline" in result["warning"].lower()

    def test_traffic_normalization(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_optimization_roi_adapter",
            return_value=_port(_data()),
        ):
            from hexawyn.mcp.tools.compute_optimization_roi import compute_optimization_roi

            result = compute_optimization_roi(sprint_id="sprint-42", traffic_growth_pct=20.0)

        assert result["traffic_normalized"] is True
        assert result["monthly_saving_eur"] == 375.0

    def test_handles_error_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_optimization_roi_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.compute_optimization_roi import compute_optimization_roi

            result = compute_optimization_roi(sprint_id="sprint-42")

        assert result["monthly_saving_eur"] == 0.0
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.compute_optimization_roi import register

        assert callable(register)
