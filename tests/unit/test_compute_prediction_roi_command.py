import dataclasses


class TestComputePredictionRoiCommand:
    def test_holds_period(self) -> None:
        from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_command import (  # noqa: E501
            ComputePredictionRoiCommand,
        )

        command = ComputePredictionRoiCommand(period="2026-06")
        assert command.period == "2026-06"
        assert dataclasses.is_dataclass(ComputePredictionRoiCommand)
