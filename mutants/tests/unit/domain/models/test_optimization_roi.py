from dataclasses import fields


class TestOptimizationItem:
    def test_fields(self) -> None:
        from hexawyn.domain.models.optimization_roi import OptimizationItem

        names = {f.name for f in fields(OptimizationItem)}
        assert names == {"name", "category", "monthly_saving_eur", "description"}

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.optimization_roi import OptimizationItem

        item = OptimizationItem(
            name="right-size payment-api",
            category="right_sizing",
            monthly_saving_eur=350.0,
            description="Reduced CPU requests from 1.0 to 0.3 cores",
        )

        assert item.category == "right_sizing"
        assert item.monthly_saving_eur == 350.0  # noqa: PLR2004


class TestPerformanceImpact:
    def test_fields(self) -> None:
        from hexawyn.domain.models.optimization_roi import PerformanceImpact

        names = {f.name for f in fields(PerformanceImpact)}
        assert names == {"metric", "before", "after", "improved", "regressed"}

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.optimization_roi import PerformanceImpact

        impact = PerformanceImpact(
            metric="p99_latency_ms", before=120.0, after=95.0, improved=True, regressed=False
        )

        assert impact.metric == "p99_latency_ms"
        assert impact.improved is True


class TestOptimizationRoiReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.optimization_roi import OptimizationRoiReport

        report = OptimizationRoiReport()

        assert report.baseline_monthly_eur == 0.0
        assert report.current_monthly_eur == 0.0
        assert report.monthly_saving_eur == 0.0
        assert report.annual_saving_eur == 0.0
        assert report.savings_pct == 0.0
        assert report.optimizations == []
        assert report.top_optimization is None
        assert report.performance_impacts == []
        assert report.has_regression is False
        assert report.traffic_normalized is False
        assert report.traffic_growth_pct == 0.0
        assert report.has_baseline is True
        assert report.warning == ""

    def test_holds_summary(self) -> None:
        from hexawyn.domain.models.optimization_roi import OptimizationRoiReport

        report = OptimizationRoiReport(
            baseline_monthly_eur=500.0,
            current_monthly_eur=150.0,
            monthly_saving_eur=350.0,
            annual_saving_eur=4200.0,
            savings_pct=70.0,
            has_regression=True,
        )

        assert report.monthly_saving_eur == 350.0  # noqa: PLR2004
        assert report.annual_saving_eur == 4200.0  # noqa: PLR2004
        assert report.has_regression is True
