from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumAgentHealth,
    CiliumAuditFinding,
    CiliumDenialGroup,
    CiliumDenialsQuery,
    CiliumDenialsResult,
    CiliumDetectionResult,
    CiliumEncryptionStatusResult,
    CiliumFlowEntry,
    CiliumFlowQuery,
    CiliumFlowsResult,
    CiliumIdentitiesResult,
    CiliumIdentityInfo,
    CiliumL7RuleSummary,
    CiliumNetworkPoliciesResult,
    CiliumNetworkPolicyDetail,
    CiliumNetworkPolicyInfo,
    CiliumPathFinding,
    CiliumPolicyAuditResult,
    CiliumRuleSummary,
    CiliumSegmentationAuditResult,
    CiliumStatusResult,
    CiliumWorkload,
)


class TestCiliumAgentHealth:
    def test_constructs_with_defaults(self) -> None:
        agent = CiliumAgentHealth(
            node="node-1",
            pod_name="cilium-abc",
            namespace="kube-system",
            ready=True,
            phase="Running",
            restart_count=0,
        )

        assert agent.node == "node-1"
        assert agent.pod_name == "cilium-abc"
        assert agent.namespace == "kube-system"
        assert agent.ready is True
        assert agent.phase == "Running"
        assert agent.restart_count == 0
        assert agent.image is None
        assert agent.message is None

    def test_constructs_with_image_and_message(self) -> None:
        agent = CiliumAgentHealth(
            node="node-2",
            pod_name="cilium-def",
            namespace="kube-system",
            ready=False,
            phase="Running",
            restart_count=3,
            image="quay.io/cilium/cilium:v1.16.3",
            message="agent not ready",
        )

        assert agent.image == "quay.io/cilium/cilium:v1.16.3"
        assert agent.message == "agent not ready"


class TestCiliumDetectionResult:
    def test_constructs_not_installed(self) -> None:
        result = CiliumDetectionResult(
            installed=False,
            status="not_installed",
            version=None,
            mode="UNKNOWN",
            namespace=None,
            total_agents=0,
            ready_agents=0,
            degraded_summary=None,
            agents=[],
            note="Cilium is not installed",
        )

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.mode == "UNKNOWN"
        assert result.agents == []
        assert result.note == "Cilium is not installed"

    def test_constructs_installed(self) -> None:
        agents = [
            CiliumAgentHealth(
                node="node-1",
                pod_name="cilium-abc",
                namespace="kube-system",
                ready=True,
                phase="Running",
                restart_count=0,
            )
        ]
        result = CiliumDetectionResult(
            installed=True,
            status="installed",
            version="v1.16.3",
            mode="native-routing",
            namespace="kube-system",
            total_agents=1,
            ready_agents=1,
            degraded_summary=None,
            agents=agents,
            note=None,
        )

        assert result.installed is True
        assert result.status == "installed"
        assert result.version == "v1.16.3"
        assert result.namespace == "kube-system"
        assert result.total_agents == 1  # noqa: PLR2004
        assert result.ready_agents == 1  # noqa: PLR2004


class TestCiliumStatusResult:
    def test_constructs_not_installed(self) -> None:
        result = CiliumStatusResult(
            installed=False,
            status="not_installed",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=[],
            note="Cilium is not installed",
        )

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.controller_errors == 0
        assert result.connectivity is None
        assert result.nodes == []

    def test_constructs_healthy(self) -> None:
        nodes = [
            CiliumAgentHealth(
                node="node-1",
                pod_name="cilium-a",
                namespace="kube-system",
                ready=True,
                phase="Running",
                restart_count=0,
            )
        ]
        result = CiliumStatusResult(
            installed=True,
            status="healthy",
            ready_agents=1,
            total_agents=1,
            degraded_summary=None,
            controller_errors=0,
            connectivity="ok",
            nodes=nodes,
            note=None,
        )

        assert result.status == "healthy"
        assert result.connectivity == "ok"
        assert result.nodes[0].node == "node-1"

    def test_preserves_raw_phase_value(self) -> None:
        nodes = [
            CiliumAgentHealth(
                node="node-3",
                pod_name="cilium-c",
                namespace="kube-system",
                ready=False,
                phase="CrashLoopBackOff",
                restart_count=7,
            )
        ]
        result = CiliumStatusResult(
            installed=True,
            status="degraded",
            ready_agents=0,
            total_agents=1,
            degraded_summary="0/1 agents ready",
            controller_errors=1,
            connectivity="degraded",
            nodes=nodes,
            note=None,
        )

        assert result.nodes[0].phase == "CrashLoopBackOff"


