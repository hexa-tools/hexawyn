from abc import ABC


class TestComputeSecurityPostureServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_service_port import (  # noqa: E501
            ComputeSecurityPostureServicePort,
        )

        assert issubclass(ComputeSecurityPostureServicePort, ABC)

    def test_declares_compute_method(self) -> None:
        from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_service_port import (  # noqa: E501
            ComputeSecurityPostureServicePort,
        )

        assert "compute" in ComputeSecurityPostureServicePort.__abstractmethods__
