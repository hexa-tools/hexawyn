from abc import ABC


class TestGenerateSlaReportServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_service_port import (  # noqa: E501
            GenerateSlaReportServicePort,
        )

        assert issubclass(GenerateSlaReportServicePort, ABC)

    def test_declares_generate_method(self) -> None:
        from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_service_port import (  # noqa: E501
            GenerateSlaReportServicePort,
        )

        assert "generate" in GenerateSlaReportServicePort.__abstractmethods__
