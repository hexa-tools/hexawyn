from __future__ import annotations

import pytest
from hexawyn.domain.models.historical_pod import (
    HistoricalPod,
    HistoricalStateSnapshot,
    PodRestartStatus,
    StateComparison,
)


class TestHistoricalPod:
    def test_is_frozen_dataclass(self) -> None:
        pod = HistoricalPod(
            name="payment-pod-abc",
            namespace="payment",
            phase="Running",
            restart_count=0,
            queried_timestamp="2026-06-09T10:00:00Z",
        )
        with pytest.raises(AttributeError):
            pod.name = "changed"  # type: ignore[misc]

    def test_all_fields_required(self) -> None:
        pod = HistoricalPod(
            name="payment-pod-abc",
            namespace="payment",
            phase="Running",
            restart_count=0,
            queried_timestamp="2026-06-09T10:00:00Z",
        )
        assert pod.name == "payment-pod-abc"
        assert pod.namespace == "payment"
        assert pod.phase == "Running"
        assert pod.restart_count == 0
        assert pod.queried_timestamp == "2026-06-09T10:00:00Z"
        assert pod.currently_exists is True
        assert pod.status_changed_since is False

    def test_failing_pod_is_flagged(self) -> None:
        pod = HistoricalPod(
            name="payment-worker-xyz",
            namespace="payment",
            phase="CrashLoopBackOff",
            restart_count=23,
            queried_timestamp="2026-06-09T10:00:00Z",
        )
        assert pod.phase == "CrashLoopBackOff"
        assert pod.restart_count == 23  # noqa: PLR2004

    def test_high_restart_count_flagged(self) -> None:
        pod = HistoricalPod(
            name="payment-pod-def",
            namespace="payment",
            phase="Running",
            restart_count=8,
            queried_timestamp="2026-06-09T10:00:00Z",
        )
        assert pod.restart_count > 5  # noqa: PLR2004


class TestHistoricalStateSnapshot:
    def test_creates_with_test_data(self) -> None:
        pods = [
            HistoricalPod(
                name="payment-pod-abc",
                namespace="payment",
                phase="Running",
                restart_count=0,
                queried_timestamp="2026-06-09T10:00:00Z",
            ),
            HistoricalPod(
                name="payment-pod-def",
                namespace="payment",
                phase="Running",
                restart_count=8,
                queried_timestamp="2026-06-09T10:00:00Z",
            ),
            HistoricalPod(
                name="payment-worker-xyz",
                namespace="payment",
                phase="CrashLoopBackOff",
                restart_count=23,
                queried_timestamp="2026-06-09T10:00:00Z",
            ),
        ]
        snapshot = HistoricalStateSnapshot(
            namespace="payment",
            resource_type="pods",
            queried_timestamp="2026-06-09T10:00:00Z",
            total_resources=8,
            pods=pods,
        )
        assert snapshot.namespace == "payment"
        assert snapshot.total_resources == 8  # noqa: PLR2004
        assert len(snapshot.pods) == 3  # noqa: PLR2004

    def test_empty_snapshot_no_pods_found(self) -> None:
        snapshot = HistoricalStateSnapshot(
            namespace="empty-ns",
            resource_type="pods",
            queried_timestamp="2026-06-09T10:00:00Z",
            total_resources=0,
            pods=[],
        )
        assert snapshot.total_resources == 0
        assert len(snapshot.pods) == 0

    def test_restarting_pods_filtered(self) -> None:
        pods = [
            HistoricalPod(
                name="stable-a",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="t",
            ),
            HistoricalPod(
                name="restarter-b",
                namespace="ns",
                phase="Running",
                restart_count=8,
                queried_timestamp="t",
            ),
            HistoricalPod(
                name="crash-c",
                namespace="ns",
                phase="CrashLoopBackOff",
                restart_count=23,
                queried_timestamp="t",
            ),
            HistoricalPod(
                name="stable-d",
                namespace="ns",
                phase="Running",
                restart_count=2,
                queried_timestamp="t",
            ),
        ]
        snapshot = HistoricalStateSnapshot(
            namespace="ns",
            resource_type="pods",
            queried_timestamp="t",
            total_resources=4,
            pods=pods,
        )
        restarting = snapshot.get_restarting_pods(threshold=5)
        assert len(restarting) == 2  # noqa: PLR2004
        assert restarting[0].name == "restarter-b"
        assert restarting[1].name == "crash-c"

    def test_failing_pods_filtered(self) -> None:
        pods = [
            HistoricalPod(
                name="running-a",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="t",
            ),
            HistoricalPod(
                name="crashloop-b",
                namespace="ns",
                phase="CrashLoopBackOff",
                restart_count=5,
                queried_timestamp="t",
            ),
            HistoricalPod(
                name="error-c",
                namespace="ns",
                phase="Error",
                restart_count=3,
                queried_timestamp="t",
            ),
        ]
        snapshot = HistoricalStateSnapshot(
            namespace="ns",
            resource_type="pods",
            queried_timestamp="t",
            total_resources=3,
            pods=pods,
        )
        failing = snapshot.get_failing_pods()
        assert len(failing) == 2  # noqa: PLR2004
        names = {p.name for p in failing}
        assert names == {"crashloop-b", "error-c"}


