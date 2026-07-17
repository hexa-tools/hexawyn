from abc import ABC


class TestCheckClusterOperatorHealthServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_service_port import (  # noqa: E501
            CheckClusterOperatorHealthServicePort,
        )

        assert issubclass(CheckClusterOperatorHealthServicePort, ABC)

    def test_declares_check_method(self) -> None:
        from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_service_port import (  # noqa: E501
            CheckClusterOperatorHealthServicePort,
        )

        assert "check" in CheckClusterOperatorHealthServicePort.__abstractmethods__
