from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolRawData,
)
from hexawyn.application.use_case.cluster.check_machine_config_pool_status.check_machine_config_pool_status_use_case import (  # noqa: E501
    CheckMachineConfigPoolStatusUseCase,
)
from hexawyn.application.use_case.cluster.check_machine_config_pool_status.command import (
    CheckMachineConfigPoolStatusCommand,
)
from hexawyn.application.use_case.cluster.check_machine_config_pool_status.response import (
    CheckMachineConfigPoolStatusResponse,
)
from hexawyn.domain.models.machine_config_pool_health import (
    MachineConfigPoolHealthReport,
)


def _make_raw_pool(  # noqa: PLR0913
    name: str = "worker",
    machine_count: int = 3,
    ready_machine_count: int = 3,
    updated_machine_count: int = 3,
    degraded_machine_count: int = 0,
    updating: bool = False,
    degraded: bool = False,
    paused: bool = False,
    current_config: str = "rendered-worker-abc",
    desired_config: str = "rendered-worker-abc",
    reason: str = "",
    updating_since: str | None = None,
) -> MachineConfigPoolRawData:  # noqa: PLR0913
    return {
        "name": name,
        "machine_count": machine_count,
        "ready_machine_count": ready_machine_count,
        "updated_machine_count": updated_machine_count,
        "degraded_machine_count": degraded_machine_count,
        "updating": updating,
        "degraded": degraded,
        "paused": paused,
        "current_config": current_config,
        "desired_config": desired_config,
        "reason": reason,
        "updating_since": updating_since,
    }


class TestCheckMachineConfigPoolStatusUseCase:
    def test_execute_returns_response_type(self) -> None:
        port = MagicMock()
        port.list_machine_config_pools.return_value = []

        use_case = CheckMachineConfigPoolStatusUseCase(machine_config_pool_port=port)
        result = use_case.execute(CheckMachineConfigPoolStatusCommand())

        assert isinstance(result, CheckMachineConfigPoolStatusResponse)
        assert isinstance(result.result, MachineConfigPoolHealthReport)

    def test_execute_delegates_to_port_and_service(self) -> None:
        port = MagicMock()
        port.list_machine_config_pools.return_value = [
            _make_raw_pool(name="worker"),
        ]

        use_case = CheckMachineConfigPoolStatusUseCase(machine_config_pool_port=port)
        result = use_case.execute(CheckMachineConfigPoolStatusCommand())

        port.list_machine_config_pools.assert_called_once()
        assert result.result.total == 1
        assert result.result.all_healthy is True
        assert result.result.pools[0].name == "worker"

    def test_execute_with_degraded_pool(self) -> None:
        port = MagicMock()
        port.list_machine_config_pools.return_value = [
            _make_raw_pool(name="worker", degraded=True, reason="NodeDegraded"),
        ]

        use_case = CheckMachineConfigPoolStatusUseCase(machine_config_pool_port=port)
        result = use_case.execute(CheckMachineConfigPoolStatusCommand())

        assert result.result.degraded == 1
        assert result.result.all_healthy is False
        assert result.result.pools[0].state == "degraded"

    def test_execute_with_mixed_pools(self) -> None:
        port = MagicMock()
        port.list_machine_config_pools.return_value = [
            _make_raw_pool(name="master"),
            _make_raw_pool(name="worker", degraded=True),
            _make_raw_pool(name="infra", paused=True),
        ]

        use_case = CheckMachineConfigPoolStatusUseCase(machine_config_pool_port=port)
        result = use_case.execute(CheckMachineConfigPoolStatusCommand())

        assert result.result.total == 3  # noqa: PLR2004
        assert result.result.healthy == 1  # noqa: PLR2004
        assert result.result.degraded == 1  # noqa: PLR2004
        assert result.result.paused == 1  # noqa: PLR2004
        assert result.result.all_healthy is False

    def test_execute_all_healthy_empty_pools(self) -> None:
        port = MagicMock()
        port.list_machine_config_pools.return_value = []

        use_case = CheckMachineConfigPoolStatusUseCase(machine_config_pool_port=port)
        result = use_case.execute(CheckMachineConfigPoolStatusCommand())

        assert result.result.total == 0
        assert result.result.all_healthy is True