class TestCiliumNetworkPolicyInfo:
    def test_constructs_namespaced(self) -> None:
        policy = CiliumNetworkPolicyInfo(
            kind="CiliumNetworkPolicy",
            name="allow-db",
            namespace="payments",
            endpoint_selector="matchLabels: app=db",
            ingress_rule_count=2,
            egress_rule_count=1,
            l7_rule_count=1,
            l7_protocols=("http", "dns"),
        )

        assert policy.kind == "CiliumNetworkPolicy"
        assert policy.namespace == "payments"
        assert policy.l7_protocols == ("http", "dns")

    def test_constructs_clusterwide_without_namespace(self) -> None:
        policy = CiliumNetworkPolicyInfo(
            kind="CiliumClusterwideNetworkPolicy",
            name="global-allow",
            namespace=None,
            endpoint_selector="matchLabels: {}",
            ingress_rule_count=0,
            egress_rule_count=0,
            l7_rule_count=0,
            l7_protocols=(),
        )

        assert policy.kind == "CiliumClusterwideNetworkPolicy"
        assert policy.namespace is None


class TestCiliumNetworkPoliciesResult:
    def test_constructs_not_installed(self) -> None:
        result = CiliumNetworkPoliciesResult(
            installed=False,
            status="not_installed",
            total_policies=0,
            namespaced_count=0,
            clusterwide_count=0,
            policies=[],
            note="Cilium is not installed in this cluster",
        )

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.policies == []


class TestCiliumL7RuleSummary:
    def test_constructs(self) -> None:
        l7 = CiliumL7RuleSummary(protocol="http", match=("GET", "/api"))
        assert l7.protocol == "http"
        assert l7.match == ("GET", "/api")


class TestCiliumRuleSummary:
    def test_constructs(self) -> None:
        rule = CiliumRuleSummary(
            direction="ingress",
            endpoints=("matchLabels: app=web",),
            ports=("443/TCP",),
            l7=(CiliumL7RuleSummary(protocol="grpc", match=("health",)),),
        )
        assert rule.direction == "ingress"
        assert rule.ports == ("443/TCP",)


class TestCiliumNetworkPolicyDetail:
    def test_constructs(self) -> None:
        detail = CiliumNetworkPolicyDetail(
            installed=True,
            status="ok",
            kind="CiliumNetworkPolicy",
            name="allow-db",
            namespace="payments",
            endpoint_selector="matchLabels: app=db",
            ingress_rules=(),
            egress_rules=(),
            l7_protocols=("http",),
            spec={"endpointSelector": {"matchLabels": {"app": "db"}}},
            note=None,
        )

        assert detail.installed is True
        assert detail.kind == "CiliumNetworkPolicy"
        assert detail.namespace == "payments"
        assert detail.l7_protocols == ("http",)
        assert detail.spec["endpointSelector"] == {"matchLabels": {"app": "db"}}


class TestCiliumWorkload:
    def test_constructs(self) -> None:
        workload = CiliumWorkload(namespace="payments", name="db-0", labels={"app": "db"})
        assert workload.namespace == "payments"
        assert workload.labels == {"app": "db"}


class TestCiliumAuditFinding:
    def test_constructs(self) -> None:
        finding = CiliumAuditFinding(
            namespace="payments",
            workload="db-0",
            coverage="no_policy",
            ingress_restricted=False,
            egress_restricted=False,
            l7_restricted=False,
            risk="critical",
            note=None,
        )
        assert finding.coverage == "no_policy"
        assert finding.risk == "critical"


class TestCiliumPolicyAuditResult:
    def test_constructs_not_installed(self) -> None:
        result = CiliumPolicyAuditResult(
            installed=False,
            status="not_installed",
            view="vanilla",
            total_workloads=0,
            uncovered_count=0,
            findings=[],
            summary="",
            note="Cilium is not installed in this cluster",
        )
        assert result.installed is False
        assert result.view == "vanilla"

    def test_network_policy_info_carries_endpoint_labels(self) -> None:
        policy = CiliumNetworkPolicyInfo(
            kind="CiliumNetworkPolicy",
            name="allow-db",
            namespace="payments",
            endpoint_selector="matchLabels: app=db",
            ingress_rule_count=1,
            egress_rule_count=1,
            l7_rule_count=0,
            l7_protocols=(),
            endpoint_labels=(("app", "db"),),
        )
        assert policy.endpoint_labels == (("app", "db"),)


