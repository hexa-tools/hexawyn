from abc import ABC


class TestOptimizationRoiPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.optimization_roi_port import (
            OptimizationRoiPort,
        )

        assert issubclass(OptimizationRoiPort, ABC)

    def test_declares_get_sprint_roi_data(self) -> None:
        from hexawyn.application.ports.driven.optimization_roi_port import (
            OptimizationRoiPort,
        )

        assert "get_sprint_roi_data" in OptimizationRoiPort.__abstractmethods__


class TestSprintRoiData:
    def test_shape(self) -> None:
        from hexawyn.application.ports.driven.optimization_roi_port import SprintRoiData

        data: SprintRoiData = {
            "has_baseline": True,
            "baseline_monthly_eur": 500.0,
            "current_monthly_eur": 150.0,
            "optimizations": [
                {
                    "name": "right-size payment-api",
                    "category": "right_sizing",
                    "monthly_saving_eur": 350.0,
                    "description": "1.0 → 0.3 cores",
                }
            ],
            "performance_metrics": [{"metric": "p99_latency_ms", "before": 120.0, "after": 95.0}],
        }

        assert data["has_baseline"] is True
        assert data["baseline_monthly_eur"] == 500.0
        assert data["optimizations"][0]["category"] == "right_sizing"
        assert data["performance_metrics"][0]["metric"] == "p99_latency_ms"
