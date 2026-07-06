from abc import ABC, abstractmethod
from typing import TypedDict


class ProbeContainerRawData(TypedDict):
    container_name: str
    is_init_container: bool
    exposed_ports: list[int]
    has_liveness_probe: bool
    has_readiness_probe: bool
    liveness_probe_type: str
    readiness_probe_type: str
    liveness_http_path: str
    readiness_http_path: str
    liveness_port: int
    readiness_port: int


class ProbeDeploymentRawData(TypedDict):
    deployment_name: str
    namespace: str
    workload_type: str
    containers: list[ProbeContainerRawData]
    has_service: bool
    is_exposed_externally: bool


class ProbeAuditPort(ABC):
    @abstractmethod
    def get_probe_audit_data(
        self, namespace: str | None = None
    ) -> list[ProbeDeploymentRawData]: ...
