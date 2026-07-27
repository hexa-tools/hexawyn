from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.networking.east_west_network_segmentation.command import (
    EastWestNetworkSegmentationCommand,
)
from hexawyn.application.use_case.networking.east_west_network_segmentation.east_west_network_segmentation_use_case import (  # noqa: E501
    EastWestNetworkSegmentationUseCase,
)
from hexawyn.application.use_case.networking.east_west_network_segmentation.response import (
    EastWestNetworkSegmentationResponse,
)


class TestEastWestNetworkSegmentationUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.audit_network_policies.return_value = []

        use_case = EastWestNetworkSegmentationUseCase(port=port)
        result = use_case.execute(EastWestNetworkSegmentationCommand())

        assert isinstance(result, EastWestNetworkSegmentationResponse)

    def test_execute_empty_namespace(self) -> None:
        port = MagicMock()
        port.audit_network_policies.return_value = []

        use_case = EastWestNetworkSegmentationUseCase(port=port)
        result = use_case.execute(EastWestNetworkSegmentationCommand())

        assert result.total_namespaces == 0
