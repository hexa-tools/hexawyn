from __future__ import annotations

from abc import ABC

import pytest


class TestCrossNamespaceTrafficPort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
            CrossNamespaceTrafficPort,
        )

        assert issubclass(CrossNamespaceTrafficPort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
            CrossNamespaceTrafficPort,
        )

        with pytest.raises(TypeError):
            CrossNamespaceTrafficPort()  # type: ignore[abstract]
