from __future__ import annotations

from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort
from hexawyn.domain.models.error_attribution import ErrorAttributionRequest


class OTelErrorAttributionAdapter(ErrorAttributionPort):
    def fetch_error_attribution(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        return []
