from __future__ import annotations

from abc import ABC

import pytest


class TestImageDriftPort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.image_drift_port import ImageDriftPort

        assert issubclass(ImageDriftPort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driven.image_drift_port import ImageDriftPort

        with pytest.raises(TypeError):
            ImageDriftPort()  # type: ignore[abstract]
