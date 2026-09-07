from __future__ import annotations

from abc import ABC

from hexawyn.application.ports.driving.container_image_drift.container_image_drift_service_port import (  # noqa: E501
    ContainerImageDriftServicePort,
)


class TestContainerImageDriftServicePort:
    def test_port_is_abstract(self) -> None:
        assert issubclass(ContainerImageDriftServicePort, ABC)

    def test_port_defines_detect_image_drift(self) -> None:
        assert hasattr(ContainerImageDriftServicePort, "detect_image_drift")
