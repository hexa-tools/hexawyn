import dataclasses


class TestComputeSecurityPostureCommand:
    def test_defaults_to_no_previous_score(self) -> None:
        from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_command import (  # noqa: E501
            ComputeSecurityPostureCommand,
        )

        command = ComputeSecurityPostureCommand()

        assert command.previous_score_pct is None

    def test_holds_previous_score(self) -> None:
        from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_command import (  # noqa: E501
            ComputeSecurityPostureCommand,
        )

        command = ComputeSecurityPostureCommand(previous_score_pct=75.0)

        assert command.previous_score_pct == 75.0
        assert dataclasses.is_dataclass(ComputeSecurityPostureCommand)
