from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort


class TestErrorAttributionPort:
    def test_is_abstract(self) -> None:
        assert issubclass(ErrorAttributionPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ErrorAttributionPort()  # type: ignore[abstract]
