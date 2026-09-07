from __future__ import annotations

from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
    DeploymentLatencyComparisonPort,
)
from hexawyn.application.use_case.observability.deployment_latency.command import (
    DeploymentLatencyCommand,
)
from hexawyn.application.use_case.observability.deployment_latency.response import (
    DeploymentLatencyResponse,
)
from hexawyn.domain.models.deployment_latency import (
    DeploymentComparisonRequest,
    DeploymentComparisonResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDeploymentLatencyUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DeploymentLatencyUseCase:
    @_mutmut_mutated(mutants_xǁDeploymentLatencyUseCaseǁ__init____mutmut)
    def __init__(self, port: DeploymentLatencyComparisonPort) -> None:
        self._port = port
    def xǁDeploymentLatencyUseCaseǁ__init____mutmut_orig(self, port: DeploymentLatencyComparisonPort) -> None:
        self._port = port
    def xǁDeploymentLatencyUseCaseǁ__init____mutmut_1(self, port: DeploymentLatencyComparisonPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut)
    def execute(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_orig(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_1(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = None
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_2(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=None,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_3(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=None,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_4(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_5(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_6(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = None
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_7(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(None)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_8(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = None
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_9(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(None)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_10(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = None
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_11(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=None, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_12(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=None, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_13(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=None)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_14(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_15(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_16(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, )
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_17(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=None,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_18(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=None,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_19(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=None,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_20(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=None,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_21(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=None,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_22(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=None,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_23(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=None,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_24(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=None,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_25(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_26(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_27(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_28(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_29(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_30(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_31(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            suggestion=r.suggestion,
        )

    def xǁDeploymentLatencyUseCaseǁexecute__mutmut_32(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            )

mutants_xǁDeploymentLatencyUseCaseǁ__init____mutmut['_mutmut_orig'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁ__init____mutmut['xǁDeploymentLatencyUseCaseǁ__init____mutmut_1'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['_mutmut_orig'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_1'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_2'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_3'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_4'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_5'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_6'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_7'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_8'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_9'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_10'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_11'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_12'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_13'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_14'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_15'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_16'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_17'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_18'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_19'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_20'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_21'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_22'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_23'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_24'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_25'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_26'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_27'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_28'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_29'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_30'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_31'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDeploymentLatencyUseCaseǁexecute__mutmut['xǁDeploymentLatencyUseCaseǁexecute__mutmut_32'] = DeploymentLatencyUseCase.xǁDeploymentLatencyUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
