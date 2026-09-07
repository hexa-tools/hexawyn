"""CalicoFelixMetricsUseCase — per-policy Felix allow/deny counters."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_felix_metrics.command import (
    CalicoFelixMetricsCommand,
)
from hexawyn.application.use_case.calico.calico_felix_metrics.response import (
    CalicoFelixMetricsResponse,
)
from hexawyn.domain.services.calico.felix_metrics_service import (
    build_calico_felix_metrics_result,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCalicoFelixMetricsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CalicoFelixMetricsUseCase:
    """Orchestrates Felix metrics — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁCalicoFelixMetricsUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoFelixMetricsUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoFelixMetricsUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut)
    def execute(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_orig(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_1(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = None
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_2(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_3(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=None,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_4(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=None,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_5(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=None,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_6(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=None,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_7(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_8(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_9(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_10(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_11(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=True,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_12(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=True,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_13(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = None
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_14(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = None
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_15(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=None, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_16(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=None)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_17(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_18(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, )
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_19(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=None,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_20(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=None,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_21(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=None,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_22(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=None,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_23(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=None,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_24(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=None,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_25(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=None,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_26(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=None,
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_27(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=None,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_28(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_29(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_30(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_31(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_32(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_33(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_34(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            policies=list(result.policies),
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_35(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            error=result.error,
        )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_36(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            )

    def xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_37(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(None),
            error=result.error,
        )

mutants_xǁCalicoFelixMetricsUseCaseǁ__init____mutmut['_mutmut_orig'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁ__init____mutmut['xǁCalicoFelixMetricsUseCaseǁ__init____mutmut_1'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['_mutmut_orig'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_1'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_2'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_3'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_4'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_5'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_6'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_7'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_8'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_9'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_10'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_11'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_12'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_13'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_14'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_15'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_16'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_17'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_18'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_19'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_20'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_21'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_22'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_23'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_24'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_25'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_26'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_27'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_28'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_29'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_30'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_31'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_32'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_33'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_34'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_35'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_36'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCalicoFelixMetricsUseCaseǁexecute__mutmut['xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_37'] = CalicoFelixMetricsUseCase.xǁCalicoFelixMetricsUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
