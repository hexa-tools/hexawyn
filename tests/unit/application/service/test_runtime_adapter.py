from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch

from hexawyn.application.service.runtime_adapter import (
    StubRuntimeAdapter,
    _resolve_runtime,
    get_runtime,
    set_runtime,
)
from hexawyn.domain.models.cluster import ClusterContext


class TestStubRuntimeAdapter:
    def test_set_adapter_is_noop(self) -> None:
        adapter = StubRuntimeAdapter()
        adapter.set_adapter(MagicMock())

    def test_run_investigation_returns_unavailable(self) -> None:
        adapter = StubRuntimeAdapter()
        context = ClusterContext(name="test-cluster")

        result = adapter.run_investigation(
            query="test query",
            cluster_context=context,
        )

        assert result["status"] == "unavailable"
        assert result["error"] is not None
        assert "hexawyn-control-plane" in result["answer"]

    def test_run_startup_scan_returns_offline(self) -> None:
        adapter = StubRuntimeAdapter()

        result = adapter.run_startup_scan(cluster_name="test-cluster")

        assert result.provider_badge == "[offline]"
        assert result.health_score == 0
        assert "hexawyn-control-plane" in result.top_issues[0]

    def test_check_quota_returns_allowed(self) -> None:
        adapter = StubRuntimeAdapter()

        result = adapter.check_quota()

        assert result["allowed"] is True
        assert result["used"] == 0

    def test_increment_quota_is_noop(self) -> None:
        adapter = StubRuntimeAdapter()
        adapter.increment_quota()


class TestGetRuntime:
    def test_get_runtime_returns_instance(self) -> None:
        set_runtime(StubRuntimeAdapter())
        try:
            result = get_runtime()
            assert isinstance(result, StubRuntimeAdapter)
        finally:
            set_runtime(StubRuntimeAdapter())

    def test_set_and_get_runtime_returns_same_instance(self) -> None:
        original = get_runtime()
        custom = StubRuntimeAdapter()
        set_runtime(custom)

        result = get_runtime()

        assert result is custom
        set_runtime(original)


class TestResolveRuntime:
    def test_resolve_runtime_defaults_to_stub(self) -> None:
        with patch(
            "hexawyn.application.service.runtime_adapter.get_runtime_mode",
            return_value="stub",
        ):
            result = _resolve_runtime()

        assert isinstance(result, StubRuntimeAdapter)

    def test_resolve_runtime_remote_with_missing_endpoint_raises(self) -> None:
        with patch(
            "hexawyn.application.service.runtime_adapter.get_runtime_mode",
            return_value="remote",
        ):
            with patch(
                "hexawyn.application.service.runtime_adapter.get_runtime_endpoint",
                return_value="",
            ):
                try:
                    _resolve_runtime()
                except ValueError as exc:
                    assert "endpoint" in str(exc)
                else:
                    raise AssertionError("Expected ValueError")

    def test_resolve_runtime_remote_with_valid_endpoint(self) -> None:
        mock_adapter_instance = StubRuntimeAdapter()
        mock_adapter_class = MagicMock(return_value=mock_adapter_instance)
        mock_http_module = MagicMock()
        mock_http_module.HttpRuntimeAdapter = mock_adapter_class
        sys.modules["hexawyn.application.service.http_runtime_adapter"] = mock_http_module
        try:
            with patch(
                "hexawyn.application.service.runtime_adapter.get_runtime_mode",
                return_value="remote",
            ):
                with patch(
                    "hexawyn.application.service.runtime_adapter.get_runtime_endpoint",
                    return_value="http://localhost:8000",
                ):
                    result = _resolve_runtime()

            assert result is mock_adapter_instance
            mock_adapter_class.assert_called_once_with(endpoint="http://localhost:8000")
        finally:
            del sys.modules["hexawyn.application.service.http_runtime_adapter"]

    def test_get_runtime_when_instance_is_none_resolves(self) -> None:
        from hexawyn.application.service import runtime_adapter

        runtime_adapter._runtime_instance = None
        try:
            with patch(
                "hexawyn.application.service.runtime_adapter._resolve_runtime",
                return_value=StubRuntimeAdapter(),
            ) as mock_resolve:
                result = get_runtime()
                assert isinstance(result, StubRuntimeAdapter)
                mock_resolve.assert_called_once()
        finally:
            runtime_adapter._runtime_instance = StubRuntimeAdapter()
