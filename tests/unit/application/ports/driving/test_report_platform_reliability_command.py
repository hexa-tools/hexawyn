import dataclasses


class TestReportPlatformReliabilityCommand:
    def test_holds_period(self) -> None:
        from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_command import (  # noqa: E501
            ReportPlatformReliabilityCommand,
        )

        command = ReportPlatformReliabilityCommand(period="2026-06")

        assert command.period == "2026-06"
        assert dataclasses.is_dataclass(ReportPlatformReliabilityCommand)
