from __future__ import annotations

from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.command import (
    DetectLogAnomaliesCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_log_anomalies.response import (
    DetectLogAnomaliesResponse,
    LogAnomalyDict,
)
from hexawyn.domain.models.analyze_pod_logs import AnalyzePodLogsRequest
from hexawyn.domain.models.log_anomaly import DetectLogAnomaliesRequest, DetectLogAnomaliesResult
from hexawyn.domain.services.log_analysis.log_anomaly_detector import detect_log_anomalies


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectLogAnomaliesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DetectLogAnomaliesUseCase:
    @_mutmut_mutated(mutants_xǁDetectLogAnomaliesUseCaseǁ__init____mutmut)
    def __init__(self, port: PodLogsPort) -> None:
        self._port = port
    def xǁDetectLogAnomaliesUseCaseǁ__init____mutmut_orig(self, port: PodLogsPort) -> None:
        self._port = port
    def xǁDetectLogAnomaliesUseCaseǁ__init____mutmut_1(self, port: PodLogsPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut)
    def execute(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_orig(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_1(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = None
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_2(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=None,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_3(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=None,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_4(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=None,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_5(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_6(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_7(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_8(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = None

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_9(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(None)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_10(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = None
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_11(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=None,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_12(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=None,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_13(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=None,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_14(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=None,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_15(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_16(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_17(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_18(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_19(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = None
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_20(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(None, log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_21(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, None)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_22(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(log_lines)
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_23(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, )
        return _to_response(result)

    def xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_24(self, command: DetectLogAnomaliesCommand) -> DetectLogAnomaliesResponse:
        fetch_request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(fetch_request)

        request = DetectLogAnomaliesRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            zscore_threshold=command.zscore_threshold,
        )
        result = detect_log_anomalies(request, log_lines)
        return _to_response(None)

mutants_xǁDetectLogAnomaliesUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁ__init____mutmut['xǁDetectLogAnomaliesUseCaseǁ__init____mutmut_1'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['_mutmut_orig'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_1'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_2'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_3'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_4'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_5'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_6'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_7'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_8'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_9'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_10'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_11'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_12'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_13'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_14'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_15'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_16'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_17'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_18'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_19'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_20'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_21'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_22'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_23'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDetectLogAnomaliesUseCaseǁexecute__mutmut['xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_24'] = DetectLogAnomaliesUseCase.xǁDetectLogAnomaliesUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_orig(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_1(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=None,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_2(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=None,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_3(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=None,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_4(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=None,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_5(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=None,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_6(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=None,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_7(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=None,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_8(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=None,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_9(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=None,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_10(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=None,
    )


def x__to_response__mutmut_11(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_12(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_13(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_14(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_15(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_16(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_17(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_18(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_19(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_20(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        )


def x__to_response__mutmut_21(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=None,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_22(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=None,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_23(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=None,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_24(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=None,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_25(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=None,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_26(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_27(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                anomaly_score=a.anomaly_score,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_28(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                type=a.type,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_29(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                low_confidence=a.low_confidence,
            )
            for a in result.anomalies
        ],
    )


def x__to_response__mutmut_30(result: DetectLogAnomaliesResult) -> DetectLogAnomaliesResponse:
    return DetectLogAnomaliesResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        baseline_mean_lines_per_minute=result.baseline_mean_lines_per_minute,
        baseline_std_dev=result.baseline_std_dev,
        summary=result.summary,
        insufficient_data=result.insufficient_data,
        formats_analyzed_separately=result.formats_analyzed_separately,  # type: ignore
        anomalies=[
            LogAnomalyDict(  # type: ignore
                timestamp=a.timestamp,
                log_line=a.log_line,
                anomaly_score=a.anomaly_score,
                type=a.type,
                )
            for a in result.anomalies
        ],
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
mutants_x__to_response__mutmut['x__to_response__mutmut_13'] = x__to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_14'] = x__to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_15'] = x__to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_16'] = x__to_response__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_17'] = x__to_response__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_18'] = x__to_response__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_19'] = x__to_response__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_20'] = x__to_response__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_21'] = x__to_response__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_22'] = x__to_response__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_23'] = x__to_response__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_24'] = x__to_response__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_25'] = x__to_response__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_26'] = x__to_response__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_27'] = x__to_response__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_28'] = x__to_response__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_29'] = x__to_response__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_30'] = x__to_response__mutmut_30 # type: ignore # mutmut generated
