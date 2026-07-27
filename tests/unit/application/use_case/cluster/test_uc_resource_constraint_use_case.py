from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.resource_constraint.command import (
    ResourceConstraintCommand,
)
from hexawyn.application.use_case.cluster.resource_constraint.resource_constraint_use_case import (  # noqa: E501
    ResourceConstraintUseCase,
)
from hexawyn.application.use_case.cluster.resource_constraint.response import (
    ResourceConstraintResponse,
)


class TestResourceConstraintUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = []

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand(namespace="default"))

        assert isinstance(result, ResourceConstraintResponse)

    def test_execute_empty_namespace(self) -> None:
        port = MagicMock()
        port.list_container_resources.return_value = []

        use_case = ResourceConstraintUseCase(port=port)
        result = use_case.execute(ResourceConstraintCommand())

        assert result.total_pods == 0
        assert result.critical_count == 0
