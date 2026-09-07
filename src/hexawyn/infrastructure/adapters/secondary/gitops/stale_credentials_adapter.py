from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.stale_credentials_port import (
    StaleCredentialRaw,
    StaleCredentialsPort,
)


class StaleCredentialsSource(Protocol):
    def fetch_stale_credentials(self, min_days: int) -> list[StaleCredentialRaw]: ...


class StaleCredentialsAdapter(StaleCredentialsPort):
    def __init__(self, source: StaleCredentialsSource) -> None:
        self._source = source

    def get_stale_credentials(self, min_days: int) -> list[StaleCredentialRaw]:
        return self._source.fetch_stale_credentials(min_days)
