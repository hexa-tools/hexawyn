from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.redundant_call_detection_port import (
    RedundantCallDetectionPort,
)


class TestRedundantCallDetectionPort:
    def test_is_abstract(self) -> None:
        assert issubclass(RedundantCallDetectionPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            RedundantCallDetectionPort()  # type: ignore[abstract]
