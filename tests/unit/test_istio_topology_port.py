from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort


class TestIstioTopologyPort:
    def test_is_abstract(self) -> None:
        assert issubclass(IstioTopologyPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            IstioTopologyPort()  # type: ignore[abstract]
