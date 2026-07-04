from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewPort


class TestNamespaceOverviewPort:
    def test_is_abstract(self) -> None:
        assert issubclass(NamespaceOverviewPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            NamespaceOverviewPort()  # type: ignore[abstract]
