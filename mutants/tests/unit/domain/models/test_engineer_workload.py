class TestNightInterventionReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.engineer_workload import NightInterventionReport

        report = NightInterventionReport(period_label="Ce mois")

        assert report.period_label == "Ce mois"
        assert report.avg_interventions_per_night == 0.0
        assert report.previous_avg_per_night is None
        assert report.delta_pct == 0.0
        assert report.trend == "stable"
        assert report.summary == ""

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.engineer_workload import NightInterventionReport

        report = NightInterventionReport(
            period_label="Ce mois",
            avg_interventions_per_night=0.8,
            previous_avg_per_night=1.4,
            delta_pct=-42.9,
            trend="improving",
            summary="Moins sollicites : -43% d'interventions nocturnes.",
        )

        assert report.avg_interventions_per_night == 0.8  # noqa: PLR2004
        assert report.delta_pct == -42.9  # noqa: PLR2004
