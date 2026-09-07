from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.policy import (
    Policy,
    PolicyAction,
    PolicyDenialExplanation,
    PolicyDetectionResult,
    PolicyEngine,
    PolicyViolation,
    ViolationSeverity,
)

_K8S_FORBIDDEN = 403
_KYVERNO_GROUP = "kyverno.io"
_KYVERNO_VERSION = "v1"
_POLICIES_PLURAL = "policies"
_POLICYREPORTS_PLURAL = "policyreports"

_ACTION_BY_NAME = {
    "enforce": PolicyAction.ENFORCE,
    "audit": PolicyAction.AUDIT,
    "generate": PolicyAction.GENERATE,
    "mutate": PolicyAction.MUTATE,
}


class PolicyDetector(PolicyPort):
    """Auto-detects Kyverno via CRD presence and reads policies / violations
    from the real K8s API. Read-only. Graceful degradation: a cluster without
    the Kyverno CRDs behaves as engine=NONE / empty lists; a 403 surfaces as
    InsufficientPermissionsError (consistent with the other K8s adapters)."""

    def _translate_error(self, exc: Exception) -> Exception:
        status = getattr(exc, "status", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def _list_crds(self, plural: str) -> list[dict[str, object]]:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_KYVERNO_GROUP,
                version=_KYVERNO_VERSION,
                plural=plural,
            )
        except Exception as exc:
            raise self._translate_error(exc) from exc
        items = raw.get("items", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def detect_engine(self) -> PolicyDetectionResult:
        try:
            policies = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return PolicyDetectionResult(
                engine=PolicyEngine.NONE,
                version=None,
                namespace=None,
                total_policies=0,
                enforce_policies=0,
                audit_policies=0,
                total_violations=0,
                high_severity=0,
            )
        enforce = audit = 0
        for p in policies:
            action = _policy_action(p).value
            if action == PolicyAction.ENFORCE.value:
                enforce += 1
            elif action == PolicyAction.AUDIT.value:
                audit += 1
        violations = self._list_violations_safe()
        high = sum(1 for v in violations if v.severity == ViolationSeverity.HIGH)
        return PolicyDetectionResult(
            engine=PolicyEngine.KYVERNO if policies else PolicyEngine.NONE,
            version=None,
            namespace=None,
            total_policies=len(policies),
            enforce_policies=enforce,
            audit_policies=audit,
            total_violations=len(violations),
            high_severity=high,
        )

    def list_policies(self, namespace: str | None = None) -> list[Policy]:
        try:
            raw = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_policy(item) for item in raw]

    def get_policy(self, name: str, namespace: str | None = None) -> Policy:
        for p in self.list_policies(namespace):
            if p.name == name:
                return p
        raise KeyError(f"Policy '{name}' not found.")

    def _list_violations_safe(self) -> list[PolicyViolation]:
        try:
            return self.list_violations()
        except Exception:
            return []

    def list_violations(self, namespace: str | None = None) -> list[PolicyViolation]:
        try:
            raw = self._list_crds(_POLICYREPORTS_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_violation(item) for item in raw]

    def explain_denial(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
                    resource_kind=v.resource_kind,
                    resource_name=v.resource_name,
                    namespace=v.resource_namespace,
                    policy_name=v.policy_name,
                    rule_name=v.rule_name,
                    raw_message=v.message,
                    human_explanation="The resource does not satisfy the policy "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def audit(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(1 for v in violations if v.severity == ViolationSeverity.HIGH)
        return {
            "total_policies": len(policies),
            "enforce_policies": enforce,
            "audit_policies": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }


def _as_dict(value: object) -> dict[str, object]:
    return value if isinstance(value, dict) else {}


def _policy_action(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def _to_policy(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        name=str(metadata.get("name", "?")),
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def _to_violation(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )
