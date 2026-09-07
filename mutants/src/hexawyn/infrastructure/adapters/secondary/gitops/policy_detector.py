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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPolicyDetectorǁ_translate_error__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyDetectorǁ_list_crds__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyDetectorǁdetect_engine__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyDetectorǁlist_policies__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyDetectorǁget_policy__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyDetectorǁlist_violations__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyDetectorǁexplain_denial__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyDetectorǁaudit__mutmut: MutantDict = {}  # type: ignore


class PolicyDetector(PolicyPort):
    """Auto-detects Kyverno via CRD presence and reads policies / violations
    from the real K8s API. Read-only. Graceful degradation: a cluster without
    the Kyverno CRDs behaves as engine=NONE / empty lists; a 403 surfaces as
    InsufficientPermissionsError (consistent with the other K8s adapters)."""

    @_mutmut_mutated(mutants_xǁPolicyDetectorǁ_translate_error__mutmut)
    def _translate_error(self, exc: Exception) -> Exception:
        status = getattr(exc, "status", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_orig(self, exc: Exception) -> Exception:
        status = getattr(exc, "status", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_1(self, exc: Exception) -> Exception:
        status = None
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_2(self, exc: Exception) -> Exception:
        status = getattr(None, "status", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_3(self, exc: Exception) -> Exception:
        status = getattr(exc, None, None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_4(self, exc: Exception) -> Exception:
        status = getattr("status", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_5(self, exc: Exception) -> Exception:
        status = getattr(exc, None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_6(self, exc: Exception) -> Exception:
        status = getattr(exc, "status", )
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_7(self, exc: Exception) -> Exception:
        status = getattr(exc, "XXstatusXX", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_8(self, exc: Exception) -> Exception:
        status = getattr(exc, "STATUS", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_9(self, exc: Exception) -> Exception:
        status = getattr(exc, "status", None)
        if status != _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC denied access to Kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_10(self, exc: Exception) -> Exception:
        status = getattr(exc, "status", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError(None)
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_11(self, exc: Exception) -> Exception:
        status = getattr(exc, "status", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("XXRBAC denied access to Kyverno resourcesXX")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_12(self, exc: Exception) -> Exception:
        status = getattr(exc, "status", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("rbac denied access to kyverno resources")
        return exc

    def xǁPolicyDetectorǁ_translate_error__mutmut_13(self, exc: Exception) -> Exception:
        status = getattr(exc, "status", None)
        if status == _K8S_FORBIDDEN:
            return InsufficientPermissionsError("RBAC DENIED ACCESS TO KYVERNO RESOURCES")
        return exc

    @_mutmut_mutated(mutants_xǁPolicyDetectorǁ_list_crds__mutmut)
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

    def xǁPolicyDetectorǁ_list_crds__mutmut_orig(self, plural: str) -> list[dict[str, object]]:
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

    def xǁPolicyDetectorǁ_list_crds__mutmut_1(self, plural: str) -> list[dict[str, object]]:
        from kubernetes import client as k8s

        try:
            crd_api = None
            raw = crd_api.list_cluster_custom_object(
                group=_KYVERNO_GROUP,
                version=_KYVERNO_VERSION,
                plural=plural,
            )
        except Exception as exc:
            raise self._translate_error(exc) from exc
        items = raw.get("items", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_2(self, plural: str) -> list[dict[str, object]]:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = None
        except Exception as exc:
            raise self._translate_error(exc) from exc
        items = raw.get("items", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_3(self, plural: str) -> list[dict[str, object]]:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=None,
                version=_KYVERNO_VERSION,
                plural=plural,
            )
        except Exception as exc:
            raise self._translate_error(exc) from exc
        items = raw.get("items", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_4(self, plural: str) -> list[dict[str, object]]:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_KYVERNO_GROUP,
                version=None,
                plural=plural,
            )
        except Exception as exc:
            raise self._translate_error(exc) from exc
        items = raw.get("items", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_5(self, plural: str) -> list[dict[str, object]]:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_KYVERNO_GROUP,
                version=_KYVERNO_VERSION,
                plural=None,
            )
        except Exception as exc:
            raise self._translate_error(exc) from exc
        items = raw.get("items", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_6(self, plural: str) -> list[dict[str, object]]:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                version=_KYVERNO_VERSION,
                plural=plural,
            )
        except Exception as exc:
            raise self._translate_error(exc) from exc
        items = raw.get("items", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_7(self, plural: str) -> list[dict[str, object]]:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_KYVERNO_GROUP,
                plural=plural,
            )
        except Exception as exc:
            raise self._translate_error(exc) from exc
        items = raw.get("items", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_8(self, plural: str) -> list[dict[str, object]]:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_KYVERNO_GROUP,
                version=_KYVERNO_VERSION,
                )
        except Exception as exc:
            raise self._translate_error(exc) from exc
        items = raw.get("items", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_9(self, plural: str) -> list[dict[str, object]]:
        from kubernetes import client as k8s

        try:
            crd_api = k8s.CustomObjectsApi()
            raw = crd_api.list_cluster_custom_object(
                group=_KYVERNO_GROUP,
                version=_KYVERNO_VERSION,
                plural=plural,
            )
        except Exception as exc:
            raise self._translate_error(None) from exc
        items = raw.get("items", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_10(self, plural: str) -> list[dict[str, object]]:
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
        items = None
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_11(self, plural: str) -> list[dict[str, object]]:
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
        items = raw.get(None, []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_12(self, plural: str) -> list[dict[str, object]]:
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
        items = raw.get("items", None) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_13(self, plural: str) -> list[dict[str, object]]:
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
        items = raw.get([]) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_14(self, plural: str) -> list[dict[str, object]]:
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
        items = raw.get("items", ) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_15(self, plural: str) -> list[dict[str, object]]:
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
        items = raw.get("XXitemsXX", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    def xǁPolicyDetectorǁ_list_crds__mutmut_16(self, plural: str) -> list[dict[str, object]]:
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
        items = raw.get("ITEMS", []) if isinstance(raw, dict) else []
        return [item for item in items if isinstance(item, dict)]

    @_mutmut_mutated(mutants_xǁPolicyDetectorǁdetect_engine__mutmut)
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_orig(self) -> PolicyDetectionResult:
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_1(self) -> PolicyDetectionResult:
        try:
            policies = None
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_2(self) -> PolicyDetectionResult:
        try:
            policies = self._list_crds(None)
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_3(self) -> PolicyDetectionResult:
        try:
            policies = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return PolicyDetectionResult(
                engine=None,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_4(self) -> PolicyDetectionResult:
        try:
            policies = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return PolicyDetectionResult(
                engine=PolicyEngine.NONE,
                version=None,
                namespace=None,
                total_policies=None,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_5(self) -> PolicyDetectionResult:
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
                enforce_policies=None,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_6(self) -> PolicyDetectionResult:
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
                audit_policies=None,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_7(self) -> PolicyDetectionResult:
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
                total_violations=None,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_8(self) -> PolicyDetectionResult:
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
                high_severity=None,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_9(self) -> PolicyDetectionResult:
        try:
            policies = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return PolicyDetectionResult(
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_10(self) -> PolicyDetectionResult:
        try:
            policies = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return PolicyDetectionResult(
                engine=PolicyEngine.NONE,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_11(self) -> PolicyDetectionResult:
        try:
            policies = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return PolicyDetectionResult(
                engine=PolicyEngine.NONE,
                version=None,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_12(self) -> PolicyDetectionResult:
        try:
            policies = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return PolicyDetectionResult(
                engine=PolicyEngine.NONE,
                version=None,
                namespace=None,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_13(self) -> PolicyDetectionResult:
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_14(self) -> PolicyDetectionResult:
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_15(self) -> PolicyDetectionResult:
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_16(self) -> PolicyDetectionResult:
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_17(self) -> PolicyDetectionResult:
        try:
            policies = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return PolicyDetectionResult(
                engine=PolicyEngine.NONE,
                version=None,
                namespace=None,
                total_policies=1,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_18(self) -> PolicyDetectionResult:
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
                enforce_policies=1,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_19(self) -> PolicyDetectionResult:
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
                audit_policies=1,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_20(self) -> PolicyDetectionResult:
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
                total_violations=1,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_21(self) -> PolicyDetectionResult:
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
                high_severity=1,
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_22(self) -> PolicyDetectionResult:
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
        enforce = audit = None
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_23(self) -> PolicyDetectionResult:
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
        enforce = audit = 1
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_24(self) -> PolicyDetectionResult:
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
            action = None
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_25(self) -> PolicyDetectionResult:
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
            action = _policy_action(None).value
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_26(self) -> PolicyDetectionResult:
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
            if action != PolicyAction.ENFORCE.value:
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_27(self) -> PolicyDetectionResult:
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
                enforce = 1
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_28(self) -> PolicyDetectionResult:
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
                enforce -= 1
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_29(self) -> PolicyDetectionResult:
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
                enforce += 2
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_30(self) -> PolicyDetectionResult:
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
            elif action != PolicyAction.AUDIT.value:
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_31(self) -> PolicyDetectionResult:
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
                audit = 1
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_32(self) -> PolicyDetectionResult:
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
                audit -= 1
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_33(self) -> PolicyDetectionResult:
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
                audit += 2
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_34(self) -> PolicyDetectionResult:
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
        violations = None
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_35(self) -> PolicyDetectionResult:
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
        high = None
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_36(self) -> PolicyDetectionResult:
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
        high = sum(None)
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_37(self) -> PolicyDetectionResult:
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
        high = sum(2 for v in violations if v.severity == ViolationSeverity.HIGH)
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_38(self) -> PolicyDetectionResult:
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
        high = sum(1 for v in violations if v.severity != ViolationSeverity.HIGH)
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

    def xǁPolicyDetectorǁdetect_engine__mutmut_39(self) -> PolicyDetectionResult:
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
            engine=None,
            version=None,
            namespace=None,
            total_policies=len(policies),
            enforce_policies=enforce,
            audit_policies=audit,
            total_violations=len(violations),
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_40(self) -> PolicyDetectionResult:
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
            total_policies=None,
            enforce_policies=enforce,
            audit_policies=audit,
            total_violations=len(violations),
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_41(self) -> PolicyDetectionResult:
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
            enforce_policies=None,
            audit_policies=audit,
            total_violations=len(violations),
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_42(self) -> PolicyDetectionResult:
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
            audit_policies=None,
            total_violations=len(violations),
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_43(self) -> PolicyDetectionResult:
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
            total_violations=None,
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_44(self) -> PolicyDetectionResult:
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
            high_severity=None,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_45(self) -> PolicyDetectionResult:
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
            version=None,
            namespace=None,
            total_policies=len(policies),
            enforce_policies=enforce,
            audit_policies=audit,
            total_violations=len(violations),
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_46(self) -> PolicyDetectionResult:
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
            namespace=None,
            total_policies=len(policies),
            enforce_policies=enforce,
            audit_policies=audit,
            total_violations=len(violations),
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_47(self) -> PolicyDetectionResult:
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
            total_policies=len(policies),
            enforce_policies=enforce,
            audit_policies=audit,
            total_violations=len(violations),
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_48(self) -> PolicyDetectionResult:
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
            enforce_policies=enforce,
            audit_policies=audit,
            total_violations=len(violations),
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_49(self) -> PolicyDetectionResult:
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
            audit_policies=audit,
            total_violations=len(violations),
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_50(self) -> PolicyDetectionResult:
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
            total_violations=len(violations),
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_51(self) -> PolicyDetectionResult:
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
            high_severity=high,
        )

    def xǁPolicyDetectorǁdetect_engine__mutmut_52(self) -> PolicyDetectionResult:
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
            )

    @_mutmut_mutated(mutants_xǁPolicyDetectorǁlist_policies__mutmut)
    def list_policies(self, namespace: str | None = None) -> list[Policy]:
        try:
            raw = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_policy(item) for item in raw]

    def xǁPolicyDetectorǁlist_policies__mutmut_orig(self, namespace: str | None = None) -> list[Policy]:
        try:
            raw = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_policy(item) for item in raw]

    def xǁPolicyDetectorǁlist_policies__mutmut_1(self, namespace: str | None = None) -> list[Policy]:
        try:
            raw = None
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_policy(item) for item in raw]

    def xǁPolicyDetectorǁlist_policies__mutmut_2(self, namespace: str | None = None) -> list[Policy]:
        try:
            raw = self._list_crds(None)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_policy(item) for item in raw]

    def xǁPolicyDetectorǁlist_policies__mutmut_3(self, namespace: str | None = None) -> list[Policy]:
        try:
            raw = self._list_crds(_POLICIES_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_policy(None) for item in raw]

    @_mutmut_mutated(mutants_xǁPolicyDetectorǁget_policy__mutmut)
    def get_policy(self, name: str, namespace: str | None = None) -> Policy:
        for p in self.list_policies(namespace):
            if p.name == name:
                return p
        raise KeyError(f"Policy '{name}' not found.")

    def xǁPolicyDetectorǁget_policy__mutmut_orig(self, name: str, namespace: str | None = None) -> Policy:
        for p in self.list_policies(namespace):
            if p.name == name:
                return p
        raise KeyError(f"Policy '{name}' not found.")

    def xǁPolicyDetectorǁget_policy__mutmut_1(self, name: str, namespace: str | None = None) -> Policy:
        for p in self.list_policies(None):
            if p.name == name:
                return p
        raise KeyError(f"Policy '{name}' not found.")

    def xǁPolicyDetectorǁget_policy__mutmut_2(self, name: str, namespace: str | None = None) -> Policy:
        for p in self.list_policies(namespace):
            if p.name != name:
                return p
        raise KeyError(f"Policy '{name}' not found.")

    def xǁPolicyDetectorǁget_policy__mutmut_3(self, name: str, namespace: str | None = None) -> Policy:
        for p in self.list_policies(namespace):
            if p.name == name:
                return p
        raise KeyError(None)

    def _list_violations_safe(self) -> list[PolicyViolation]:
        try:
            return self.list_violations()
        except Exception:
            return []

    @_mutmut_mutated(mutants_xǁPolicyDetectorǁlist_violations__mutmut)
    def list_violations(self, namespace: str | None = None) -> list[PolicyViolation]:
        try:
            raw = self._list_crds(_POLICYREPORTS_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_violation(item) for item in raw]

    def xǁPolicyDetectorǁlist_violations__mutmut_orig(self, namespace: str | None = None) -> list[PolicyViolation]:
        try:
            raw = self._list_crds(_POLICYREPORTS_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_violation(item) for item in raw]

    def xǁPolicyDetectorǁlist_violations__mutmut_1(self, namespace: str | None = None) -> list[PolicyViolation]:
        try:
            raw = None
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_violation(item) for item in raw]

    def xǁPolicyDetectorǁlist_violations__mutmut_2(self, namespace: str | None = None) -> list[PolicyViolation]:
        try:
            raw = self._list_crds(None)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_violation(item) for item in raw]

    def xǁPolicyDetectorǁlist_violations__mutmut_3(self, namespace: str | None = None) -> list[PolicyViolation]:
        try:
            raw = self._list_crds(_POLICYREPORTS_PLURAL)
        except InsufficientPermissionsError:
            raise
        except Exception:
            return []
        return [_to_violation(None) for item in raw]

    @_mutmut_mutated(mutants_xǁPolicyDetectorǁexplain_denial__mutmut)
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

    def xǁPolicyDetectorǁexplain_denial__mutmut_orig(
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

    def xǁPolicyDetectorǁexplain_denial__mutmut_1(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(None):
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

    def xǁPolicyDetectorǁexplain_denial__mutmut_2(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name != resource_name:
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

    def xǁPolicyDetectorǁexplain_denial__mutmut_3(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
                    resource_kind=None,
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

    def xǁPolicyDetectorǁexplain_denial__mutmut_4(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
                    resource_kind=v.resource_kind,
                    resource_name=None,
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

    def xǁPolicyDetectorǁexplain_denial__mutmut_5(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
                    resource_kind=v.resource_kind,
                    resource_name=v.resource_name,
                    namespace=None,
                    policy_name=v.policy_name,
                    rule_name=v.rule_name,
                    raw_message=v.message,
                    human_explanation="The resource does not satisfy the policy "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_6(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
                    resource_kind=v.resource_kind,
                    resource_name=v.resource_name,
                    namespace=v.resource_namespace,
                    policy_name=None,
                    rule_name=v.rule_name,
                    raw_message=v.message,
                    human_explanation="The resource does not satisfy the policy "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_7(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
                    resource_kind=v.resource_kind,
                    resource_name=v.resource_name,
                    namespace=v.resource_namespace,
                    policy_name=v.policy_name,
                    rule_name=None,
                    raw_message=v.message,
                    human_explanation="The resource does not satisfy the policy "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_8(
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
                    raw_message=None,
                    human_explanation="The resource does not satisfy the policy "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_9(
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
                    human_explanation=None,
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_10(
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
                    fix_suggestion=None,
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_11(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
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

    def xǁPolicyDetectorǁexplain_denial__mutmut_12(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
                    resource_kind=v.resource_kind,
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

    def xǁPolicyDetectorǁexplain_denial__mutmut_13(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
                    resource_kind=v.resource_kind,
                    resource_name=v.resource_name,
                    policy_name=v.policy_name,
                    rule_name=v.rule_name,
                    raw_message=v.message,
                    human_explanation="The resource does not satisfy the policy "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_14(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
                    resource_kind=v.resource_kind,
                    resource_name=v.resource_name,
                    namespace=v.resource_namespace,
                    rule_name=v.rule_name,
                    raw_message=v.message,
                    human_explanation="The resource does not satisfy the policy "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_15(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        for v in self.list_violations(namespace):
            if v.resource_name == resource_name:
                return PolicyDenialExplanation(
                    resource_kind=v.resource_kind,
                    resource_name=v.resource_name,
                    namespace=v.resource_namespace,
                    policy_name=v.policy_name,
                    raw_message=v.message,
                    human_explanation="The resource does not satisfy the policy "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_16(
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
                    human_explanation="The resource does not satisfy the policy "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_17(
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
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_18(
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
                    )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_19(
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
                    human_explanation="XXThe resource does not satisfy the policy XX"
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_20(
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
                    human_explanation="the resource does not satisfy the policy "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_21(
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
                    human_explanation="THE RESOURCE DOES NOT SATISFY THE POLICY "
                    f"'{v.policy_name}' as enforced by Kyverno.",
                    fix_suggestion=f"Update {resource_kind}/{resource_name} to satisfy "
                    f"'{v.policy_name}': {v.message}",
                )
        raise KeyError(f"No policy denial found for {resource_kind}/{resource_name}.")

    def xǁPolicyDetectorǁexplain_denial__mutmut_22(
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
        raise KeyError(None)

    @_mutmut_mutated(mutants_xǁPolicyDetectorǁaudit__mutmut)
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

    def xǁPolicyDetectorǁaudit__mutmut_orig(self, namespace: str | None = None) -> dict[str, object]:
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

    def xǁPolicyDetectorǁaudit__mutmut_1(self, namespace: str | None = None) -> dict[str, object]:
        policies = None
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

    def xǁPolicyDetectorǁaudit__mutmut_2(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(None)
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

    def xǁPolicyDetectorǁaudit__mutmut_3(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = None
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

    def xǁPolicyDetectorǁaudit__mutmut_4(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = None
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

    def xǁPolicyDetectorǁaudit__mutmut_5(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(None)
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

    def xǁPolicyDetectorǁaudit__mutmut_6(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(2 for p in policies if p.action == PolicyAction.ENFORCE)
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

    def xǁPolicyDetectorǁaudit__mutmut_7(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action != PolicyAction.ENFORCE)
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

    def xǁPolicyDetectorǁaudit__mutmut_8(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = None
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

    def xǁPolicyDetectorǁaudit__mutmut_9(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(None)
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

    def xǁPolicyDetectorǁaudit__mutmut_10(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(2 for p in policies if p.action == PolicyAction.AUDIT)
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

    def xǁPolicyDetectorǁaudit__mutmut_11(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action != PolicyAction.AUDIT)
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

    def xǁPolicyDetectorǁaudit__mutmut_12(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = None
        return {
            "total_policies": len(policies),
            "enforce_policies": enforce,
            "audit_policies": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_13(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(None)
        return {
            "total_policies": len(policies),
            "enforce_policies": enforce,
            "audit_policies": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_14(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(2 for v in violations if v.severity == ViolationSeverity.HIGH)
        return {
            "total_policies": len(policies),
            "enforce_policies": enforce,
            "audit_policies": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_15(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(1 for v in violations if v.severity != ViolationSeverity.HIGH)
        return {
            "total_policies": len(policies),
            "enforce_policies": enforce,
            "audit_policies": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_16(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(1 for v in violations if v.severity == ViolationSeverity.HIGH)
        return {
            "XXtotal_policiesXX": len(policies),
            "enforce_policies": enforce,
            "audit_policies": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_17(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(1 for v in violations if v.severity == ViolationSeverity.HIGH)
        return {
            "TOTAL_POLICIES": len(policies),
            "enforce_policies": enforce,
            "audit_policies": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_18(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(1 for v in violations if v.severity == ViolationSeverity.HIGH)
        return {
            "total_policies": len(policies),
            "XXenforce_policiesXX": enforce,
            "audit_policies": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_19(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(1 for v in violations if v.severity == ViolationSeverity.HIGH)
        return {
            "total_policies": len(policies),
            "ENFORCE_POLICIES": enforce,
            "audit_policies": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_20(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(1 for v in violations if v.severity == ViolationSeverity.HIGH)
        return {
            "total_policies": len(policies),
            "enforce_policies": enforce,
            "XXaudit_policiesXX": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_21(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(1 for v in violations if v.severity == ViolationSeverity.HIGH)
        return {
            "total_policies": len(policies),
            "enforce_policies": enforce,
            "AUDIT_POLICIES": audit,
            "total_violations": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_22(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(1 for v in violations if v.severity == ViolationSeverity.HIGH)
        return {
            "total_policies": len(policies),
            "enforce_policies": enforce,
            "audit_policies": audit,
            "XXtotal_violationsXX": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_23(self, namespace: str | None = None) -> dict[str, object]:
        policies = self.list_policies(namespace)
        violations = self._list_violations_safe()
        enforce = sum(1 for p in policies if p.action == PolicyAction.ENFORCE)
        audit = sum(1 for p in policies if p.action == PolicyAction.AUDIT)
        high = sum(1 for v in violations if v.severity == ViolationSeverity.HIGH)
        return {
            "total_policies": len(policies),
            "enforce_policies": enforce,
            "audit_policies": audit,
            "TOTAL_VIOLATIONS": len(violations),
            "high_severity": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_24(self, namespace: str | None = None) -> dict[str, object]:
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
            "XXhigh_severityXX": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_25(self, namespace: str | None = None) -> dict[str, object]:
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
            "HIGH_SEVERITY": high,
            "policies": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_26(self, namespace: str | None = None) -> dict[str, object]:
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
            "XXpoliciesXX": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_27(self, namespace: str | None = None) -> dict[str, object]:
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
            "POLICIES": [p.name for p in policies],
            "violations": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_28(self, namespace: str | None = None) -> dict[str, object]:
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
            "XXviolationsXX": [v.resource_name for v in violations],
        }

    def xǁPolicyDetectorǁaudit__mutmut_29(self, namespace: str | None = None) -> dict[str, object]:
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
            "VIOLATIONS": [v.resource_name for v in violations],
        }

mutants_xǁPolicyDetectorǁ_translate_error__mutmut['_mutmut_orig'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_1'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_2'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_3'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_4'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_5'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_6'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_7'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_8'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_9'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_10'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_11'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_12'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_translate_error__mutmut['xǁPolicyDetectorǁ_translate_error__mutmut_13'] = PolicyDetector.xǁPolicyDetectorǁ_translate_error__mutmut_13 # type: ignore # mutmut generated

mutants_xǁPolicyDetectorǁ_list_crds__mutmut['_mutmut_orig'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_1'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_2'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_3'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_4'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_5'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_6'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_7'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_8'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_9'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_10'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_11'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_12'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_13'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_14'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_15'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁ_list_crds__mutmut['xǁPolicyDetectorǁ_list_crds__mutmut_16'] = PolicyDetector.xǁPolicyDetectorǁ_list_crds__mutmut_16 # type: ignore # mutmut generated

mutants_xǁPolicyDetectorǁdetect_engine__mutmut['_mutmut_orig'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_1'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_2'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_3'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_4'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_5'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_6'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_7'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_8'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_9'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_10'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_11'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_12'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_13'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_14'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_15'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_16'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_17'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_18'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_19'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_20'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_21'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_22'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_23'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_24'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_25'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_26'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_27'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_28'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_29'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_30'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_31'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_32'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_33'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_34'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_35'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_36'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_37'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_38'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_39'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_40'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_41'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_42'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_43'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_43 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_44'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_44 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_45'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_45 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_46'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_46 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_47'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_47 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_48'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_48 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_49'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_49 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_50'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_50 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_51'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_51 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁdetect_engine__mutmut['xǁPolicyDetectorǁdetect_engine__mutmut_52'] = PolicyDetector.xǁPolicyDetectorǁdetect_engine__mutmut_52 # type: ignore # mutmut generated

mutants_xǁPolicyDetectorǁlist_policies__mutmut['_mutmut_orig'] = PolicyDetector.xǁPolicyDetectorǁlist_policies__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁlist_policies__mutmut['xǁPolicyDetectorǁlist_policies__mutmut_1'] = PolicyDetector.xǁPolicyDetectorǁlist_policies__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁlist_policies__mutmut['xǁPolicyDetectorǁlist_policies__mutmut_2'] = PolicyDetector.xǁPolicyDetectorǁlist_policies__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁlist_policies__mutmut['xǁPolicyDetectorǁlist_policies__mutmut_3'] = PolicyDetector.xǁPolicyDetectorǁlist_policies__mutmut_3 # type: ignore # mutmut generated

mutants_xǁPolicyDetectorǁget_policy__mutmut['_mutmut_orig'] = PolicyDetector.xǁPolicyDetectorǁget_policy__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁget_policy__mutmut['xǁPolicyDetectorǁget_policy__mutmut_1'] = PolicyDetector.xǁPolicyDetectorǁget_policy__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁget_policy__mutmut['xǁPolicyDetectorǁget_policy__mutmut_2'] = PolicyDetector.xǁPolicyDetectorǁget_policy__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁget_policy__mutmut['xǁPolicyDetectorǁget_policy__mutmut_3'] = PolicyDetector.xǁPolicyDetectorǁget_policy__mutmut_3 # type: ignore # mutmut generated

mutants_xǁPolicyDetectorǁlist_violations__mutmut['_mutmut_orig'] = PolicyDetector.xǁPolicyDetectorǁlist_violations__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁlist_violations__mutmut['xǁPolicyDetectorǁlist_violations__mutmut_1'] = PolicyDetector.xǁPolicyDetectorǁlist_violations__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁlist_violations__mutmut['xǁPolicyDetectorǁlist_violations__mutmut_2'] = PolicyDetector.xǁPolicyDetectorǁlist_violations__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁlist_violations__mutmut['xǁPolicyDetectorǁlist_violations__mutmut_3'] = PolicyDetector.xǁPolicyDetectorǁlist_violations__mutmut_3 # type: ignore # mutmut generated

mutants_xǁPolicyDetectorǁexplain_denial__mutmut['_mutmut_orig'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_1'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_2'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_3'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_4'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_5'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_6'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_7'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_8'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_9'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_10'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_11'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_12'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_13'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_14'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_15'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_16'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_17'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_18'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_19'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_20'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_21'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁexplain_denial__mutmut['xǁPolicyDetectorǁexplain_denial__mutmut_22'] = PolicyDetector.xǁPolicyDetectorǁexplain_denial__mutmut_22 # type: ignore # mutmut generated

mutants_xǁPolicyDetectorǁaudit__mutmut['_mutmut_orig'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_1'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_2'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_3'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_4'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_5'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_6'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_7'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_8'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_9'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_10'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_11'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_12'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_13'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_14'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_15'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_16'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_17'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_18'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_19'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_20'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_21'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_22'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_23'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_24'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_25'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_26'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_27'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_28'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPolicyDetectorǁaudit__mutmut['xǁPolicyDetectorǁaudit__mutmut_29'] = PolicyDetector.xǁPolicyDetectorǁaudit__mutmut_29 # type: ignore # mutmut generated


def _as_dict(value: object) -> dict[str, object]:
    return value if isinstance(value, dict) else {}
mutants_x__policy_action__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__policy_action__mutmut)
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


def x__policy_action__mutmut_orig(item: dict[str, object]) -> PolicyAction:
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


def x__policy_action__mutmut_1(item: dict[str, object]) -> PolicyAction:
    spec = None
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_2(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(None)
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_3(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get(None))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_4(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("XXspecXX"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_5(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("SPEC"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_6(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = None
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_7(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get(None, [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_8(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", None)
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_9(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get([])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_10(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", )
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_11(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("XXrulesXX", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_12(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("RULES", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_13(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) or rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_14(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = None
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_15(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(None)
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_16(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[1])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_17(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = None
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_18(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).upper()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_19(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(None).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_20(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get(None, "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_21(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", None)).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_22(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_23(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", )).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_24(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(None).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_25(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get(None, {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_26(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", None)).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_27(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get({})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_28(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", )).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_29(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("XXvalidateXX", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_30(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("VALIDATE", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_31(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("XXfailureActionXX", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_32(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureaction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_33(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("FAILUREACTION", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_34(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "XXauditXX")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_35(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "AUDIT")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_36(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action not in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_37(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "XXenforceXX" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_38(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "ENFORCE" in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT


def x__policy_action__mutmut_39(item: dict[str, object]) -> PolicyAction:
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    if isinstance(rules, list) and rules:
        first_rule = _as_dict(rules[0])
        action = str(_as_dict(first_rule.get("validate", {})).get("failureAction", "audit")).lower()
        if action in _ACTION_BY_NAME:
            return _ACTION_BY_NAME[action]
        if "enforce" not in action:
            return PolicyAction.ENFORCE
    return PolicyAction.AUDIT

mutants_x__policy_action__mutmut['_mutmut_orig'] = x__policy_action__mutmut_orig # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_1'] = x__policy_action__mutmut_1 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_2'] = x__policy_action__mutmut_2 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_3'] = x__policy_action__mutmut_3 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_4'] = x__policy_action__mutmut_4 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_5'] = x__policy_action__mutmut_5 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_6'] = x__policy_action__mutmut_6 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_7'] = x__policy_action__mutmut_7 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_8'] = x__policy_action__mutmut_8 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_9'] = x__policy_action__mutmut_9 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_10'] = x__policy_action__mutmut_10 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_11'] = x__policy_action__mutmut_11 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_12'] = x__policy_action__mutmut_12 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_13'] = x__policy_action__mutmut_13 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_14'] = x__policy_action__mutmut_14 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_15'] = x__policy_action__mutmut_15 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_16'] = x__policy_action__mutmut_16 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_17'] = x__policy_action__mutmut_17 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_18'] = x__policy_action__mutmut_18 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_19'] = x__policy_action__mutmut_19 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_20'] = x__policy_action__mutmut_20 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_21'] = x__policy_action__mutmut_21 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_22'] = x__policy_action__mutmut_22 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_23'] = x__policy_action__mutmut_23 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_24'] = x__policy_action__mutmut_24 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_25'] = x__policy_action__mutmut_25 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_26'] = x__policy_action__mutmut_26 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_27'] = x__policy_action__mutmut_27 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_28'] = x__policy_action__mutmut_28 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_29'] = x__policy_action__mutmut_29 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_30'] = x__policy_action__mutmut_30 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_31'] = x__policy_action__mutmut_31 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_32'] = x__policy_action__mutmut_32 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_33'] = x__policy_action__mutmut_33 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_34'] = x__policy_action__mutmut_34 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_35'] = x__policy_action__mutmut_35 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_36'] = x__policy_action__mutmut_36 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_37'] = x__policy_action__mutmut_37 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_38'] = x__policy_action__mutmut_38 # type: ignore # mutmut generated
mutants_x__policy_action__mutmut['x__policy_action__mutmut_39'] = x__policy_action__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_policy__mutmut)
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


def x__to_policy__mutmut_orig(item: dict[str, object]) -> Policy:
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


def x__to_policy__mutmut_1(item: dict[str, object]) -> Policy:
    metadata = None
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


def x__to_policy__mutmut_2(item: dict[str, object]) -> Policy:
    metadata = _as_dict(None)
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


def x__to_policy__mutmut_3(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get(None))
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


def x__to_policy__mutmut_4(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("XXmetadataXX"))
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


def x__to_policy__mutmut_5(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("METADATA"))
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


def x__to_policy__mutmut_6(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = None
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


def x__to_policy__mutmut_7(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(None)
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


def x__to_policy__mutmut_8(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get(None))
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


def x__to_policy__mutmut_9(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("XXspecXX"))
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


def x__to_policy__mutmut_10(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("SPEC"))
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


def x__to_policy__mutmut_11(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = None
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


def x__to_policy__mutmut_12(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get(None, [])
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


def x__to_policy__mutmut_13(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", None)
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


def x__to_policy__mutmut_14(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get([])
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


def x__to_policy__mutmut_15(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", )
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


def x__to_policy__mutmut_16(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("XXrulesXX", [])
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


def x__to_policy__mutmut_17(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("RULES", [])
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


def x__to_policy__mutmut_18(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = None
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


def x__to_policy__mutmut_19(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = None
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


def x__to_policy__mutmut_20(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = "XXXX"
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


def x__to_policy__mutmut_21(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = None
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


def x__to_policy__mutmut_22(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(None)
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


def x__to_policy__mutmut_23(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[1])
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


def x__to_policy__mutmut_24(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = None
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


def x__to_policy__mutmut_25(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(None)
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


def x__to_policy__mutmut_26(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get(None, ""))
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


def x__to_policy__mutmut_27(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", None))
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


def x__to_policy__mutmut_28(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get(""))
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


def x__to_policy__mutmut_29(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ))
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


def x__to_policy__mutmut_30(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(None).get("message", ""))
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


def x__to_policy__mutmut_31(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get(None, {})).get("message", ""))
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


def x__to_policy__mutmut_32(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", None)).get("message", ""))
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


def x__to_policy__mutmut_33(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get({})).get("message", ""))
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


def x__to_policy__mutmut_34(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", )).get("message", ""))
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


def x__to_policy__mutmut_35(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("XXvalidateXX", {})).get("message", ""))
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


def x__to_policy__mutmut_36(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("VALIDATE", {})).get("message", ""))
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


def x__to_policy__mutmut_37(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("XXmessageXX", ""))
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


def x__to_policy__mutmut_38(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("MESSAGE", ""))
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


def x__to_policy__mutmut_39(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", "XXXX"))
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


def x__to_policy__mutmut_40(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        name=None,
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_41(item: dict[str, object]) -> Policy:
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
        namespace=None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_42(item: dict[str, object]) -> Policy:
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
        engine=None,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_43(item: dict[str, object]) -> Policy:
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
        kind=None,
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_44(item: dict[str, object]) -> Policy:
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
        action=None,
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_45(item: dict[str, object]) -> Policy:
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
        description=None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_46(item: dict[str, object]) -> Policy:
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
        rules_count=None,
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_47(item: dict[str, object]) -> Policy:
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
        violations_count=None,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_48(item: dict[str, object]) -> Policy:
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
        ready=None,
    )


def x__to_policy__mutmut_49(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_50(item: dict[str, object]) -> Policy:
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
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_51(item: dict[str, object]) -> Policy:
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
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_52(item: dict[str, object]) -> Policy:
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
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_53(item: dict[str, object]) -> Policy:
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
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_54(item: dict[str, object]) -> Policy:
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
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_55(item: dict[str, object]) -> Policy:
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
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_56(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_57(item: dict[str, object]) -> Policy:
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
        )


def x__to_policy__mutmut_58(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        name=str(None),
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_59(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        name=str(metadata.get(None, "?")),
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_60(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        name=str(metadata.get("name", None)),
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_61(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        name=str(metadata.get("?")),
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_62(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        name=str(metadata.get("name", )),
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_63(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        name=str(metadata.get("XXnameXX", "?")),
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_64(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        name=str(metadata.get("NAME", "?")),
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_65(item: dict[str, object]) -> Policy:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    rules = spec.get("rules", [])
    rules_list = rules if isinstance(rules, list) else []
    message = ""
    if rules_list:
        first_rule = _as_dict(rules_list[0])
        message = str(_as_dict(first_rule.get("validate", {})).get("message", ""))
    return Policy(
        name=str(metadata.get("name", "XX?XX")),
        namespace=str(metadata.get("namespace") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_66(item: dict[str, object]) -> Policy:
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
        namespace=str(metadata.get("namespace") or None) and None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_67(item: dict[str, object]) -> Policy:
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
        namespace=str(None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_68(item: dict[str, object]) -> Policy:
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
        namespace=str(metadata.get("namespace") and None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_69(item: dict[str, object]) -> Policy:
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
        namespace=str(metadata.get(None) or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_70(item: dict[str, object]) -> Policy:
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
        namespace=str(metadata.get("XXnamespaceXX") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_71(item: dict[str, object]) -> Policy:
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
        namespace=str(metadata.get("NAMESPACE") or None) or None,
        engine=PolicyEngine.KYVERNO,
        kind=str(item.get("kind", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_72(item: dict[str, object]) -> Policy:
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
        kind=str(None),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_73(item: dict[str, object]) -> Policy:
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
        kind=str(item.get(None, "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_74(item: dict[str, object]) -> Policy:
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
        kind=str(item.get("kind", None)),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_75(item: dict[str, object]) -> Policy:
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
        kind=str(item.get("ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_76(item: dict[str, object]) -> Policy:
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
        kind=str(item.get("kind", )),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_77(item: dict[str, object]) -> Policy:
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
        kind=str(item.get("XXkindXX", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_78(item: dict[str, object]) -> Policy:
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
        kind=str(item.get("KIND", "ClusterPolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_79(item: dict[str, object]) -> Policy:
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
        kind=str(item.get("kind", "XXClusterPolicyXX")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_80(item: dict[str, object]) -> Policy:
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
        kind=str(item.get("kind", "clusterpolicy")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_81(item: dict[str, object]) -> Policy:
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
        kind=str(item.get("kind", "CLUSTERPOLICY")),
        action=_policy_action(item),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_82(item: dict[str, object]) -> Policy:
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
        action=_policy_action(None),
        description=message or None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_83(item: dict[str, object]) -> Policy:
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
        description=message and None,
        rules_count=len(rules_list),
        violations_count=0,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_84(item: dict[str, object]) -> Policy:
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
        violations_count=1,
        ready=str(metadata.get("status", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_85(item: dict[str, object]) -> Policy:
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
        ready=str(None) == "Ready",
    )


def x__to_policy__mutmut_86(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get(None, "Ready")) == "Ready",
    )


def x__to_policy__mutmut_87(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("status", None)) == "Ready",
    )


def x__to_policy__mutmut_88(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("Ready")) == "Ready",
    )


def x__to_policy__mutmut_89(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("status", )) == "Ready",
    )


def x__to_policy__mutmut_90(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("XXstatusXX", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_91(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("STATUS", "Ready")) == "Ready",
    )


def x__to_policy__mutmut_92(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("status", "XXReadyXX")) == "Ready",
    )


def x__to_policy__mutmut_93(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("status", "ready")) == "Ready",
    )


def x__to_policy__mutmut_94(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("status", "READY")) == "Ready",
    )


def x__to_policy__mutmut_95(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("status", "Ready")) != "Ready",
    )


def x__to_policy__mutmut_96(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("status", "Ready")) == "XXReadyXX",
    )


def x__to_policy__mutmut_97(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("status", "Ready")) == "ready",
    )


def x__to_policy__mutmut_98(item: dict[str, object]) -> Policy:
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
        ready=str(metadata.get("status", "Ready")) == "READY",
    )

mutants_x__to_policy__mutmut['_mutmut_orig'] = x__to_policy__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_1'] = x__to_policy__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_2'] = x__to_policy__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_3'] = x__to_policy__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_4'] = x__to_policy__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_5'] = x__to_policy__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_6'] = x__to_policy__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_7'] = x__to_policy__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_8'] = x__to_policy__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_9'] = x__to_policy__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_10'] = x__to_policy__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_11'] = x__to_policy__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_12'] = x__to_policy__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_13'] = x__to_policy__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_14'] = x__to_policy__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_15'] = x__to_policy__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_16'] = x__to_policy__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_17'] = x__to_policy__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_18'] = x__to_policy__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_19'] = x__to_policy__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_20'] = x__to_policy__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_21'] = x__to_policy__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_22'] = x__to_policy__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_23'] = x__to_policy__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_24'] = x__to_policy__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_25'] = x__to_policy__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_26'] = x__to_policy__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_27'] = x__to_policy__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_28'] = x__to_policy__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_29'] = x__to_policy__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_30'] = x__to_policy__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_31'] = x__to_policy__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_32'] = x__to_policy__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_33'] = x__to_policy__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_34'] = x__to_policy__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_35'] = x__to_policy__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_36'] = x__to_policy__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_37'] = x__to_policy__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_38'] = x__to_policy__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_39'] = x__to_policy__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_40'] = x__to_policy__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_41'] = x__to_policy__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_42'] = x__to_policy__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_43'] = x__to_policy__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_44'] = x__to_policy__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_45'] = x__to_policy__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_46'] = x__to_policy__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_47'] = x__to_policy__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_48'] = x__to_policy__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_49'] = x__to_policy__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_50'] = x__to_policy__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_51'] = x__to_policy__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_52'] = x__to_policy__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_53'] = x__to_policy__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_54'] = x__to_policy__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_55'] = x__to_policy__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_56'] = x__to_policy__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_57'] = x__to_policy__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_58'] = x__to_policy__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_59'] = x__to_policy__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_60'] = x__to_policy__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_61'] = x__to_policy__mutmut_61 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_62'] = x__to_policy__mutmut_62 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_63'] = x__to_policy__mutmut_63 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_64'] = x__to_policy__mutmut_64 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_65'] = x__to_policy__mutmut_65 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_66'] = x__to_policy__mutmut_66 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_67'] = x__to_policy__mutmut_67 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_68'] = x__to_policy__mutmut_68 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_69'] = x__to_policy__mutmut_69 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_70'] = x__to_policy__mutmut_70 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_71'] = x__to_policy__mutmut_71 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_72'] = x__to_policy__mutmut_72 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_73'] = x__to_policy__mutmut_73 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_74'] = x__to_policy__mutmut_74 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_75'] = x__to_policy__mutmut_75 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_76'] = x__to_policy__mutmut_76 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_77'] = x__to_policy__mutmut_77 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_78'] = x__to_policy__mutmut_78 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_79'] = x__to_policy__mutmut_79 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_80'] = x__to_policy__mutmut_80 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_81'] = x__to_policy__mutmut_81 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_82'] = x__to_policy__mutmut_82 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_83'] = x__to_policy__mutmut_83 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_84'] = x__to_policy__mutmut_84 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_85'] = x__to_policy__mutmut_85 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_86'] = x__to_policy__mutmut_86 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_87'] = x__to_policy__mutmut_87 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_88'] = x__to_policy__mutmut_88 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_89'] = x__to_policy__mutmut_89 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_90'] = x__to_policy__mutmut_90 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_91'] = x__to_policy__mutmut_91 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_92'] = x__to_policy__mutmut_92 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_93'] = x__to_policy__mutmut_93 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_94'] = x__to_policy__mutmut_94 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_95'] = x__to_policy__mutmut_95 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_96'] = x__to_policy__mutmut_96 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_97'] = x__to_policy__mutmut_97 # type: ignore # mutmut generated
mutants_x__to_policy__mutmut['x__to_policy__mutmut_98'] = x__to_policy__mutmut_98 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_violation__mutmut)
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


def x__to_violation__mutmut_orig(item: dict[str, object]) -> PolicyViolation:
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


def x__to_violation__mutmut_1(item: dict[str, object]) -> PolicyViolation:
    metadata = None
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


def x__to_violation__mutmut_2(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(None)
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


def x__to_violation__mutmut_3(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get(None))
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


def x__to_violation__mutmut_4(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("XXmetadataXX"))
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


def x__to_violation__mutmut_5(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("METADATA"))
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


def x__to_violation__mutmut_6(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = None
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


def x__to_violation__mutmut_7(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(None)
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


def x__to_violation__mutmut_8(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get(None))
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


def x__to_violation__mutmut_9(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("XXspecXX"))
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


def x__to_violation__mutmut_10(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("SPEC"))
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


def x__to_violation__mutmut_11(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=None,
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_12(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=None,
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_13(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=None,
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_14(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=None,
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_15(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=None,
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_16(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=None,
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_17(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=None,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_18(item: dict[str, object]) -> PolicyViolation:
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
        action=None,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_19(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=None,
    )


def x__to_violation__mutmut_20(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_21(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_22(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_23(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_24(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_25(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_26(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_27(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_28(item: dict[str, object]) -> PolicyViolation:
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
        )


def x__to_violation__mutmut_29(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(None),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_30(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get(None, "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_31(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", None)),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_32(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_33(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", )),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_34(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("XXpolicyXX", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_35(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("POLICY", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_36(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "XX?XX")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_37(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(None),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_38(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get(None, "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_39(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", None)),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_40(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_41(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", )),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_42(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("XXresourceKindXX", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_43(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourcekind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_44(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("RESOURCEKIND", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_45(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "XXPodXX")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_46(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_47(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "POD")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_48(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(None),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_49(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get(None, "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_50(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", None)),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_51(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_52(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", )),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_53(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("XXresourceXX", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_54(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("RESOURCE", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_55(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "XX?XX")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_56(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(None),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_57(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get(None, "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_58(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", None)),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_59(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_60(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", )),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_61(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("XXnamespaceXX", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_62(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("NAMESPACE", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_63(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "XXdefaultXX")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_64(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "DEFAULT")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_65(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(None),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_66(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get(None, "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_67(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", None)),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_68(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_69(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", )),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_70(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("XXruleXX", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_71(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("RULE", "?")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_72(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "XX?XX")),
        message=str(spec.get("message", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_73(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(None),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_74(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get(None, "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_75(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", None)),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_76(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_77(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", )),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_78(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("XXmessageXX", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_79(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("MESSAGE", "")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_80(item: dict[str, object]) -> PolicyViolation:
    metadata = _as_dict(item.get("metadata"))
    spec = _as_dict(item.get("spec"))
    return PolicyViolation(
        policy_name=str(spec.get("policy", "?")),
        resource_kind=str(spec.get("resourceKind", "Pod")),
        resource_name=str(spec.get("resource", "?")),
        resource_namespace=str(metadata.get("namespace", "default")),
        rule_name=str(spec.get("rule", "?")),
        message=str(spec.get("message", "XXXX")),
        severity=ViolationSeverity.HIGH,
        action=PolicyAction.ENFORCE,
        timestamp=str(metadata.get("creationTimestamp", "")),
    )


def x__to_violation__mutmut_81(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=str(None),
    )


def x__to_violation__mutmut_82(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=str(metadata.get(None, "")),
    )


def x__to_violation__mutmut_83(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=str(metadata.get("creationTimestamp", None)),
    )


def x__to_violation__mutmut_84(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=str(metadata.get("")),
    )


def x__to_violation__mutmut_85(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=str(metadata.get("creationTimestamp", )),
    )


def x__to_violation__mutmut_86(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=str(metadata.get("XXcreationTimestampXX", "")),
    )


def x__to_violation__mutmut_87(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=str(metadata.get("creationtimestamp", "")),
    )


def x__to_violation__mutmut_88(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=str(metadata.get("CREATIONTIMESTAMP", "")),
    )


def x__to_violation__mutmut_89(item: dict[str, object]) -> PolicyViolation:
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
        timestamp=str(metadata.get("creationTimestamp", "XXXX")),
    )

mutants_x__to_violation__mutmut['_mutmut_orig'] = x__to_violation__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_1'] = x__to_violation__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_2'] = x__to_violation__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_3'] = x__to_violation__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_4'] = x__to_violation__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_5'] = x__to_violation__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_6'] = x__to_violation__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_7'] = x__to_violation__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_8'] = x__to_violation__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_9'] = x__to_violation__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_10'] = x__to_violation__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_11'] = x__to_violation__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_12'] = x__to_violation__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_13'] = x__to_violation__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_14'] = x__to_violation__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_15'] = x__to_violation__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_16'] = x__to_violation__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_17'] = x__to_violation__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_18'] = x__to_violation__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_19'] = x__to_violation__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_20'] = x__to_violation__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_21'] = x__to_violation__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_22'] = x__to_violation__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_23'] = x__to_violation__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_24'] = x__to_violation__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_25'] = x__to_violation__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_26'] = x__to_violation__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_27'] = x__to_violation__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_28'] = x__to_violation__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_29'] = x__to_violation__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_30'] = x__to_violation__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_31'] = x__to_violation__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_32'] = x__to_violation__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_33'] = x__to_violation__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_34'] = x__to_violation__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_35'] = x__to_violation__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_36'] = x__to_violation__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_37'] = x__to_violation__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_38'] = x__to_violation__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_39'] = x__to_violation__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_40'] = x__to_violation__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_41'] = x__to_violation__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_42'] = x__to_violation__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_43'] = x__to_violation__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_44'] = x__to_violation__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_45'] = x__to_violation__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_46'] = x__to_violation__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_47'] = x__to_violation__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_48'] = x__to_violation__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_49'] = x__to_violation__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_50'] = x__to_violation__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_51'] = x__to_violation__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_52'] = x__to_violation__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_53'] = x__to_violation__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_54'] = x__to_violation__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_55'] = x__to_violation__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_56'] = x__to_violation__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_57'] = x__to_violation__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_58'] = x__to_violation__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_59'] = x__to_violation__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_60'] = x__to_violation__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_61'] = x__to_violation__mutmut_61 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_62'] = x__to_violation__mutmut_62 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_63'] = x__to_violation__mutmut_63 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_64'] = x__to_violation__mutmut_64 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_65'] = x__to_violation__mutmut_65 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_66'] = x__to_violation__mutmut_66 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_67'] = x__to_violation__mutmut_67 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_68'] = x__to_violation__mutmut_68 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_69'] = x__to_violation__mutmut_69 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_70'] = x__to_violation__mutmut_70 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_71'] = x__to_violation__mutmut_71 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_72'] = x__to_violation__mutmut_72 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_73'] = x__to_violation__mutmut_73 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_74'] = x__to_violation__mutmut_74 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_75'] = x__to_violation__mutmut_75 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_76'] = x__to_violation__mutmut_76 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_77'] = x__to_violation__mutmut_77 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_78'] = x__to_violation__mutmut_78 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_79'] = x__to_violation__mutmut_79 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_80'] = x__to_violation__mutmut_80 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_81'] = x__to_violation__mutmut_81 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_82'] = x__to_violation__mutmut_82 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_83'] = x__to_violation__mutmut_83 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_84'] = x__to_violation__mutmut_84 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_85'] = x__to_violation__mutmut_85 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_86'] = x__to_violation__mutmut_86 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_87'] = x__to_violation__mutmut_87 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_88'] = x__to_violation__mutmut_88 # type: ignore # mutmut generated
mutants_x__to_violation__mutmut['x__to_violation__mutmut_89'] = x__to_violation__mutmut_89 # type: ignore # mutmut generated
