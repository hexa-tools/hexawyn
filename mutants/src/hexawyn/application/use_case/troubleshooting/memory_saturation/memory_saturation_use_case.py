from __future__ import annotations

from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
from hexawyn.application.use_case.troubleshooting.memory_saturation.command import (
    MemorySaturationCommand,
)
from hexawyn.application.use_case.troubleshooting.memory_saturation.mapper import (
    attach_otel_root_cause,
    predictions_to_dicts,
)
from hexawyn.application.use_case.troubleshooting.memory_saturation.response import (
    MemorySaturationResponse,
)
from hexawyn.domain.models.memory_saturation import (
    MemorySaturationRequest,
    MemorySaturationResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁMemorySaturationUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class MemorySaturationUseCase:
    @_mutmut_mutated(mutants_xǁMemorySaturationUseCaseǁ__init____mutmut)
    def __init__(self, port: MemorySaturationPort) -> None:
        self._port = port
    def xǁMemorySaturationUseCaseǁ__init____mutmut_orig(self, port: MemorySaturationPort) -> None:
        self._port = port
    def xǁMemorySaturationUseCaseǁ__init____mutmut_1(self, port: MemorySaturationPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁMemorySaturationUseCaseǁexecute__mutmut)
    def execute(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_orig(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_1(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = None
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_2(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=None,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_3(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = None
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_4(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(None)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_5(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = None

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_6(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=None, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_7(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=None)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_8(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_9(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, )

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_10(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = None
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_11(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(None):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_12(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = None
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_13(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(None, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_14(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, None)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_15(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_16(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, )
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_17(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = None

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_18(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(None, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_19(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, None)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_20(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_21(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, )

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_22(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=None,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_23(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=None,
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_24(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=None,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_25(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_26(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            safe_pod_count=result.safe_pod_count,
        )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_27(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            )

    def xǁMemorySaturationUseCaseǁexecute__mutmut_28(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(None),
            safe_pod_count=result.safe_pod_count,
        )

mutants_xǁMemorySaturationUseCaseǁ__init____mutmut['_mutmut_orig'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁ__init____mutmut['xǁMemorySaturationUseCaseǁ__init____mutmut_1'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['_mutmut_orig'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_1'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_2'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_3'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_4'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_5'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_6'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_7'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_8'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_9'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_10'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_11'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_12'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_13'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_14'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_15'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_16'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_17'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_18'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_19'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_20'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_21'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_22'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_23'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_24'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_25'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_26'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_27'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMemorySaturationUseCaseǁexecute__mutmut['xǁMemorySaturationUseCaseǁexecute__mutmut_28'] = MemorySaturationUseCase.xǁMemorySaturationUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
