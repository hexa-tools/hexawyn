from hexawyn.adapters.secondary.gitops.critical_cve_source import EmptyCriticalCveSource


class TestEmptyCriticalCveSource:
    def test_returns_empty(self) -> None:
        assert EmptyCriticalCveSource().fetch_critical_cves() == []
