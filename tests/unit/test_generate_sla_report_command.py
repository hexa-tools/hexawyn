import dataclasses


class TestGenerateSlaReportCommand:
    def test_holds_quarter(self) -> None:
        from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_command import (  # noqa: E501
            GenerateSlaReportCommand,
        )

        command = GenerateSlaReportCommand(quarter="2026-Q1")

        assert command.quarter == "2026-Q1"
        assert dataclasses.is_dataclass(GenerateSlaReportCommand)
