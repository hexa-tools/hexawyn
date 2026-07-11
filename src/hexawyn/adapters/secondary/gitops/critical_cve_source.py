from __future__ import annotations

from hexawyn.application.ports.driven.critical_cve_port import CveRaw


class EmptyCriticalCveSource:
    def fetch_critical_cves(self) -> list[CveRaw]:
        return []
