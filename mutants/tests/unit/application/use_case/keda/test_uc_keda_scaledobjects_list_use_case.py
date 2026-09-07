from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.keda.keda_scaledobjects_list.command import (
    KedaScaledobjectsListCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobjects_list.keda_scaledobjects_list_use_case import (  # noqa: E501
    KedaScaledobjectsListUseCase,
)
from hexawyn.application.use_case.keda.keda_scaledobjects_list.response import (
    KedaScaledobjectsListResponse,
)


class TestKedaScaledobjectsListUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        r = MagicMock()
        port.list_scaledobjects.return_value = r
        use_case = KedaScaledobjectsListUseCase(port=port)
        result = use_case.execute(KedaScaledobjectsListCommand())
        assert isinstance(result, KedaScaledobjectsListResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.list_scaledobjects.return_value = []
        use_case = KedaScaledobjectsListUseCase(port=port)
        result = use_case.execute(KedaScaledobjectsListCommand())
        assert isinstance(result, KedaScaledobjectsListResponse)
