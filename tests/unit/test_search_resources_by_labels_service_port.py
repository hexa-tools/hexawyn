from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_service_port import (
    SearchResourcesByLabelsServicePort,
)


class TestSearchResourcesByLabelsServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(SearchResourcesByLabelsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            SearchResourcesByLabelsServicePort()  # type: ignore[abstract]
