from __future__ import annotations


class TestClassifyTrend:
    def test_improving_when_higher(self) -> None:
        from hexawyn.domain.services.sla_report.sla_trend import classify_trend

        assert classify_trend(current=99.8, previous=99.5) == "improving"

    def test_degrading_when_lower(self) -> None:
        from hexawyn.domain.services.sla_report.sla_trend import classify_trend

        assert classify_trend(current=99.2, previous=99.5) == "degrading"

    def test_stable_when_equal(self) -> None:
        from hexawyn.domain.services.sla_report.sla_trend import classify_trend

        assert classify_trend(current=99.5, previous=99.5) == "stable"

    def test_stable_within_tolerance(self) -> None:
        from hexawyn.domain.services.sla_report.sla_trend import classify_trend

        assert classify_trend(current=99.53, previous=99.5) == "stable"

    def test_stable_when_no_previous(self) -> None:
        from hexawyn.domain.services.sla_report.sla_trend import classify_trend

        assert classify_trend(current=99.8, previous=None) == "stable"

    def test_improving_beyond_tolerance(self) -> None:
        from hexawyn.domain.services.sla_report.sla_trend import classify_trend

        assert classify_trend(current=99.7, previous=99.5) == "improving"
