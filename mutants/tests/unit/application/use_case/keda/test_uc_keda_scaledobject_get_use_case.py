from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.keda.keda_scaledobject_get.command import (
    KedaScaledobjectGetCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_get.keda_scaledobject_get_use_case import (  # noqa: E501
    KedaScaledobjectGetUseCase,
)
from hexawyn.application.use_case.keda.keda_scaledobject_get.response import (
    KedaScaledobjectGetResponse,
)


class TestKedaScaledobjectGetUseCase:
    def test_execute_returns_response(self) -> None:
        so = MagicMock()
        so.name = "my-scaler"
        so.namespace = "default"
        so.phase = MagicMock()
        so.phase.value = "Ready"
        so.min_replicas = 1
        so.max_replicas = 5
        so.current_replicas = 3
        so.hpa_target_replicas = 4
        so.hpa_name = "keda-hpa"
        so.hpa_status = MagicMock()
        so.hpa_status.value = "Active"
        so.cooldown_period_seconds = 300
        so.last_scale_time = None
        so.idle_replicas = 0

        port = MagicMock()
        port.get_scaledobject.return_value = so

        use_case = KedaScaledobjectGetUseCase(port=port)
        result = use_case.execute(KedaScaledobjectGetCommand(name="my-scaler", namespace="default"))

        assert isinstance(result, KedaScaledobjectGetResponse)
        assert result.phase == "Ready"
