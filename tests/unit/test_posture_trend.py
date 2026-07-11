from __future__ import annotations


class TestClassifyTrend:
    def test_improving_when_score_higher(self) -> None:
        from hexawyn.domain.services.security_posture.posture_trend import classify_trend

        assert classify_trend(current=80.0, previous=75.0) == "improving"

    def test_degrading_when_score_lower(self) -> None:
        from hexawyn.domain.services.security_posture.posture_trend import classify_trend

        assert classify_trend(current=70.0, previous=75.0) == "degrading"

    def test_stable_when_equal(self) -> None:
        from hexawyn.domain.services.security_posture.posture_trend import classify_trend

        assert classify_trend(current=80.0, previous=80.0) == "stable"

    def test_stable_when_within_tolerance(self) -> None:
        from hexawyn.domain.services.security_posture.posture_trend import classify_trend

        assert classify_trend(current=80.4, previous=80.0) == "stable"

    def test_stable_when_no_previous(self) -> None:
        from hexawyn.domain.services.security_posture.posture_trend import classify_trend

        assert classify_trend(current=80.0, previous=None) == "stable"

    def test_improving_beyond_tolerance(self) -> None:
        from hexawyn.domain.services.security_posture.posture_trend import classify_trend

        assert classify_trend(current=81.0, previous=80.0) == "improving"
