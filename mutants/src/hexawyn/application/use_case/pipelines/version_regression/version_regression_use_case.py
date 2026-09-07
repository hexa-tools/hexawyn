from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort
from hexawyn.application.use_case.pipelines.version_regression.command import (
    VersionRegressionCommand,
)
from hexawyn.application.use_case.pipelines.version_regression.response import (
    VersionRegressionResponse,
)
from hexawyn.domain.models.version_regression import (
    VersionComparisonRequest,
    VersionComparisonResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁVersionRegressionUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class VersionRegressionUseCase:
    @_mutmut_mutated(mutants_xǁVersionRegressionUseCaseǁ__init____mutmut)
    def __init__(self, port: VersionRegressionPort) -> None:
        self._port = port
    def xǁVersionRegressionUseCaseǁ__init____mutmut_orig(self, port: VersionRegressionPort) -> None:
        self._port = port
    def xǁVersionRegressionUseCaseǁ__init____mutmut_1(self, port: VersionRegressionPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁVersionRegressionUseCaseǁexecute__mutmut)
    def execute(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_orig(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_1(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = None
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_2(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=None, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_3(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=None
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_4(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_5(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_6(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = None
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_7(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(None)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_8(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = None
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_9(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(None)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_10(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = None
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_11(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=None, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_12(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=None, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_13(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=None)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_14(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_15(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_16(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, )
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_17(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=None,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_18(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=None,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_19(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=None,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_20(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=None,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_21(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=None,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_22(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=None,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_23(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=None,
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_24(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_25(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_26(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_27(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_28(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_29(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_30(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            )

    def xǁVersionRegressionUseCaseǁexecute__mutmut_31(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(None) for f in r.flags],
        )

mutants_xǁVersionRegressionUseCaseǁ__init____mutmut['_mutmut_orig'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁ__init____mutmut['xǁVersionRegressionUseCaseǁ__init____mutmut_1'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['_mutmut_orig'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_1'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_2'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_3'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_4'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_5'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_6'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_7'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_8'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_9'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_10'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_11'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_12'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_13'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_14'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_15'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_16'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_17'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_18'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_19'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_20'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_21'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_22'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_23'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_24'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_25'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_26'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_27'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_28'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_29'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_30'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVersionRegressionUseCaseǁexecute__mutmut['xǁVersionRegressionUseCaseǁexecute__mutmut_31'] = VersionRegressionUseCase.xǁVersionRegressionUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
