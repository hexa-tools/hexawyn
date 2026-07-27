from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.openshift.tekton_adapter import OpenShiftTektonAdapter


class TestOpenShiftTektonAdapter:
    def test_list_pipeline_runs_delegates(self) -> None:
        delegate = Mock()
        delegate.list_pipeline_runs.return_value = []
        adapter = OpenShiftTektonAdapter(delegate=delegate)
        assert adapter.list_pipeline_runs("ns") == []
        delegate.list_pipeline_runs.assert_called_once_with("ns", 500)

    def test_get_failed_pipeline_runs_filters(self) -> None:
        delegate = Mock()
        delegate.list_pipeline_runs.return_value = [
            {"name": "ok", "status": "Succeeded"},
            {"name": "bad", "status": "Failed"},
            {"name": "also-bad", "status": "Failed"},
        ]
        adapter = OpenShiftTektonAdapter(delegate=delegate)
        result = adapter.get_failed_pipeline_runs("ns")
        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "bad"

    def test_get_failed_pipeline_runs_empty(self) -> None:
        delegate = Mock()
        delegate.list_pipeline_runs.return_value = []
        adapter = OpenShiftTektonAdapter(delegate=delegate)
        assert adapter.get_failed_pipeline_runs("ns") == []

    def test_get_failed_pipeline_runs_all_succeeded(self) -> None:
        delegate = Mock()
        delegate.list_pipeline_runs.return_value = [
            {"name": "a", "status": "Succeeded"},
            {"name": "b", "status": "Running"},
        ]
        adapter = OpenShiftTektonAdapter(delegate=delegate)
        assert adapter.get_failed_pipeline_runs("ns") == []

    def test_delegate_none_uses_kubernetes(self) -> None:
        from unittest.mock import patch

        with patch(
            "hexawyn.adapters.secondary.kubernetes_tekton_adapter.KubernetesTektonAdapter"
        ) as mock_k8s:
            mock_k8s.return_value.list_pipeline_runs.return_value = []
            adapter = OpenShiftTektonAdapter(delegate=None)
            result = adapter.list_pipeline_runs("ns", 10)
            assert result == []
