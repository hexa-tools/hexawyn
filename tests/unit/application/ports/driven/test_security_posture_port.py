from abc import ABC


class TestSecurityPosturePortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.security_posture_port import (
            SecurityPosturePort,
        )

        assert issubclass(SecurityPosturePort, ABC)

    def test_declares_required_methods(self) -> None:
        from hexawyn.application.ports.driven.security_posture_port import (
            SecurityPosturePort,
        )

        expected = {"list_workload_compliance", "get_defined_categories", "is_partial"}

        assert expected <= SecurityPosturePort.__abstractmethods__


class TestWorkloadComplianceRaw:
    def test_shape(self) -> None:
        from hexawyn.application.ports.driven.security_posture_port import (
            WorkloadComplianceRaw,
        )

        raw: WorkloadComplianceRaw = {
            "workload": "payment-api",
            "namespace": "production",
            "category": "tls",
            "compliant": False,
            "exempt": False,
            "detail": "No TLS configured",
        }

        assert raw["workload"] == "payment-api"
        assert raw["category"] == "tls"
        assert raw["compliant"] is False
