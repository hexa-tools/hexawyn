from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_service_port import (
    AdvancedNamespaceEventAnalyticsServicePort,
)


class TestAdvancedNamespaceEventAnalyticsServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(AdvancedNamespaceEventAnalyticsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            AdvancedNamespaceEventAnalyticsServicePort()  # type: ignore[abstract]
