from __future__ import annotations

from hexawyn.application.ports.driven.tekton_pipeline_status_port import (
    PipelineRunRecord,
    TektonPipelineStatusPort,
)

_FAILED_STATUS = "Failed"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOpenShiftTektonAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftTektonAdapterǁ_runs_source__mutmut: MutantDict = {}  # type: ignore


class OpenShiftTektonAdapter(TektonPipelineStatusPort):
    """Tekton adapter for OpenShift Pipelines (native CI/CD).

    Tekton on OpenShift uses the same `tekton.dev` CRDs as vanilla clusters, so
    PipelineRun reads are delegated to the shared KubernetesTektonAdapter. This
    adapter adds an OpenShift-oriented convenience for surfacing failed runs.
    """

    @_mutmut_mutated(mutants_xǁOpenShiftTektonAdapterǁ__init____mutmut)
    def __init__(self, delegate: TektonPipelineStatusPort | None = None) -> None:
        self._delegate = delegate

    def xǁOpenShiftTektonAdapterǁ__init____mutmut_orig(self, delegate: TektonPipelineStatusPort | None = None) -> None:
        self._delegate = delegate

    def xǁOpenShiftTektonAdapterǁ__init____mutmut_1(self, delegate: TektonPipelineStatusPort | None = None) -> None:
        self._delegate = None

    @_mutmut_mutated(mutants_xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut)
    def list_pipeline_runs(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        return self._runs_source().list_pipeline_runs(namespace, limit)

    def xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_orig(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        return self._runs_source().list_pipeline_runs(namespace, limit)

    def xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_1(self, namespace: str, limit: int = 501) -> list[PipelineRunRecord]:
        return self._runs_source().list_pipeline_runs(namespace, limit)

    def xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_2(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        return self._runs_source().list_pipeline_runs(None, limit)

    def xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_3(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        return self._runs_source().list_pipeline_runs(namespace, None)

    def xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_4(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        return self._runs_source().list_pipeline_runs(limit)

    def xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_5(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        return self._runs_source().list_pipeline_runs(namespace, )

    @_mutmut_mutated(mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut)
    def get_failed_pipeline_runs(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(namespace, limit)
        return [run for run in runs if run["status"] == _FAILED_STATUS]

    def xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_orig(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(namespace, limit)
        return [run for run in runs if run["status"] == _FAILED_STATUS]

    def xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_1(self, namespace: str, limit: int = 501) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(namespace, limit)
        return [run for run in runs if run["status"] == _FAILED_STATUS]

    def xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_2(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = None
        return [run for run in runs if run["status"] == _FAILED_STATUS]

    def xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_3(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(None, limit)
        return [run for run in runs if run["status"] == _FAILED_STATUS]

    def xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_4(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(namespace, None)
        return [run for run in runs if run["status"] == _FAILED_STATUS]

    def xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_5(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(limit)
        return [run for run in runs if run["status"] == _FAILED_STATUS]

    def xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_6(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(namespace, )
        return [run for run in runs if run["status"] == _FAILED_STATUS]

    def xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_7(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(namespace, limit)
        return [run for run in runs if run["XXstatusXX"] == _FAILED_STATUS]

    def xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_8(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(namespace, limit)
        return [run for run in runs if run["STATUS"] == _FAILED_STATUS]

    def xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_9(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(namespace, limit)
        return [run for run in runs if run["status"] != _FAILED_STATUS]

    @_mutmut_mutated(mutants_xǁOpenShiftTektonAdapterǁ_runs_source__mutmut)
    def _runs_source(self) -> TektonPipelineStatusPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.kubernetes_tekton_adapter import (
                KubernetesTektonAdapter,
            )

            self._delegate = KubernetesTektonAdapter()
        return self._delegate

    def xǁOpenShiftTektonAdapterǁ_runs_source__mutmut_orig(self) -> TektonPipelineStatusPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.kubernetes_tekton_adapter import (
                KubernetesTektonAdapter,
            )

            self._delegate = KubernetesTektonAdapter()
        return self._delegate

    def xǁOpenShiftTektonAdapterǁ_runs_source__mutmut_1(self) -> TektonPipelineStatusPort:
        if self._delegate is not None:
            from hexawyn.infrastructure.adapters.secondary.kubernetes_tekton_adapter import (
                KubernetesTektonAdapter,
            )

            self._delegate = KubernetesTektonAdapter()
        return self._delegate

    def xǁOpenShiftTektonAdapterǁ_runs_source__mutmut_2(self) -> TektonPipelineStatusPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.kubernetes_tekton_adapter import (
                KubernetesTektonAdapter,
            )

            self._delegate = None
        return self._delegate

mutants_xǁOpenShiftTektonAdapterǁ__init____mutmut['_mutmut_orig'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁ__init____mutmut['xǁOpenShiftTektonAdapterǁ__init____mutmut_1'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut['_mutmut_orig'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_1'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_2'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_3'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_4'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_5'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁlist_pipeline_runs__mutmut_5 # type: ignore # mutmut generated

mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut['_mutmut_orig'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_1'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_2'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_3'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_4'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_5'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_6'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_7'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_8'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut['xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_9'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁget_failed_pipeline_runs__mutmut_9 # type: ignore # mutmut generated

mutants_xǁOpenShiftTektonAdapterǁ_runs_source__mutmut['_mutmut_orig'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁ_runs_source__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁ_runs_source__mutmut['xǁOpenShiftTektonAdapterǁ_runs_source__mutmut_1'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁ_runs_source__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftTektonAdapterǁ_runs_source__mutmut['xǁOpenShiftTektonAdapterǁ_runs_source__mutmut_2'] = OpenShiftTektonAdapter.xǁOpenShiftTektonAdapterǁ_runs_source__mutmut_2 # type: ignore # mutmut generated
