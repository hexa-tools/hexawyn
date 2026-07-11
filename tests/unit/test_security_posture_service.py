from __future__ import annotations

from hexawyn.application.ports.driven.security_posture_port import WorkloadComplianceRaw

_ALL_CATEGORIES = ["tls", "rbac", "pod_security", "image_scanning", "secret_rotation"]


def _raw(
    workload: str,
    category: str,
    compliant: bool = True,
    exempt: bool = False,
) -> WorkloadComplianceRaw:
    return WorkloadComplianceRaw(
        workload=workload,
        namespace="production",
        category=category,
        compliant=compliant,
        exempt=exempt,
        detail="" if compliant else f"{category} violation",
    )


class TestBuildReport:
    def test_fifty_workloads_forty_compliant(self) -> None:
        from hexawyn.domain.services.security_posture.security_posture_service import (
            SecurityPostureService,
        )

        records = [_raw(f"tls{i}", "tls", compliant=i >= 5) for i in range(10)]
        records += [_raw(f"psp{i}", "pod_security", compliant=i >= 3) for i in range(10)]
        records += [_raw(f"sec{i}", "secret_rotation", compliant=i >= 2) for i in range(10)]
        records += [_raw(f"rbac{i}", "rbac", compliant=True) for i in range(10)]
        records += [_raw(f"img{i}", "image_scanning", compliant=True) for i in range(10)]

        report = SecurityPostureService().build_report(
            records=records, defined_categories=_ALL_CATEGORIES, partial=False
        )

        tls = next(c for c in report.categories if c.category == "tls")
        assert tls.non_compliant == 5
        assert tls.score_pct == 50.0
        assert report.overall_score_pct < 100.0

    def test_all_compliant_no_remediation(self) -> None:
        from hexawyn.domain.services.security_posture.security_posture_service import (
            SecurityPostureService,
        )

        records = [_raw(f"w{i}", category) for i in range(3) for category in _ALL_CATEGORIES]

        report = SecurityPostureService().build_report(
            records=records, defined_categories=_ALL_CATEGORIES, partial=False
        )

        assert report.overall_score_pct == 100.0
        assert all(c.non_compliant_workloads == [] for c in report.categories)

    def test_new_workload_without_security_context_is_non_compliant(self) -> None:
        from hexawyn.domain.services.security_posture.security_posture_service import (
            SecurityPostureService,
        )

        records = [_raw("legacy", "pod_security", compliant=True)]
        records.append(_raw("new-deploy", "pod_security", compliant=False))

        report = SecurityPostureService().build_report(
            records=records, defined_categories=_ALL_CATEGORIES, partial=False
        )

        psp = next(c for c in report.categories if c.category == "pod_security")
        assert any(w.workload == "new-deploy" for w in psp.non_compliant_workloads)


class TestPolicyNotDefined:
    def test_missing_policy_flagged_not_compliant(self) -> None:
        from hexawyn.domain.services.security_posture.security_posture_service import (
            SecurityPostureService,
        )

        report = SecurityPostureService().build_report(
            records=[_raw("w", "tls", compliant=True)],
            defined_categories=["tls", "rbac", "pod_security", "image_scanning"],
            partial=False,
        )

        secret = next(c for c in report.categories if c.category == "secret_rotation")
        assert secret.policy_defined is False


class TestRemediationOrdering:
    def test_non_compliant_sorted_by_priority(self) -> None:
        from hexawyn.domain.services.security_posture.security_posture_service import (
            SecurityPostureService,
        )

        records = [
            _raw("tls-bad", "tls", compliant=False),
            _raw("img-bad", "image_scanning", compliant=False),
            _raw("rbac-bad", "rbac", compliant=False),
        ]

        report = SecurityPostureService().build_report(
            records=records, defined_categories=_ALL_CATEGORIES, partial=False
        )

        priorities = [w.remediation_priority for w in report.remediation_order]
        assert priorities == sorted(priorities)
        assert report.remediation_order[0].category == "image_scanning"


class TestTrend:
    def test_trend_improving_with_previous_score(self) -> None:
        from hexawyn.domain.services.security_posture.security_posture_service import (
            SecurityPostureService,
        )

        records = [_raw(f"w{i}", category) for i in range(4) for category in _ALL_CATEGORIES]

        report = SecurityPostureService().build_report(
            records=records,
            defined_categories=_ALL_CATEGORIES,
            partial=False,
            previous_score_pct=90.0,
        )

        assert report.previous_score_pct == 90.0
        assert report.trend == "improving"


class TestPartial:
    def test_partial_sets_warning(self) -> None:
        from hexawyn.domain.services.security_posture.security_posture_service import (
            SecurityPostureService,
        )

        report = SecurityPostureService().build_report(
            records=[_raw("w", "tls")],
            defined_categories=_ALL_CATEGORIES,
            partial=True,
        )

        assert report.partial is True
        assert report.warning != ""

    def test_complete_scan_no_warning(self) -> None:
        from hexawyn.domain.services.security_posture.security_posture_service import (
            SecurityPostureService,
        )

        report = SecurityPostureService().build_report(
            records=[_raw("w", "tls")],
            defined_categories=_ALL_CATEGORIES,
            partial=False,
        )

        assert report.partial is False
        assert report.warning == ""
