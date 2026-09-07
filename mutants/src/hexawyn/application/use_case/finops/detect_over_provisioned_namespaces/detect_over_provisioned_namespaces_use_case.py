from hexawyn.application.ports.driven.namespace_waste_port import (
    NamespaceRawData,
    NamespaceWasteAnalysisPort,
)
from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.response import (
    DetectOverProvisionedNamespacesResponse,
)
from hexawyn.domain.services.namespace_waste.namespace_over_provisioning_service import (
    NamespaceOverProvisioningService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut: MutantDict = {}  # type: ignore


class DetectOverProvisionedNamespacesUseCase:
    """Orchestrates K8s+Prometheus data fetch and domain-level waste analysis."""

    @_mutmut_mutated(mutants_xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut)
    def __init__(self, waste_port: NamespaceWasteAnalysisPort) -> None:
        self._waste_port = waste_port
        self._domain_service = NamespaceOverProvisioningService()

    def xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut_orig(self, waste_port: NamespaceWasteAnalysisPort) -> None:
        self._waste_port = waste_port
        self._domain_service = NamespaceOverProvisioningService()

    def xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut_1(self, waste_port: NamespaceWasteAnalysisPort) -> None:
        self._waste_port = None
        self._domain_service = NamespaceOverProvisioningService()

    def xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut_2(self, waste_port: NamespaceWasteAnalysisPort) -> None:
        self._waste_port = waste_port
        self._domain_service = None

    @_mutmut_mutated(mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut)
    def detect_over_provisioned_namespaces(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_orig(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_1(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = None
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_2(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=None
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_3(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = None
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_4(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(None)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_5(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = None
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_6(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=None,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_7(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=None,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_8(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=None,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_9(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_10(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_11(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_12(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=None,
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_13(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=None,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_14(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            prometheus_available=prometheus_available,
        )

    def xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_15(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            )

mutants_xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut_1'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut_2'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['_mutmut_orig'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_1'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_2'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_3'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_4'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_5'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_6'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_7'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_8'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_9'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_10'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_11'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_12'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_13'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_14'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut['xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_15'] = DetectOverProvisionedNamespacesUseCase.xǁDetectOverProvisionedNamespacesUseCaseǁdetect_over_provisioned_namespaces__mutmut_15 # type: ignore # mutmut generated
mutants_x__any_actual_usage_present__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__any_actual_usage_present__mutmut)
def _any_actual_usage_present(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        item["cpu_actual_avg_cores"] is not None or item["memory_actual_avg_gb"] is not None
        for item in raw_data
    )


def x__any_actual_usage_present__mutmut_orig(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        item["cpu_actual_avg_cores"] is not None or item["memory_actual_avg_gb"] is not None
        for item in raw_data
    )


def x__any_actual_usage_present__mutmut_1(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        None
    )


def x__any_actual_usage_present__mutmut_2(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        item["cpu_actual_avg_cores"] is not None and item["memory_actual_avg_gb"] is not None
        for item in raw_data
    )


def x__any_actual_usage_present__mutmut_3(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        item["XXcpu_actual_avg_coresXX"] is not None or item["memory_actual_avg_gb"] is not None
        for item in raw_data
    )


def x__any_actual_usage_present__mutmut_4(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        item["CPU_ACTUAL_AVG_CORES"] is not None or item["memory_actual_avg_gb"] is not None
        for item in raw_data
    )


def x__any_actual_usage_present__mutmut_5(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        item["cpu_actual_avg_cores"] is None or item["memory_actual_avg_gb"] is not None
        for item in raw_data
    )


def x__any_actual_usage_present__mutmut_6(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        item["cpu_actual_avg_cores"] is not None or item["XXmemory_actual_avg_gbXX"] is not None
        for item in raw_data
    )


def x__any_actual_usage_present__mutmut_7(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        item["cpu_actual_avg_cores"] is not None or item["MEMORY_ACTUAL_AVG_GB"] is not None
        for item in raw_data
    )


def x__any_actual_usage_present__mutmut_8(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        item["cpu_actual_avg_cores"] is not None or item["memory_actual_avg_gb"] is None
        for item in raw_data
    )

mutants_x__any_actual_usage_present__mutmut['_mutmut_orig'] = x__any_actual_usage_present__mutmut_orig # type: ignore # mutmut generated
mutants_x__any_actual_usage_present__mutmut['x__any_actual_usage_present__mutmut_1'] = x__any_actual_usage_present__mutmut_1 # type: ignore # mutmut generated
mutants_x__any_actual_usage_present__mutmut['x__any_actual_usage_present__mutmut_2'] = x__any_actual_usage_present__mutmut_2 # type: ignore # mutmut generated
mutants_x__any_actual_usage_present__mutmut['x__any_actual_usage_present__mutmut_3'] = x__any_actual_usage_present__mutmut_3 # type: ignore # mutmut generated
mutants_x__any_actual_usage_present__mutmut['x__any_actual_usage_present__mutmut_4'] = x__any_actual_usage_present__mutmut_4 # type: ignore # mutmut generated
mutants_x__any_actual_usage_present__mutmut['x__any_actual_usage_present__mutmut_5'] = x__any_actual_usage_present__mutmut_5 # type: ignore # mutmut generated
mutants_x__any_actual_usage_present__mutmut['x__any_actual_usage_present__mutmut_6'] = x__any_actual_usage_present__mutmut_6 # type: ignore # mutmut generated
mutants_x__any_actual_usage_present__mutmut['x__any_actual_usage_present__mutmut_7'] = x__any_actual_usage_present__mutmut_7 # type: ignore # mutmut generated
mutants_x__any_actual_usage_present__mutmut['x__any_actual_usage_present__mutmut_8'] = x__any_actual_usage_present__mutmut_8 # type: ignore # mutmut generated
