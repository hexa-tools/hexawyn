from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TopologySnapshot:
    cluster_name: str
    snapshot: dict[str, object] = field(default_factory=dict)

    @property
    def node_count(self) -> int:
        return _get_int(self.snapshot, "nodes")

    @property
    def pod_count(self) -> int:
        return _get_int(self.snapshot, "pods")

    @property
    def service_count(self) -> int:
        return _get_int(self.snapshot, "services")

    @property
    def namespace_count(self) -> int:
        namespaces = self.snapshot.get("namespaces")
        if isinstance(namespaces, list):
            return len(namespaces)
        return _get_int(self.snapshot, "namespaces")

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> TopologySnapshot:
        raw_snapshot = data.get("snapshot", {})
        if isinstance(raw_snapshot, dict):
            snapshot: dict[str, object] = raw_snapshot
        else:
            snapshot = {}
        return cls(
            cluster_name=str(data.get("cluster_name", "")),
            snapshot=snapshot,
        )


def _get_int(source: dict[str, object], key: str) -> int:
    value = source.get(key, 0)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return 0
