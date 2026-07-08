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
        mock_client.stream_investigation.return_value = iter(
            [
                ("plan", {"intent": "diagnose"}),
                ("execute", {"tool_output": {}}),
                (
                    "report",
                    {
                        "llm_response": "OOMKilled — memory limit too low",
                        "suggestions": ["Increase memory limit", "Add HPA"],
                        "status": "complete",
                    },
                ),
            ]
        )

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
        assert result["status"] == "complete"
        assert len(result["suggestions"]) == 2
        assert result["error"] is None

    def test_run_investigation_failed_status(self) -> None:
        mock_client = MagicMock()
        mock_client.stream_investigation.return_value = iter(
            [("error", {"error": "Cluster unreachable"})]
        )

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
        mock_client.stream_investigation.side_effect = Exception("connection refused")

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

    def test_fetch_pods_returns_adapter_pods_not_empty_list(self) -> None:
        """_fetch_pods() must return actual pods from the adapter.

        If it silently returns [] (e.g. when the adapter raises due to wrong K8s
        context), the backend receives no pods and falls back to its own K8s
        client, which is configured for a different cluster (kind-hexawyn).
        This was the root cause of investigation responses containing kind data
        instead of hetzner-preprod data.
        """
        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = [
            {
                "name": "airflow-scheduler",
                "namespace": "airflow",
                "status": "Running",
                "restarts": 0,
            },
            {"name": "airflow-worker", "namespace": "airflow", "status": "Running", "restarts": 1},
        ]

        adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
        adapter.set_adapter(mock_adapter)

        pods = adapter._fetch_pods()

        assert len(pods) == 2, (
            "_fetch_pods() returned an empty list even though the adapter has pods. "
            "This means the backend would receive no pods and fall back to K8s, "
            "potentially fetching data from the wrong cluster."
        )
        assert pods[0]["name"] == "airflow-scheduler"
        assert pods[0]["namespace"] == "airflow"
        mock_adapter.list_pods.assert_called_once()

    def test_fetch_pods_returns_empty_when_no_adapter(self) -> None:
        adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
        assert adapter._fetch_pods() == []

    def test_fetch_pods_returns_empty_and_does_not_raise_when_adapter_fails(self) -> None:
        """_fetch_pods() must not propagate K8s connection errors.

        Connection errors happen when the K8s API is unreachable (wrong context,
        network issue, etc.). Propagating them here would mask the real error with
        an unhelpful HTTP exception instead of a clear backend response.
        """
        mock_adapter = MagicMock()
        mock_adapter.list_pods.side_effect = Exception("HTTPSConnectionPool: connection refused")

        adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
        adapter.set_adapter(mock_adapter)

        pods = adapter._fetch_pods()
        assert pods == []

    def test_run_investigation_sends_pods_in_http_payload(self) -> None:
        """Pods fetched from the adapter must be included in the HTTP POST.

        If pods are not sent, the backend's RetrieverAgent gets an empty pod list
        and falls back to calling K8s directly — which fails on the VPS (no kubeconfig).
        """
        mock_client = MagicMock()
        mock_client.stream_investigation.return_value = iter(
            [("report", {"llm_response": "ok", "suggestions": [], "status": "complete"})]
        )

        mock_adapter = MagicMock()
        mock_adapter.list_pods.return_value = [
            {"name": "pod-a", "namespace": "airflow", "status": "Running", "restarts": 0},
        ]

        with patch(
            "hexawyn.application.service.http_runtime_adapter.RuntimeClient",
            return_value=mock_client,
        ):
            adapter = HttpRuntimeAdapter(endpoint="http://localhost:8000")
            adapter.set_adapter(mock_adapter)
            adapter.run_investigation(
                query="how many pods in airflow?",
                cluster_context=_mock_cluster_context(),
            )

        call_kwargs = mock_client.stream_investigation.call_args[1]
        assert "pods" in call_kwargs, "pods must be included in the HTTP payload"
        assert len(call_kwargs["pods"]) == 1, "pods list must not be empty"
        assert call_kwargs["pods"][0]["namespace"] == "airflow"

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
