from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_command import (
    QueryKubeArchiveCommand,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_response import (
    QueryKubeArchiveResponse,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_service_port import (
    QueryKubeArchiveServicePort,
)
from hexawyn.application.use_case.query_kubearchive.query_kubearchive_use_case import (
    QueryKubeArchiveUseCase,
)


class TestQueryKubeArchiveUseCase:
    def test_delegates_to_service_port(self) -> None:
        fake_service = MagicMock(spec=QueryKubeArchiveServicePort)
        expected = QueryKubeArchiveResponse(total_resources=8, pods=[])
        fake_service.query.return_value = expected

        use_case = QueryKubeArchiveUseCase(service=fake_service)
        result = use_case.execute(
            QueryKubeArchiveCommand(
                namespace="payment",
                resource_type="pods",
                timestamp="2026-06-09T10:00:00Z",
            )
        )

        assert result.total_resources == 8
        fake_service.query.assert_called_once()

    def test_passes_command_to_service(self) -> None:
        fake_service = MagicMock(spec=QueryKubeArchiveServicePort)
        fake_service.query.return_value = QueryKubeArchiveResponse()

        cmd = QueryKubeArchiveCommand(
            namespace="production",
            resource_type="pods",
            timestamp="2026-06-07T00:00:00Z",
            compare_with_current=True,
        )
        use_case = QueryKubeArchiveUseCase(service=fake_service)
        use_case.execute(cmd)

        fake_service.query.assert_called_once_with(cmd)

    def test_propagates_error_from_service(self) -> None:
        fake_service = MagicMock(spec=QueryKubeArchiveServicePort)
        fake_service.query.return_value = QueryKubeArchiveResponse(
            error="KubeArchive not available"
        )

        use_case = QueryKubeArchiveUseCase(service=fake_service)
        result = use_case.execute(
            QueryKubeArchiveCommand(
                namespace="payment",
                resource_type="pods",
                timestamp="t",
            )
        )

        assert result.error == "KubeArchive not available"
