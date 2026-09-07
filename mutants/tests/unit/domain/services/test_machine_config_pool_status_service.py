from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolRawData,
)
from hexawyn.domain.services.machine_config_pool_status.machine_config_pool_status_service import (  # noqa: E501
    MachineConfigPoolStatusService,
)


def _make_pool(  # noqa: PLR0913
    name: str = "worker",
    machine_count: int = 3,
    ready_machine_count: int = 3,
    updated_machine_count: int = 3,
    degraded_machine_count: int = 0,
    updating: bool = False,
    degraded: bool = False,
    paused: bool = False,
    current_config: str = "rendered-abc",
    desired_config: str = "rendered-abc",
    reason: str = "",
    updating_since: str | None = None,
) -> MachineConfigPoolRawData:
    return {
        "name": name,
        "machine_count": machine_count,
        "ready_machine_count": ready_machine_count,
        "updated_machine_count": updated_machine_count,
        "degraded_machine_count": degraded_machine_count,
        "updating": updating,
        "degraded": degraded,
        "paused": paused,
        "current_config": current_config,
        "desired_config": desired_config,
        "reason": reason,
        "updating_since": updating_since,
    }


class TestMachineConfigPoolStatusService:
    def test_happy_path_all_healthy(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(name="master"),
            _make_pool(name="worker"),
        ]
        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.total == 2  # noqa: PLR2004
        assert report.healthy == 2  # noqa: PLR2004
        assert report.degraded == 0
        assert report.updating == 0
        assert report.paused == 0
        assert report.all_healthy is True

    def test_degraded_pool(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(name="worker", degraded=True, degraded_machine_count=2),
        ]
        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.degraded == 1
        assert report.healthy == 0
        assert report.all_healthy is False
        assert report.pools[0].state == "degraded"

    def test_updating_pool(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(name="worker", updating=True),
        ]
        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.updating == 1
        assert report.healthy == 0
        assert report.pools[0].state == "updating"

    def test_paused_pool(self) -> None:
        paused_now = datetime(2026, 7, 1, 12, 0, 0, tzinfo=UTC)

        def fixed_clock() -> datetime:
            return paused_now

        pools: list[MachineConfigPoolRawData] = [
            _make_pool(name="worker", paused=True, updating=True, degraded=True),
        ]
        service = MachineConfigPoolStatusService(clock=fixed_clock)
        report = service.evaluate(pools)

        assert report.paused == 1
        assert report.pools[0].state == "paused"

    def test_degraded_and_updating(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(name="worker", degraded=True, updating=True),
        ]

        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.pools[0].state == "degraded+updating"
        assert report.degraded == 1

    def test_config_mismatch_detected(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(
                name="worker",
                current_config="rendered-old",
                desired_config="rendered-new",
            ),
        ]
        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.pools[0].config_mismatch is True

    def test_config_match(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(current_config="rendered-v1", desired_config="rendered-v1"),
        ]
        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.pools[0].config_mismatch is False

    def test_updating_not_stuck_under_threshold(self) -> None:
        recent = datetime(2026, 7, 1, 12, 10, 0, tzinfo=UTC)

        def fixed_clock() -> datetime:
            return recent

        pools: list[MachineConfigPoolRawData] = [
            _make_pool(
                name="worker",
                updating=True,
                updating_since="2026-07-01T12:00:00Z",
            ),
        ]
        service = MachineConfigPoolStatusService(clock=fixed_clock)
        report = service.evaluate(pools)

        assert report.pools[0].is_stuck is False
        assert report.pools[0].updating_duration_minutes <= 30  # noqa: PLR2004

    def test_updating_stuck_beyond_threshold(self) -> None:
        stuck_time = datetime(2026, 7, 1, 13, 0, 0, tzinfo=UTC)

        def fixed_clock() -> datetime:
            return stuck_time

        pools: list[MachineConfigPoolRawData] = [
            _make_pool(
                name="worker",
                updating=True,
                updating_since="2026-07-01T12:00:00Z",
            ),
        ]
        service = MachineConfigPoolStatusService(clock=fixed_clock)
        report = service.evaluate(pools)

        assert report.pools[0].is_stuck is True
        assert report.pools[0].updating_duration_minutes > 30  # noqa: PLR2004

    def test_non_updating_state_has_zero_duration(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(name="worker", updating_since="2026-07-01T12:00:00Z"),
        ]
        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.pools[0].updating_duration_minutes == 0
        assert report.pools[0].is_stuck is False

    def test_updating_since_none_zero_duration(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(name="worker", updating=True, updating_since=None),
        ]
        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.pools[0].updating_duration_minutes == 0

    def test_invalid_updating_since_returns_zero(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(name="worker", updating=True, updating_since="not-a-date"),
        ]
        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.pools[0].updating_duration_minutes == 0

    def test_empty_pools_list(self) -> None:
        service = MachineConfigPoolStatusService()
        report = service.evaluate([])

        assert report.total == 0
        assert report.healthy == 0
        assert report.all_healthy is True

    def test_mixed_pools(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(name="master"),
            _make_pool(name="worker", updating=True),
            _make_pool(name="infra", degraded=True),
            _make_pool(name="edge", paused=True),
        ]
        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.total == 4  # noqa: PLR2004
        assert report.healthy == 1
        assert report.degraded == 1
        assert report.updating == 1
        assert report.paused == 1
        assert report.all_healthy is False

    def test_pool_with_reason_field(self) -> None:
        pools: list[MachineConfigPoolRawData] = [
            _make_pool(name="worker", degraded=True, reason="NodeNotReady"),
        ]
        service = MachineConfigPoolStatusService()
        report = service.evaluate(pools)

        assert report.pools[0].reason == "NodeNotReady"
