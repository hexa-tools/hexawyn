from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_service_port import (
    LiveTopologyMapperServicePort,
)


class TestLiveTopologyMapperServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(LiveTopologyMapperServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            LiveTopologyMapperServicePort()  # type: ignore[abstract]
