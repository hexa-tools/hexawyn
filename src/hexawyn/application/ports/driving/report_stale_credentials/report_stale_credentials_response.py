from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.stale_credentials import StaleCredentialsReport


@dataclass
class ReportStaleCredentialsResponse:
    result: StaleCredentialsReport
