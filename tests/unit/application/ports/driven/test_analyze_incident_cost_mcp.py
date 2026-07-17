"""RED → GREEN — MCP tool: analyze_incident_cost."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.incident_cost_port import (
    IncidentCostData,
    IncidentCostPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _data(revenue: float | None = 500.0, downtime: int = 27) -> IncidentCostData:
    return IncidentCostData(
        business_service_name="Service Paiement",
        downtime_minutes=downtime,
        impacted_service_count=3,
        resolved_at="14h23",
        sla_breached=False,
        business_config={
            "revenue_per_minute": revenue,
            "support_cost_per_hour": None,
            "sla_penalty_per_hour": None,
        },
    )


def _port(data: IncidentCostData) -> MagicMock:
    port = MagicMock(spec=IncidentCostPort)
    port.get_incident_cost_data.return_value = data
    return port


class TestAnalyzeIncidentCostTool:
    def test_demo_scenario_13500(self) -> None:
        with patch("hexawyn.mcp.server.build_incident_cost_adapter", return_value=_port(_data())):
            from hexawyn.mcp.tools.analyze_incident_cost import analyze_incident_cost

            result = analyze_incident_cost(incident_ref="yesterday")

        assert result["business_service_name"] == "Service Paiement"
        assert result["downtime_minutes"] == 27
        assert result["revenue_impact_eur"] == 13500.0
        assert result["total_cost_eur"] == 13500.0
        assert result["impacted_service_count"] == 3
        assert result["config_available"] is True
        assert result["error"] is None

    def test_calculation_basis_exposed(self) -> None:
        with patch("hexawyn.mcp.server.build_incident_cost_adapter", return_value=_port(_data())):
            from hexawyn.mcp.tools.analyze_incident_cost import analyze_incident_cost

            result = analyze_incident_cost(incident_ref="yesterday")

        basis = result["calculation_basis"]
        assert basis is not None
        assert "revenue_per_minute" in basis["config_values_used"]
        assert "downtime" in basis["formula"].lower()

    def test_missing_config_returns_explanation_no_amount(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_incident_cost_adapter",
            return_value=_port(_data(revenue=None)),
        ):
            from hexawyn.mcp.tools.analyze_incident_cost import analyze_incident_cost

            result = analyze_incident_cost(incident_ref="yesterday")

        assert result["config_available"] is False
        assert result["revenue_impact_eur"] is None
        assert result["total_cost_eur"] is None
        assert "revenue_per_minute" in result["explanation"]

    def test_no_kubernetes_jargon_in_service_name(self) -> None:
        with patch("hexawyn.mcp.server.build_incident_cost_adapter", return_value=_port(_data())):
            from hexawyn.mcp.tools.analyze_incident_cost import analyze_incident_cost

            result = analyze_incident_cost(incident_ref="yesterday")

        name = result["business_service_name"].lower()
        for term in ("pod", "deployment", "replicaset", "statefulset", "hpa"):
            assert term not in name

    def test_handles_error_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_incident_cost_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.analyze_incident_cost import analyze_incident_cost

            result = analyze_incident_cost(incident_ref="yesterday")

        assert result["total_cost_eur"] is None
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.analyze_incident_cost import register

        assert callable(register)
