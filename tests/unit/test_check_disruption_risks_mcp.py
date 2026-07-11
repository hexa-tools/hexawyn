from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.disruption_risk_port import (
    DisruptionRiskPort,
    RiskEventRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _risks() -> list[RiskEventRaw]:
    return [
        RiskEventRaw(
            business_service_name="moteur de recommandation",
            risk_type="memory_saturation",
            predicted_date="2026-09-20",
            days_from_now=3,
            detail="Saturation memoire prevue",
        )
    ]


def _port(risks: list[RiskEventRaw]) -> MagicMock:
    port = MagicMock(spec=DisruptionRiskPort)
    port.get_disruption_risks.return_value = risks
    return port


class TestCheckDisruptionRisksTool:
    def test_memory_saturation_in_three_days(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_disruption_risk_adapter",
            return_value=_port(_risks()),
        ):
            from hexawyn.mcp.tools.check_disruption_risks import check_disruption_risks

            result = check_disruption_risks()

        assert result["has_risks"] is True
        assert result["risks"][0]["days_from_now"] == 3
        assert result["risks"][0]["business_service_name"] == "moteur de recommandation"
        assert result["error"] is None

    def test_no_risks_stable(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_disruption_risk_adapter",
            return_value=_port([]),
        ):
            from hexawyn.mcp.tools.check_disruption_risks import check_disruption_risks

            result = check_disruption_risks()

        assert result["has_risks"] is False

    def test_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_disruption_risk_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.check_disruption_risks import check_disruption_risks

            result = check_disruption_risks()

        assert "down" in result["error"]

    def test_has_register(self) -> None:
        from hexawyn.mcp.tools.check_disruption_risks import register

        assert callable(register)
