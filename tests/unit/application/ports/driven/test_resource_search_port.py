from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.resource_search_port import ResourceSearchPort


class TestResourceSearchPort:
    def test_is_abstract(self) -> None:
        assert issubclass(ResourceSearchPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ResourceSearchPort()  # type: ignore[abstract]
