from hexawyn.adapters.secondary.gitops.night_intervention_source import (
    EmptyNightInterventionSource,
)


class TestEmptyNightInterventionSource:
    def test_returns_months_silent(self) -> None:
        result = EmptyNightInterventionSource().fetch_night_intervention_data(6)

        assert len(result) == 6
        assert result[0]["night_intervention_count"] == 0
