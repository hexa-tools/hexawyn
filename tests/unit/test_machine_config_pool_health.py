from dataclasses import fields


class TestMachineConfigPoolStatus:
    def test_is_frozen_dataclass_with_expected_fields(self) -> None:
        from hexawyn.domain.models.machine_config_pool_health import (
            MachineConfigPoolStatus,
        )

        field_names = {f.name for f in fields(MachineConfigPoolStatus)}

        assert field_names == {
            "name",
            "state",
            "machine_count",
            "ready_machine_count",
            "updated_machine_count",
            "degraded_machine_count",
            "current_config",
            "desired_config",
            "config_mismatch",
            "paused",
            "reason",
            "updating_duration_minutes",
            "is_stuck",
        }

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.machine_config_pool_health import (
            MachineConfigPoolStatus,
        )

        status = MachineConfigPoolStatus(
            name="worker",
            state="updating",
            machine_count=5,
            ready_machine_count=3,
            updated_machine_count=2,
            degraded_machine_count=0,
            current_config="rendered-worker-old456",
            desired_config="rendered-worker-new789",
            config_mismatch=True,
            paused=False,
            reason="",
            updating_duration_minutes=45,
            is_stuck=True,
        )

        assert status.name == "worker"
        assert status.state == "updating"
        assert status.is_stuck is True
        assert status.config_mismatch is True


class TestMachineConfigPoolHealthReport:
    def test_defaults_to_all_healthy_empty(self) -> None:
        from hexawyn.domain.models.machine_config_pool_health import (
            MachineConfigPoolHealthReport,
        )

        report = MachineConfigPoolHealthReport()

        assert report.pools == []
        assert report.total == 0
        assert report.healthy == 0
        assert report.degraded == 0
        assert report.updating == 0
        assert report.paused == 0
        assert report.all_healthy is True

    def test_holds_summary(self) -> None:
        from hexawyn.domain.models.machine_config_pool_health import (
            MachineConfigPoolHealthReport,
        )

        report = MachineConfigPoolHealthReport(
            total=3, healthy=1, degraded=1, updating=1, all_healthy=False
        )

        assert report.total == 3
        assert report.degraded == 1
        assert report.all_healthy is False
