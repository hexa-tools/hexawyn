from hexawyn.domain.models.topology_snapshot import TopologySnapshot


class TestTopologySnapshot:
    def test_minimal_construction(self) -> None:
        entry = TopologySnapshot(cluster_name="prod-eu")
        assert entry.cluster_name == "prod-eu"
        assert entry.snapshot == {}

    def test_full_construction_with_snapshot(self) -> None:
        entry = TopologySnapshot(
            cluster_name="prod-eu",
            snapshot={
                "nodes": 6,
                "pods": 142,
                "services": 18,
                "namespaces": ["prod", "staging", "monitoring"],
            },
        )
        assert entry.cluster_name == "prod-eu"
        assert entry.snapshot == {
            "nodes": 6,
            "pods": 142,
            "services": 18,
            "namespaces": ["prod", "staging", "monitoring"],
        }

    def test_is_dataclass(self) -> None:
        entry = TopologySnapshot(cluster_name="test")
        assert hasattr(entry, "__dataclass_fields__")

    def test_node_count_returns_zero_when_no_nodes_key(self) -> None:
        entry = TopologySnapshot(cluster_name="empty")
        assert entry.node_count == 0

    def test_node_count_extracts_from_snapshot(self) -> None:
        entry = TopologySnapshot(cluster_name="big", snapshot={"nodes": 24, "pods": 500})
        assert entry.node_count == 24  # noqa: PLR2004

    def test_pod_count_returns_zero_when_missing(self) -> None:
        entry = TopologySnapshot(cluster_name="empty")
        assert entry.pod_count == 0

    def test_pod_count_extracts_from_snapshot(self) -> None:
        entry = TopologySnapshot(cluster_name="busy", snapshot={"nodes": 3, "pods": 89})
        assert entry.pod_count == 89  # noqa: PLR2004

    def test_namespace_count_returns_zero_when_missing(self) -> None:
        entry = TopologySnapshot(cluster_name="empty")
        assert entry.namespace_count == 0

    def test_namespace_count_from_list(self) -> None:
        entry = TopologySnapshot(
            cluster_name="multi",
            snapshot={"namespaces": ["prod", "staging", "dev", "monitoring"]},
        )
        assert entry.namespace_count == 4  # noqa: PLR2004

    def test_service_count_extracts_from_snapshot(self) -> None:
        entry = TopologySnapshot(cluster_name="mesh", snapshot={"services": 12})
        assert entry.service_count == 12  # noqa: PLR2004

    def test_from_dict_constructs_full_object(self) -> None:
        data: dict[str, object] = {
            "cluster_name": "prod-us",
            "snapshot": {"nodes": 10, "pods": 200, "services": 25},
        }
        entry = TopologySnapshot.from_dict(data)
        assert entry.cluster_name == "prod-us"
        assert entry.node_count == 10  # noqa: PLR2004
        assert entry.pod_count == 200  # noqa: PLR2004
        assert entry.service_count == 25  # noqa: PLR2004

    def test_from_dict_uses_defaults(self) -> None:
        entry = TopologySnapshot.from_dict({"cluster_name": "bare"})
        assert entry.cluster_name == "bare"
        assert entry.snapshot == {}
        assert entry.node_count == 0

    def test_from_dict_with_list_count_returns_zero(self) -> None:
        entry = TopologySnapshot.from_dict(
            {"cluster_name": "odd", "snapshot": {"nodes": [1, 2, 3]}}
        )
        assert entry.node_count == 0
