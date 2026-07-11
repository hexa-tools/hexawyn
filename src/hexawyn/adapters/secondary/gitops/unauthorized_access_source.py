from __future__ import annotations

from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessRaw


class EmptyUnauthorizedAccessSource:
    def fetch_unauthorized_access_data(self) -> UnauthorizedAccessRaw:
        return UnauthorizedAccessRaw(attempt_count=0, window_minutes=30, source_type="unknown")
