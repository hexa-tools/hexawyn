from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.adaptive_investigation_port import AdaptiveInvestigationPort


class TestAdaptiveInvestigationPort:
    def test_is_abstract(self) -> None:
        assert issubclass(AdaptiveInvestigationPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            AdaptiveInvestigationPort()  # type: ignore[abstract]
