from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.etcd_logs.command import (
    ETCDLogsCommand,
)
from hexawyn.application.use_case.observability.etcd_logs.etcd_logs_use_case import (  # noqa: E501
    ETCDLogsUseCase,
)
from hexawyn.application.use_case.observability.etcd_logs.response import (
    ETCDLogsResponse,
)


class TestETCDLogsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_etcd_logs.return_value = []

        use_case = ETCDLogsUseCase(port=port)
        result = use_case.execute(ETCDLogsCommand())

        assert isinstance(result, ETCDLogsResponse)

    def test_execute_empty_logs(self) -> None:
        port = MagicMock()
        port.get_etcd_logs.return_value = []

        use_case = ETCDLogsUseCase(port=port)
        result = use_case.execute(ETCDLogsCommand())

        assert isinstance(result, ETCDLogsResponse)
