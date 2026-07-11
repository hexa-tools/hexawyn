from hexawyn.adapters.secondary.gitops.stale_credentials_source import EmptyStaleCredentialsSource


class TestEmptyStaleCredentialsSource:
    def test_returns_empty(self) -> None:
        assert EmptyStaleCredentialsSource().fetch_stale_credentials(90) == []
