from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCheckMachineConfigPoolStatusMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.check_machine_config_pool_status import (
            check_machine_config_pool_status,
        )

        mock_port = MagicMock()
        mock_port.list_machine_config_pools.return_value = []

        with patch(
            "hexawyn.mcp.server.build_machine_config_pool_adapter",
            return_value=mock_port,
        ):
            result = check_machine_config_pool_status()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert result["total"] == 0
        assert result["pools"] == []

    def test_returns_pools_from_port(self) -> None:
        from hexawyn.mcp.tools.check_machine_config_pool_status import (
            check_machine_config_pool_status,
        )

        mock_port = MagicMock()
        mock_port.list_machine_config_pools.return_value = [
            {
                "name": "worker",
                "machine_count": 3,
                "ready_machine_count": 3,
                "updated_machine_count": 3,
                "degraded_machine_count": 0,
                "updating": False,
                "degraded": False,
                "paused": False,
                "current_config": "rendered-worker-abc",
                "desired_config": "rendered-worker-abc",
                "reason": "",
                "updating_since": None,
            },
        ]

        with patch(
            "hexawyn.mcp.server.build_machine_config_pool_adapter",
            return_value=mock_port,
        ):
            result = check_machine_config_pool_status()

        assert result["error"] is None
        assert result["total"] == 1
        assert result["all_healthy"] is True
        assert result["pools"][0]["name"] == "worker"  # type: ignore[index]

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.check_machine_config_pool_status import (
            check_machine_config_pool_status,
        )

        with patch(
            "hexawyn.mcp.server.build_machine_config_pool_adapter",
            side_effect=RuntimeError("openshift unreachable"),
        ):
            result = check_machine_config_pool_status()

        assert isinstance(result, dict)
        assert "openshift unreachable" in str(result["error"])
        assert result["total"] == 0
