from hexawyn.application.ports.driven.unauthorized_access_port import (
    UnauthorizedAccessPort,
    UnauthorizedAccessRaw,
)


class _FakeSource:
    def fetch_unauthorized_access_data(self) -> UnauthorizedAccessRaw:
        return UnauthorizedAccessRaw(attempt_count=0, window_minutes=30, source_type="unknown")


class TestPortImplementation:
    def test_is_unauthorized_access_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.unauthorized_access_adapter import (
            UnauthorizedAccessAdapter,
        )

        assert isinstance(UnauthorizedAccessAdapter(source=_FakeSource()), UnauthorizedAccessPort)

    def test_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.unauthorized_access_adapter import (
            UnauthorizedAccessAdapter,
        )

        adapter = UnauthorizedAccessAdapter(source=_FakeSource())
        assert adapter.get_unauthorized_access_data()["attempt_count"] == 0
