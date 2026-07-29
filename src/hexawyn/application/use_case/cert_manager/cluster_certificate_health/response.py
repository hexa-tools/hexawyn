from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.certificate import ClusterCertificateReport


@dataclass
class ClusterCertificateHealthResponse:
    report: ClusterCertificateReport | None = None
    error: str | None = None
