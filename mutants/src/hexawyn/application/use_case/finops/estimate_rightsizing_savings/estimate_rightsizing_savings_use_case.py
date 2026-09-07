from __future__ import annotations

from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort, WorkloadRawData
from hexawyn.application.use_case.finops.estimate_rightsizing_savings.command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.use_case.finops.estimate_rightsizing_savings.response import (
    EstimateRightsizingSavingsResponse,
)
from hexawyn.domain.services.rightsizing.rightsizing_analysis_service import (
    RightsizingAnalysisService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut: MutantDict = {}  # type: ignore


class EstimateRightsizingSavingsUseCase:
    @_mutmut_mutated(mutants_xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut)
    def __init__(self, rightsizing_port: RightsizingPort) -> None:
        self._port = rightsizing_port
        self._domain_service = RightsizingAnalysisService()
    def xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut_orig(self, rightsizing_port: RightsizingPort) -> None:
        self._port = rightsizing_port
        self._domain_service = RightsizingAnalysisService()
    def xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut_1(self, rightsizing_port: RightsizingPort) -> None:
        self._port = None
        self._domain_service = RightsizingAnalysisService()
    def xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut_2(self, rightsizing_port: RightsizingPort) -> None:
        self._port = rightsizing_port
        self._domain_service = None

    @_mutmut_mutated(mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut)
    def estimate_rightsizing_savings(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_orig(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_1(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = None
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_2(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = None
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_3(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(None)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_4(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = None
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_5(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=None,
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_6(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=None,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_7(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_8(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_9(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(None) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_10(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=None,  # type: ignore
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_11(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            metrics_server_available=None,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_12(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            metrics_server_available=metrics_available,
        )

    def xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_13(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,  # type: ignore
            )

mutants_xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut['_mutmut_orig'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut['xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut_1'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut['xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut_2'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['_mutmut_orig'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_1'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_2'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_3'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_4'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_5'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_6'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_7'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_7 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_8'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_8 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_9'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_9 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_10'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_10 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_11'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_11 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_12'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_12 # type: ignore # mutmut generated
mutants_xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut['xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_13'] = EstimateRightsizingSavingsUseCase.xǁEstimateRightsizingSavingsUseCaseǁestimate_rightsizing_savings__mutmut_13 # type: ignore # mutmut generated
mutants_x__any_actual_present__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__any_actual_present__mutmut)
def _any_actual_present(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        item["cpu_actual_cores"] is not None or item["memory_actual_mi"] is not None
        for item in raw_data
    )


def x__any_actual_present__mutmut_orig(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        item["cpu_actual_cores"] is not None or item["memory_actual_mi"] is not None
        for item in raw_data
    )


def x__any_actual_present__mutmut_1(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        None
    )


def x__any_actual_present__mutmut_2(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        item["cpu_actual_cores"] is not None and item["memory_actual_mi"] is not None
        for item in raw_data
    )


def x__any_actual_present__mutmut_3(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        item["XXcpu_actual_coresXX"] is not None or item["memory_actual_mi"] is not None
        for item in raw_data
    )


def x__any_actual_present__mutmut_4(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        item["CPU_ACTUAL_CORES"] is not None or item["memory_actual_mi"] is not None
        for item in raw_data
    )


def x__any_actual_present__mutmut_5(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        item["cpu_actual_cores"] is None or item["memory_actual_mi"] is not None
        for item in raw_data
    )


def x__any_actual_present__mutmut_6(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        item["cpu_actual_cores"] is not None or item["XXmemory_actual_miXX"] is not None
        for item in raw_data
    )


def x__any_actual_present__mutmut_7(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        item["cpu_actual_cores"] is not None or item["MEMORY_ACTUAL_MI"] is not None
        for item in raw_data
    )


def x__any_actual_present__mutmut_8(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        item["cpu_actual_cores"] is not None or item["memory_actual_mi"] is None
        for item in raw_data
    )

mutants_x__any_actual_present__mutmut['_mutmut_orig'] = x__any_actual_present__mutmut_orig # type: ignore # mutmut generated
mutants_x__any_actual_present__mutmut['x__any_actual_present__mutmut_1'] = x__any_actual_present__mutmut_1 # type: ignore # mutmut generated
mutants_x__any_actual_present__mutmut['x__any_actual_present__mutmut_2'] = x__any_actual_present__mutmut_2 # type: ignore # mutmut generated
mutants_x__any_actual_present__mutmut['x__any_actual_present__mutmut_3'] = x__any_actual_present__mutmut_3 # type: ignore # mutmut generated
mutants_x__any_actual_present__mutmut['x__any_actual_present__mutmut_4'] = x__any_actual_present__mutmut_4 # type: ignore # mutmut generated
mutants_x__any_actual_present__mutmut['x__any_actual_present__mutmut_5'] = x__any_actual_present__mutmut_5 # type: ignore # mutmut generated
mutants_x__any_actual_present__mutmut['x__any_actual_present__mutmut_6'] = x__any_actual_present__mutmut_6 # type: ignore # mutmut generated
mutants_x__any_actual_present__mutmut['x__any_actual_present__mutmut_7'] = x__any_actual_present__mutmut_7 # type: ignore # mutmut generated
mutants_x__any_actual_present__mutmut['x__any_actual_present__mutmut_8'] = x__any_actual_present__mutmut_8 # type: ignore # mutmut generated
