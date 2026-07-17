from __future__ import annotations

from abc import ABC

import pytest


class TestDetectUnintendedExternalExposureServicePort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_service_port import (
            DetectUnintendedExternalExposureServicePort,
        )

        assert issubclass(DetectUnintendedExternalExposureServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_service_port import (
            DetectUnintendedExternalExposureServicePort,
        )

        with pytest.raises(TypeError):
            DetectUnintendedExternalExposureServicePort()  # type: ignore[abstract]
