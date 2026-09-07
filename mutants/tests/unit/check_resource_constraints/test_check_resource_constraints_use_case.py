from __future__ import annotations

from unittest.mock import MagicMock


class TestCheckResourceConstraintsUseCase:
    def test_execute_returns_response(self) -> None:
        from hexawyn.application.use_case.cluster.check_resource_constraints.check_resource_constraints_use_case import (  # noqa: E501
            CheckResourceConstraintsUseCase,
        )
        from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
            CheckResourceConstraintsCommand,
        )
        from hexawyn.application.use_case.cluster.check_resource_constraints.response import (
            CheckResourceConstraintsResponse,
        )

        port = MagicMock()
        port.list_container_resources.return_value = []
        use_case = CheckResourceConstraintsUseCase(port=port)
        result = use_case.execute(CheckResourceConstraintsCommand())
        assert isinstance(result, CheckResourceConstraintsResponse)
