from hexawyn.application.ports.driven.stale_credentials_port import (
    StaleCredentialRaw,
    StaleCredentialsPort,
)


class _FakeSource:
    def fetch_stale_credentials(self, min_days: int) -> list[StaleCredentialRaw]:
        return []


class TestPortImplementation:
    def test_is_stale_credentials_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.stale_credentials_adapter import (
            StaleCredentialsAdapter,
        )

        assert isinstance(StaleCredentialsAdapter(source=_FakeSource()), StaleCredentialsPort)

    def test_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.stale_credentials_adapter import (
            StaleCredentialsAdapter,
        )

        adapter = StaleCredentialsAdapter(source=_FakeSource())
        assert adapter.get_stale_credentials(90) == []
