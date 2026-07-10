from abc import ABC, abstractmethod
from typing import TypedDict


class MachineConfigPoolRawData(TypedDict):
    name: str
    machine_count: int
    ready_machine_count: int
    updated_machine_count: int
    degraded_machine_count: int
    updating: bool
    degraded: bool
    paused: bool
    current_config: str
    desired_config: str
    reason: str
    updating_since: str | None


class MachineConfigPoolPort(ABC):
    """Driven port — reads MachineConfigPool status from an OpenShift cluster.

    MachineConfigPools live in the machineconfiguration.openshift.io/v1 API
    group and expose Updating / Degraded conditions plus machine counts and the
    current/desired rendered MachineConfig.
    """

    @abstractmethod
    def list_machine_config_pools(self) -> list[MachineConfigPoolRawData]:
        """Return every MachineConfigPool with its parsed status.

        Raises MachineConfigPoolCRDNotFoundError when the CRD is absent (404,
        e.g. vanilla Kubernetes).
        Raises InsufficientPermissionsError on RBAC 403.
        Raises ClusterUnreachableError on other API failures.
        """
