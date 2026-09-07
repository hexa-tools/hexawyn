from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.keda.keda_triggerauth_list.command import (
    KedaTriggerauthListCommand,
)
from hexawyn.application.use_case.keda.keda_triggerauth_list.keda_triggerauth_list_use_case import (
    KedaTriggerauthListUseCase,
)
from hexawyn.application.use_case.keda.keda_triggerauth_list.response import (
    KedaTriggerauthListResponse,
)


class TestKedaTriggerauthListUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        r = MagicMock()
        port.list_trigger_auths.return_value = r
        use_case = KedaTriggerauthListUseCase(port=port)
        result = use_case.execute(KedaTriggerauthListCommand())
        assert isinstance(result, KedaTriggerauthListResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.list_trigger_auths.return_value = []
        use_case = KedaTriggerauthListUseCase(port=port)
        result = use_case.execute(KedaTriggerauthListCommand())
        assert isinstance(result, KedaTriggerauthListResponse)
