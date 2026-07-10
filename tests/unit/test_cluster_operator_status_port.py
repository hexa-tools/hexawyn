from abc import ABC


class TestClusterOperatorStatusPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.cluster_operator_status_port import (
            ClusterOperatorStatusPort,
        )

        assert issubclass(ClusterOperatorStatusPort, ABC)

    def test_declares_list_cluster_operators(self) -> None:
        from hexawyn.application.ports.driven.cluster_operator_status_port import (
            ClusterOperatorStatusPort,
        )

        assert "list_cluster_operators" in ClusterOperatorStatusPort.__abstractmethods__


class TestClusterOperatorRawData:
    def test_shape(self) -> None:
        from hexawyn.application.ports.driven.cluster_operator_status_port import (
            ClusterOperatorRawData,
        )

        raw: ClusterOperatorRawData = {
            "name": "etcd",
            "available": True,
            "progressing": False,
            "degraded": True,
            "available_unknown": False,
            "message": "etcd member not responding",
            "degraded_since": "2026-06-16T01:00:00Z",
        }

        assert raw["name"] == "etcd"
        assert raw["degraded"] is True
        assert raw["degraded_since"] == "2026-06-16T01:00:00Z"
