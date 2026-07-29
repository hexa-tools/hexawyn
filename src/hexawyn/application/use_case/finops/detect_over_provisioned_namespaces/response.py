from dataclasses import dataclass


@dataclass
class DetectOverProvisionedNamespacesResponse:
    report: object = None
    prometheus_available: bool = False
    error: str | None = None
