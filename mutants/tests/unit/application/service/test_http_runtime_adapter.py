from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.service.http_runtime_adapter import HttpRuntimeAdapter
from hexawyn.domain.models.cluster import ClusterContext


def _make_adapter() -> HttpRuntimeAdapter:
    with patch(
        "hexawyn.infrastructure.config.config_manager.get_api_key",
        return_value=None,
    ):
        return HttpRuntimeAdapter(endpoint="http://test:8080")


def _cluster_context() -> ClusterContext:
    return ClusterContext(name="test-cluster")


class TestHttpRuntimeAdapterConstruction:
    def test_close_delegates_to_client(self) -> None:
        adapter = _make_adapter()
        adapter._client = MagicMock()
        adapter.close()
        adapter._client.close.assert_called_once()

    def test_set_adapter_stores_reference(self) -> None:
        adapter = _make_adapter()
        inner = MagicMock()
        adapter.set_adapter(inner)
        assert adapter._adapter is inner


class TestFetchPods:
    def test_fetch_pods_without_adapter_returns_empty(self) -> None:
        adapter = _make_adapter()
        adapter._adapter = None
        assert adapter._fetch_pods() == []

    def test_fetch_pods_without_list_pods_returns_empty(self) -> None:
        adapter = _make_adapter()
        adapter._adapter = MagicMock(spec=["get_health_score"])
        assert adapter._fetch_pods() == []

    def test_fetch_pods_returns_dicts(self) -> None:
        adapter = _make_adapter()

        class _Pod:
            def __init__(self, name: str, status: str) -> None:
                self._data = {"name": name, "status": status}

            def keys(self):
                return self._data.keys()

            def __getitem__(self, key: str) -> object:
                return self._data[key]

        adapter._adapter = MagicMock()
        adapter._adapter.list_pods.return_value = [_Pod("p1", "Running")]

        result = adapter._fetch_pods()

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["name"] == "p1"
        assert result[0]["status"] == "Running"

    def test_fetch_pods_handles_adapter_error(self) -> None:
        adapter = _make_adapter()
        adapter._adapter = MagicMock()
        adapter._adapter.list_pods.side_effect = RuntimeError("k8s down")

        assert adapter._fetch_pods() == []


class TestRunInvestigation:
    def test_run_investigation_error_node(self) -> None:
        adapter = _make_adapter()
        mock_client = MagicMock()
        mock_client.stream_investigation.return_value = [
            ("error", {"error": "boom"}),
        ]
        adapter._client = mock_client

        result = adapter.run_investigation(
            query="why?",
            cluster_context=_cluster_context(),
        )

        assert result["status"] == "error"
        assert result["error"] == "boom"
        assert result["predicted_intents"] == []

    def test_run_investigation_full_report(self) -> None:
        adapter = _make_adapter()
        mock_client = MagicMock()
        mock_client.stream_investigation.return_value = [
            (
                "report",
                {
                    "llm_response": "the answer",
                    "cause": "the cause",
                    "solution": "the solution",
                    "status": "complete",
                    "suggestions": ["check logs"],
                    "embedding": [0.1, 0.2],
                    "usage": {"tokens": 120},
                    "predicted_intents": ["investigate"],
                },
            ),
        ]
        adapter._client = mock_client
        on_progress = MagicMock()

        result = adapter.run_investigation(
            query="why?",
            cluster_context=_cluster_context(),
            on_progress=on_progress,
        )

        assert result["status"] == "complete"
        assert result["answer"] == "the answer"
        assert result["cause"] == "the cause"
        assert result["solution"] == "the solution"
        assert result["suggestions"] == ["check logs"]
        assert result["embedding"] == [0.1, 0.2]
        assert result["predicted_intents"] == ["investigate"]
        assert result["usage"] == {"tokens": 120}
        on_progress.assert_called_once()

    def test_run_investigation_malformed_usage_and_lists(self) -> None:
        adapter = _make_adapter()
        mock_client = MagicMock()
        mock_client.stream_investigation.return_value = [
            (
                "report",
                {
                    "llm_response": "x",
                    "usage": "not-a-dict",
                    "suggestions": "not-a-list",
                    "embedding": ["bad", 1.5, True],
                    "predicted_intents": 42,
                },
            ),
        ]
        adapter._client = mock_client

        result = adapter.run_investigation(
            query="why?",
            cluster_context=_cluster_context(),
        )

        assert result["usage"] == {}
        assert result["suggestions"] == []
        assert result["embedding"] == [1.5]
        assert result["predicted_intents"] == []

    def test_run_investigation_handles_stream_error(self) -> None:
        adapter = _make_adapter()
        mock_client = MagicMock()
        mock_client.stream_investigation.side_effect = RuntimeError("connection refused")
        adapter._client = mock_client

        result = adapter.run_investigation(
            query="why?",
            cluster_context=_cluster_context(),
        )

        assert result["status"] == "error"
        assert result["error"] == "connection refused"
        assert result["predicted_intents"] == []


