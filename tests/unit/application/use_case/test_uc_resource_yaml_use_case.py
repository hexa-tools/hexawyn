"""Unit tests for ResourceYAMLUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.resource_yaml.resource_yaml_service_port import (
    ResourceYAMLServicePort,
)
from hexawyn.application.use_case.resource_yaml.resource_yaml_use_case import ResourceYAMLUseCase


class TestResourceYAMLUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ResourceYAMLServicePort)
        use_case = ResourceYAMLUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_resource.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ResourceYAMLServicePort)
        mock_service.get_resource.side_effect = RuntimeError("test error")
        use_case = ResourceYAMLUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
