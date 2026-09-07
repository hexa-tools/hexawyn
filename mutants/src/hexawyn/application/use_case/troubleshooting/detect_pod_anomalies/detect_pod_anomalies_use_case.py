from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.pod_metrics_baseline_port import PodMetricsBaselinePort
from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.command import (
    DetectPodAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_pod_anomalies.response import (
    DetectPodAnomaliesResponse,
    ExcludedPodDict,
    PodAnomalyDict,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.pod_anomaly import ExcludedPod, PodAnomaly, PodAnomalyDetectionReport
from hexawyn.domain.services.pod_anomaly_detection.detector import detect_pod_anomalies


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectPodAnomaliesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut: MutantDict = {}  # type: ignore


class DetectPodAnomaliesUseCase:
    @_mutmut_mutated(mutants_xǁDetectPodAnomaliesUseCaseǁ__init____mutmut)
    def __init__(self, port: PodMetricsBaselinePort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port
    def xǁDetectPodAnomaliesUseCaseǁ__init____mutmut_orig(self, port: PodMetricsBaselinePort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port
    def xǁDetectPodAnomaliesUseCaseǁ__init____mutmut_1(self, port: PodMetricsBaselinePort, k8s_port: K8sPort) -> None:
        self._port = None
        self._k8s_port = k8s_port
    def xǁDetectPodAnomaliesUseCaseǁ__init____mutmut_2(self, port: PodMetricsBaselinePort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut)
    def execute(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(raw_data, baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_orig(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(raw_data, baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_1(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(None)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(raw_data, baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_2(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = None
        report = detect_pod_anomalies(raw_data, baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_3(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=None, window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(raw_data, baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_4(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=None
        )
        report = detect_pod_anomalies(raw_data, baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_5(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(raw_data, baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_6(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, )
        report = detect_pod_anomalies(raw_data, baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_7(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=command.baseline_window_days
        )
        report = None
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_8(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(None, baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_9(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(raw_data, baseline_window_days=None)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_10(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(baseline_window_days=command.baseline_window_days)
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_11(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(raw_data, )
        return _to_response(report)

    def xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_12(self, command: DetectPodAnomaliesCommand) -> DetectPodAnomaliesResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_all_pod_metrics_data(
            namespace=command.namespace, window_days=command.baseline_window_days
        )
        report = detect_pod_anomalies(raw_data, baseline_window_days=command.baseline_window_days)
        return _to_response(None)

    @_mutmut_mutated(mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut)
    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_orig(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_1(self, namespace: str) -> None:
        namespaces = None
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_2(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_3(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(None):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_4(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["XXnameXX"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_5(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["NAME"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_6(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] != namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_7(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                None, context={"namespace": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_8(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context=None
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_9(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                context={"namespace": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_10(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_11(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"XXnamespaceXX": namespace}
            )

    def xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_12(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"NAMESPACE": namespace}
            )

mutants_xǁDetectPodAnomaliesUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ__init____mutmut['xǁDetectPodAnomaliesUseCaseǁ__init____mutmut_1'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ__init____mutmut['xǁDetectPodAnomaliesUseCaseǁ__init____mutmut_2'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['_mutmut_orig'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_1'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_2'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_3'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_4'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_5'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_6'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_7'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_8'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_9'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_10'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_11'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁexecute__mutmut['xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_12'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated

mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['_mutmut_orig'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_1'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_2'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_3'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_4'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_5'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_6'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_7'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_8'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_9'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_10'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_11'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut['xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_12'] = DetectPodAnomaliesUseCase.xǁDetectPodAnomaliesUseCaseǁ_validate_namespace_exists__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=report.summary,
    )


def x__to_response__mutmut_orig(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=report.summary,
    )


def x__to_response__mutmut_1(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=None,
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=report.summary,
    )


def x__to_response__mutmut_2(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=None,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=report.summary,
    )


def x__to_response__mutmut_3(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        anomalies=None,
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=report.summary,
    )


def x__to_response__mutmut_4(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=None,
        summary=report.summary,
    )


def x__to_response__mutmut_5(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=None,
    )


def x__to_response__mutmut_6(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=report.summary,
    )


def x__to_response__mutmut_7(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=report.summary,
    )


def x__to_response__mutmut_8(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=report.summary,
    )


def x__to_response__mutmut_9(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        summary=report.summary,
    )


def x__to_response__mutmut_10(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        )


def x__to_response__mutmut_11(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(None) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(excluded) for excluded in report.excluded_pods],
        summary=report.summary,
    )


def x__to_response__mutmut_12(report: PodAnomalyDetectionReport) -> DetectPodAnomaliesResponse:
    return DetectPodAnomaliesResponse(
        namespace=report.namespace,
        total_pods=report.total_pods,
        anomalies=[_to_anomaly_dict(anomaly) for anomaly in report.anomalies],
        excluded_pods=[_to_excluded_dict(None) for excluded in report.excluded_pods],
        summary=report.summary,
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_anomaly_dict__mutmut)
def _to_anomaly_dict(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_orig(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_1(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=None,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_2(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=None,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_3(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=None,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_4(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=None,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_5(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=None,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_6(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=None,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_7(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=None,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_8(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=None,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_9(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=None,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_10(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=None,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_11(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=None,
    )


def x__to_anomaly_dict__mutmut_12(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_13(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_14(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_15(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_16(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_17(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_18(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_19(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_20(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        baseline_mean=anomaly.baseline_mean,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_21(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        note=anomaly.note,
    )


def x__to_anomaly_dict__mutmut_22(anomaly: PodAnomaly) -> PodAnomalyDict:
    return PodAnomalyDict(  # type: ignore
        pod_name=anomaly.pod_name,
        namespace=anomaly.namespace,
        metric=anomaly.metric,
        severity=anomaly.severity.value,
        deviation_pct=anomaly.deviation_pct,
        z_score=anomaly.z_score,
        isolation_forest_score=anomaly.isolation_forest_score,
        detection_method=anomaly.detection_method,
        current_value=anomaly.current_value,
        baseline_mean=anomaly.baseline_mean,
        )

mutants_x__to_anomaly_dict__mutmut['_mutmut_orig'] = x__to_anomaly_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_1'] = x__to_anomaly_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_2'] = x__to_anomaly_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_3'] = x__to_anomaly_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_4'] = x__to_anomaly_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_5'] = x__to_anomaly_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_6'] = x__to_anomaly_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_7'] = x__to_anomaly_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_8'] = x__to_anomaly_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_9'] = x__to_anomaly_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_10'] = x__to_anomaly_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_11'] = x__to_anomaly_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_12'] = x__to_anomaly_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_13'] = x__to_anomaly_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_14'] = x__to_anomaly_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_15'] = x__to_anomaly_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_16'] = x__to_anomaly_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_17'] = x__to_anomaly_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_18'] = x__to_anomaly_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_19'] = x__to_anomaly_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_20'] = x__to_anomaly_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_21'] = x__to_anomaly_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_anomaly_dict__mutmut['x__to_anomaly_dict__mutmut_22'] = x__to_anomaly_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_excluded_dict__mutmut)
def _to_excluded_dict(excluded: ExcludedPod) -> ExcludedPodDict:
    return ExcludedPodDict(  # type: ignore
        pod_name=excluded.pod_name, namespace=excluded.namespace, reason=excluded.reason
    )


def x__to_excluded_dict__mutmut_orig(excluded: ExcludedPod) -> ExcludedPodDict:
    return ExcludedPodDict(  # type: ignore
        pod_name=excluded.pod_name, namespace=excluded.namespace, reason=excluded.reason
    )


def x__to_excluded_dict__mutmut_1(excluded: ExcludedPod) -> ExcludedPodDict:
    return ExcludedPodDict(  # type: ignore
        pod_name=None, namespace=excluded.namespace, reason=excluded.reason
    )


def x__to_excluded_dict__mutmut_2(excluded: ExcludedPod) -> ExcludedPodDict:
    return ExcludedPodDict(  # type: ignore
        pod_name=excluded.pod_name, namespace=None, reason=excluded.reason
    )


def x__to_excluded_dict__mutmut_3(excluded: ExcludedPod) -> ExcludedPodDict:
    return ExcludedPodDict(  # type: ignore
        pod_name=excluded.pod_name, namespace=excluded.namespace, reason=None
    )


def x__to_excluded_dict__mutmut_4(excluded: ExcludedPod) -> ExcludedPodDict:
    return ExcludedPodDict(  # type: ignore
        namespace=excluded.namespace, reason=excluded.reason
    )


def x__to_excluded_dict__mutmut_5(excluded: ExcludedPod) -> ExcludedPodDict:
    return ExcludedPodDict(  # type: ignore
        pod_name=excluded.pod_name, reason=excluded.reason
    )


def x__to_excluded_dict__mutmut_6(excluded: ExcludedPod) -> ExcludedPodDict:
    return ExcludedPodDict(  # type: ignore
        pod_name=excluded.pod_name, namespace=excluded.namespace, )

mutants_x__to_excluded_dict__mutmut['_mutmut_orig'] = x__to_excluded_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_1'] = x__to_excluded_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_2'] = x__to_excluded_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_3'] = x__to_excluded_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_4'] = x__to_excluded_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_5'] = x__to_excluded_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_6'] = x__to_excluded_dict__mutmut_6 # type: ignore # mutmut generated