class TestCheckQuota:
    def test_check_quota_parses_values(self) -> None:
        adapter = _make_adapter()
        mock_client = MagicMock()
        mock_client.check_quota.return_value = {
            "allowed": True,
            "used": 3,
            "limit": 10,
            "remaining": 7,
        }
        adapter._client = mock_client

        result = adapter.check_quota()

        assert result == {"allowed": True, "used": 3, "limit": 10, "remaining": 7}

    def test_check_quota_handles_error(self) -> None:
        adapter = _make_adapter()
        mock_client = MagicMock()
        mock_client.check_quota.side_effect = RuntimeError("down")
        adapter._client = mock_client

        result = adapter.check_quota()

        assert result == {"allowed": True, "used": 0, "limit": -1, "remaining": -1}


class TestIncrementQuota:
    def test_increment_quota_delegates(self) -> None:
        adapter = _make_adapter()
        mock_client = MagicMock()
        adapter._client = mock_client
        adapter.increment_quota()
        mock_client.increment_quota.assert_called_once()

    def test_increment_quota_handles_error(self) -> None:
        adapter = _make_adapter()
        mock_client = MagicMock()
        mock_client.increment_quota.side_effect = RuntimeError("down")
        adapter._client = mock_client
        adapter.increment_quota()


class TestRunStartupScan:
    def test_run_startup_scan_parses_response(self) -> None:
        adapter = _make_adapter()
        mock_client = MagicMock()
        mock_client.startup_scan.return_value = {
            "health_score": 85,
            "narrative_summary": "cluster healthy",
            "provider_badge": "[vanilla]",
            "top_issues": ["node pressure"],
            "suggestions": [{"label": "scale", "value": "scale up"}, {"bad": "ignored"}],
            "provider": "vanilla",
            "provider_display": "Vanilla",
        }
        adapter._client = mock_client

        result = adapter.run_startup_scan("test-cluster")

        assert result.health_score == 85  # noqa: PLR2004
        assert result.narrative_summary == "cluster healthy"
        assert result.provider_badge == "[vanilla]"
        assert result.top_issues == ["node pressure"]
        assert result.suggestions == [
            {"label": "scale", "value": "scale up"},
            {"label": "", "value": ""},
        ]
        assert result.provider == "vanilla"
        assert result.provider_display == "Vanilla"

    def test_run_startup_scan_handles_error(self) -> None:
        adapter = _make_adapter()
        mock_client = MagicMock()
        mock_client.startup_scan.side_effect = RuntimeError("unreachable")
        adapter._client = mock_client

        result = adapter.run_startup_scan("test-cluster")

        assert result.health_score == 0
        assert "unavailable" in result.narrative_summary
        assert result.top_issues[0].startswith("Could not reach")


class TestTranslateResponse:
    def test_translate_response_failed_without_result(self) -> None:
        adapter = _make_adapter()
        result = adapter._translate_response({"status": "failed"})

        assert result["status"] == "error"
        assert result["error"] == "No result in response"
        assert result["predicted_intents"] == []

    def test_translate_response_with_result(self) -> None:
        adapter = _make_adapter()
        result = adapter._translate_response(
            {
                "status": "complete",
                "result": {
                    "answer": "a",
                    "cause": "c",
                    "solution": "s",
                    "status": "complete",
                    "suggestions": ["s1"],
                    "error": None,
                    "embedding": [0.5],
                    "predicted_intents": ["intent1"],
                },
            }
        )

        assert result["answer"] == "a"
        assert result["status"] == "complete"
        assert result["suggestions"] == ["s1"]
        assert result["error"] is None
        assert result["embedding"] == [0.5]
        assert result["predicted_intents"] == ["intent1"]
