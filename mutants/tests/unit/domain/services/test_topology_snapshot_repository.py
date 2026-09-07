from __future__ import annotations

import json
from unittest.mock import MagicMock

from hexawyn.domain.services.topology.exporter import DependencyGraphExport
from hexawyn.infrastructure.memory.topology_snapshot_repository import (
    TopologySnapshotRepository,
)


def _graph_export() -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[],
        edges=[],
        single_points_of_failure=["auth-service"],
        orphan_nodes=[],
        cycles=[],
        inference_source="NETWORK_POLICY",
        truncated=False,
        namespace_scope=None,
    )


class TestTopologySnapshotRepository:
    def setup_method(self) -> None:
        self.mock_conn = MagicMock()
        self.repo = TopologySnapshotRepository(conn=self.mock_conn)

    def test_save_snapshot_executes_insert_with_serialized_json(self) -> None:
        self.repo.save_snapshot("prod-cluster", _graph_export())

        self.mock_conn.execute.assert_called_once()
        args, _ = self.mock_conn.execute.call_args
        params = args[1]
        assert params[0] == "prod-cluster"
        assert json.loads(params[1]) == _graph_export()

    def test_save_snapshot_failure_is_swallowed(self) -> None:
        self.mock_conn.execute.side_effect = Exception("db locked")

        self.repo.save_snapshot("prod-cluster", _graph_export())
