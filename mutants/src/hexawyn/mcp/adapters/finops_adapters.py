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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_cost_forecast_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cost_forecast_adapter__mutmut)
def build_cost_forecast_adapter() -> CostForecastPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_cost_forecast_adapter__mutmut_orig() -> CostForecastPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_cost_forecast_adapter__mutmut_1() -> CostForecastPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_cost_forecast_adapter__mutmut_2() -> CostForecastPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name == "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_cost_forecast_adapter__mutmut_3() -> CostForecastPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "XXunknownXX" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_cost_forecast_adapter__mutmut_4() -> CostForecastPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "UNKNOWN" else None
    return VanillaAdapter(cluster_name=context or "default")


def x_build_cost_forecast_adapter__mutmut_5() -> CostForecastPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=None)


def x_build_cost_forecast_adapter__mutmut_6() -> CostForecastPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context and "default")


def x_build_cost_forecast_adapter__mutmut_7() -> CostForecastPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "XXdefaultXX")


def x_build_cost_forecast_adapter__mutmut_8() -> CostForecastPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "DEFAULT")

mutants_x_build_cost_forecast_adapter__mutmut['_mutmut_orig'] = x_build_cost_forecast_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cost_forecast_adapter__mutmut['x_build_cost_forecast_adapter__mutmut_1'] = x_build_cost_forecast_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cost_forecast_adapter__mutmut['x_build_cost_forecast_adapter__mutmut_2'] = x_build_cost_forecast_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_cost_forecast_adapter__mutmut['x_build_cost_forecast_adapter__mutmut_3'] = x_build_cost_forecast_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_cost_forecast_adapter__mutmut['x_build_cost_forecast_adapter__mutmut_4'] = x_build_cost_forecast_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_cost_forecast_adapter__mutmut['x_build_cost_forecast_adapter__mutmut_5'] = x_build_cost_forecast_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_cost_forecast_adapter__mutmut['x_build_cost_forecast_adapter__mutmut_6'] = x_build_cost_forecast_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_cost_forecast_adapter__mutmut['x_build_cost_forecast_adapter__mutmut_7'] = x_build_cost_forecast_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_cost_forecast_adapter__mutmut['x_build_cost_forecast_adapter__mutmut_8'] = x_build_cost_forecast_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_budget_projection_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_budget_projection_adapter__mutmut)
def build_budget_projection_adapter() -> BudgetProjectionPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.budget_projection_adapter import (
        BudgetProjectionAdapter,
    )

    return BudgetProjectionAdapter(cost_forecast_port=build_cost_forecast_adapter())


def x_build_budget_projection_adapter__mutmut_orig() -> BudgetProjectionPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.budget_projection_adapter import (
        BudgetProjectionAdapter,
    )

    return BudgetProjectionAdapter(cost_forecast_port=build_cost_forecast_adapter())


def x_build_budget_projection_adapter__mutmut_1() -> BudgetProjectionPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.budget_projection_adapter import (
        BudgetProjectionAdapter,
    )

    return BudgetProjectionAdapter(cost_forecast_port=None)

mutants_x_build_budget_projection_adapter__mutmut['_mutmut_orig'] = x_build_budget_projection_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_budget_projection_adapter__mutmut['x_build_budget_projection_adapter__mutmut_1'] = x_build_budget_projection_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cost_saving_adapter__mutmut)
def build_cost_saving_adapter() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_orig() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_1() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_2() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name == "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_3() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "XXunknownXX" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_4() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "UNKNOWN" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_5() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = None
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_6() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get(None, "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_7() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", None)
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_8() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_9() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", )
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_10() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("XXPROMETHEUS_URLXX", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_11() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("prometheus_url", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_12() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "XXXX")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_13() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=None, prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_14() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=None)


def x_build_cost_saving_adapter__mutmut_15() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_16() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", )


def x_build_cost_saving_adapter__mutmut_17() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context and "default", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_18() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "XXdefaultXX", prometheus_url=prometheus_url)


def x_build_cost_saving_adapter__mutmut_19() -> CostSavingEstimationPort:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "DEFAULT", prometheus_url=prometheus_url)

mutants_x_build_cost_saving_adapter__mutmut['_mutmut_orig'] = x_build_cost_saving_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_1'] = x_build_cost_saving_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_2'] = x_build_cost_saving_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_3'] = x_build_cost_saving_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_4'] = x_build_cost_saving_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_5'] = x_build_cost_saving_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_6'] = x_build_cost_saving_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_7'] = x_build_cost_saving_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_8'] = x_build_cost_saving_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_9'] = x_build_cost_saving_adapter__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_10'] = x_build_cost_saving_adapter__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_11'] = x_build_cost_saving_adapter__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_12'] = x_build_cost_saving_adapter__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_13'] = x_build_cost_saving_adapter__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_14'] = x_build_cost_saving_adapter__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_15'] = x_build_cost_saving_adapter__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_16'] = x_build_cost_saving_adapter__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_17'] = x_build_cost_saving_adapter__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_18'] = x_build_cost_saving_adapter__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_cost_saving_adapter__mutmut['x_build_cost_saving_adapter__mutmut_19'] = x_build_cost_saving_adapter__mutmut_19 # type: ignore # mutmut generated


