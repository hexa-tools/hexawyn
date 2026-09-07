from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorRawData,
)
from hexawyn.application.use_case.cluster.check_cluster_operator_health.check_cluster_operator_health_use_case import (  # noqa: E501
    CheckClusterOperatorHealthUseCase,
)
from hexawyn.application.use_case.cluster.check_cluster_operator_health.command import (
    CheckClusterOperatorHealthCommand,
)
from hexawyn.application.use_case.cluster.check_cluster_operator_health.response import (
    CheckClusterOperatorHealthResponse,
)
from hexawyn.domain.models.cluster_operator_health import (
    ClusterOperatorHealthReport,
)


def _make_raw_operator(  # noqa: PLR0913
    name: str = "authentication",
    available: bool = True,
    progressing: bool = False,
    degraded: bool = False,
    available_unknown: bool = False,
    message: str = "",
    degraded_since: str | None = None,
) -> ClusterOperatorRawData:
    return {
        "name": name,
        "available": available,
        "progressing": progressing,
        "degraded": degraded,
        "available_unknown": available_unknown,
        "message": message,
        "degraded_since": degraded_since,
    }


class TestCheckClusterOperatorHealthUseCase:
    def test_execute_returns_check_cluster_operator_health_response(self) -> None:
        port = MagicMock()
        port.list_cluster_operators.return_value = []

        use_case = CheckClusterOperatorHealthUseCase(operator_port=port)
        result = use_case.execute(CheckClusterOperatorHealthCommand())

        assert isinstance(result, CheckClusterOperatorHealthResponse)
        assert isinstance(result.result, ClusterOperatorHealthReport)

    def test_execute_delegates_to_port_and_service(self) -> None:
        port = MagicMock()
        port.list_cluster_operators.return_value = [
            _make_raw_operator(name="etcd"),
        ]

        use_case = CheckClusterOperatorHealthUseCase(operator_port=port)
        result = use_case.execute(CheckClusterOperatorHealthCommand())

        port.list_cluster_operators.assert_called_once()
        assert result.result.total == 1
        assert result.result.all_healthy is True
        assert result.result.operators[0].name == "etcd"

    def test_execute_with_degraded_operator(self) -> None:
        port = MagicMock()
        port.list_cluster_operators.return_value = [
            _make_raw_operator(
                name="etcd",
                available=False,
                degraded=True,
                message="etcd cluster down",
            ),
        ]

        use_case = CheckClusterOperatorHealthUseCase(operator_port=port)
        result = use_case.execute(CheckClusterOperatorHealthCommand())

        assert result.result.degraded == 1
        assert result.result.all_healthy is False
        assert result.result.operators[0].health == "degraded"

    def test_execute_with_mixed_operators(self) -> None:
        port = MagicMock()
        port.list_cluster_operators.return_value = [
            _make_raw_operator(name="authentication"),
            _make_raw_operator(name="console", degraded=True),
            _make_raw_operator(name="dns", progressing=True, available=False),
        ]

        use_case = CheckClusterOperatorHealthUseCase(operator_port=port)
        result = use_case.execute(CheckClusterOperatorHealthCommand())

        assert result.result.total == 3  # noqa: PLR2004
        assert result.result.healthy == 1  # noqa: PLR2004
        assert result.result.degraded == 1  # noqa: PLR2004
        assert result.result.progressing == 1  # noqa: PLR2004
        assert result.result.all_healthy is False

    def test_execute_all_healthy_empty_operators(self) -> None:
        port = MagicMock()
        port.list_cluster_operators.return_value = []

        use_case = CheckClusterOperatorHealthUseCase(operator_port=port)
        result = use_case.execute(CheckClusterOperatorHealthCommand())

        assert result.result.total == 0
        assert result.result.all_healthy is True
