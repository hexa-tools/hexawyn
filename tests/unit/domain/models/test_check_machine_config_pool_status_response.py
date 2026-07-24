from hexawyn.domain.models.machine_config_pool_health import (
    MachineConfigPoolHealthReport,
)


class TestCheckMachineConfigPoolStatusResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.use_case.check_machine_config_pool_status.response import (  # noqa: E501
            CheckMachineConfigPoolStatusResponse,
        )

        report = MachineConfigPoolHealthReport(total=3, healthy=1, degraded=1, updating=1)
        response = CheckMachineConfigPoolStatusResponse(result=report)

        assert response.result is report
        assert response.result.total == 3
