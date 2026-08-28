from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumAgentHealth,
    CiliumDetectionResult,
    CiliumL7RuleSummary,
    CiliumNetworkPoliciesResult,
    CiliumNetworkPolicyDetail,
    CiliumNetworkPolicyInfo,
    CiliumRuleSummary,
    CiliumStatusResult,
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
