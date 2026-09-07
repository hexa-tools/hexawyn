from __future__ import annotations

from hexawyn.application.ports.driven.cost_saving_estimation_port import (
    CostSavingEstimationPort,
)
from hexawyn.application.use_case.finops.estimate_cost_saving.command import (
    EstimateCostSavingCommand,
)
from hexawyn.application.use_case.finops.estimate_cost_saving.response import (
    EstimateCostSavingResponse,
)
from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import (
    RightSizingCostEstimationService,
)

_SIGNIFICANT_TREND_PCT = 0.10  # 10% change triggers trend flag


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁEstimateCostSavingUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut: MutantDict = {}  # type: ignore


class EstimateCostSavingUseCase:
    @_mutmut_mutated(mutants_xǁEstimateCostSavingUseCaseǁ__init____mutmut)
    def __init__(self, cost_saving_port: CostSavingEstimationPort) -> None:
        self._port = cost_saving_port
        self._domain_service = RightSizingCostEstimationService()
    def xǁEstimateCostSavingUseCaseǁ__init____mutmut_orig(self, cost_saving_port: CostSavingEstimationPort) -> None:
        self._port = cost_saving_port
        self._domain_service = RightSizingCostEstimationService()
    def xǁEstimateCostSavingUseCaseǁ__init____mutmut_1(self, cost_saving_port: CostSavingEstimationPort) -> None:
        self._port = None
        self._domain_service = RightSizingCostEstimationService()
    def xǁEstimateCostSavingUseCaseǁ__init____mutmut_2(self, cost_saving_port: CostSavingEstimationPort) -> None:
        self._port = cost_saving_port
        self._domain_service = None

    @_mutmut_mutated(mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut)
    def estimate_cost_saving(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_orig(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_1(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = None
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_2(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = None

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_3(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = None

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_4(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=None,
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_5(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=None,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_6(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=None,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_7(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=None,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_8(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_9(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_10(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_11(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_12(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(None) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_13(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = None

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_14(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(None, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_15(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, None)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_16(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_17(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, )

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_18(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_19(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(None)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_20(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=None,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_21(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=None,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_22(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=None,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_23(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            previous_total_saving_usd=previous_saving,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_24(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            saving_trend=trend,  # type: ignore
        )

    def xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_25(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,  # type: ignore
            previous_total_saving_usd=previous_saving,  # type: ignore
            )

mutants_xǁEstimateCostSavingUseCaseǁ__init____mutmut['_mutmut_orig'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁ__init____mutmut['xǁEstimateCostSavingUseCaseǁ__init____mutmut_1'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁ__init____mutmut['xǁEstimateCostSavingUseCaseǁ__init____mutmut_2'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['_mutmut_orig'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_1'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_2'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_3'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_4'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_5'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_6'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_7'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_7 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_8'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_8 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_9'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_9 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_10'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_10 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_11'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_11 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_12'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_12 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_13'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_13 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_14'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_14 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_15'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_15 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_16'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_16 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_17'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_17 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_18'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_18 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_19'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_19 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_20'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_20 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_21'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_21 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_22'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_22 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_23'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_23 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_24'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_24 # type: ignore # mutmut generated
mutants_xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut['xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_25'] = EstimateCostSavingUseCase.xǁEstimateCostSavingUseCaseǁestimate_cost_saving__mutmut_25 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_trend__mutmut)
def _compute_trend(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_orig(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_1(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None and previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_2(previous: float | None, current: float | None) -> str | None:
    if previous is None and current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_3(previous: float | None, current: float | None) -> str | None:
    if previous is not None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_4(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is not None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_5(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous != 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_6(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 1:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_7(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = None
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_8(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) * previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_9(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current + previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_10(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct >= _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_11(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "XXincreasingXX"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_12(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "INCREASING"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_13(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct <= -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_14(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < +_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x__compute_trend__mutmut_15(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "XXdecreasingXX"
    return "stable"


def x__compute_trend__mutmut_16(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "DECREASING"
    return "stable"


def x__compute_trend__mutmut_17(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "XXstableXX"


def x__compute_trend__mutmut_18(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "STABLE"

mutants_x__compute_trend__mutmut['_mutmut_orig'] = x__compute_trend__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_1'] = x__compute_trend__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_2'] = x__compute_trend__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_3'] = x__compute_trend__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_4'] = x__compute_trend__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_5'] = x__compute_trend__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_6'] = x__compute_trend__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_7'] = x__compute_trend__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_8'] = x__compute_trend__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_9'] = x__compute_trend__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_10'] = x__compute_trend__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_11'] = x__compute_trend__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_12'] = x__compute_trend__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_13'] = x__compute_trend__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_14'] = x__compute_trend__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_15'] = x__compute_trend__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_16'] = x__compute_trend__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_17'] = x__compute_trend__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_18'] = x__compute_trend__mutmut_18 # type: ignore # mutmut generated
