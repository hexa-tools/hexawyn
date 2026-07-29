from __future__ import annotations

from hexawyn.domain.models.security_posture import (
    CategoryScore,
    SecurityPostureReport,
    WorkloadCompliance,
    WorkloadComplianceRaw,
)
from hexawyn.domain.services.security_posture.security_posture_service import (
    SecurityPostureService,
    _remediation_order,
)


def _make_raw(  # noqa: PLR0913
    workload: str,
    namespace: str,
    category: str,
    compliant: bool = True,
    exempt: bool = False,
    detail: str = "",
) -> WorkloadComplianceRaw:
    return {
        "workload": workload,
        "namespace": namespace,
        "category": category,
        "compliant": compliant,
        "exempt": exempt,
        "detail": detail,
    }


class TestSecurityPostureService:
    def test_build_report_all_compliant(self) -> None:
        service = SecurityPostureService()
        records: list[WorkloadComplianceRaw] = [
            _make_raw("svc-a", "ns", "tls"),
            _make_raw("svc-b", "ns", "rbac"),
            _make_raw("svc-c", "ns", "pod_security"),
            _make_raw("svc-d", "ns", "image_scanning"),
            _make_raw("svc-e", "ns", "secret_rotation"),
        ]
        defined_categories = ["tls", "rbac", "pod_security", "image_scanning", "secret_rotation"]

        report = service.build_report(records, defined_categories, partial=False)

        assert isinstance(report, SecurityPostureReport)
        assert report.overall_score_pct == 100.0  # noqa: PLR2004
        assert report.partial is False
        assert report.warning == ""

    def test_build_report_all_non_compliant(self) -> None:
        service = SecurityPostureService()
        records: list[WorkloadComplianceRaw] = [
            _make_raw("svc-a", "ns", "tls", compliant=False),
            _make_raw("svc-b", "ns", "rbac", compliant=False),
            _make_raw("svc-c", "ns", "pod_security", compliant=False),
            _make_raw("svc-d", "ns", "image_scanning", compliant=False),
            _make_raw("svc-e", "ns", "secret_rotation", compliant=False),
        ]
        defined_categories = ["tls", "rbac", "pod_security", "image_scanning", "secret_rotation"]

        report = service.build_report(records, defined_categories, partial=False)

        assert report.overall_score_pct == 0.0
        assert len(report.remediation_order) > 0

    def test_build_report_empty_records_no_defined_categories(self) -> None:
        service = SecurityPostureService()

        report = service.build_report([], [], partial=False)

        assert report.overall_score_pct == 0.0
        assert report.trend == "stable"
        assert report.partial is False
        assert report.warning == ""

    def test_build_report_partial_sets_warning(self) -> None:
        service = SecurityPostureService()

        report = service.build_report([], [], partial=True)

        assert report.partial is True
        assert "Partial results" in report.warning

    def test_build_report_with_previous_score_improving(self) -> None:
        service = SecurityPostureService()
        records: list[WorkloadComplianceRaw] = [
            _make_raw("svc-a", "ns", "tls"),
            _make_raw("svc-b", "ns", "rbac"),
            _make_raw("svc-c", "ns", "pod_security"),
            _make_raw("svc-d", "ns", "image_scanning"),
            _make_raw("svc-e", "ns", "secret_rotation"),
        ]
        defined_categories = ["tls", "rbac", "pod_security", "image_scanning", "secret_rotation"]

        report = service.build_report(
            records, defined_categories, partial=False, previous_score_pct=50.0
        )

        assert report.overall_score_pct == 100.0  # noqa: PLR2004
        assert report.trend == "improving"
        assert report.previous_score_pct == 50.0  # noqa: PLR2004

    def test_build_report_with_previous_score_degrading(self) -> None:
        service = SecurityPostureService()
        records: list[WorkloadComplianceRaw] = [
            _make_raw("svc-a", "ns", "tls", compliant=False),
        ]

        report = service.build_report(records, ["tls"], partial=False, previous_score_pct=100.0)

        assert report.trend == "degrading"

    def test_build_report_with_none_previous_score(self) -> None:
        service = SecurityPostureService()

        report = service.build_report([], [], partial=False, previous_score_pct=None)

        assert report.previous_score_pct is None
        assert report.trend == "stable"

    def test_remediation_order_sorted_by_priority(self) -> None:
        service = SecurityPostureService()
        records: list[WorkloadComplianceRaw] = [
            _make_raw("high-prio", "ns", "image_scanning", compliant=False),
            _make_raw("low-prio", "ns", "tls", compliant=False),
        ]
        defined_categories = ["image_scanning", "tls"]

        report = service.build_report(records, defined_categories, partial=False)

        assert len(report.remediation_order) == 2  # noqa: PLR2004
        assert report.remediation_order[0].workload == "high-prio"
        assert report.remediation_order[1].workload == "low-prio"

    def test_remediation_order_empty_when_no_non_compliant(self) -> None:
        service = SecurityPostureService()
        records: list[WorkloadComplianceRaw] = [
            _make_raw("svc-a", "ns", "tls", compliant=True),
        ]

        report = service.build_report(records, ["tls"], partial=False)

        assert report.remediation_order == []

    def test_category_not_in_defined_categories_scores_zero(self) -> None:
        service = SecurityPostureService()
        records: list[WorkloadComplianceRaw] = [
            _make_raw("svc-a", "ns", "tls", compliant=True),
        ]

        report = service.build_report(records, [], partial=False)

        assert report.overall_score_pct == 0.0

    def test_all_categories_present_in_report(self) -> None:
        service = SecurityPostureService()

        report = service.build_report([], [], partial=False)

        category_names = [c.category for c in report.categories]
        assert "tls" in category_names
        assert "rbac" in category_names
        assert "pod_security" in category_names
        assert "image_scanning" in category_names
        assert "secret_rotation" in category_names


class TestRemediationOrder:
    def test_empty_categories_returns_empty_list(self) -> None:
        result = _remediation_order([])

        assert result == []

    def test_sorts_by_remediation_priority_ascending(self) -> None:
        categories = [
            CategoryScore(
                category="cat-a",
                total=1,
                compliant=0,
                non_compliant=1,
                exempt=0,
                score_pct=0.0,
                policy_defined=True,
                non_compliant_workloads=[
                    WorkloadCompliance(
                        workload="low",
                        namespace="ns",
                        category="cat-a",
                        status="non_compliant",
                        remediation_priority=10,
                        detail="",
                    ),
                ],
            ),
            CategoryScore(
                category="cat-b",
                total=1,
                compliant=0,
                non_compliant=1,
                exempt=0,
                score_pct=0.0,
                policy_defined=True,
                non_compliant_workloads=[
                    WorkloadCompliance(
                        workload="high",
                        namespace="ns",
                        category="cat-b",
                        status="non_compliant",
                        remediation_priority=1,
                        detail="",
                    ),
                ],
            ),
        ]

        result = _remediation_order(categories)

        assert result[0].workload == "high"
        assert result[1].workload == "low"
