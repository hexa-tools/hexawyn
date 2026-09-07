"""RED → GREEN — MTTR Trend domain logic."""

from hexawyn.domain.models.mttr_trend import (
    MTTRPerSeverity,
    SlowestIncident,
)
from hexawyn.domain.services.mttr_trend.mttr_trend_engine import (
    MTTRTrendEngine,
    _as_bool,
    _as_int,
    _compute_trend,
    _rank_slowest,
)


def _incident(  # noqa: PLR0913
    incident_id: str = "INC-001",
    service_name: str = "payment-service",
    severity: str = "P1",
    resolution_minutes: int = 45,
    resolved: bool = True,
    root_cause: str = "OOMKilled",
) -> dict[str, object]:
    return {
        "incident_id": incident_id,
        "service_name": service_name,
        "severity": severity,
        "resolution_minutes": resolution_minutes,
        "resolved": resolved,
        "root_cause": root_cause,
    }


class TestMTTRCalculation:
    def test_mttr_per_month_per_severity(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [
                _incident(severity="P1", resolution_minutes=45),
                _incident(incident_id="INC-002", severity="P1", resolution_minutes=60),
                _incident(incident_id="INC-003", severity="P1", resolution_minutes=30),
                _incident(incident_id="INC-004", severity="P2", resolution_minutes=120),
            ],
            "2026-06": [
                _incident(severity="P1", resolution_minutes=32),
                _incident(incident_id="INC-005", severity="P1", resolution_minutes=32),
                _incident(incident_id="INC-006", severity="P2", resolution_minutes=110),
            ],
            "2026-07": [
                _incident(severity="P1", resolution_minutes=18),
            ],
        }

        result = engine.compute(months)

        assert result.per_month["2026-05"]["P1"].mttr_minutes == 45.0  # noqa: PLR2004
        assert result.per_month["2026-06"]["P1"].mttr_minutes == 32.0  # noqa: PLR2004
        assert result.per_month["2026-07"]["P1"].mttr_minutes == 18.0  # noqa: PLR2004

    def test_mttr_improving_trend(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [_incident(resolution_minutes=45)],
            "2026-06": [_incident(incident_id="INC-002", resolution_minutes=32)],
            "2026-07": [_incident(incident_id="INC-003", resolution_minutes=18)],
        }

        result = engine.compute(months)

        assert result.trend == "improving"

    def test_mttr_degrading_trend(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [_incident(resolution_minutes=20)],
            "2026-06": [_incident(incident_id="INC-002", resolution_minutes=45)],
            "2026-07": [_incident(incident_id="INC-003", resolution_minutes=90)],
        }

        result = engine.compute(months)

        assert result.trend == "degrading"

    def test_stable_trend(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [_incident(resolution_minutes=30)],
            "2026-06": [_incident(incident_id="INC-002", resolution_minutes=30)],
            "2026-07": [_incident(incident_id="INC-003", resolution_minutes=30)],
        }

        result = engine.compute(months)

        assert result.trend == "stable"

    def test_no_p1_incidents_mttr_na(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-07": [],
        }

        result = engine.compute(months)

        assert result.per_month["2026-07"]["P1"].mttr_minutes is None

    def test_single_incident_mttr_equals_resolution(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-07": [_incident(resolution_minutes=72)],
        }

        result = engine.compute(months)

        assert result.per_month["2026-07"]["P1"].mttr_minutes == 72.0  # noqa: PLR2004


class TestSlowestIncidents:
    def test_top_three_slowest_ranked(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [
                _incident(resolution_minutes=120, root_cause="db-deadlock", service_name="payment"),
                _incident(
                    incident_id="INC-002",
                    resolution_minutes=90,
                    root_cause="mem-leak",
                    service_name="auth",
                ),
                _incident(
                    incident_id="INC-003",
                    resolution_minutes=60,
                    root_cause="dns-timeout",
                    service_name="cart",
                ),
                _incident(
                    incident_id="INC-004",
                    resolution_minutes=30,
                    root_cause="quick-fix",
                    service_name="infra",
                ),
            ],
        }

        result = engine.compute(months)

        assert len(result.slowest_incidents) == 3  # noqa: PLR2004
        assert result.slowest_incidents[0].resolution_minutes == 120  # noqa: PLR2004
        assert result.slowest_incidents[2].resolution_minutes == 60  # noqa: PLR2004


