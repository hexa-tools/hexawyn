from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort


class TestLiveResourcePort:
    def test_is_abstract(self) -> None:
        assert issubclass(LiveResourcePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            LiveResourcePort()  # type: ignore[abstract]
