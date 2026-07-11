from abc import ABC


class TestPlanSpikeProvisioningServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_service_port import (  # noqa: E501
            PlanSpikeProvisioningServicePort,
        )

        assert issubclass(PlanSpikeProvisioningServicePort, ABC)

    def test_declares_plan_method(self) -> None:
        from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_service_port import (  # noqa: E501
            PlanSpikeProvisioningServicePort,
        )

        assert "plan" in PlanSpikeProvisioningServicePort.__abstractmethods__
