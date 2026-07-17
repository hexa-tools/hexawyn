import dataclasses


class TestDiffHelmValuesCommand:
    def test_holds_release_and_namespaces(self) -> None:
        from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_command import (
            DiffHelmValuesCommand,
        )

        command = DiffHelmValuesCommand(
            release="payment-service",
            source_namespace="staging",
            target_namespace="production",
        )

        assert command.release == "payment-service"
        assert command.source_namespace == "staging"
        assert command.target_namespace == "production"
        assert command.source_env == "staging"
        assert command.target_env == "production"

    def test_is_frozen_dataclass(self) -> None:
        from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_command import (
            DiffHelmValuesCommand,
        )

        assert dataclasses.is_dataclass(DiffHelmValuesCommand)
