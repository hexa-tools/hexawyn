from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.keda.keda_scaledjobs_list.command import (
    KedaScaledjobsListCommand,
)
from hexawyn.application.use_case.keda.keda_scaledjobs_list.keda_scaledjobs_list_use_case import (
    KedaScaledjobsListUseCase,
)
from hexawyn.application.use_case.keda.keda_scaledjobs_list.response import (
    KedaScaledjobsListResponse,
)


class TestKedaScaledjobsListUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        r = MagicMock()
        port.list_scaledjobs.return_value = r
        use_case = KedaScaledjobsListUseCase(port=port)
        result = use_case.execute(KedaScaledjobsListCommand())
        assert isinstance(result, KedaScaledjobsListResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.list_scaledjobs.return_value = []
        use_case = KedaScaledjobsListUseCase(port=port)
        result = use_case.execute(KedaScaledjobsListCommand())
        assert isinstance(result, KedaScaledjobsListResponse)
