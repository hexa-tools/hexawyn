from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.domain.models.policy import (
    Policy,
    PolicyAction,
    PolicyDenialExplanation,
    PolicyDetectionResult,
    PolicyEngine,
    PolicyViolation,
    ViolationSeverity,
)


class TestPolicyDetect:
    def test_tool_returns_detection(self) -> None:
        from hexawyn.mcp.tools.policy_detect import policy_detect

        with patch("hexawyn.mcp.server.build_policy_adapter") as mock_build:
            adapter = MagicMock(spec=PolicyPort)
            adapter.detect_engine.return_value = PolicyDetectionResult(
                engine=PolicyEngine.KYVERNO,
                version="v1.13.0",
                namespace="kyverno",
                total_policies=8,
                enforce_policies=5,
                audit_policies=3,
                total_violations=12,
                high_severity=4,
            )
            mock_build.return_value = adapter
            result = policy_detect()
        assert result["error"] is None
        assert result["engine"] == "kyverno"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_detect import policy_detect

        with patch("hexawyn.mcp.server.build_policy_adapter", side_effect=RuntimeError("boom")):
            result = policy_detect()
        assert result["error"] == "boom"


class TestPolicyList:
    def test_tool_returns_policies(self) -> None:
        from hexawyn.mcp.tools.policy_list import policy_list

        with patch("hexawyn.mcp.server.build_policy_adapter") as mock_build:
            adapter = MagicMock(spec=PolicyPort)
            adapter.list_policies.return_value = [
                Policy(
                    name="require-non-root",
                    namespace=None,
                    engine=PolicyEngine.KYVERNO,
                    kind="ClusterPolicy",
                    action=PolicyAction.ENFORCE,
                    description=None,
                    rules_count=1,
                    violations_count=3,
                    ready=True,
                ),
            ]
            mock_build.return_value = adapter
            result = policy_list()
        assert result["error"] is None
        assert len(result["policies"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_list import policy_list

        with patch("hexawyn.mcp.server.build_policy_adapter", side_effect=RuntimeError("boom")):
            result = policy_list()
        assert result["error"] == "boom"


class TestPolicyGet:
    def test_tool_returns_detail(self) -> None:
        from hexawyn.mcp.tools.policy_get import policy_get

        with patch("hexawyn.mcp.server.build_policy_adapter") as mock_build:
            adapter = MagicMock(spec=PolicyPort)
            adapter.get_policy.return_value = Policy(
                name="require-non-root",
                namespace=None,
                engine=PolicyEngine.KYVERNO,
                kind="ClusterPolicy",
                action=PolicyAction.ENFORCE,
                description="Blocks root containers",
                rules_count=1,
                violations_count=3,
                ready=True,
            )
            mock_build.return_value = adapter
            result = policy_get(name="require-non-root")
        assert result["error"] is None
        assert result["name"] == "require-non-root"
        assert result["engine"] == "kyverno"

    def test_service_get_policy(self) -> None:
        from hexawyn.application.ports.driving.policy_get.policy_get_command import (
            PolicyGetCommand,
        )
        from hexawyn.application.service.policy_get_service import PolicyGetService

        adapter = MagicMock(spec=PolicyPort)
        adapter.get_policy.return_value = Policy(
            name="deny-latest",
            namespace="production",
            engine=PolicyEngine.GATEKEEPER,
            kind="Constraint",
            action=PolicyAction.AUDIT,
            description="No latest tags",
            rules_count=1,
            violations_count=0,
            ready=True,
        )
        svc = PolicyGetService(policy_port=adapter)
        result = svc.get_policy(PolicyGetCommand(name="deny-latest", namespace="production"))
        assert result.name == "deny-latest"
        assert result.action == "audit"

    def test_use_case_delegates(self) -> None:
        from hexawyn.application.ports.driving.policy_get.policy_get_command import (
            PolicyGetCommand,
        )
        from hexawyn.application.ports.driving.policy_get.policy_get_response import (
            PolicyGetResponse,
        )
        from hexawyn.application.ports.driving.policy_get.policy_get_service_port import (
            PolicyGetServicePort,
        )
        from hexawyn.application.use_case.policy_get.policy_get_use_case import (
            PolicyGetUseCase,
        )

        fake = MagicMock(spec=PolicyGetServicePort)
        fake.get_policy.return_value = PolicyGetResponse(name="test", engine="kyverno")
        uc = PolicyGetUseCase(service=fake)
        result = uc.execute(PolicyGetCommand(name="test"))
        assert result.name == "test"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_get import policy_get

        with patch("hexawyn.mcp.server.build_policy_adapter", side_effect=RuntimeError("boom")):
            result = policy_get(name="x")
        assert result["error"] == "boom"


class TestPolicyViolationsList:
    def test_tool_returns_violations(self) -> None:
        from hexawyn.mcp.tools.policy_violations_list import policy_violations_list

        with patch("hexawyn.mcp.server.build_policy_adapter") as mock_build:
            adapter = MagicMock(spec=PolicyPort)
            adapter.list_violations.return_value = [
                PolicyViolation(
                    policy_name="require-non-root",
                    resource_kind="Deployment",
                    resource_name="nginx",
                    resource_namespace="default",
                    rule_name="check-containers",
                    message="Running as root forbidden",
                    severity=ViolationSeverity.HIGH,
                    action=PolicyAction.ENFORCE,
                    timestamp="2026-07-01T12:00:00Z",
                ),
            ]
            mock_build.return_value = adapter
            result = policy_violations_list(namespace="default")
        assert result["error"] is None
        assert len(result["violations"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_violations_list import policy_violations_list

        with patch("hexawyn.mcp.server.build_policy_adapter", side_effect=RuntimeError("boom")):
            result = policy_violations_list()
        assert result["error"] == "boom"


class TestPolicyExplainDenial:
    def test_tool_returns_explanation(self) -> None:
        from hexawyn.mcp.tools.policy_explain_denial import policy_explain_denial

        with patch("hexawyn.mcp.server.build_policy_adapter") as mock_build:
            adapter = MagicMock(spec=PolicyPort)
            adapter.explain_denial.return_value = PolicyDenialExplanation(
                resource_kind="Deployment",
                resource_name="nginx",
                namespace="default",
                policy_name="require-non-root",
                rule_name="check-containers",
                raw_message="admission webhook denied: Running as root is forbidden",
                human_explanation="Your deployment runs as root, which is blocked.",
                fix_suggestion="Set securityContext.runAsNonRoot to true.",
            )
            mock_build.return_value = adapter
            result = policy_explain_denial(
                resource_kind="Deployment",
                resource_name="nginx",
                namespace="default",
            )
        assert result["error"] is None
        assert result["policy_name"] == "require-non-root"
        assert result["fix_suggestion"] != ""

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_explain_denial import policy_explain_denial

        with patch("hexawyn.mcp.server.build_policy_adapter", side_effect=RuntimeError("boom")):
            result = policy_explain_denial(
                resource_kind="Pod",
                resource_name="x",
                namespace="ns",
            )
        assert result["error"] == "boom"


class TestPolicyAudit:
    def test_tool_returns_audit(self) -> None:
        from hexawyn.mcp.tools.policy_audit import policy_audit

        with patch("hexawyn.mcp.server.build_policy_adapter") as mock_build:
            adapter = MagicMock(spec=PolicyPort)
            adapter.audit.return_value = {"total_violations": 5, "compliant": False}
            mock_build.return_value = adapter
            result = policy_audit(namespace="production")
        assert result["error"] is None
        assert result["results"]["total_violations"] == 5

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.policy_audit import policy_audit

        with patch("hexawyn.mcp.server.build_policy_adapter", side_effect=RuntimeError("boom")):
            result = policy_audit()
        assert result["error"] == "boom"


class TestBuildPolicyAdapter:
    def test_returns_policy_port(self) -> None:
        from hexawyn.application.ports.driven.policy_port import PolicyPort
        from hexawyn.mcp.server import build_policy_adapter

        adapter = build_policy_adapter()
        assert isinstance(adapter, PolicyPort)


class TestRegisterFunctions:
    def test_all_policy_tools_have_register(self) -> None:
        import importlib

        tools = [
            "policy_detect",
            "policy_list",
            "policy_get",
            "policy_violations_list",
            "policy_explain_denial",
            "policy_audit",
        ]
        from fastmcp import FastMCP

        test_mcp = FastMCP("test-policy")
        for tool_name in tools:
            mod = importlib.import_module(f"hexawyn.mcp.tools.{tool_name}")
            register_fn = getattr(mod, "register", None)
            assert callable(register_fn)
            register_fn(test_mcp)
