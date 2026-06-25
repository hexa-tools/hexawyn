from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.runtime_port import RuntimePort
from hexawyn.application.service.http_runtime_adapter import HttpRuntimeAdapter
from hexawyn.domain.models.cluster import CloudProvider, ClusterContext


def _mock_cluster_context() -> ClusterContext:
    return ClusterContext(name="prod-eu", provider=CloudProvider.VANILLA)


class TestHttpRuntimeAdapter:
    def test_implements_runtime_port(self) -> None:
        adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
        assert isinstance(adapter, RuntimePort)

    def test_set_adapter_is_noop(self) -> None:
        adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
        mock_adapter = MagicMock()
        adapter.set_adapter(mock_adapter)

    def test_run_investigation_posts_and_polls(self) -> None:
        mock_client = MagicMock()
        mock_client.post_investigation.return_value = "job-42"
        mock_client.poll_investigation.return_value = {
            "job_id": "job-42",
            "status": "completed",
            "result": {
                "answer": "OOMKilled — memory limit too low",
                "cause": "Memory limit set to 128Mi",
                "solution": "Increase to 512Mi",
                "status": "complete",
                "suggestions": ["Increase memory limit", "Add HPA"],
                "error": None,
            },
        }

        with patch(
            "hexawyn.application.service.http_runtime_adapter.RuntimeClient",
            return_value=mock_client,
        ):
            adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
            result = adapter.run_investigation(
                query="why is payments-api crashing?",
                cluster_context=_mock_cluster_context(),
            )

        assert result["answer"] == "OOMKilled — memory limit too low"
        assert result["cause"] == "Memory limit set to 128Mi"
        assert result["status"] == "complete"
        assert len(result["suggestions"]) == 2
        assert result["error"] is None

        mock_client.post_investigation.assert_called_once_with(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
            provider="vanilla",
        )
        mock_client.poll_investigation.assert_called_once_with("job-42")

    def test_run_investigation_failed_status(self) -> None:
        mock_client = MagicMock()
        mock_client.post_investigation.return_value = "job-fail"
        mock_client.poll_investigation.return_value = {
            "job_id": "job-fail",
            "status": "failed",
            "result": {"error": "Cluster unreachable"},
        }

        with patch(
            "hexawyn.application.service.http_runtime_adapter.RuntimeClient",
            return_value=mock_client,
        ):
            adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
            result = adapter.run_investigation(
                query="test",
                cluster_context=_mock_cluster_context(),
            )

        assert result["status"] == "error"
        assert result["error"] == "Cluster unreachable"

    def test_run_investigation_http_error(self) -> None:
        mock_client = MagicMock()
        mock_client.post_investigation.side_effect = Exception("connection refused")

        with patch(
            "hexawyn.application.service.http_runtime_adapter.RuntimeClient",
            return_value=mock_client,
        ):
            adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
            result = adapter.run_investigation(
                query="test",
                cluster_context=_mock_cluster_context(),
            )

        assert result["status"] == "error"
        assert "connection refused" in str(result["error"])

    def test_run_startup_scan_not_supported(self) -> None:
        adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
        result = adapter.run_startup_scan(cluster_name="test")

        assert result.health_score == 0
        assert "not available" in result.narrative_summary.lower()

    def test_close_closes_client(self) -> None:
        mock_client = MagicMock()

        with patch(
            "hexawyn.application.service.http_runtime_adapter.RuntimeClient",
            return_value=mock_client,
        ):
            adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
            adapter.close()

        mock_client.close.assert_called_once()
