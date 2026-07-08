from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.log_search_port import LogSearchPort


class TestLogSearchPort:
    def test_is_abstract(self) -> None:
        assert issubclass(LogSearchPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            LogSearchPort()  # type: ignore[abstract]
