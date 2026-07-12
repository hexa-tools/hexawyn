from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.unauthorized_access_port import (
    UnauthorizedAccessPort,
    UnauthorizedAccessRaw,
)


class UnauthorizedAccessSource(Protocol):
    def fetch_unauthorized_access_data(self) -> UnauthorizedAccessRaw: ...


class UnauthorizedAccessAdapter(UnauthorizedAccessPort):
    def __init__(self, source: UnauthorizedAccessSource) -> None:
        self._source = source

    def get_unauthorized_access_data(self) -> UnauthorizedAccessRaw:
        return self._source.fetch_unauthorized_access_data()
