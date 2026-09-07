from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort, CveRaw


class CriticalCveSource(Protocol):
    def fetch_critical_cves(self) -> list[CveRaw]: ...


class CriticalCveAdapter(CriticalCvePort):
    def __init__(self, source: CriticalCveSource) -> None:
        self._source = source

    def get_critical_cves(self) -> list[CveRaw]:
        return self._source.fetch_critical_cves()
