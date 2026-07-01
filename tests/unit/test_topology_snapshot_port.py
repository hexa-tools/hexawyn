from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort


class TestTopologySnapshotPort:
    def test_is_abstract(self) -> None:
        assert issubclass(TopologySnapshotPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            TopologySnapshotPort()  # type: ignore[abstract]
