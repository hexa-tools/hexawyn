from abc import ABC


class TestComputePredictionRoiServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_service_port import (  # noqa: E501
            ComputePredictionRoiServicePort,
        )

        assert issubclass(ComputePredictionRoiServicePort, ABC)

    def test_declares_compute_method(self) -> None:
        from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_service_port import (  # noqa: E501
            ComputePredictionRoiServicePort,
        )

        assert "compute" in ComputePredictionRoiServicePort.__abstractmethods__
