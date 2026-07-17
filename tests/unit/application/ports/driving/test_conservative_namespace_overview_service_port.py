from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_service_port import (
    ConservativeNamespaceOverviewServicePort,
)


class TestConservativeNamespaceOverviewServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(ConservativeNamespaceOverviewServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ConservativeNamespaceOverviewServicePort()  # type: ignore[abstract]
