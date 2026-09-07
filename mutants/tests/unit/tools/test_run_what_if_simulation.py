from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRunWhatIfSimulationMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.run_what_if_simulation import (
            run_what_if_simulation,
        )

        mock_port = MagicMock()
        mock_port.get_current_replicas.return_value = 3
        mock_port.get_current_cpu_utilization.return_value = 50.0
        mock_port.get_service_topology.return_value = {}
        mock_port.get_pdb_info.return_value = {}
        mock_port.get_hpa_info.return_value = {}
        mock_port.get_dependency_graph.return_value = {}

        mock_impact = MagicMock()
        mock_impact.target_service = "test-svc"
        mock_impact.namespace = "test-ns"
        mock_impact.current_replicas = 3
        mock_impact.proposed_replicas = 5
        mock_impact.risk = 0
        mock_impact.risk_level = 0
        mock_impact.affected_services = []
        mock_impact.estimated_latency_increase_percent = 0.0
        mock_impact.error_risk = ""
        mock_impact.pdb_violation = False
        mock_impact.hpa_detected = False
        mock_impact.circular_dependency = False
        mock_impact.recommendation = ""
        mock_impact.affected_services = []

        with (
            patch(
                "hexawyn.mcp.server.build_what_if_simulation_adapter",
                return_value=mock_port,
            ),
            patch(
                "hexawyn.domain.services.simulation.what_if_scenario_simulator_service.WhatIfScenarioSimulatorService.compute_scenario",
                return_value=mock_impact,
            ),
        ):
            result = run_what_if_simulation(
                target_service="test-svc",
                namespace="test-ns",
                proposed_replicas=5,
            )

        assert isinstance(result, dict)
        assert result["error"] is None

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.run_what_if_simulation import (
            run_what_if_simulation,
        )

        with patch(
            "hexawyn.mcp.server.build_what_if_simulation_adapter",
            side_effect=RuntimeError("cluster dead"),
        ):
            result = run_what_if_simulation()

        assert isinstance(result, dict)
        assert "cluster dead" in str(result["error"])
