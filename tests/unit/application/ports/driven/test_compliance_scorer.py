from __future__ import annotations

from hexawyn.application.ports.driven.security_posture_port import WorkloadComplianceRaw


def _raw(
    workload: str,
    category: str,
    compliant: bool = True,
    exempt: bool = False,
    namespace: str = "production",
    detail: str = "",
) -> WorkloadComplianceRaw:
    return WorkloadComplianceRaw(
        workload=workload,
        namespace=namespace,
        category=category,
        compliant=compliant,
        exempt=exempt,
        detail=detail,
    )


class TestCategoryScoring:
    def test_eighty_percent_compliant(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import score_category

        records = [_raw(f"w{i}", "tls", compliant=True) for i in range(8)]
        records += [_raw(f"bad{i}", "tls", compliant=False) for i in range(2)]

        score = score_category("tls", records, policy_defined=True)

        assert score.total == 10
        assert score.compliant == 8
        assert score.non_compliant == 2
        assert score.score_pct == 80.0

    def test_all_compliant_is_hundred_percent(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import score_category

        records = [_raw(f"w{i}", "rbac", compliant=True) for i in range(5)]

        score = score_category("rbac", records, policy_defined=True)

        assert score.score_pct == 100.0
        assert score.non_compliant_workloads == []


class TestExemption:
    def test_exempt_workloads_excluded_from_denominator(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import score_category

        records = [
            _raw("a", "tls", compliant=True),
            _raw("b", "tls", compliant=True),
            _raw("legacy", "tls", compliant=False, exempt=True),
        ]

        score = score_category("tls", records, policy_defined=True)

        assert score.exempt == 1
        assert score.total == 2
        assert score.score_pct == 100.0

    def test_exempt_not_listed_as_non_compliant(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import score_category

        records = [_raw("legacy", "tls", compliant=False, exempt=True)]

        score = score_category("tls", records, policy_defined=True)

        assert score.non_compliant_workloads == []


class TestPolicyNotDefined:
    def test_policy_not_defined_is_not_compliant(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import score_category

        score = score_category("secret_rotation", [], policy_defined=False)

        assert score.policy_defined is False
        assert score.score_pct == 0.0

    def test_defined_policy_with_no_workloads_is_hundred(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import score_category

        score = score_category("secret_rotation", [], policy_defined=True)

        assert score.policy_defined is True
        assert score.score_pct == 100.0


class TestRemediationPriority:
    def test_non_compliant_workloads_carry_priority(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import score_category

        records = [_raw("scanme", "image_scanning", compliant=False)]

        score = score_category("image_scanning", records, policy_defined=True)

        assert score.non_compliant_workloads[0].remediation_priority == 1

    def test_tls_priority_lower_than_image_scanning(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import score_category

        image = score_category(
            "image_scanning", [_raw("a", "image_scanning", compliant=False)], policy_defined=True
        )
        tls = score_category("tls", [_raw("b", "tls", compliant=False)], policy_defined=True)

        assert (
            image.non_compliant_workloads[0].remediation_priority
            < tls.non_compliant_workloads[0].remediation_priority
        )


class TestOverallScore:
    def test_overall_is_mean_of_defined_categories(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            compute_overall_score,
            score_category,
        )

        tls = score_category("tls", [_raw("a", "tls", compliant=True)], policy_defined=True)
        rbac = score_category("rbac", [_raw("b", "rbac", compliant=False)], policy_defined=True)

        overall = compute_overall_score([tls, rbac])

        assert overall == 50.0

    def test_overall_ignores_undefined_policies(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            compute_overall_score,
            score_category,
        )

        tls = score_category("tls", [_raw("a", "tls", compliant=True)], policy_defined=True)
        undefined = score_category("secret_rotation", [], policy_defined=False)

        overall = compute_overall_score([tls, undefined])

        assert overall == 100.0

    def test_overall_zero_when_no_defined_policies(self) -> None:
        from hexawyn.domain.services.security_posture.compliance_scorer import (
            compute_overall_score,
            score_category,
        )

        undefined = score_category("secret_rotation", [], policy_defined=False)

        assert compute_overall_score([undefined]) == 0.0
