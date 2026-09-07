from __future__ import annotations

from hexawyn.domain.models.security_posture import CategoryScore, WorkloadComplianceRaw


class TestScoreCategory:
    def test_all_compliant_no_exempt(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            score_category,
        )

        records: list[WorkloadComplianceRaw] = [
            {
                "workload": "svc-a",
                "namespace": "ns",
                "category": "tls",
                "compliant": True,
                "exempt": False,
                "detail": "",
            },
            {
                "workload": "svc-b",
                "namespace": "ns",
                "category": "tls",
                "compliant": True,
                "exempt": False,
                "detail": "",
            },
        ]

        result = score_category("tls", records, policy_defined=True)

        assert result.category == "tls"
        assert result.total == 2  # noqa: PLR2004
        assert result.compliant == 2  # noqa: PLR2004
        assert result.non_compliant == 0
        assert result.exempt == 0
        assert result.score_pct == 100.0  # noqa: PLR2004
        assert result.policy_defined is True
        assert result.non_compliant_workloads == []

    def test_all_non_compliant(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            score_category,
        )

        records: list[WorkloadComplianceRaw] = [
            {
                "workload": "svc-a",
                "namespace": "ns",
                "category": "rbac",
                "compliant": False,
                "exempt": False,
                "detail": "missing role",
            },
        ]

        result = score_category("rbac", records, policy_defined=True)

        assert result.score_pct == 0.0
        assert result.non_compliant == 1
        assert len(result.non_compliant_workloads) == 1
        assert result.non_compliant_workloads[0].workload == "svc-a"

    def test_mixed_compliant_non_compliant_exempt(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            score_category,
        )

        records: list[WorkloadComplianceRaw] = [
            {
                "workload": "svc-a",
                "namespace": "ns",
                "category": "rbac",
                "compliant": True,
                "exempt": False,
                "detail": "",
            },
            {
                "workload": "svc-b",
                "namespace": "ns",
                "category": "rbac",
                "compliant": False,
                "exempt": False,
                "detail": "",
            },
            {
                "workload": "svc-c",
                "namespace": "ns",
                "category": "rbac",
                "compliant": False,
                "exempt": True,
                "detail": "",
            },
        ]

        result = score_category("rbac", records, policy_defined=True)

        assert result.total == 2  # noqa: PLR2004
        assert result.compliant == 1
        assert result.non_compliant == 1
        assert result.exempt == 1
        assert result.score_pct == 50.0  # noqa: PLR2004

    def test_policy_not_defined_scores_zero(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            score_category,
        )

        records: list[WorkloadComplianceRaw] = [
            {
                "workload": "svc-a",
                "namespace": "ns",
                "category": "tls",
                "compliant": True,
                "exempt": False,
                "detail": "",
            },
        ]

        result = score_category("tls", records, policy_defined=False)

        assert result.score_pct == 0.0
        assert result.policy_defined is False

    def test_all_exempt_zero_evaluated(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            score_category,
        )

        records: list[WorkloadComplianceRaw] = [
            {
                "workload": "svc-a",
                "namespace": "ns",
                "category": "tls",
                "compliant": False,
                "exempt": True,
                "detail": "",
            },
            {
                "workload": "svc-b",
                "namespace": "ns",
                "category": "tls",
                "compliant": False,
                "exempt": True,
                "detail": "",
            },
        ]

        result = score_category("tls", records, policy_defined=True)

        assert result.total == 0
        assert result.exempt == 2  # noqa: PLR2004
        assert result.score_pct == 100.0  # noqa: PLR2004

    def test_empty_records_policy_defined(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            score_category,
        )

        result = score_category("tls", [], policy_defined=True)

        assert result.total == 0
        assert result.score_pct == 100.0  # noqa: PLR2004

    def test_empty_records_policy_undefined(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            score_category,
        )

        result = score_category("tls", [], policy_defined=False)

        assert result.score_pct == 0.0

    def test_result_is_category_score_instance(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            score_category,
        )

        result = score_category("tls", [], policy_defined=True)

        assert isinstance(result, CategoryScore)


class TestComputeOverallScore:
    def test_all_defined_categories_averaged(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            compute_overall_score,
        )

        categories = [
            CategoryScore(
                category="tls",
                total=10,
                compliant=10,
                non_compliant=0,
                exempt=0,
                score_pct=100.0,
                policy_defined=True,
                non_compliant_workloads=[],
            ),
            CategoryScore(
                category="rbac",
                total=10,
                compliant=5,
                non_compliant=5,
                exempt=0,
                score_pct=50.0,
                policy_defined=True,
                non_compliant_workloads=[],
            ),
        ]

        result = compute_overall_score(categories)

        assert result == 75.0  # noqa: PLR2004

    def test_undefined_categories_excluded_from_mean(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            compute_overall_score,
        )

        categories = [
            CategoryScore(
                category="tls",
                total=10,
                compliant=10,
                non_compliant=0,
                exempt=0,
                score_pct=100.0,
                policy_defined=True,
                non_compliant_workloads=[],
            ),
            CategoryScore(
                category="secret_rotation",
                total=0,
                compliant=0,
                non_compliant=0,
                exempt=0,
                score_pct=0.0,
                policy_defined=False,
                non_compliant_workloads=[],
            ),
        ]

        result = compute_overall_score(categories)

        assert result == 100.0  # noqa: PLR2004

    def test_no_defined_categories_returns_zero(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            compute_overall_score,
        )

        categories = [
            CategoryScore(
                category="tls",
                total=0,
                compliant=0,
                non_compliant=0,
                exempt=0,
                score_pct=0.0,
                policy_defined=False,
                non_compliant_workloads=[],
            ),
        ]

        result = compute_overall_score(categories)

        assert result == 0.0

    def test_empty_categories_list_returns_zero(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            compute_overall_score,
        )

        result = compute_overall_score([])

        assert result == 0.0

    def test_score_rounded_to_one_decimal(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            compute_overall_score,
        )

        categories = [
            CategoryScore(
                category="tls",
                total=3,
                compliant=1,
                non_compliant=2,
                exempt=0,
                score_pct=33.3,
                policy_defined=True,
                non_compliant_workloads=[],
            ),
            CategoryScore(
                category="rbac",
                total=3,
                compliant=2,
                non_compliant=1,
                exempt=0,
                score_pct=66.7,
                policy_defined=True,
                non_compliant_workloads=[],
            ),
        ]

        result = compute_overall_score(categories)

        assert result == round((33.3 + 66.7) / 2, 1)

    def test_return_type_is_float(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            compute_overall_score,
        )

        result = compute_overall_score([])

        assert isinstance(result, float)
