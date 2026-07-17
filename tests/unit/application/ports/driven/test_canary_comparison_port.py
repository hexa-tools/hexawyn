from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.canary_comparison_port import CanaryComparisonPort


class TestCanaryComparisonPort:
    def test_is_abstract(self) -> None:
        assert issubclass(CanaryComparisonPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            CanaryComparisonPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        assert getattr(
            getattr(CanaryComparisonPort, "fetch_stable_metrics"), "__isabstractmethod__", False
        )
        assert getattr(
            getattr(CanaryComparisonPort, "fetch_canary_metrics"), "__isabstractmethod__", False
        )
