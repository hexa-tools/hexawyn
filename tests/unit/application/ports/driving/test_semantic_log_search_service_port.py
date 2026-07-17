from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_service_port import (
    SemanticLogSearchServicePort,
)


class TestSemanticLogSearchServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(SemanticLogSearchServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            SemanticLogSearchServicePort()  # type: ignore[abstract]
