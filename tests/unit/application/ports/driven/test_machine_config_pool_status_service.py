from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolRawData,
)


def _now() -> datetime:
    return datetime(2026, 6, 16, 3, 0, 0, tzinfo=UTC)


def _raw(
    name: str,
    machine_count: int = 3,
    ready: int = 3,
    updated: int = 3,
    degraded_count: int = 0,
    updating: bool = False,
    degraded: bool = False,
    paused: bool = False,
    current: str = "rendered-abc",
    desired: str = "rendered-abc",
    reason: str = "",
    updating_since: str | None = None,
) -> MachineConfigPoolRawData:
    return MachineConfigPoolRawData(
        name=name,
        machine_count=machine_count,
        ready_machine_count=ready,
        updated_machine_count=updated,
        degraded_machine_count=degraded_count,
        updating=updating,
        degraded=degraded,
        paused=paused,
        current_config=current,
        desired_config=desired,
        reason=reason,
        updating_since=updating_since,
    )


class TestSummary:
    def test_three_pools_master_ready_worker_updating_infra_degraded(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [
            _raw("master", machine_count=3, ready=3, updated=3),
            _raw(
                "worker",
                machine_count=5,
                ready=3,
                updated=2,
                updating=True,
                current="rendered-worker-old456",
                desired="rendered-worker-new789",
            ),
            _raw(
                "infra",
                machine_count=1,
                ready=0,
                updated=0,
                degraded_count=1,
                degraded=True,
                reason="failed to apply MachineConfig rendered-infra-xyz",
            ),
        ]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.total == 3
        assert report.healthy == 1
        assert report.degraded == 1
        assert report.updating == 1
        assert report.all_healthy is False

    def test_all_ready_is_all_healthy(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [_raw("master"), _raw("worker", machine_count=5, ready=5, updated=5)]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.all_healthy is True
        assert report.healthy == 2
        assert report.degraded == 0

    def test_single_node_cluster_master_one_machine(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [_raw("master", machine_count=1, ready=1, updated=1)]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.total == 1
        assert report.pools[0].machine_count == 1
        assert report.pools[0].state == "ready"


class TestStateClassification:
    def test_degraded_pool_surfaces_reason_and_count(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [
            _raw(
                "infra",
                degraded=True,
                degraded_count=1,
                reason="failed to apply MachineConfig rendered-infra-xyz",
            )
        ]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].state == "degraded"
        assert report.pools[0].degraded_machine_count == 1
        assert report.pools[0].reason == "failed to apply MachineConfig rendered-infra-xyz"

    def test_degraded_and_updating_combined_state(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [_raw("worker", updating=True, degraded=True, degraded_count=1)]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].state == "degraded+updating"
        assert report.degraded == 1
        assert report.updating == 0

    def test_paused_pool_is_not_degraded(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [
            _raw(
                "worker",
                paused=True,
                updating=True,
                current="rendered-old",
                desired="rendered-new",
            )
        ]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].state == "paused"
        assert report.pools[0].paused is True
        assert report.paused == 1
        assert report.degraded == 0

    def test_config_mismatch_flagged(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [_raw("worker", updating=True, current="rendered-old", desired="rendered-new")]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].config_mismatch is True

    def test_matching_config_not_flagged(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [_raw("master", current="rendered-same", desired="rendered-same")]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].config_mismatch is False

    def test_empty_pool_zero_machine_count(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [_raw("worker", machine_count=0, ready=0, updated=0)]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].machine_count == 0
        assert report.pools[0].state == "ready"


class TestStuckDetection:
    def test_updating_ten_minutes_is_not_stuck(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        since = (_now() - timedelta(minutes=10)).isoformat().replace("+00:00", "Z")
        pools = [_raw("worker", updating=True, updating_since=since)]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].is_stuck is False
        assert report.pools[0].updating_duration_minutes == 10

    def test_updating_over_thirty_minutes_is_stuck(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        since = (_now() - timedelta(minutes=45)).isoformat().replace("+00:00", "Z")
        pools = [_raw("worker", updating=True, updating_since=since)]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].is_stuck is True
        assert report.pools[0].updating_duration_minutes == 45

    def test_exactly_thirty_minutes_is_not_stuck(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        since = (_now() - timedelta(minutes=30)).isoformat().replace("+00:00", "Z")
        pools = [_raw("worker", updating=True, updating_since=since)]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].is_stuck is False

    def test_ready_pool_is_never_stuck(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        since = (_now() - timedelta(hours=5)).isoformat().replace("+00:00", "Z")
        pools = [_raw("master", updating_since=since)]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].is_stuck is False
        assert report.pools[0].updating_duration_minutes == 0

    def test_missing_updating_since_is_not_stuck(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [_raw("worker", updating=True, updating_since=None)]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].updating_duration_minutes == 0
        assert report.pools[0].is_stuck is False

    def test_malformed_updating_since_is_not_stuck(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [_raw("worker", updating=True, updating_since="not-a-date")]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].updating_duration_minutes == 0
        assert report.pools[0].is_stuck is False

    def test_default_clock_used_when_none_injected(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        since = "2020-01-01T00:00:00Z"
        report = MachineConfigPoolStatusService().evaluate(
            [_raw("worker", updating=True, updating_since=since)]
        )

        assert report.pools[0].is_stuck is True
        assert report.pools[0].updating_duration_minutes > 30


class TestOrdering:
    def test_unhealthy_pools_listed_first(self) -> None:
        from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
            MachineConfigPoolStatusService,
        )

        pools = [
            _raw("master"),
            _raw("worker", updating=True),
            _raw("infra", degraded=True, degraded_count=1),
        ]

        report = MachineConfigPoolStatusService(clock=_now).evaluate(pools)

        assert report.pools[0].name == "infra"
        assert report.pools[1].name == "worker"
        assert report.pools[2].name == "master"
