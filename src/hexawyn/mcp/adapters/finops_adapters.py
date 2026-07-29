from __future__ import annotations

import os

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
from hexawyn.mcp.providers.detector import context_name


def build_cost_forecast_adapter() -> CostForecastPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_budget_projection_adapter() -> BudgetProjectionPort:
    from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
        BudgetProjectionAdapter,
    )

    return BudgetProjectionAdapter(cost_forecast_port=build_cost_forecast_adapter())


def build_cost_saving_adapter() -> CostSavingEstimationPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def build_cost_profiling_adapter() -> CostProfilingPort:
    from hexawyn.adapters.secondary.gitops.otel_cost_profiling_adapter import (
        OTelCostProfilingAdapter,
    )

    return OTelCostProfilingAdapter()


def build_optimization_roi_adapter() -> OptimizationRoiPort:
    from hexawyn.adapters.secondary.gitops.optimization_roi_adapter import (
        OptimizationRoiAdapter,
    )
    from hexawyn.adapters.secondary.gitops.optimization_roi_source import (
        EmptySprintRoiSource,
    )

    return OptimizationRoiAdapter(source=EmptySprintRoiSource())


def build_sla_report_adapter() -> SlaReportPort:
    from hexawyn.adapters.secondary.gitops.sla_report_adapter import SlaReportAdapter
    from hexawyn.adapters.secondary.gitops.sla_report_source import (
        EmptyQuarterSlaSource,
    )

    return SlaReportAdapter(source=EmptyQuarterSlaSource())


def build_platform_reliability_adapter() -> PlatformReliabilityPort:
    from hexawyn.adapters.secondary.gitops.platform_reliability_adapter import (
        PlatformReliabilityAdapter,
    )
    from hexawyn.adapters.secondary.gitops.platform_reliability_source import (
        EmptyReliabilityDataSource,
    )

    return PlatformReliabilityAdapter(source=EmptyReliabilityDataSource())


def build_incident_cost_adapter() -> IncidentCostPort:
    from hexawyn.adapters.secondary.gitops.incident_cost_adapter import (
        IncidentCostAdapter,
    )
    from hexawyn.adapters.secondary.gitops.incident_cost_source import (
        ConfigIncidentCostSource,
    )

    return IncidentCostAdapter(source=ConfigIncidentCostSource())


def build_prediction_roi_adapter() -> PredictionRoiPort:
    from hexawyn.adapters.secondary.gitops.prediction_roi_adapter import (
        PredictionRoiAdapter,
    )
    from hexawyn.adapters.secondary.gitops.prediction_roi_source import (
        ConfigPredictionRoiSource,
    )

    return PredictionRoiAdapter(source=ConfigPredictionRoiSource())


def build_budget_intelligence_adapter() -> BudgetIntelligencePort:
    from hexawyn.adapters.secondary.gitops.budget_intelligence_adapter import (
        BudgetIntelligenceAdapter,
    )
    from hexawyn.adapters.secondary.gitops.budget_intelligence_source import (
        ConfigBudgetIntelligenceSource,
    )

    return BudgetIntelligenceAdapter(source=ConfigBudgetIntelligenceSource())


def build_night_intervention_adapter() -> EngineerWorkloadPort:
    from hexawyn.adapters.secondary.gitops.night_intervention_adapter import (
        NightInterventionAdapter,
    )
    from hexawyn.adapters.secondary.gitops.night_intervention_source import (
        EmptyNightInterventionSource,
    )

    return NightInterventionAdapter(source=EmptyNightInterventionSource())


def build_disruption_risk_adapter() -> DisruptionRiskPort:
    from hexawyn.adapters.secondary.gitops.disruption_risk_adapter import (
        DisruptionRiskAdapter,
    )
    from hexawyn.adapters.secondary.gitops.disruption_risk_source import (
        EmptyDisruptionRiskSource,
    )

    return DisruptionRiskAdapter(source=EmptyDisruptionRiskSource())


def build_cost_adapter() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import AzureCostAdapter

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.adapters.secondary.vanilla.vanilla_cost_adapter import VanillaCostAdapter

    return VanillaCostAdapter()


def build_service_cost_adapter() -> ServiceCostPort:
    from hexawyn.adapters.secondary.gitops.service_cost_prometheus_adapter import (
        ServiceCostPrometheusAdapter,
    )

    return ServiceCostPrometheusAdapter()


def build_team_cost_adapter() -> TeamCostPort:
    from hexawyn.adapters.secondary.gitops.team_cost_kubernetes_adapter import (
        TeamCostKubernetesAdapter,
    )

    return TeamCostKubernetesAdapter()


def build_monthly_incident_adapter() -> MonthlyIncidentPort:
    from hexawyn.adapters.secondary.gitops.monthly_incident_adapter import (
        MonthlyIncidentAdapter,
    )

    return MonthlyIncidentAdapter()


def build_mttr_trend_adapter() -> MTTRTrendPort:
    from hexawyn.adapters.secondary.gitops.mttr_trend_adapter import (
        MTTRTrendAdapter,
    )

    return MTTRTrendAdapter()
