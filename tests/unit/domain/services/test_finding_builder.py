from __future__ import annotations

from hexawyn.application.ports.driven.rbac_security_audit_port import (
    ApiUsageEventRaw,
    ApiUsageFetchResult,
    PolicyRuleRaw,
    RoleBindingRaw,
    RoleRaw,
    RoleRefRaw,
    ServiceAccountRaw,
    SubjectRaw,
)
from hexawyn.domain.models.rbac_audit import SuggestedRole
from hexawyn.domain.services.rbac_audit.finding_builder import (
    build_finding,
    index_bindings_by_service_account,
    index_pods_by_service_account,
    resolve_role,
    to_candidate,
    to_policy_rule,
)


def _sa(name: str = "default", namespace: str = "default") -> ServiceAccountRaw:
    return ServiceAccountRaw(name=name, namespace=namespace)


def _subject(name: str = "default", namespace: str | None = "default") -> SubjectRaw:
    return SubjectRaw(kind="ServiceAccount", name=name, namespace=namespace)


def _role_ref(kind: str = "ClusterRole", name: str = "edit") -> RoleRefRaw:
    return RoleRefRaw(kind=kind, name=name)  # type: ignore[typeddict-item]


def _binding(
    name: str = "binding-1",
    namespace: str | None = "default",
    subjects: list[SubjectRaw] | None = None,
    role_ref: RoleRefRaw | None = None,
) -> RoleBindingRaw:
    return RoleBindingRaw(
        binding_kind="RoleBinding",  # type: ignore[typeddict-item]
        binding_name=name,
        namespace=namespace,
        subjects=subjects or [_subject()],
        role_ref=role_ref or _role_ref(),
    )


def _role(  # noqa: PLR0913
    name: str = "edit",
    kind: str = "ClusterRole",
    namespace: str | None = None,
    rules: list[PolicyRuleRaw] | None = None,
    labels: dict[str, str] | None = None,
    aggregation_selectors: list[dict[str, str]] | None = None,
) -> RoleRaw:
    return RoleRaw(
        kind=kind,  # type: ignore[typeddict-item]
        name=name,
        namespace=namespace,
        rules=rules or [PolicyRuleRaw(verbs=["get", "list"], resources=["pods"], api_groups=[""])],
        labels=labels or {},
        aggregation_selectors=aggregation_selectors or [],
    )


def _rule(
    verbs: list[str] | None = None,
    resources: list[str] | None = None,
    api_groups: list[str] | None = None,
) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=verbs or ["get"],
        resources=resources or ["pods"],
        api_groups=api_groups or [""],
    )


def _api_usage(
    events: list[ApiUsageEventRaw] | None = None, available: bool = True
) -> ApiUsageFetchResult:
    return ApiUsageFetchResult(available=available, events=events or [])


def _api_event(
    service_account: str = "default",
    namespace: str = "default",
    verb: str = "get",
    resource: str = "pods",
) -> ApiUsageEventRaw:
    return ApiUsageEventRaw(
        service_account=service_account,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp="2026-01-01T00:00:00Z",
    )


class TestToPolicyRule:
    def test_converts_raw_to_policy_rule(self) -> None:
        raw = _rule(verbs=["get", "list"], resources=["pods"], api_groups=[""])
        result = to_policy_rule(raw)
        assert result.verbs == ["get", "list"]
        assert result.resources == ["pods"]
        assert result.api_groups == [""]

    def test_converts_wildcard_verbs(self) -> None:
        raw = _rule(verbs=["*"], resources=["pods"], api_groups=["*"])
        result = to_policy_rule(raw)
        assert result.verbs == ["*"]
        assert result.api_groups == ["*"]


class TestToCandidate:
    def test_converts_role_to_candidate(self) -> None:
        role = _role(
            name="test-role",
            labels={"app": "test"},
            rules=[_rule(verbs=["get"], resources=["pods"])],
        )
        result = to_candidate(role)
        assert result.name == "test-role"
        assert result.labels == {"app": "test"}
        assert len(result.rules) == 1
        assert result.rules[0].verbs == ["get"]

    def test_converts_role_with_multiple_rules(self) -> None:
        role = _role(
            name="multi-rule",
            rules=[
                _rule(verbs=["get"], resources=["pods"]),
                _rule(verbs=["list"], resources=["services"]),
            ],
        )
        result = to_candidate(role)
        assert len(result.rules) == 2  # noqa: PLR2004


class TestResolveRole:
    def test_cluster_role_resolved_by_name(self) -> None:
        cluster_roles = {"edit": _role(name="edit", kind="ClusterRole")}
        result = resolve_role(
            _role_ref(kind="ClusterRole", name="edit"),
            _binding(),
            cluster_roles_by_name=cluster_roles,
            roles_by_namespace_name={},
        )
        assert result is not None
        assert result["name"] == "edit"

    def test_role_resolved_by_namespace_and_name(self) -> None:
        namespaced_roles: dict[tuple[str | None, str], RoleRaw] = {
            ("default", "my-role"): _role(name="my-role", kind="Role", namespace="default"),
        }
        result = resolve_role(
            _role_ref(kind="Role", name="my-role"),
            _binding(namespace="default"),
            cluster_roles_by_name={},
            roles_by_namespace_name=namespaced_roles,
        )
        assert result is not None
        assert result["name"] == "my-role"

    def test_missing_cluster_role_returns_none(self) -> None:
        result = resolve_role(
            _role_ref(kind="ClusterRole", name="missing"),
            _binding(),
            cluster_roles_by_name={},
            roles_by_namespace_name={},
        )
        assert result is None

    def test_missing_namespaced_role_returns_none(self) -> None:
        result = resolve_role(
            _role_ref(kind="Role", name="missing"),
            _binding(namespace="default"),
            cluster_roles_by_name={},
            roles_by_namespace_name={},
        )
        assert result is None


class TestIndexBindingsByServiceAccount:
    def test_single_binding_maps_to_sa(self) -> None:
        bindings = [_binding(subjects=[_subject(name="my-sa", namespace="my-ns")])]
        result = index_bindings_by_service_account(bindings)
        assert ("my-ns", "my-sa") in result
        assert len(result[("my-ns", "my-sa")]) == 1

    def test_multiple_bindings_for_same_sa(self) -> None:
        bindings = [
            _binding(name="b1", subjects=[_subject(name="my-sa", namespace="ns")]),
            _binding(name="b2", subjects=[_subject(name="my-sa", namespace="ns")]),
        ]
        result = index_bindings_by_service_account(bindings)
        assert len(result[("ns", "my-sa")]) == 2  # noqa: PLR2004

    def test_binding_with_multiple_subjects(self) -> None:
        bindings = [
            _binding(
                subjects=[
                    _subject(name="sa1", namespace="ns"),
                    _subject(name="sa2", namespace="ns"),
                ],
            ),
        ]
        result = index_bindings_by_service_account(bindings)
        assert ("ns", "sa1") in result
        assert ("ns", "sa2") in result

    def test_non_service_account_subject_skipped(self) -> None:
        bindings = [
            _binding(subjects=[SubjectRaw(kind="User", name="bob", namespace=None)]),
        ]
        result = index_bindings_by_service_account(bindings)
        assert result == {}

    def test_subject_with_no_namespace_falls_back_to_binding_namespace(self) -> None:
        bindings = [
            _binding(
                namespace="fallback-ns",
                subjects=[SubjectRaw(kind="ServiceAccount", name="sa", namespace=None)],
            ),
        ]
        result = index_bindings_by_service_account(bindings)
        assert ("fallback-ns", "sa") in result

    def test_subject_with_null_fallback_namespace_skipped(self) -> None:
        bindings = [
            _binding(
                namespace=None,
                subjects=[SubjectRaw(kind="ServiceAccount", name="sa", namespace=None)],
            ),
        ]
        result = index_bindings_by_service_account(bindings)
        assert result == {}

    def test_empty_bindings_returns_empty(self) -> None:
        result = index_bindings_by_service_account([])
        assert result == {}


class TestIndexPodsByServiceAccount:
    def test_single_pod_mapped(self) -> None:
        pods = [{"pod_name": "my-pod", "namespace": "ns", "service_account_name": "sa"}]
        result = index_pods_by_service_account(pods)
        assert ("ns", "sa") in result
        assert result[("ns", "sa")] == ["my-pod"]

    def test_multiple_pods_same_sa(self) -> None:
        pods = [
            {"pod_name": "pod1", "namespace": "ns", "service_account_name": "sa"},
            {"pod_name": "pod2", "namespace": "ns", "service_account_name": "sa"},
        ]
        result = index_pods_by_service_account(pods)
        assert len(result[("ns", "sa")]) == 2  # noqa: PLR2004

    def test_different_namespaces(self) -> None:
        pods = [
            {"pod_name": "pod1", "namespace": "ns1", "service_account_name": "sa"},
            {"pod_name": "pod2", "namespace": "ns2", "service_account_name": "sa"},
        ]
        result = index_pods_by_service_account(pods)
        assert ("ns1", "sa") in result
        assert ("ns2", "sa") in result

    def test_empty_pods_returns_empty(self) -> None:
        result = index_pods_by_service_account([])
        assert result == {}


