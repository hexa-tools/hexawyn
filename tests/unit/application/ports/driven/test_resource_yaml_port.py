from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort


class TestResourceYAMLPort:
    def test_is_abstract(self) -> None:
        assert issubclass(ResourceYAMLPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ResourceYAMLPort()  # type: ignore[abstract]
