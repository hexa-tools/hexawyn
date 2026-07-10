from __future__ import annotations

from hexawyn.application.ports.driven.tekton_pipeline_status_port import (
    PipelineRunRecord,
    TektonPipelineStatusPort,
)

_FAILED_STATUS = "Failed"


class OpenShiftTektonAdapter(TektonPipelineStatusPort):
    """Tekton adapter for OpenShift Pipelines (native CI/CD).

    Tekton on OpenShift uses the same `tekton.dev` CRDs as vanilla clusters, so
    PipelineRun reads are delegated to the shared KubernetesTektonAdapter. This
    adapter adds an OpenShift-oriented convenience for surfacing failed runs.
    """

    def __init__(self, delegate: TektonPipelineStatusPort | None = None) -> None:
        self._delegate = delegate

    def list_pipeline_runs(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        return self._runs_source().list_pipeline_runs(namespace, limit)

    def get_failed_pipeline_runs(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return only the PipelineRuns whose status is Failed."""
        runs = self.list_pipeline_runs(namespace, limit)
        return [run for run in runs if run["status"] == _FAILED_STATUS]

    def _runs_source(self) -> TektonPipelineStatusPort:
        if self._delegate is None:
            from hexawyn.adapters.secondary.kubernetes_tekton_adapter import (
                KubernetesTektonAdapter,
            )

            self._delegate = KubernetesTektonAdapter()
        return self._delegate
