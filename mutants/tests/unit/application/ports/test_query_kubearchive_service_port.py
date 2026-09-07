from __future__ import annotations

from abc import ABC

from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_service_port import (
    QueryKubeArchiveServicePort,
)


class TestQueryKubeArchiveServicePort:
    def test_port_is_abstract(self) -> None:
        assert issubclass(QueryKubeArchiveServicePort, ABC)

    def test_port_defines_query(self) -> None:
        assert hasattr(QueryKubeArchiveServicePort, "query")
