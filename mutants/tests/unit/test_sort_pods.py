from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import PodInfo
from hexawyn.application.use_case.workloads.list_pods.sort_pods import (
    sort_pods_unsafe_first,
)


class TestSortPods:
    def test_sort_pods_unsafe_first_places_unhealthy_before_healthy(self) -> None:
        crash: PodInfo = {"name": "crash", "status": "CrashLoopBackOff"}
        running: PodInfo = {"name": "nginx", "status": "Running"}

        result = sort_pods_unsafe_first([running, crash])

        assert result[0]["name"] == "crash"
        assert result[1]["name"] == "nginx"

    def test_sort_pods_unsafe_first_returns_empty_list(self) -> None:
        result = sort_pods_unsafe_first([])
        assert result == []

    def test_sort_pods_unsafe_first_pending_before_running(self) -> None:
        pending: PodInfo = {"name": "pending", "status": "Pending"}
        running: PodInfo = {"name": "running", "status": "Running"}

        result = sort_pods_unsafe_first([running, pending])

        assert result[0]["name"] == "pending"

    def test_sort_pods_unsafe_first_terminating_after_error(self) -> None:
        error: PodInfo = {"name": "error", "status": "Error"}
        terminating: PodInfo = {"name": "terminating", "status": "Terminating"}

        result = sort_pods_unsafe_first([terminating, error])

        assert result[0]["name"] == "error"

    def test_sort_pods_unsafe_first_unknown_status_at_end(self) -> None:
        unknown: PodInfo = {"name": "unknown", "status": "SomeUnknownStatus"}
        running: PodInfo = {"name": "running", "status": "Running"}

        result = sort_pods_unsafe_first([running, unknown])

        assert result[0]["name"] == "running"