def build_cost_profiling_adapter() -> CostProfilingPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_cost_profiling_adapter import (
        OTelCostProfilingAdapter,
    )

    return OTelCostProfilingAdapter()
mutants_x_build_optimization_roi_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_optimization_roi_adapter__mutmut)
def build_optimization_roi_adapter() -> OptimizationRoiPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.optimization_roi_adapter import (
        OptimizationRoiAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.optimization_roi_source import (
        EmptySprintRoiSource,
    )

    return OptimizationRoiAdapter(source=EmptySprintRoiSource())


def x_build_optimization_roi_adapter__mutmut_orig() -> OptimizationRoiPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.optimization_roi_adapter import (
        OptimizationRoiAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.optimization_roi_source import (
        EmptySprintRoiSource,
    )

    return OptimizationRoiAdapter(source=EmptySprintRoiSource())


def x_build_optimization_roi_adapter__mutmut_1() -> OptimizationRoiPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.optimization_roi_adapter import (
        OptimizationRoiAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.optimization_roi_source import (
        EmptySprintRoiSource,
    )

    return OptimizationRoiAdapter(source=None)

mutants_x_build_optimization_roi_adapter__mutmut['_mutmut_orig'] = x_build_optimization_roi_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_optimization_roi_adapter__mutmut['x_build_optimization_roi_adapter__mutmut_1'] = x_build_optimization_roi_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_sla_report_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_sla_report_adapter__mutmut)
def build_sla_report_adapter() -> SlaReportPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.sla_report_adapter import SlaReportAdapter
    from hexawyn.infrastructure.adapters.secondary.gitops.sla_report_source import (
        EmptyQuarterSlaSource,
    )

    return SlaReportAdapter(source=EmptyQuarterSlaSource())


def x_build_sla_report_adapter__mutmut_orig() -> SlaReportPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.sla_report_adapter import SlaReportAdapter
    from hexawyn.infrastructure.adapters.secondary.gitops.sla_report_source import (
        EmptyQuarterSlaSource,
    )

    return SlaReportAdapter(source=EmptyQuarterSlaSource())


def x_build_sla_report_adapter__mutmut_1() -> SlaReportPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.sla_report_adapter import SlaReportAdapter
    from hexawyn.infrastructure.adapters.secondary.gitops.sla_report_source import (
        EmptyQuarterSlaSource,
    )

    return SlaReportAdapter(source=None)

mutants_x_build_sla_report_adapter__mutmut['_mutmut_orig'] = x_build_sla_report_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_sla_report_adapter__mutmut['x_build_sla_report_adapter__mutmut_1'] = x_build_sla_report_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_platform_reliability_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_platform_reliability_adapter__mutmut)
def build_platform_reliability_adapter() -> PlatformReliabilityPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.platform_reliability_adapter import (
        PlatformReliabilityAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.platform_reliability_source import (
        EmptyReliabilityDataSource,
    )

    return PlatformReliabilityAdapter(source=EmptyReliabilityDataSource())


def x_build_platform_reliability_adapter__mutmut_orig() -> PlatformReliabilityPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.platform_reliability_adapter import (
        PlatformReliabilityAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.platform_reliability_source import (
        EmptyReliabilityDataSource,
    )

    return PlatformReliabilityAdapter(source=EmptyReliabilityDataSource())


def x_build_platform_reliability_adapter__mutmut_1() -> PlatformReliabilityPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.platform_reliability_adapter import (
        PlatformReliabilityAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.platform_reliability_source import (
        EmptyReliabilityDataSource,
    )

    return PlatformReliabilityAdapter(source=None)

mutants_x_build_platform_reliability_adapter__mutmut['_mutmut_orig'] = x_build_platform_reliability_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_platform_reliability_adapter__mutmut['x_build_platform_reliability_adapter__mutmut_1'] = x_build_platform_reliability_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_incident_cost_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_incident_cost_adapter__mutmut)
def build_incident_cost_adapter() -> IncidentCostPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.incident_cost_adapter import (
        IncidentCostAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.incident_cost_source import (
        ConfigIncidentCostSource,
    )

    return IncidentCostAdapter(source=ConfigIncidentCostSource())


def x_build_incident_cost_adapter__mutmut_orig() -> IncidentCostPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.incident_cost_adapter import (
        IncidentCostAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.incident_cost_source import (
        ConfigIncidentCostSource,
    )

    return IncidentCostAdapter(source=ConfigIncidentCostSource())


def x_build_incident_cost_adapter__mutmut_1() -> IncidentCostPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.incident_cost_adapter import (
        IncidentCostAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.incident_cost_source import (
        ConfigIncidentCostSource,
    )

    return IncidentCostAdapter(source=None)

mutants_x_build_incident_cost_adapter__mutmut['_mutmut_orig'] = x_build_incident_cost_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_incident_cost_adapter__mutmut['x_build_incident_cost_adapter__mutmut_1'] = x_build_incident_cost_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_prediction_roi_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_prediction_roi_adapter__mutmut)
def build_prediction_roi_adapter() -> PredictionRoiPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prediction_roi_adapter import (
        PredictionRoiAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.prediction_roi_source import (
        ConfigPredictionRoiSource,
    )

    return PredictionRoiAdapter(source=ConfigPredictionRoiSource())


def x_build_prediction_roi_adapter__mutmut_orig() -> PredictionRoiPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prediction_roi_adapter import (
        PredictionRoiAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.prediction_roi_source import (
        ConfigPredictionRoiSource,
    )

    return PredictionRoiAdapter(source=ConfigPredictionRoiSource())


def x_build_prediction_roi_adapter__mutmut_1() -> PredictionRoiPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prediction_roi_adapter import (
        PredictionRoiAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.prediction_roi_source import (
        ConfigPredictionRoiSource,
    )

    return PredictionRoiAdapter(source=None)

mutants_x_build_prediction_roi_adapter__mutmut['_mutmut_orig'] = x_build_prediction_roi_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_prediction_roi_adapter__mutmut['x_build_prediction_roi_adapter__mutmut_1'] = x_build_prediction_roi_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_budget_intelligence_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_budget_intelligence_adapter__mutmut)
def build_budget_intelligence_adapter() -> BudgetIntelligencePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.budget_intelligence_adapter import (
        BudgetIntelligenceAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.budget_intelligence_source import (
        ConfigBudgetIntelligenceSource,
    )

    return BudgetIntelligenceAdapter(source=ConfigBudgetIntelligenceSource())


def x_build_budget_intelligence_adapter__mutmut_orig() -> BudgetIntelligencePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.budget_intelligence_adapter import (
        BudgetIntelligenceAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.budget_intelligence_source import (
        ConfigBudgetIntelligenceSource,
    )

    return BudgetIntelligenceAdapter(source=ConfigBudgetIntelligenceSource())


def x_build_budget_intelligence_adapter__mutmut_1() -> BudgetIntelligencePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.budget_intelligence_adapter import (
        BudgetIntelligenceAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.budget_intelligence_source import (
        ConfigBudgetIntelligenceSource,
    )

    return BudgetIntelligenceAdapter(source=None)

mutants_x_build_budget_intelligence_adapter__mutmut['_mutmut_orig'] = x_build_budget_intelligence_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_budget_intelligence_adapter__mutmut['x_build_budget_intelligence_adapter__mutmut_1'] = x_build_budget_intelligence_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_night_intervention_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_night_intervention_adapter__mutmut)
def build_night_intervention_adapter() -> EngineerWorkloadPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.night_intervention_adapter import (
        NightInterventionAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.night_intervention_source import (
        EmptyNightInterventionSource,
    )

    return NightInterventionAdapter(source=EmptyNightInterventionSource())


def x_build_night_intervention_adapter__mutmut_orig() -> EngineerWorkloadPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.night_intervention_adapter import (
        NightInterventionAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.night_intervention_source import (
        EmptyNightInterventionSource,
    )

    return NightInterventionAdapter(source=EmptyNightInterventionSource())


def x_build_night_intervention_adapter__mutmut_1() -> EngineerWorkloadPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.night_intervention_adapter import (
        NightInterventionAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.night_intervention_source import (
        EmptyNightInterventionSource,
    )

    return NightInterventionAdapter(source=None)

mutants_x_build_night_intervention_adapter__mutmut['_mutmut_orig'] = x_build_night_intervention_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_night_intervention_adapter__mutmut['x_build_night_intervention_adapter__mutmut_1'] = x_build_night_intervention_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_disruption_risk_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_disruption_risk_adapter__mutmut)
def build_disruption_risk_adapter() -> DisruptionRiskPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.disruption_risk_adapter import (
        DisruptionRiskAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.disruption_risk_source import (
        EmptyDisruptionRiskSource,
    )

    return DisruptionRiskAdapter(source=EmptyDisruptionRiskSource())


def x_build_disruption_risk_adapter__mutmut_orig() -> DisruptionRiskPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.disruption_risk_adapter import (
        DisruptionRiskAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.disruption_risk_source import (
        EmptyDisruptionRiskSource,
    )

    return DisruptionRiskAdapter(source=EmptyDisruptionRiskSource())


def x_build_disruption_risk_adapter__mutmut_1() -> DisruptionRiskPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.disruption_risk_adapter import (
        DisruptionRiskAdapter,
    )
    from hexawyn.infrastructure.adapters.secondary.gitops.disruption_risk_source import (
        EmptyDisruptionRiskSource,
    )

    return DisruptionRiskAdapter(source=None)

mutants_x_build_disruption_risk_adapter__mutmut['_mutmut_orig'] = x_build_disruption_risk_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_disruption_risk_adapter__mutmut['x_build_disruption_risk_adapter__mutmut_1'] = x_build_disruption_risk_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cost_adapter__mutmut)
def build_cost_adapter() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_orig() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_1() -> CostEstimationPort:
    provider = None
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_2() -> CostEstimationPort:
    provider = context_name and ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_3() -> CostEstimationPort:
    provider = context_name or "XXXX"
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_4() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = None

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_5() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.upper()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_6() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower and provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_7() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "XXeksXX" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_8() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "EKS" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_9() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" not in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_10() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower != "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_11() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "XXawsXX":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_12() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "AWS":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_13() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region=None)
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_14() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="XXus-east-1XX")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_15() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="US-EAST-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_16() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower and provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_17() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "XXaksXX" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_18() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "AKS" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_19() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" not in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_20() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower != "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_21() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "XXazureXX":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_22() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "AZURE":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_23() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id=None)
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_24() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="XXunknownXX")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_25() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="UNKNOWN")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_26() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower and provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_27() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "XXgkeXX" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_28() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "GKE" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_29() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" not in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_30() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower != "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_31() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "XXgcpXX":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_32() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "GCP":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_33() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id=None)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_34() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="XXunknownXX")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()


def x_build_cost_adapter__mutmut_35() -> CostEstimationPort:
    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.infrastructure.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.infrastructure.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.infrastructure.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="UNKNOWN")

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_cost_adapter import (
        VanillaCostAdapter,
    )

    return VanillaCostAdapter()

mutants_x_build_cost_adapter__mutmut['_mutmut_orig'] = x_build_cost_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_1'] = x_build_cost_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_2'] = x_build_cost_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_3'] = x_build_cost_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_4'] = x_build_cost_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_5'] = x_build_cost_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_6'] = x_build_cost_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_7'] = x_build_cost_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_8'] = x_build_cost_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_9'] = x_build_cost_adapter__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_10'] = x_build_cost_adapter__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_11'] = x_build_cost_adapter__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_12'] = x_build_cost_adapter__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_13'] = x_build_cost_adapter__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_14'] = x_build_cost_adapter__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_15'] = x_build_cost_adapter__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_16'] = x_build_cost_adapter__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_17'] = x_build_cost_adapter__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_18'] = x_build_cost_adapter__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_19'] = x_build_cost_adapter__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_20'] = x_build_cost_adapter__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_21'] = x_build_cost_adapter__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_22'] = x_build_cost_adapter__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_23'] = x_build_cost_adapter__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_24'] = x_build_cost_adapter__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_25'] = x_build_cost_adapter__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_26'] = x_build_cost_adapter__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_27'] = x_build_cost_adapter__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_28'] = x_build_cost_adapter__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_29'] = x_build_cost_adapter__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_30'] = x_build_cost_adapter__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_31'] = x_build_cost_adapter__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_32'] = x_build_cost_adapter__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_33'] = x_build_cost_adapter__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_34'] = x_build_cost_adapter__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_cost_adapter__mutmut['x_build_cost_adapter__mutmut_35'] = x_build_cost_adapter__mutmut_35 # type: ignore # mutmut generated


def build_service_cost_adapter() -> ServiceCostPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.service_cost_prometheus_adapter import (
        ServiceCostPrometheusAdapter,
    )

    return ServiceCostPrometheusAdapter()


def build_team_cost_adapter() -> TeamCostPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.team_cost_kubernetes_adapter import (
        TeamCostKubernetesAdapter,
    )

    return TeamCostKubernetesAdapter()


def build_monthly_incident_adapter() -> MonthlyIncidentPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.monthly_incident_adapter import (
        MonthlyIncidentAdapter,
    )

    return MonthlyIncidentAdapter()


def build_mttr_trend_adapter() -> MTTRTrendPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.mttr_trend_adapter import (
        MTTRTrendAdapter,
    )

    return MTTRTrendAdapter()