class TestBuildFinding:
    def test_basic_finding_built(self) -> None:
        sa = _sa(name="my-sa", namespace="default")
        role = _role(name="edit", kind="ClusterRole")
        binding = _binding(
            namespace="default",
            subjects=[_subject(name="my-sa", namespace="default")],
            role_ref=_role_ref(kind="ClusterRole", name="edit"),
        )
        api_usage_result = _api_usage(
            events=[_api_event(service_account="my-sa", namespace="default")]
        )

        finding = build_finding(
            service_account=sa,
            bindings=[binding],
            cluster_roles_by_name={"edit": role},
            roles_by_namespace_name={},
            cluster_role_candidates=[],
            pods_using=["pod-1"],
            api_usage=api_usage_result,
        )
        assert finding.service_account == "my-sa"
        assert finding.namespace == "default"
        assert finding.pods_using == ["pod-1"]

    def test_cluster_admin_detected(self) -> None:
        sa = _sa(name="admin-sa", namespace="default")
        role = _role(name="cluster-admin", kind="ClusterRole")
        binding = _binding(
            namespace="default",
            subjects=[_subject(name="admin-sa", namespace="default")],
            role_ref=_role_ref(kind="ClusterRole", name="cluster-admin"),
        )
        api_usage_result = _api_usage(events=[])

        finding = build_finding(
            service_account=sa,
            bindings=[binding],
            cluster_roles_by_name={"cluster-admin": role},
            roles_by_namespace_name={},
            cluster_role_candidates=[],
            pods_using=[],
            api_usage=api_usage_result,
        )
        assert finding.risk_level == "critical"

    def test_no_roles_returns_low_risk(self) -> None:
        sa = _sa(name="no-role-sa", namespace="default")
        api_usage_result = _api_usage(events=[], available=False)

        finding = build_finding(
            service_account=sa,
            bindings=[],
            cluster_roles_by_name={},
            roles_by_namespace_name={},
            cluster_role_candidates=[],
            pods_using=[],
            api_usage=api_usage_result,
        )
        assert finding.risk_level == "low"

    def test_finding_has_reasons(self) -> None:
        sa = _sa(name="my-sa", namespace="default")
        role = _role(name="edit", kind="ClusterRole")
        binding = _binding(
            namespace="default",
            subjects=[_subject(name="my-sa", namespace="default")],
            role_ref=_role_ref(kind="ClusterRole", name="edit"),
        )
        api_usage_result = _api_usage(
            events=[_api_event(service_account="my-sa", namespace="default")]
        )

        finding = build_finding(
            service_account=sa,
            bindings=[binding],
            cluster_roles_by_name={"edit": role},
            roles_by_namespace_name={},
            cluster_role_candidates=[],
            pods_using=["pod-1"],
            api_usage=api_usage_result,
        )
        assert isinstance(finding.reasons, list)

    def test_finding_has_recommendation(self) -> None:
        sa = _sa(name="my-sa", namespace="default")
        role = _role(name="edit", kind="ClusterRole")
        binding = _binding(
            namespace="default",
            subjects=[_subject(name="my-sa", namespace="default")],
            role_ref=_role_ref(kind="ClusterRole", name="edit"),
        )
        api_usage_result = _api_usage(
            events=[_api_event(service_account="my-sa", namespace="default")]
        )

        finding = build_finding(
            service_account=sa,
            bindings=[binding],
            cluster_roles_by_name={"edit": role},
            roles_by_namespace_name={},
            cluster_role_candidates=[],
            pods_using=["pod-1"],
            api_usage=api_usage_result,
        )
        assert len(finding.recommendation) > 0

    def test_finding_has_suggested_role(self) -> None:
        sa = _sa(name="my-sa", namespace="default")
        role = _role(name="edit", kind="ClusterRole")
        binding = _binding(
            namespace="default",
            subjects=[_subject(name="my-sa", namespace="default")],
            role_ref=_role_ref(kind="ClusterRole", name="edit"),
        )
        api_usage_result = _api_usage(
            events=[_api_event(service_account="my-sa", namespace="default")]
        )

        finding = build_finding(
            service_account=sa,
            bindings=[binding],
            cluster_roles_by_name={"edit": role},
            roles_by_namespace_name={},
            cluster_role_candidates=[],
            pods_using=["pod-1"],
            api_usage=api_usage_result,
        )
        assert isinstance(finding.suggested_role, SuggestedRole)

    def test_finding_with_missing_role_continues(self) -> None:
        sa = _sa(name="my-sa", namespace="default")
        binding = _binding(
            namespace="default",
            subjects=[_subject(name="my-sa", namespace="default")],
            role_ref=_role_ref(kind="ClusterRole", name="nonexistent"),
        )
        api_usage_result = _api_usage(
            events=[_api_event(service_account="my-sa", namespace="default")]
        )

        finding = build_finding(
            service_account=sa,
            bindings=[binding],
            cluster_roles_by_name={},
            roles_by_namespace_name={},
            cluster_role_candidates=[],
            pods_using=[],
            api_usage=api_usage_result,
        )
        assert finding.service_account == "my-sa"
        assert finding.risk_level == "low"

    def test_api_usage_not_available(self) -> None:
        sa = _sa(name="my-sa", namespace="default")
        role = _role(name="edit", kind="ClusterRole")
        binding = _binding(
            namespace="default",
            subjects=[_subject(name="my-sa", namespace="default")],
            role_ref=_role_ref(kind="ClusterRole", name="edit"),
        )
        api_usage_result = _api_usage(events=[], available=False)

        finding = build_finding(
            service_account=sa,
            bindings=[binding],
            cluster_roles_by_name={"edit": role},
            roles_by_namespace_name={},
            cluster_role_candidates=[],
            pods_using=["pod-1"],
            api_usage=api_usage_result,
        )
        assert isinstance(finding.suggested_role, SuggestedRole)
