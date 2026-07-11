from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.engineer_workload_port import (
    EngineerWorkloadPort,
    MonthNightData,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _months(
    current_interventions: int = 24, previous_interventions: int = 42
) -> list[MonthNightData]:
    return [
        MonthNightData(
            month="2026-04", night_intervention_count=previous_interventions // 3, total_nights=30
        ),
        MonthNightData(
            month="2026-05", night_intervention_count=previous_interventions // 3, total_nights=30
        ),
        MonthNightData(
            month="2026-06", night_intervention_count=previous_interventions // 3, total_nights=30
        ),
        MonthNightData(
            month="2026-07", night_intervention_count=current_interventions // 3, total_nights=30
        ),
        MonthNightData(
            month="2026-08", night_intervention_count=current_interventions // 3, total_nights=30
        ),
        MonthNightData(
            month="2026-09", night_intervention_count=current_interventions // 3, total_nights=30
        ),
    ]


def _port(months: list[MonthNightData]) -> MagicMock:
    port = MagicMock(spec=EngineerWorkloadPort)
    port.get_night_intervention_data.return_value = months
    return port


class TestReportNightInterventionsTool:
    def test_returns_avg_and_trend(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_night_intervention_adapter",
            return_value=_port(_months(current_interventions=24, previous_interventions=126)),
        ):
            from hexawyn.mcp.tools.report_night_interventions import report_night_interventions

            result = report_night_interventions()

        assert result["avg_interventions_per_night"] <= 1.0
        assert result["trend"] in ("improving", "stable", "degrading")
        assert "intervention" in result["summary"]
        assert result["error"] is None

    def test_zero_interventions_is_zero(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_night_intervention_adapter",
            return_value=_port(_months(current_interventions=0, previous_interventions=0)),
        ):
            from hexawyn.mcp.tools.report_night_interventions import report_night_interventions

            result = report_night_interventions()

        assert result["avg_interventions_per_night"] == 0.0

    def test_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_night_intervention_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.report_night_interventions import report_night_interventions

            result = report_night_interventions()

        assert "down" in result["error"]

    def test_has_register(self) -> None:
        from hexawyn.mcp.tools.report_night_interventions import register

        assert callable(register)
