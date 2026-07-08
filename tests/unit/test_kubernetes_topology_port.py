from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.kubernetes_topology_port import (
    EdgeRecordData,
    KubernetesTopologyPort,
    ServiceRecordData,
)


class TestKubernetesTopologyPort:
    def test_is_abstract(self) -> None:
        assert issubclass(KubernetesTopologyPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            KubernetesTopologyPort()  # type: ignore[abstract]

    def test_service_record_data_typed_dict(self) -> None:
        record: ServiceRecordData = {
            "name": "auth-service",
            "namespace": "production",
            "replicas": 1,
            "is_external": False,
        }
        assert record["name"] == "auth-service"

    def test_edge_record_data_typed_dict(self) -> None:
        edge: EdgeRecordData = {"caller": "api-gateway", "callee": "auth-service"}
        assert edge["callee"] == "auth-service"
