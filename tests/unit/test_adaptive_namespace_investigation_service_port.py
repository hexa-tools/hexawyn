from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_service_port import (
    AdaptiveNamespaceInvestigationServicePort,
)


class TestAdaptiveNamespaceInvestigationServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(AdaptiveNamespaceInvestigationServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            AdaptiveNamespaceInvestigationServicePort()  # type: ignore[abstract]
