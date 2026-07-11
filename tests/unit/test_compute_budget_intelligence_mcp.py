from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.budget_intelligence_port import (
    BudgetIntelligenceData,
    BudgetIntelligencePort,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _data(projected: float = 16000.0, budget: float | None = 12000.0) -> BudgetIntelligenceData:
    return BudgetIntelligenceData(
        current_spend_eur=4000.0,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
    )


def _port(data: BudgetIntelligenceData) -> MagicMock:
    port = MagicMock(spec=BudgetIntelligencePort)
    port.get_budget_intelligence_data.return_value = data
    return port


class TestComputeBudgetIntelligenceTool:
    def test_budget_alert(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_budget_intelligence_adapter",
            return_value=_port(_data(projected=16000.0, budget=12000.0)),
        ):
            from hexawyn.mcp.tools.compute_budget_intelligence import (
                compute_budget_intelligence,
            )

            result = compute_budget_intelligence(period="2026-06")

        assert result["budget_exceeded"] is True
        assert result["overshoot_pct"] > 0
        assert len(result["recommendations"]) == 3
        assert result["error"] is None

    def test_within_budget_no_alert(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_budget_intelligence_adapter",
            return_value=_port(_data(projected=8000.0, budget=12000.0)),
        ):
            from hexawyn.mcp.tools.compute_budget_intelligence import (
                compute_budget_intelligence,
            )

            result = compute_budget_intelligence(period="2026-06")

        assert result["budget_exceeded"] is False

    def test_missing_budget_explains(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_budget_intelligence_adapter",
            return_value=_port(_data(budget=None)),
        ):
            from hexawyn.mcp.tools.compute_budget_intelligence import (
                compute_budget_intelligence,
            )

            result = compute_budget_intelligence(period="2026-06")

        assert result["config_available"] is False
        assert "cloud_budget_monthly" in result["explanation"]

    def test_handles_error_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_budget_intelligence_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.compute_budget_intelligence import (
                compute_budget_intelligence,
            )

            result = compute_budget_intelligence(period="2026-06")

        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.compute_budget_intelligence import register

        assert callable(register)
