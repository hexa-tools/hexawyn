from abc import ABC


class TestBudgetProjectionPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.budget_projection_port import (
            BudgetProjectionPort,
        )

        assert issubclass(BudgetProjectionPort, ABC)

    def test_declares_get_monthly_cost_history(self) -> None:
        from hexawyn.application.ports.driven.budget_projection_port import (
            BudgetProjectionPort,
        )

        assert "get_monthly_cost_history" in BudgetProjectionPort.__abstractmethods__


class TestMonthlyCostRaw:
    def test_shape(self) -> None:
        from hexawyn.application.ports.driven.budget_projection_port import (
            MonthlyCostRaw,
        )

        raw: MonthlyCostRaw = {
            "month": "2026-06",
            "total_usd": 8000.0,
            "compute_usd": 5000.0,
            "storage_usd": 2000.0,
            "network_usd": 1000.0,
        }

        assert raw["month"] == "2026-06"
        assert raw["total_usd"] == 8000.0
        assert raw["compute_usd"] == 5000.0
