"""RED tests — application/ports/driven/rightsizing_port.py"""

from hexawyn.application.ports.driven.rightsizing_port import (
    RightsizingPort,
    WorkloadRawData,
)


class TestWorkloadRawData:
    def test_required_keys_present(self) -> None:
        data: WorkloadRawData = {
            "resource_name": "ml-worker",
            "namespace": "production",
            "kind": "Deployment",
            "cpu_requested_cores": 4.0,
            "memory_requested_mi": 8192.0,
            "cpu_actual_cores": 0.8,
            "memory_actual_mi": 2100.0,
        }
        assert data["resource_name"] == "ml-worker"
        assert data["kind"] == "Deployment"
        assert data["cpu_actual_cores"] == 0.8

    def test_actual_cores_can_be_none(self) -> None:
        data: WorkloadRawData = {
            "resource_name": "svc",
            "namespace": "ns",
            "kind": "StatefulSet",
            "cpu_requested_cores": 2.0,
            "memory_requested_mi": 4096.0,
            "cpu_actual_cores": None,
            "memory_actual_mi": None,
        }
        assert data["cpu_actual_cores"] is None
        assert data["memory_actual_mi"] is None


class TestRightsizingPortIsAbstract:
    def test_cannot_instantiate_directly(self) -> None:
        import pytest

        with pytest.raises(TypeError):
            RightsizingPort()  # type: ignore[abstract]

    def test_has_get_workload_rightsizing_data_method(self) -> None:
        assert hasattr(RightsizingPort, "get_workload_rightsizing_data")
