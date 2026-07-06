from __future__ import annotations

from hexawyn.application.ports.driven.tls_compliance_port import (
    TLSCompliancePort,
    TLSServiceRawData,
)


class TLSComplianceAdapter(TLSCompliancePort):
    def scan_services(self) -> list[TLSServiceRawData]:
        return []
