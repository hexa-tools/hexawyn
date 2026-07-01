from __future__ import annotations

from hexawyn.domain.models.policy import (
    Policy,
    PolicyAction,
    PolicyDenialExplanation,
    PolicyDetectionResult,
    PolicyEngine,
    PolicyViolation,
    ViolationSeverity,
)


class TestEnums:
    def test_policy_engine(self) -> None:
        assert PolicyEngine.KYVERNO.value == "kyverno"
        assert PolicyEngine.GATEKEEPER.value == "gatekeeper"
        assert PolicyEngine.NONE.value == "none"

    def test_policy_action(self) -> None:
        assert PolicyAction.ENFORCE.value == "enforce"
        assert PolicyAction.AUDIT.value == "audit"

    def test_violation_severity(self) -> None:
        assert ViolationSeverity.HIGH.value == "high"
        assert ViolationSeverity.LOW.value == "low"


class TestPolicy:
    def test_cluster_policy(self) -> None:
        p = Policy(
            name="require-run-as-non-root",
            namespace=None,
            engine=PolicyEngine.KYVERNO,
            kind="ClusterPolicy",
            action=PolicyAction.ENFORCE,
            description="Blocks root containers",
            rules_count=1,
            violations_count=3,
            ready=True,
        )
        assert p.namespace is None
        assert p.violations_count == 3

    def test_namespaced_policy(self) -> None:
        p = Policy(
            name="deny-latest-tag",
            namespace="production",
            engine=PolicyEngine.GATEKEEPER,
            kind="Constraint",
            action=PolicyAction.AUDIT,
            description=None,
            rules_count=2,
            violations_count=0,
            ready=True,
        )
        assert p.namespace == "production"


class TestPolicyViolation:
    def test_enforce_violation(self) -> None:
        v = PolicyViolation(
            policy_name="require-run-as-non-root",
            resource_kind="Deployment",
            resource_name="nginx",
            resource_namespace="default",
            rule_name="check-containers",
            message="Running as root is forbidden",
            severity=ViolationSeverity.HIGH,
            action=PolicyAction.ENFORCE,
            timestamp="2026-07-01T12:00:00Z",
        )
        assert v.action == PolicyAction.ENFORCE
        assert v.severity == ViolationSeverity.HIGH


class TestPolicyDenialExplanation:
    def test_all_fields_filled(self) -> None:
        e = PolicyDenialExplanation(
            resource_kind="Pod",
            resource_name="nginx-abc",
            namespace="default",
            policy_name="require-run-as-non-root",
            rule_name="check-containers",
            raw_message="admission webhook denied: Running as root is forbidden",
            human_explanation="Your pod nginx-abc runs as root which is blocked by policy require-run-as-non-root.",
            fix_suggestion="Set securityContext.runAsNonRoot to true and use a non-root user.",
        )
        assert e.human_explanation != ""
        assert e.fix_suggestion != ""


class TestPolicyDetectionResult:
    def test_kyverno_detected(self) -> None:
        r = PolicyDetectionResult(
            engine=PolicyEngine.KYVERNO,
            version="v1.13.0",
            namespace="kyverno",
            total_policies=8,
            enforce_policies=5,
            audit_policies=3,
            total_violations=12,
            high_severity=4,
        )
        assert r.engine == PolicyEngine.KYVERNO
        assert r.total_violations == 12


class TestPolicyEngineNotFoundError:
    def test_inherits_and_message(self) -> None:
        from hexawyn.domain.errors import HexawynError, PolicyEngineNotFoundError

        error = PolicyEngineNotFoundError()
        assert isinstance(error, HexawynError)
        assert "policy engine" in str(error).lower()
        assert "kyverno" in str(error).lower()