class TestEdgeCases:
    def test_unresolved_incident_excluded(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-07": [
                _incident(resolution_minutes=30),
                _incident(incident_id="INC-002", resolved=False, resolution_minutes=0),
            ],
        }

        result = engine.compute(months)

        assert result.per_month["2026-07"]["P1"].mttr_minutes == 30.0  # noqa: PLR2004

    def test_benchmark_p1_under_30min_pass(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-07": [_incident(resolution_minutes=25)],
        }

        result = engine.compute(months)

        assert result.per_month["2026-07"]["P1"].mttr_minutes == 25.0  # noqa: PLR2004
        assert result.per_month["2026-07"]["P1"].meets_benchmark is True

    def test_benchmark_p2_under_120min_fail(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-07": [_incident(severity="P2", resolution_minutes=150)],
        }

        result = engine.compute(months)

        assert result.per_month["2026-07"]["P2"].meets_benchmark is False


class TestHelperFunctions:
    def test_as_int_none_returns_zero(self) -> None:
        assert _as_int(None) == 0

    def test_as_int_list_returns_zero(self) -> None:
        assert _as_int([1, 2]) == 0

    def test_as_bool_none_false(self) -> None:
        assert _as_bool(None) is False

    def test_as_bool_non_empty_string_true(self) -> None:
        assert _as_bool("yes") is True

    def test_first_month_zero_mttr_returns_stable(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [_incident(resolution_minutes=0)],
            "2026-06": [_incident(incident_id="INC-002", resolution_minutes=10)],
        }

        result = engine.compute(months)

        assert result.trend == "stable"


class TestComputeTrendDirect:
    def _per_month(
        self,
        values: dict[str, float | None],
    ) -> dict[str, dict[str, MTTRPerSeverity]]:
        return {
            month: {
                "P1": MTTRPerSeverity(
                    severity="P1",
                    mttr_minutes=value,
                    incident_count=1 if value is not None else 0,  # noqa: PLR2004
                    meets_benchmark=value is not None,
                ),
                "P2": MTTRPerSeverity(
                    severity="P2",
                    mttr_minutes=None,
                    incident_count=0,
                    meets_benchmark=False,
                ),
            }
            for month, value in values.items()
        }

    def test_single_month_insufficient(self) -> None:
        trend, recommendation = _compute_trend(self._per_month({"2026-05": 30.0}), ["2026-05"])

        assert trend == "insufficient_data"
        assert recommendation == "Need at least 2 months of P1 data for trend analysis"

    def test_zero_months_insufficient(self) -> None:
        trend, recommendation = _compute_trend(self._per_month({}), ["2026-05"])

        assert trend == "insufficient_data"

    def test_degrading_positive_delta(self) -> None:
        trend, recommendation = _compute_trend(
            self._per_month({"2026-05": 100.0, "2026-06": 110.0}),
            ["2026-05", "2026-06"],
        )

        assert trend == "degrading"
        assert recommendation == (
            "MTTR degraded by 10% — review on-call runbooks and escalation paths"
        )

    def test_improving_negative_delta(self) -> None:
        trend, recommendation = _compute_trend(
            self._per_month({"2026-05": 100.0, "2026-06": 90.0}),
            ["2026-05", "2026-06"],
        )

        assert trend == "improving"
        assert recommendation == ("MTTR improved by 10% — response processes are effective")

    def test_stable_within_threshold(self) -> None:
        trend, recommendation_msg = _compute_trend(
            self._per_month({"2026-05": 100.0, "2026-06": 105.0}),
            ["2026-05", "2026-06"],
        )

        assert trend == "stable"
        assert recommendation_msg == "MTTR is stable across the period"

    def test_stable_boundary_exactly_ten_percent_is_not_stable(self) -> None:
        trend, _ = _compute_trend(
            self._per_month({"2026-05": 100.0, "2026-06": 110.0}),
            ["2026-05", "2026-06"],
        )

        assert trend == "degrading"

    def test_first_value_zero_is_stable_no_change(self) -> None:
        trend, recommendation_msg = _compute_trend(
            self._per_month({"2026-05": 0.0, "2026-06": 30.0}),
            ["2026-05", "2026-06"],
        )

        assert trend == "stable"
        assert recommendation_msg == "No change in MTTR"

    def test_uses_first_and_last_values_only(self) -> None:
        trend, recommendation = _compute_trend(
            self._per_month({"2026-05": 10.0, "2026-06": 20.0, "2026-07": 30.0}),
            ["2026-05", "2026-06", "2026-07"],
        )

        assert trend == "degrading"
        assert recommendation == (
            "MTTR degraded by 200% — review on-call runbooks and escalation paths"
        )

    def test_skips_months_without_p1_mttr(self) -> None:
        trend, _ = _compute_trend(
            self._per_month({"2026-05": 30.0, "2026-06": None, "2026-07": 60.0}),
            ["2026-05", "2026-06", "2026-07"],
        )

        assert trend == "degrading"

    def test_missing_month_in_per_month_is_skipped(self) -> None:
        per_month = self._per_month({"2026-06": 30.0})
        trend, _ = _compute_trend(per_month, ["2026-05", "2026-06"])

        assert trend == "insufficient_data"

    def test_fractional_delta_rounds_one_decimal(self) -> None:
        trend, recommendation_msg = _compute_trend(
            self._per_month({"2026-05": 30.0, "2026-06": 33.0}),
            ["2026-05", "2026-06"],
        )

        # (33-30)/30*100 = 10.0 -> stable? no: exactly 10 → degrading at 10%
        assert trend == "degrading"
        assert "10%" in recommendation_msg

    def test_delta_just_below_ten_stays_stable_not_rounded_to_integer(self) -> None:
        trend, _ = _compute_trend(
            self._per_month({"2026-05": 100.0, "2026-06": 109.6}),
            ["2026-05", "2026-06"],
        )

        # delta = 9.6 -> round(1) = 9.6 < 10 => stable. round(,None) -> 10 => degrading.
        assert trend == "stable"

    def test_delta_near_ten_keeps_one_decimal_precision(self) -> None:
        trend, _ = _compute_trend(
            self._per_month({"2026-05": 100.0, "2026-06": 109.96}),
            ["2026-05", "2026-06"],
        )

        # delta ~9.96 -> round(1)=10.0 (>=10 => degrading), round(,2)=9.96 (stable)
        assert trend == "degrading"


class TestRankSlowestDirect:
    def test_returns_full_field_mapping(self) -> None:
        incidents = [
            {
                "incident_id": "INC-9",
                "service_name": "billing",
                "severity": "P1",
                "resolution_minutes": 90,
                "root_cause": "db-lock",
            }
        ]

        result = _rank_slowest(incidents)

        assert result == [
            SlowestIncident(
                incident_id="INC-9",
                service_name="billing",
                severity="P1",
                resolution_minutes=90,
                root_cause="db-lock",
                month="",
            )
        ]

    def test_sorts_descending_and_truncates_to_three(self) -> None:
        incidents = [
            {"resolution_minutes": m, "incident_id": f"INC-{m}"} for m in (10, 50, 30, 20, 40)
        ]

        result = _rank_slowest(incidents)

        assert [i.resolution_minutes for i in result] == [50, 40, 30]  # noqa: PLR2004

    def test_missing_fields_get_defaults(self) -> None:
        result = _rank_slowest([{}])

        assert result == [
            SlowestIncident(
                incident_id="",
                service_name="",
                severity="P1",
                resolution_minutes=0,
                root_cause="",
                month="",
            )
        ]

    def test_default_severity_p1_preserved(self) -> None:
        result = _rank_slowest([{"resolution_minutes": 5}])

        assert result[0].severity == "P1"

    def test_non_integer_resolution_is_parsed(self) -> None:
        result = _rank_slowest([{"resolution_minutes": "37.5", "incident_id": "X"}])

        assert result[0].resolution_minutes == 37  # noqa: PLR2004

    def test_explicit_p2_severity_is_kept(self) -> None:
        result = _rank_slowest([{"resolution_minutes": 5, "severity": "P2", "incident_id": "X"}])

        assert result[0].severity == "P2"

    def test_empty_input_returns_empty(self) -> None:
        assert _rank_slowest([]) == []

    def test_non_numeric_resolution_ranks_last(self) -> None:
        result = _rank_slowest(
            [
                {"resolution_minutes": 10, "incident_id": "A"},
                {"resolution_minutes": "abc", "incident_id": "B"},
            ]
        )

        assert result[0].incident_id == "A"
        assert result[1].incident_id == "B"


