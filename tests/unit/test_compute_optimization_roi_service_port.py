from abc import ABC


class TestComputeOptimizationRoiServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_service_port import (  # noqa: E501
            ComputeOptimizationRoiServicePort,
        )

        assert issubclass(ComputeOptimizationRoiServicePort, ABC)

    def test_declares_compute_method(self) -> None:
        from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_service_port import (  # noqa: E501
            ComputeOptimizationRoiServicePort,
        )

        assert "compute" in ComputeOptimizationRoiServicePort.__abstractmethods__
