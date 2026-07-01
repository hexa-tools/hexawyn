from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_command import (
    LiveTopologyMapperCommand,
)


class TestLiveTopologyMapperCommand:
    def test_default_namespace_is_none(self) -> None:
        command = LiveTopologyMapperCommand()
        assert command.namespace is None

    def test_namespace_field_populated(self) -> None:
        command = LiveTopologyMapperCommand(namespace="production")
        assert command.namespace == "production"

    def test_is_frozen(self) -> None:
        command = LiveTopologyMapperCommand(namespace="production")
        with pytest.raises(AttributeError):
            command.namespace = "staging"  # type: ignore[misc]
