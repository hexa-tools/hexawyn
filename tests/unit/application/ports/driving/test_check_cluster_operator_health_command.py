class TestCheckClusterOperatorHealthCommand:
    def test_is_instantiable(self) -> None:
        from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_command import (  # noqa: E501
            CheckClusterOperatorHealthCommand,
        )

        assert CheckClusterOperatorHealthCommand() is not None

    def test_is_frozen(self) -> None:
        import dataclasses

        from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_command import (  # noqa: E501
            CheckClusterOperatorHealthCommand,
        )

        assert dataclasses.is_dataclass(CheckClusterOperatorHealthCommand)
