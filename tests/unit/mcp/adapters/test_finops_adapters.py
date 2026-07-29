"""Unit tests for mcp/adapters/finops_adapters.py — every build_*_adapter() function."""

from __future__ import annotations

from hexawyn.application.ports.driven.budget_intelligence_port import BudgetIntelligencePort
from hexawyn.application.ports.driven.budget_projection_port import BudgetProjectionPort
from hexawyn.application.ports.driven.cost_estimation_port import CostEstimationPort
from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort
from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
from hexawyn.application.ports.driven.cost_saving_estimation_port import (
    CostSavingEstimationPort,
)
from hexawyn.application.ports.driven.disruption_risk_port import DisruptionRiskPort
from hexawyn.application.ports.driven.engineer_workload_port import EngineerWorkloadPort
from hexawyn.application.ports.driven.incident_cost_port import IncidentCostPort
from hexawyn.application.ports.driven.monthly_incident_port import MonthlyIncidentPort
from hexawyn.application.ports.driven.mttr_trend_port import MTTRTrendPort
from hexawyn.application.ports.driven.optimization_roi_port import OptimizationRoiPort
from hexawyn.application.ports.driven.platform_reliability_port import PlatformReliabilityPort
from hexawyn.application.ports.driven.prediction_roi_port import PredictionRoiPort
from hexawyn.application.ports.driven.service_cost_port import ServiceCostPort
from hexawyn.application.ports.driven.sla_report_port import SlaReportPort
from hexawyn.application.ports.driven.team_cost_port import TeamCostPort


class TestFinopsAdapters:
    """Verify each builder returns the correct port type."""

    def test_build_cost_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import build_cost_adapter

        result = build_cost_adapter()
        assert isinstance(result, CostEstimationPort)

    def test_build_cost_forecast_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_cost_forecast_adapter,
        )

        result = build_cost_forecast_adapter()
        assert isinstance(result, CostForecastPort)

    def test_build_cost_saving_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import build_cost_saving_adapter

        result = build_cost_saving_adapter()
        assert isinstance(result, CostSavingEstimationPort)

    def test_build_cost_profiling_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_cost_profiling_adapter,
        )

        result = build_cost_profiling_adapter()
        assert isinstance(result, CostProfilingPort)

    def test_build_team_cost_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import build_team_cost_adapter

        result = build_team_cost_adapter()
        assert isinstance(result, TeamCostPort)

    def test_build_service_cost_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import build_service_cost_adapter

        result = build_service_cost_adapter()
        assert isinstance(result, ServiceCostPort)

    def test_build_monthly_incident_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_monthly_incident_adapter,
        )

        result = build_monthly_incident_adapter()
        assert isinstance(result, MonthlyIncidentPort)

    def test_build_mttr_trend_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import build_mttr_trend_adapter

        result = build_mttr_trend_adapter()
        assert isinstance(result, MTTRTrendPort)

    def test_build_budget_projection_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_budget_projection_adapter,
        )

        result = build_budget_projection_adapter()
        assert isinstance(result, BudgetProjectionPort)

    def test_build_budget_intelligence_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_budget_intelligence_adapter,
        )

        result = build_budget_intelligence_adapter()
        assert isinstance(result, BudgetIntelligencePort)

    def test_build_optimization_roi_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_optimization_roi_adapter,
        )

        result = build_optimization_roi_adapter()
        assert isinstance(result, OptimizationRoiPort)

    def test_build_incident_cost_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_incident_cost_adapter,
        )

        result = build_incident_cost_adapter()
        assert isinstance(result, IncidentCostPort)

    def test_build_prediction_roi_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_prediction_roi_adapter,
        )

        result = build_prediction_roi_adapter()
        assert isinstance(result, PredictionRoiPort)

    def test_build_sla_report_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import build_sla_report_adapter

        result = build_sla_report_adapter()
        assert isinstance(result, SlaReportPort)

    def test_build_platform_reliability_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_platform_reliability_adapter,
        )

        result = build_platform_reliability_adapter()
        assert isinstance(result, PlatformReliabilityPort)

    def test_build_night_intervention_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_night_intervention_adapter,
        )

        result = build_night_intervention_adapter()
        assert isinstance(result, EngineerWorkloadPort)

    def test_build_disruption_risk_adapter_returns_port(self) -> None:
        from hexawyn.mcp.adapters.finops_adapters import (
            build_disruption_risk_adapter,
        )

        result = build_disruption_risk_adapter()
        assert isinstance(result, DisruptionRiskPort)
