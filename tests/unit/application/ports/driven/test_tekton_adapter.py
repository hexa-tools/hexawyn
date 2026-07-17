from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.tekton_pipeline_status_port import (
    PipelineRunRecord,
    TektonPipelineStatusPort,
)


def _run(name: str, status: str) -> PipelineRunRecord:
    return PipelineRunRecord(
        name=name,
        status=status,
        start_time=None,
        duration_seconds=None,
        failure_reason=None if status != "Failed" else "ExitCode1",
        pipeline_ref="build",
    )


class TestPortImplementation:
    def test_is_a_tekton_pipeline_status_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.tekton_adapter import (
            OpenShiftTektonAdapter,
        )

        adapter = OpenShiftTektonAdapter(delegate=MagicMock(spec=TektonPipelineStatusPort))

        assert isinstance(adapter, TektonPipelineStatusPort)


class TestListPipelineRuns:
    def test_delegates_to_injected_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.tekton_adapter import (
            OpenShiftTektonAdapter,
        )

        delegate = MagicMock(spec=TektonPipelineStatusPort)
        delegate.list_pipeline_runs.return_value = [_run("pr-1", "Succeeded")]
        adapter = OpenShiftTektonAdapter(delegate=delegate)

        result = adapter.list_pipeline_runs("team-a", limit=10)

        delegate.list_pipeline_runs.assert_called_once_with("team-a", 10)
        assert result[0]["name"] == "pr-1"

    def test_defaults_to_kubernetes_tekton_adapter(self) -> None:
        from hexawyn.adapters.secondary.openshift.tekton_adapter import (
            OpenShiftTektonAdapter,
        )

        fake_delegate = MagicMock(spec=TektonPipelineStatusPort)
        fake_delegate.list_pipeline_runs.return_value = []
        adapter = OpenShiftTektonAdapter()

        with patch(
            "hexawyn.adapters.secondary.kubernetes_tekton_adapter.KubernetesTektonAdapter",
            return_value=fake_delegate,
        ) as adapter_cls:
            result = adapter.list_pipeline_runs("team-a")

        adapter_cls.assert_called_once_with()
        assert result == []


class TestGetFailedPipelineRuns:
    def test_returns_only_failed_runs(self) -> None:
        from hexawyn.adapters.secondary.openshift.tekton_adapter import (
            OpenShiftTektonAdapter,
        )

        delegate = MagicMock(spec=TektonPipelineStatusPort)
        delegate.list_pipeline_runs.return_value = [
            _run("pr-1", "Succeeded"),
            _run("pr-2", "Failed"),
            _run("pr-3", "Running"),
            _run("pr-4", "Failed"),
        ]
        adapter = OpenShiftTektonAdapter(delegate=delegate)

        failed = adapter.get_failed_pipeline_runs("team-a")

        assert [run["name"] for run in failed] == ["pr-2", "pr-4"]

    def test_returns_empty_when_no_failures(self) -> None:
        from hexawyn.adapters.secondary.openshift.tekton_adapter import (
            OpenShiftTektonAdapter,
        )

        delegate = MagicMock(spec=TektonPipelineStatusPort)
        delegate.list_pipeline_runs.return_value = [_run("pr-1", "Succeeded")]
        adapter = OpenShiftTektonAdapter(delegate=delegate)

        assert adapter.get_failed_pipeline_runs("team-a") == []
