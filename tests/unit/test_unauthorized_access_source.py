from hexawyn.adapters.secondary.gitops.unauthorized_access_source import (
    EmptyUnauthorizedAccessSource,
)


class TestEmptyUnauthorizedAccessSource:
    def test_returns_default(self) -> None:
        raw = EmptyUnauthorizedAccessSource().fetch_unauthorized_access_data()
        assert raw["attempt_count"] == 0
