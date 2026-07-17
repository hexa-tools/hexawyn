from __future__ import annotations

from abc import ABC

import pytest


class TestContainerImageDriftServicePort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driving.container_image_drift.container_image_drift_service_port import (
            ContainerImageDriftServicePort,
        )

        assert issubclass(ContainerImageDriftServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driving.container_image_drift.container_image_drift_service_port import (
            ContainerImageDriftServicePort,
        )

        with pytest.raises(TypeError):
            ContainerImageDriftServicePort()  # type: ignore[abstract]
