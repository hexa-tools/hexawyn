"""Integration test — startup scan endpoint via HTTP.

Tests the full flow: RuntimeClient.startup_scan() → Control Plane → LangGraph startup graph.
Requires the Control Plane to be running (default: http://localhost:8000).

Run:
  CONTROL_PLANE_URL=http://localhost:8000 poetry run pytest tests/integration/test_startup_scan_integration.py -v -m integration
"""  # noqa: E501

from __future__ import annotations

import os
import time

import httpx
import pytest
from hexawyn.adapters.secondary.runtime_client import RuntimeClient

CONTROL_PLANE_URL = os.environ.get("CONTROL_PLANE_URL", "http://localhost:8000")


def _is_control_plane_available() -> bool:
    try:
        response = httpx.get(f"{CONTROL_PLANE_URL}/health", timeout=2.0)
        return response.status_code == 200  # noqa: PLR2004
    except Exception:
        return False


@pytest.mark.integration
class TestStartupScanIntegration:
    def test_startup_scan_endpoint_returns_200(self) -> None:
        if not _is_control_plane_available():
            pytest.skip(f"Control Plane not available at {CONTROL_PLANE_URL}")

        response = httpx.post(
            f"{CONTROL_PLANE_URL}/api/v1/startup-scan",
            json={"cluster_name": "test-integration"},
            timeout=60.0,
        )
        assert (
            response.status_code == 200  # noqa: PLR2004
        ), f"Expected 200, got {response.status_code}: {response.text}"

        data = response.json()
        assert "health_score" in data
        assert "narrative_summary" in data
        assert "suggestions" in data
        assert "top_issues" in data
        assert "provider" in data
        assert "provider_display" in data

    def test_startup_scan_via_runtime_client(self) -> None:
        if not _is_control_plane_available():
            pytest.skip(f"Control Plane not available at {CONTROL_PLANE_URL}")

        client = RuntimeClient(endpoint=CONTROL_PLANE_URL)

        t0 = time.monotonic()
        result = client.startup_scan(cluster_name="test-integration")
        elapsed = time.monotonic() - t0

        assert isinstance(result, dict)
        assert "health_score" in result
        assert "narrative_summary" in result
        assert "suggestions" in result
        assert "top_issues" in result

        print(f"\n  startup_scan completed in {elapsed:.1f}s")
        print(f"  health_score: {result.get('health_score')}")
        print(f"  narrative: {result.get('narrative_summary', '')[:120]}")
        print(f"  provider: {result.get('provider', 'unknown')}")
        print(f"  suggestions: {len(result.get('suggestions', []))}")

        client.close()

    def test_startup_scan_via_http_runtime_adapter(self) -> None:
        if not _is_control_plane_available():
            pytest.skip(f"Control Plane not available at {CONTROL_PLANE_URL}")

        from hexawyn.application.service.http_runtime_adapter import HttpRuntimeAdapter

        adapter = HttpRuntimeAdapter(endpoint=CONTROL_PLANE_URL)

        result = adapter.run_startup_scan(cluster_name="test-integration")

        assert result.health_score >= 0
        assert isinstance(result.narrative_summary, str)
        assert isinstance(result.suggestions, list)
        assert isinstance(result.top_issues, list)

        print(f"\n  health_score: {result.health_score}")
        print(f"  provider: {result.provider}")
        print(f"  suggestions: {len(result.suggestions)}")
        print(f"  top_issues: {len(result.top_issues)}")

        adapter.close()

    def test_get_runtime_resolves_remote(self) -> None:
        if not _is_control_plane_available():
            pytest.skip(f"Control Plane not available at {CONTROL_PLANE_URL}")

        with (
            __import__("unittest").mock.patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_mode",
                return_value="remote",
            ),
            __import__("unittest").mock.patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_endpoint",
                return_value=CONTROL_PLANE_URL,
            ),
        ):
            from hexawyn.application.service.http_runtime_adapter import HttpRuntimeAdapter
            from hexawyn.application.service.runtime_adapter import get_runtime

            runtime = get_runtime()

            assert isinstance(runtime, HttpRuntimeAdapter)
            result = runtime.run_startup_scan(cluster_name="test-integration")
            assert result.health_score >= 0
