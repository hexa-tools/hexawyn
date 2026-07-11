import dataclasses


class TestComputeOptimizationRoiCommand:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_command import (  # noqa: E501
            ComputeOptimizationRoiCommand,
        )

        command = ComputeOptimizationRoiCommand(sprint_id="sprint-42")

        assert command.sprint_id == "sprint-42"
        assert command.traffic_growth_pct == 0.0

    def test_holds_values(self) -> None:
        from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_command import (  # noqa: E501
            ComputeOptimizationRoiCommand,
        )

        command = ComputeOptimizationRoiCommand(sprint_id="s1", traffic_growth_pct=20.0)

        assert command.traffic_growth_pct == 20.0
        assert dataclasses.is_dataclass(ComputeOptimizationRoiCommand)
