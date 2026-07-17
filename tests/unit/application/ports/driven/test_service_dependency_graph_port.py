from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)


class TestServiceDependencyGraphPort:
    def test_is_abstract(self) -> None:
        assert issubclass(ServiceDependencyGraphPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ServiceDependencyGraphPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        assert getattr(
            getattr(ServiceDependencyGraphPort, "fetch_edges"), "__isabstractmethod__", False
        )
