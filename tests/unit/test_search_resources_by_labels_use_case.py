from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_response import (
    SearchResourcesByLabelsResponse,
)
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_service_port import (
    SearchResourcesByLabelsServicePort,
)
from hexawyn.application.use_case.search_resources_by_labels.search_resources_by_labels_use_case import (
    SearchResourcesByLabelsUseCase,
)


class TestSearchResourcesByLabelsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=SearchResourcesByLabelsServicePort)
        expected = SearchResourcesByLabelsResponse(label_selector="app=payment")
        service.search.return_value = expected
        use_case = SearchResourcesByLabelsUseCase(service=service)
        command = SearchResourcesByLabelsCommand(label_selector="app=payment")

        result = use_case.execute(command)

        service.search.assert_called_once_with(command)
        assert result is expected
