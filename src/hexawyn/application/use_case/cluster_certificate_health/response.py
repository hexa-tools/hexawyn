from dataclasses import dataclass


@dataclass
class ClusterCertificateHealthResponse:
    error: str | None = None
