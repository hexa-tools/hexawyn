from dataclasses import dataclass

from hexawyn.domain.models.namespace_waste import OverProvisioningReport


@dataclass
class DetectOverProvisionedNamespacesResponse:
    report: OverProvisioningReport
    prometheus_available: bool
