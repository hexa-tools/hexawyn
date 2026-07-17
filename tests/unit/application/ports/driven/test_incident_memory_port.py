from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.incident_memory_port import IncidentMemoryPort


class TestIncidentMemoryPort:
    def test_is_abstract(self) -> None:
        assert issubclass(IncidentMemoryPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            IncidentMemoryPort()  # type: ignore[abstract]
