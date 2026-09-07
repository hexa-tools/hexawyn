from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.keda.keda_scaledobject_triggers.command import (
    KedaScaledobjectTriggersCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_triggers.keda_scaledobject_triggers_use_case import (  # noqa: E501
    KedaScaledobjectTriggersUseCase,
)
from hexawyn.application.use_case.keda.keda_scaledobject_triggers.response import (
    KedaScaledobjectTriggersResponse,
)


class TestKedaScaledobjectTriggersUseCase:
    def test_execute_returns_response(self) -> None:
        so = MagicMock()
        so.triggers = []

        port = MagicMock()
        port.get_scaledobject.return_value = so

        use_case = KedaScaledobjectTriggersUseCase(port=port)
        result = use_case.get_triggers(
            KedaScaledobjectTriggersCommand(
                name="scaler",
                namespace="default",
            )
        )

        assert isinstance(result, KedaScaledobjectTriggersResponse)
