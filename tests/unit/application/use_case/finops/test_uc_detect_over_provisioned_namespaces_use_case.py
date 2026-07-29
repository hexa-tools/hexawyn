from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.command import (  # noqa: E501
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_use_case import (  # noqa: E501
    DetectOverProvisionedNamespacesUseCase,
)
from hexawyn.application.use_case.finops.detect_over_provisioned_namespaces.response import (  # noqa: E501
    DetectOverProvisionedNamespacesResponse,
)


class TestDetectOverProvisionedNamespacesUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_all_namespace_waste_data.return_value = []

        use_case = DetectOverProvisionedNamespacesUseCase(
            waste_port=port,
        )
        result = use_case.detect_over_provisioned_namespaces(
            DetectOverProvisionedNamespacesCommand()
        )

        assert isinstance(result, DetectOverProvisionedNamespacesResponse)
