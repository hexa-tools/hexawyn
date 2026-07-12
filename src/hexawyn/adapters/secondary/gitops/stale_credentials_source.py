from __future__ import annotations

from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialRaw


class EmptyStaleCredentialsSource:
    def fetch_stale_credentials(self, min_days: int) -> list[StaleCredentialRaw]:
        return []
