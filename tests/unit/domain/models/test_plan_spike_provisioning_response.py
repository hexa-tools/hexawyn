from hexawyn.domain.models.spike_provisioning import SpikeProvisioningReport


class TestPlanSpikeProvisioningResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.ports.driving.plan_spike_provisioning.plan_spike_provisioning_response import (  # noqa: E501
            PlanSpikeProvisioningResponse,
        )

        report = SpikeProvisioningReport(
            traffic_multiplier=2.8, multiplier_source="historical", verdict="provision"
        )
        response = PlanSpikeProvisioningResponse(result=report)

        assert response.result is report
        assert response.result.verdict == "provision"
