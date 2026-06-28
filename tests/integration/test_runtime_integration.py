"""Integration test — CLI → Control Plane (end-to-end).

Tests the full async flow: post investigation → poll → get result.
Requires the Control Plane to be running (default: http://localhost:8000).

Run:
  CONTROL_PLANE_URL=http://localhost:8000 poetry run pytest tests/integration/test_runtime_integration.py -v -m integration
"""

from __future__ import annotations

import os

import pytest
from hexawyn.adapters.secondary.runtime_client import RuntimeClient

CONTROL_PLANE_URL = os.environ.get("CONTROL_PLANE_URL", "http://localhost:8000")


def _is_control_plane_available() -> bool:
    """Check if the Control Plane API is reachable."""
    import httpx

    try:
        response = httpx.get(f"{CONTROL_PLANE_URL}/health", timeout=2.0)
        return response.status_code == 200
    except Exception:
        return False


@pytest.mark.integration
class TestRuntimeIntegration:
    """End-to-end test: CLI → Control Plane → Valkey → Worker → Result."""

    def test_full_investigation_flow(self) -> None:
        if not _is_control_plane_available():
            pytest.skip(f"Control Plane not available at {CONTROL_PLANE_URL}")

        client = RuntimeClient(endpoint=CONTROL_PLANE_URL)

        # 1. Create investigation
        job_id = client.post_investigation(
            query="why is my pod crashing?",
            cluster_name="test-cluster",
            provider="vanilla",
        )
        assert job_id
        assert len(job_id) > 0

        # 2. Poll for result (wait up to 60s)
        result = client.poll_investigation(job_id, timeout=60.0, interval=1.0)

        assert result["job_id"] == job_id
        assert result["status"] in ("completed", "failed")

        # 3. Validate result structure
        if result["status"] == "completed":
            inner = result.get("result")
            assert isinstance(inner, dict), f"Expected dict result, got {type(inner)}"
            assert "answer" in inner
            assert "status" in inner

        client.close()

    def test_health_endpoint(self) -> None:
        if not _is_control_plane_available():
            pytest.skip(f"Control Plane not available at {CONTROL_PLANE_URL}")

        import httpx

        response = httpx.get(f"{CONTROL_PLANE_URL}/health", timeout=5.0)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["service"] == "hexawyn-control-plane"

    def test_invalid_query_handled_gracefully(self) -> None:
        if not _is_control_plane_available():
            pytest.skip(f"Control Plane not available at {CONTROL_PLANE_URL}")

        client = RuntimeClient(endpoint=CONTROL_PLANE_URL)

        job_id = client.post_investigation(
            query="",  # empty query
            cluster_name="test",
            provider="vanilla",
        )
        assert job_id

        result = client.poll_investigation(job_id, timeout=60.0, interval=1.0)
        assert result["status"] in ("completed", "failed")

        client.close()
