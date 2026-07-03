"""Unit tests for is_pod_healthy / summarize_health — pure status logic."""

from __future__ import annotations

from hexawyn.domain.models.label_search import MatchedResourceResult
from hexawyn.domain.services.label_search.status_formatter import (
    is_pod_healthy,
    summarize_health,
)


def _resource(
    name: str, kind: str = "pod", phase: str | None = "Running", is_healthy: bool | None = True
) -> MatchedResourceResult:
    return MatchedResourceResult(
        name=name,
        namespace="production",
        kind=kind,  # type: ignore[arg-type]
        node="worker-1" if kind == "pod" else None,
        phase=phase,
        ready=(phase == "Running") if kind == "pod" else None,
        is_healthy=is_healthy,
        labels={},
    )


class TestIsPodHealthy:
    def test_running_is_healthy(self) -> None:
        assert is_pod_healthy("Running") is True

    def test_succeeded_is_healthy(self) -> None:
        assert is_pod_healthy("Succeeded") is True

    def test_crashloopbackoff_is_unhealthy(self) -> None:
        """TC5: one pod in CrashLoopBackOff → flagged."""
        assert is_pod_healthy("CrashLoopBackOff") is False

    def test_pending_is_unhealthy(self) -> None:
        assert is_pod_healthy("Pending") is False

    def test_no_phase_returns_none(self) -> None:
        """Edge case: resource has labels but no status.phase (non-pod resources)."""
        assert is_pod_healthy(None) is None


class TestSummarizeHealth:
    def test_all_healthy_pods(self) -> None:
        """TC4: all matched pods are Running → summary shows all healthy."""
        resources = [_resource("pod-a"), _resource("pod-b")]

        summary = summarize_health(resources, "app=payment")

        assert "2" in summary
        assert "healthy" in summary.lower()

    def test_one_unhealthy_pod_flagged_by_name_and_reason(self) -> None:
        """TC5."""
        resources = [
            _resource("payment-pod-abc12", phase="Running", is_healthy=True),
            _resource("payment-pod-def34", phase="CrashLoopBackOff", is_healthy=False),
        ]

        summary = summarize_health(resources, "app=payment")

        assert "payment-pod-def34" in summary
        assert "CrashLoopBackOff" in summary

    def test_non_pod_resources_are_not_counted_as_unhealthy(self) -> None:
        resources = [_resource("web-svc", kind="service", phase=None, is_healthy=None)]

        summary = summarize_health(resources, "app=payment")

        assert "unhealthy" not in summary.lower()

    def test_empty_resources_returns_no_match_message(self) -> None:
        summary = summarize_health([], "app=ghost")

        assert "app=ghost" in summary
        assert "no resources" in summary.lower()
