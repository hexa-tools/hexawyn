from dataclasses import fields


class TestWorkloadCompliance:
    def test_is_frozen_dataclass_with_expected_fields(self) -> None:
        from hexawyn.domain.models.security_posture import WorkloadCompliance

        field_names = {f.name for f in fields(WorkloadCompliance)}

        assert field_names == {
            "workload",
            "namespace",
            "category",
            "status",
            "remediation_priority",
            "detail",
        }

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.security_posture import WorkloadCompliance

        item = WorkloadCompliance(
            workload="payment-api",
            namespace="production",
            category="tls",
            status="non_compliant",
            remediation_priority=1,
            detail="No TLS configured",
        )

        assert item.workload == "payment-api"
        assert item.category == "tls"
        assert item.status == "non_compliant"


class TestCategoryScore:
    def test_holds_breakdown(self) -> None:
        from hexawyn.domain.models.security_posture import CategoryScore

        score = CategoryScore(
            category="tls",
            total=10,
            compliant=8,
            non_compliant=2,
            exempt=0,
            score_pct=80.0,
            policy_defined=True,
            non_compliant_workloads=[],
        )

        assert score.category == "tls"
        assert score.score_pct == 80.0
        assert score.policy_defined is True


class TestSecurityPostureReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.security_posture import SecurityPostureReport

        report = SecurityPostureReport(overall_score_pct=0.0)

        assert report.overall_score_pct == 0.0
        assert report.categories == []
        assert report.trend == "stable"
        assert report.previous_score_pct is None
        assert report.partial is False
        assert report.warning == ""

    def test_holds_summary(self) -> None:
        from hexawyn.domain.models.security_posture import SecurityPostureReport

        report = SecurityPostureReport(
            overall_score_pct=80.0,
            trend="improving",
            previous_score_pct=75.0,
            partial=True,
            warning="Partial results: compliance check timed out.",
        )

        assert report.overall_score_pct == 80.0
        assert report.trend == "improving"
        assert report.previous_score_pct == 75.0
        assert report.partial is True