class TestStateComparison:
    def test_delta_shows_added_pods(self) -> None:
        historical = [
            HistoricalPod(
                name="pod-a",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="t",
            ),
            HistoricalPod(
                name="pod-b",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="t",
            ),
        ]
        current = [
            HistoricalPod(
                name="pod-a",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="now",
            ),
            HistoricalPod(
                name="pod-b",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="now",
            ),
            HistoricalPod(
                name="pod-c",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="now",
            ),
        ]
        comparison = StateComparison.compare(
            namespace="ns",
            historical_pods=historical,
            current_pods=current,
            historical_timestamp="t",
        )
        assert comparison.historical_count == 2  # noqa: PLR2004
        assert comparison.current_count == 3  # noqa: PLR2004
        assert comparison.pods_added == 1
        assert comparison.pods_removed == 0
        assert "pod-c" in comparison.added_pod_names

    def test_delta_shows_removed_pods(self) -> None:
        historical = [
            HistoricalPod(
                name="pod-a",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="t",
            ),
            HistoricalPod(
                name="pod-b",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="t",
            ),
            HistoricalPod(
                name="pod-c",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="t",
            ),
        ]
        current = [
            HistoricalPod(
                name="pod-a",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="now",
            ),
        ]
        comparison = StateComparison.compare(
            namespace="ns",
            historical_pods=historical,
            current_pods=current,
            historical_timestamp="t",
        )
        assert comparison.historical_count == 3  # noqa: PLR2004
        assert comparison.current_count == 1
        assert comparison.pods_added == 0
        assert comparison.pods_removed == 2  # noqa: PLR2004
        assert "pod-b" in comparison.removed_pod_names
        assert "pod-c" in comparison.removed_pod_names

    def test_no_delta_when_same(self) -> None:
        historical = [
            HistoricalPod(
                name="pod-a",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="t",
            ),
        ]
        current = [
            HistoricalPod(
                name="pod-a",
                namespace="ns",
                phase="Running",
                restart_count=1,
                queried_timestamp="now",
            ),
        ]
        comparison = StateComparison.compare(
            namespace="ns",
            historical_pods=historical,
            current_pods=current,
            historical_timestamp="t",
        )
        assert comparison.pods_added == 0
        assert comparison.pods_removed == 0

    def test_empty_current(self) -> None:
        historical = [
            HistoricalPod(
                name="pod-a",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="t",
            ),
        ]
        comparison = StateComparison.compare(
            namespace="ns",
            historical_pods=historical,
            current_pods=[],
            historical_timestamp="t",
        )
        assert comparison.historical_count == 1
        assert comparison.current_count == 0
        assert comparison.pods_removed == 1

    def test_deleted_pods_shown(self) -> None:
        historical = [
            HistoricalPod(
                name="pod-a",
                namespace="ns",
                phase="Running",
                restart_count=0,
                queried_timestamp="t",
                currently_exists=False,
            ),
        ]
        comparison = StateComparison.compare(
            namespace="ns",
            historical_pods=historical,
            current_pods=[],
            historical_timestamp="t",
        )
        assert comparison.pods_removed == 1


class TestPodRestartStatus:
    def test_failing_phase_is_restart_flagged(self) -> None:
        pod = HistoricalPod(
            name="pod-a",
            namespace="ns",
            phase="CrashLoopBackOff",
            restart_count=10,
            queried_timestamp="t",
        )
        status = PodRestartStatus.from_pod(pod)
        assert status.is_restarting
        assert status.is_failing

    def test_high_restarts_not_failing_phase(self) -> None:
        pod = HistoricalPod(
            name="pod-a",
            namespace="ns",
            phase="Running",
            restart_count=8,
            queried_timestamp="t",
        )
        status = PodRestartStatus.from_pod(pod)
        assert status.is_restarting
        assert not status.is_failing

    def test_stable_pod(self) -> None:
        pod = HistoricalPod(
            name="pod-a",
            namespace="ns",
            phase="Running",
            restart_count=0,
            queried_timestamp="t",
        )
        status = PodRestartStatus.from_pod(pod)
        assert not status.is_restarting
        assert not status.is_failing
