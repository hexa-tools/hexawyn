from hexawyn.application.ports.driven.tekton_pipeline_status_port import TektonPipelineStatusPort
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetPipelineRunStatusUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GetPipelineRunStatusUseCase:
    @_mutmut_mutated(mutants_xǁGetPipelineRunStatusUseCaseǁ__init____mutmut)
    def __init__(self, port: TektonPipelineStatusPort) -> None:
        self._port = port
    def xǁGetPipelineRunStatusUseCaseǁ__init____mutmut_orig(self, port: TektonPipelineStatusPort) -> None:
        self._port = port
    def xǁGetPipelineRunStatusUseCaseǁ__init____mutmut_1(self, port: TektonPipelineStatusPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut)
    def execute(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_orig(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_1(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = None
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_2(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=None, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_3(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=None)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_4(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_5(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, )
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_6(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = None
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_7(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=None,
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_8(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=None,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_9(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=None,
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_10(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=None,
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_11(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=None,
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_12(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=None,
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_13(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=None,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_14(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=None,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_15(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_16(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_17(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_18(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_19(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_20(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_21(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_22(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_23(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_24(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_25(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace and "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_26(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "XXXX",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_27(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=1,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_28(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(None),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_29(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(2 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_30(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get(None) == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_31(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("XXstatusXX") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_32(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("STATUS") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_33(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") != "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_34(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "XXRunningXX"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_35(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_36(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "RUNNING"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_37(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(None),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_38(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(2 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_39(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get(None) == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_40(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("XXstatusXX") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_41(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("STATUS") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_42(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") != "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_43(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "XXSucceededXX"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_44(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_45(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "SUCCEEDED"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_46(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(None),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_47(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(2 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_48(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get(None) == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_49(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("XXstatusXX") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_50(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("STATUS") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_51(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") != "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_52(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "XXFailedXX"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_53(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_54(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "FAILED"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_55(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=1,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_56(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=1,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_57(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        from hexawyn.domain.models.pipeline import PipelineRunStatusReport

        report = PipelineRunStatusReport(
            namespace=command.namespace or "",
            window_hours=0,
            total=len(runs),
            running=sum(1 for r in runs if r.get("status") == "Running"),
            succeeded=sum(1 for r in runs if r.get("status") == "Succeeded"),
            failed=sum(1 for r in runs if r.get("status") == "Failed"),
            cancelled=0,
            not_started=0,
            most_recent_failed=None,
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=None)

mutants_xǁGetPipelineRunStatusUseCaseǁ__init____mutmut['_mutmut_orig'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁ__init____mutmut['xǁGetPipelineRunStatusUseCaseǁ__init____mutmut_1'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['_mutmut_orig'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_1'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_2'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_3'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_4'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_5'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_6'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_7'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_8'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_9'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_10'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_11'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_12'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_13'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_14'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_15'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_16'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_17'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_18'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_19'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_20'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_21'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_22'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_23'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_24'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_25'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_26'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_27'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_28'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_29'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_30'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_31'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_32'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_33'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_34'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_35'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_36'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_37'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_38'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_39'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_40'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_41'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_42'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_43'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_44'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_45'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_46'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_47'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_48'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_49'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_50'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_51'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_52'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_53'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_54'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_55'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_56'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGetPipelineRunStatusUseCaseǁexecute__mutmut['xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_57'] = GetPipelineRunStatusUseCase.xǁGetPipelineRunStatusUseCaseǁexecute__mutmut_57 # type: ignore # mutmut generated
