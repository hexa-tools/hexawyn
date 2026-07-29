from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.keda.keda_scaledobject_status.command import (
    KedaScaledobjectStatusCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_status.keda_scaledobject_status_use_case import (  # noqa: E501
    KedaScaledobjectStatusUseCase,
)
from hexawyn.application.use_case.keda.keda_scaledobject_status.response import (
    KedaScaledobjectStatusResponse,
)


class TestKedaScaledobjectStatusUseCase:
    def test_execute_returns_response(self) -> None:
        so = MagicMock()
        so.name = "scaler"
        so.namespace = "default"
        so.phase = MagicMock()
        so.phase.value = "Ready"
        so.current_replicas = 3
        so.hpa_target_replicas = 3
        so.last_scale_time = "2025-01-15T10:00:00Z"
        so.cooldown_period_seconds = 300
        so.message = None

        port = MagicMock()
        port.get_scaledobject.return_value = so

        use_case = KedaScaledobjectStatusUseCase(port=port)
        result = use_case.execute(KedaScaledobjectStatusCommand(name="scaler", namespace="default"))

        assert isinstance(result, KedaScaledobjectStatusResponse)
