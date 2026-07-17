"""Unit tests for CheckMachineConfigPoolStatusUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_service_port import (
    CheckMachineConfigPoolStatusServicePort,
)
from hexawyn.application.use_case.check_machine_config_pool_status.check_machine_config_pool_status_use_case import (
    CheckMachineConfigPoolStatusUseCase,
)


class TestCheckMachineConfigPoolStatusUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CheckMachineConfigPoolStatusServicePort)
        use_case = CheckMachineConfigPoolStatusUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.check.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CheckMachineConfigPoolStatusServicePort)
        mock_service.check.side_effect = RuntimeError("test error")
        use_case = CheckMachineConfigPoolStatusUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
