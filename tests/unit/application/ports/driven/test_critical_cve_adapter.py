from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort, CveRaw


class _FakeSource:
    def fetch_critical_cves(self) -> list[CveRaw]:
        return []


class TestPortImplementation:
    def test_is_critical_cve_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.critical_cve_adapter import CriticalCveAdapter

        assert isinstance(CriticalCveAdapter(source=_FakeSource()), CriticalCvePort)

    def test_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.critical_cve_adapter import CriticalCveAdapter

        adapter = CriticalCveAdapter(source=_FakeSource())
        assert adapter.get_critical_cves() == []
