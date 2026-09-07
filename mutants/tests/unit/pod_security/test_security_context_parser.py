"""Unit tests for resolving Kubernetes' own securityContext default/override
semantics from already-raw primitives (never touching k8s SDK objects)."""

from __future__ import annotations


class TestResolvesToRoot:
    def test_container_level_true_is_not_root(self) -> None:
        from hexawyn.domain.services.pod_security.security_context_parser import (
            resolves_to_root,
        )

        assert resolves_to_root(container_level=True, pod_level=None) is False

    def test_container_level_explicit_false_is_root(self) -> None:
        """Test Scenario 2: runAsNonRoot: false -> high violation."""
        from hexawyn.domain.services.pod_security.security_context_parser import (
            resolves_to_root,
        )

        assert resolves_to_root(container_level=False, pod_level=True) is True

    def test_container_level_wins_over_pod_level(self) -> None:
        from hexawyn.domain.services.pod_security.security_context_parser import (
            resolves_to_root,
        )

        assert resolves_to_root(container_level=False, pod_level=True) is True
        assert resolves_to_root(container_level=True, pod_level=False) is False

    def test_falls_back_to_pod_level_when_container_level_unset(self) -> None:
        from hexawyn.domain.services.pod_security.security_context_parser import (
            resolves_to_root,
        )

        assert resolves_to_root(container_level=None, pod_level=True) is False
        assert resolves_to_root(container_level=None, pod_level=False) is True

    def test_both_unset_defaults_to_root(self) -> None:
        """Edge Case 3 / Checker case 3: no securityContext at all ->
        defaults assumed (root)."""
        from hexawyn.domain.services.pod_security.security_context_parser import (
            resolves_to_root,
        )

        assert resolves_to_root(container_level=None, pod_level=None) is True


class TestAllowsPrivilegeEscalation:
    def test_unset_defaults_to_allowed(self) -> None:
        """Edge Case 3: no securityContext -> escalation allowed by default."""
        from hexawyn.domain.services.pod_security.security_context_parser import (
            allows_privilege_escalation,
        )

        assert allows_privilege_escalation(None) is True

    def test_explicit_true_is_allowed(self) -> None:
        from hexawyn.domain.services.pod_security.security_context_parser import (
            allows_privilege_escalation,
        )

        assert allows_privilege_escalation(True) is True

    def test_explicit_false_is_not_allowed(self) -> None:
        from hexawyn.domain.services.pod_security.security_context_parser import (
            allows_privilege_escalation,
        )

        assert allows_privilege_escalation(False) is False


class TestIsPrivileged:
    def test_unset_is_not_privileged(self) -> None:
        from hexawyn.domain.services.pod_security.security_context_parser import is_privileged

        assert is_privileged(None) is False

    def test_explicit_false_is_not_privileged(self) -> None:
        from hexawyn.domain.services.pod_security.security_context_parser import is_privileged

        assert is_privileged(False) is False

    def test_explicit_true_is_privileged(self) -> None:
        """Test Scenario 1: privileged: true -> critical violation."""
        from hexawyn.domain.services.pod_security.security_context_parser import is_privileged

        assert is_privileged(True) is True
