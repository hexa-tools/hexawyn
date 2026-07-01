from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class PolicyEngine(Enum):
    KYVERNO = "kyverno"
    GATEKEEPER = "gatekeeper"
    NONE = "none"


class PolicyAction(Enum):
    ENFORCE = "enforce"
    AUDIT = "audit"
    GENERATE = "generate"
    MUTATE = "mutate"


class ViolationSeverity(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


@dataclass(frozen=True)
class Policy:
    name: str
    namespace: str | None
    engine: PolicyEngine
    kind: str
    action: PolicyAction
    description: str | None
    rules_count: int
    violations_count: int
    ready: bool


@dataclass(frozen=True)
class PolicyViolation:
    policy_name: str
    resource_kind: str
    resource_name: str
    resource_namespace: str
    rule_name: str
    message: str
    severity: ViolationSeverity
    action: PolicyAction
    timestamp: str


@dataclass(frozen=True)
class PolicyDenialExplanation:
    resource_kind: str
    resource_name: str
    namespace: str
    policy_name: str
    rule_name: str
    raw_message: str
    human_explanation: str
    fix_suggestion: str


@dataclass(frozen=True)
class PolicyDetectionResult:
    engine: PolicyEngine
    version: str | None
    namespace: str | None
    total_policies: int
    enforce_policies: int
    audit_policies: int
    total_violations: int
    high_severity: int