class TestCiliumIdentityInfo:
    def test_constructs(self) -> None:
        identity = CiliumIdentityInfo(id="12345", labels=("k8s:io.cilium",), endpoint_count=3)
        assert identity.id == "12345"
        assert identity.labels == ("k8s:io.cilium",)
        assert identity.endpoint_count == 3  # noqa: PLR2004


class TestCiliumIdentitiesResult:
    def test_constructs_not_installed(self) -> None:
        result = CiliumIdentitiesResult(
            installed=False,
            status="not_installed",
            total_identities=0,
            identities=[],
            note="Cilium is not installed in this cluster",
        )
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.identities == []


class TestCiliumPathFinding:
    def test_constructs(self) -> None:
        finding = CiliumPathFinding(
            source_id="100",
            destination_id="200",
            source_labels=("app=web",),
            destination_labels=("app=db",),
            severity="high",
            note="unrestricted path",
        )
        assert finding.source_id == "100"
        assert finding.destination_id == "200"
        assert finding.severity == "high"


class TestCiliumSegmentationAuditResult:
    def test_constructs_not_installed(self) -> None:
        result = CiliumSegmentationAuditResult(
            installed=False,
            status="not_installed",
            view="vanilla",
            total_identities=0,
            total_paths=0,
            uncovered_paths=0,
            findings=[],
            summary="",
            note="Cilium is not installed in this cluster",
        )
        assert result.installed is False
        assert result.view == "vanilla"
        assert result.findings == []


class TestCiliumFlowQuery:
    def test_defaults(self) -> None:
        query = CiliumFlowQuery()
        assert query.namespace is None
        assert query.window_minutes == 15  # noqa: PLR2004
        assert query.limit == 100  # noqa: PLR2004


class TestCiliumFlowEntry:
    def test_constructs(self) -> None:
        flow = CiliumFlowEntry(
            timestamp="2026-08-28T10:00:00Z",
            source="web-0",
            destination="db-0",
            source_namespace="payments",
            destination_namespace="payments",
            source_identity="100",
            destination_identity="200",
            verdict="FORWARDED",
            drop_reason=None,
            protocol="tcp",
            destination_port="443",
            l7_protocol="http",
            direction="ingress",
        )
        assert flow.verdict == "FORWARDED"
        assert flow.destination_port == "443"
        assert flow.l7_protocol == "http"
        assert flow.source_namespace == "payments"
        assert flow.policy is None


class TestCiliumDenialsQuery:
    def test_defaults(self) -> None:
        query = CiliumDenialsQuery()
        assert query.namespace is None
        assert query.window_minutes == 5  # noqa: PLR2004
        assert query.limit == 100  # noqa: PLR2004


class TestCiliumDenialGroup:
    def test_constructs(self) -> None:
        group = CiliumDenialGroup(
            policy="default/deny-all",
            source="web-0",
            destination="db-0",
            source_namespace="payments",
            destination_namespace="payments",
            reason="Policy denied",
            count=3,  # noqa: PLR2004
        )
        assert group.policy == "default/deny-all"
        assert group.count == 3  # noqa: PLR2004


class TestCiliumDenialsResult:
    def test_constructs_not_installed(self) -> None:
        result = CiliumDenialsResult(
            installed=False,
            status="not_installed",
            total_denials=0,
            groups=[],
            note="Hubble relay is not available in this cluster",
        )
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.groups == []


class TestCiliumFlowsResult:
    def test_constructs_not_installed(self) -> None:
        result = CiliumFlowsResult(
            installed=False,
            status="not_installed",
            total_flows=0,
            flows=[],
            note="Hubble relay is not available in this cluster",
        )
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.flows == []


class TestCiliumEncryptionStatusResult:
    def test_constructs_enabled(self) -> None:
        result = CiliumEncryptionStatusResult(
            installed=True,
            status="enabled",
            mode="wireguard",
            encrypted_nodes=3,
            total_nodes=4,
            coverage="3/4",
            note=None,
        )
        assert result.installed is True
        assert result.mode == "wireguard"
        assert result.coverage == "3/4"

    def test_constructs_not_installed(self) -> None:
        result = CiliumEncryptionStatusResult(
            installed=False,
            status="not_installed",
            mode="UNKNOWN",
            encrypted_nodes=0,
            total_nodes=0,
            coverage=None,
            note="Cilium is not installed in this cluster",
        )
        assert result.installed is False
        assert result.status == "not_installed"
