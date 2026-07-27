from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.query_kubearchive.command import (
    QueryKubearchiveCommand,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.query_kubearchive_use_case import (  # noqa: E501
    QueryKubeArchiveUseCase,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.response import (  # noqa: E501
    QueryKubearchiveResponse,
)


class TestQueryKubeArchiveUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.query_historical_pods.return_value = []
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = QueryKubeArchiveUseCase(
            kubearchive_port=port,
            k8s_port=k8s,
        )
        result = use_case.execute(QueryKubearchiveCommand(namespace="default"))

        assert isinstance(result, QueryKubearchiveResponse)

    def test_execute_without_comparison(self) -> None:
        port = MagicMock()
        port.query_historical_pods.return_value = []
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = QueryKubeArchiveUseCase(
            kubearchive_port=port,
            k8s_port=k8s,
        )
        result = use_case.execute(
            QueryKubearchiveCommand(
                namespace="default",
                compare_with_current=False,
            )
        )

        assert result.comparison is None
