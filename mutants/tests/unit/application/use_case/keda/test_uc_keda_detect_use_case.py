from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.keda.keda_detect.command import (
    KedaDetectCommand,
)
from hexawyn.application.use_case.keda.keda_detect.keda_detect_use_case import (
    KedaDetectUseCase,
)
from hexawyn.application.use_case.keda.keda_detect.response import (
    KedaDetectResponse,
)


class TestKedaDetectUseCase:
    def test_execute_returns_response(self) -> None:
        r = MagicMock()
        r.installed = True
        r.version = "2.10"
        r.namespace = "keda"
        r.total_scaledobjects = 5
        r.ready_scaledobjects = 4
        r.error_scaledobjects = 1
        r.scaled_to_zero_count = 2
        r.total_scaledjobs = 0
        r.managed_namespaces = ["default", "staging"]

        port = MagicMock()
        port.detect.return_value = r

        use_case = KedaDetectUseCase(port=port)
        result = use_case.execute(KedaDetectCommand())

        assert isinstance(result, KedaDetectResponse)
        assert result.installed is True
        assert result.total_scaledobjects == 5  # noqa: PLR2004

    def test_execute_not_installed(self) -> None:
        r = MagicMock()
        r.installed = False
        r.version = None
        r.namespace = None
        r.total_scaledobjects = 0
        r.ready_scaledobjects = 0
        r.error_scaledobjects = 0
        r.scaled_to_zero_count = 0
        r.total_scaledjobs = 0
        r.managed_namespaces = None

        port = MagicMock()
        port.detect.return_value = r

        use_case = KedaDetectUseCase(port=port)
        result = use_case.execute(KedaDetectCommand())

        assert result.installed is False
