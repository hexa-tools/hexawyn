import dataclasses


class TestPlanSpikeProvisioningCommand:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_command import (  # noqa: E501
            PlanSpikeProvisioningCommand,
        )

        command = PlanSpikeProvisioningCommand(event_date="2026-11-27")

        assert command.event_date == "2026-11-27"
        assert command.traffic_multiplier is None
        assert command.provider_lead_time_hours == 24
        assert command.safety_margin_days == 3
        assert command.safe_threshold_pct == 85.0
        assert command.unpredictable is False

    def test_holds_values(self) -> None:
        from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_command import (  # noqa: E501
            PlanSpikeProvisioningCommand,
        )

        command = PlanSpikeProvisioningCommand(
            event_date="2026-11-27", traffic_multiplier=2.8, unpredictable=True
        )

        assert command.traffic_multiplier == 2.8
        assert command.unpredictable is True
        assert dataclasses.is_dataclass(PlanSpikeProvisioningCommand)
