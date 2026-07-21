from unittest.mock import MagicMock


class TestRuntimePortProgress:
    def test_http_adapter_calls_on_progress_for_each_node(self) -> None:
        from hexawyn.application.service.http_runtime_adapter import HttpRuntimeAdapter

        adapter = HttpRuntimeAdapter(endpoint="http://test:8080")

        mock_stream = [
            ("plan", {"tool": "detect_crashloop"}),
            ("execute", {"pods_found": 3}),
            ("report", {"llm_response": "3 pods are crashing"}),
        ]

        with MagicMock() as mock_client:
            mock_client.stream_investigation.return_value = mock_stream
            adapter._client = mock_client

            on_progress = MagicMock()
            result = adapter.run_investigation(
                query="why are pods crashing?",
                cluster_context=MagicMock(),
                on_progress=on_progress,
            )

        assert on_progress.call_count == 3
        on_progress.assert_any_call("plan", "Plan")
        on_progress.assert_any_call("execute", "Execute")
        on_progress.assert_any_call("report", "Report")
        assert result["status"] == "complete"

    def test_stub_adapter_accepts_on_progress(self) -> None:
        from hexawyn.application.service.runtime_adapter import StubRuntimeAdapter

        adapter = StubRuntimeAdapter()
        on_progress = MagicMock()
        result = adapter.run_investigation(
            query="test",
            cluster_context=MagicMock(),
            on_progress=on_progress,
        )
        assert result["status"] == "unavailable"
