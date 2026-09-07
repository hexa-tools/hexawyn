from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.detect_missing_probes.command import (  # noqa: E501
    DetectMissingProbesCommand,
)
from hexawyn.application.use_case.security.detect_missing_probes.detect_missing_probes_use_case import (  # noqa: E501
    DetectMissingProbesUseCase,
)
from hexawyn.application.use_case.security.detect_missing_probes.response import (  # noqa: E501
    DetectMissingProbesResponse,
)


class TestDetectMissingProbesUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_probe_audit_data.return_value = []

        use_case = DetectMissingProbesUseCase(probe_audit_port=port)
        result = use_case.detect_missing_probes(DetectMissingProbesCommand())

        assert isinstance(result, DetectMissingProbesResponse)

    def test_execute_passes_namespace_to_port(self) -> None:
        port = MagicMock()
        port.get_probe_audit_data.return_value = []

        use_case = DetectMissingProbesUseCase(probe_audit_port=port)
        use_case.detect_missing_probes(DetectMissingProbesCommand(namespace="production"))

        port.get_probe_audit_data.assert_called_once_with("production")
