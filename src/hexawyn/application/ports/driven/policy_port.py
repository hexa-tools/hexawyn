from abc import ABC, abstractmethod

from hexawyn.domain.models.policy import (
    Policy,
    PolicyDenialExplanation,
    PolicyDetectionResult,
    PolicyViolation,
)


class PolicyPort(ABC):
    """Port for policy engine (Kyverno / OPA Gatekeeper) operations — read-only."""

    @abstractmethod
    def detect_engine(self) -> PolicyDetectionResult:
        """Detect Kyverno or Gatekeeper presence."""

    @abstractmethod
    def list_policies(self, namespace: str | None = None) -> list[Policy]:
        """List all policies."""

    @abstractmethod
    def get_policy(self, name: str, namespace: str | None = None) -> Policy:
        """Get a specific policy detail."""

    @abstractmethod
    def list_violations(self, namespace: str | None = None) -> list[PolicyViolation]:
        """List current violations."""

    @abstractmethod
    def explain_denial(
        self, resource_kind: str, resource_name: str, namespace: str
    ) -> PolicyDenialExplanation:
        """Explain why a resource was denied with fix suggestion."""

    @abstractmethod
    def audit(self, namespace: str | None = None) -> dict[str, object]:
        """Run a global compliance audit."""
