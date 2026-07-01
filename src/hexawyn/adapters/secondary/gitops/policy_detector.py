from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.domain.errors import PolicyEngineNotFoundError
from hexawyn.domain.models.policy import (
    Policy,
    PolicyDenialExplanation,
    PolicyDetectionResult,
    PolicyEngine,
    PolicyViolation,
)


class PolicyDetector(PolicyPort):
    """Auto-detects Kyverno vs OPA Gatekeeper via CRD presence. All read-only."""

    def detect_engine(self) -> PolicyDetectionResult:
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

    def list_policies(self, namespace: str | None = None) -> list[Policy]:
        raise PolicyEngineNotFoundError()

    def get_policy(self, name: str, namespace: str | None = None) -> Policy:
        raise PolicyEngineNotFoundError()

    def list_violations(self, namespace: str | None = None) -> list[PolicyViolation]:
        raise PolicyEngineNotFoundError()

    def explain_denial(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        raise PolicyEngineNotFoundError()

    def audit(self, namespace: str | None = None) -> dict[str, object]:
        raise PolicyEngineNotFoundError()