class TestPerSeverityDetails:
    def test_benchmark_boundary_p1_exactly_30_meets(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [
                {
                    "severity": "P1",
                    "resolution_minutes": 30,
                    "resolved": True,
                }
            ]
        }

        result = engine.compute(months)

        assert result.per_month["2026-05"]["P1"].mttr_minutes == 30.0  # noqa: PLR2004
        assert result.per_month["2026-05"]["P1"].meets_benchmark is True

    def test_benchmark_boundary_p2_exactly_120_meets(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [
                {
                    "severity": "P2",
                    "resolution_minutes": 120,
                    "resolved": True,
                }
            ]
        }

        result = engine.compute(months)

        assert result.per_month["2026-05"]["P2"].meets_benchmark is True

    def test_fractional_mttr_rounds_one_decimal(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [
                {
                    "severity": "P1",
                    "resolution_minutes": m,
                    "resolved": True,
                }
                for m in (40, 45, 40)
            ]
        }

        result = engine.compute(months)

        # (40+45+40)/3 = 41.666 -> round(1) = 41.7
        assert result.per_month["2026-05"]["P1"].mttr_minutes == 41.7  # noqa: PLR2004
        assert result.per_month["2026-05"]["P1"].incident_count == 3  # noqa: PLR2004

    def test_severity_defaults_to_p1_when_missing(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [
                {
                    "resolution_minutes": 25,
                    "resolved": True,
                }
            ]
        }

        result = engine.compute(months)

        assert result.per_month["2026-05"]["P1"].mttr_minutes == 25.0  # noqa: PLR2004

    def test_empty_month_has_both_severity_defaults(self) -> None:
        engine = MTTRTrendEngine()
        result = engine.compute({"2026-05": []})

        assert result.per_month["2026-05"]["P1"] == MTTRPerSeverity(
            severity="P1",
            mttr_minutes=None,
            incident_count=0,
            meets_benchmark=False,
        )
        assert result.per_month["2026-05"]["P2"] == MTTRPerSeverity(
            severity="P2",
            mttr_minutes=None,
            incident_count=0,
            meets_benchmark=False,
        )

    def test_populated_severity_preserves_original_key(self) -> None:
        engine = MTTRTrendEngine()
        result = engine.compute(
            {"2026-05": [{"severity": "P2", "resolution_minutes": 60, "resolved": True}]}
        )

        assert result.per_month["2026-05"]["P2"].severity == "P2"
        assert result.per_month["2026-05"]["P2"].mttr_minutes == 60.0  # noqa: PLR2004

    def test_unresolved_in_middle_does_not_break_loop(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [
                {"resolution_minutes": 30, "resolved": True},
                {"resolution_minutes": 60, "resolved": False, "severity": "P2"},
                {"resolution_minutes": 10, "resolved": True},
            ]
        }

        result = engine.compute(months)

        assert result.per_month["2026-05"]["P1"].mttr_minutes == 20.0  # noqa: PLR2004
        assert result.per_month["2026-05"]["P1"].incident_count == 2  # noqa: PLR2004

    def test_report_recommendation_is_populated(self) -> None:
        engine = MTTRTrendEngine()
        months = {
            "2026-05": [{"resolution_minutes": 45, "resolved": True}],
            "2026-06": [{"resolution_minutes": 20, "resolved": True}],
        }

        result = engine.compute(months)

        assert result.recommendation.startswith("MTTR improved by")
        assert result.trend == "improving"
