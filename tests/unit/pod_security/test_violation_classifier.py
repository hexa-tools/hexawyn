"""Unit tests for the deterministic Pod Security Standards severity + level
matrix (Checker Node cases 1 & 2 — no LLM/heuristic ambiguity):

- privileged / host_pid / host_network / host_ipc -> critical, Baseline
- run_as_root -> high, Restricted
- dangerous_capability -> high if the capability is genuinely dangerous
  (SYS_ADMIN, NET_ADMIN, ...), medium otherwise (e.g. NET_BIND_SERVICE) -
  always Restricted
- allow_privilege_escalation -> medium, Restricted
"""

from __future__ import annotations

import pytest


class TestClassifySeverity:
    @pytest.mark.parametrize(
        "violation_type", ["privileged", "host_pid", "host_network", "host_ipc"]
    )
    def test_critical_violation_types(self, violation_type: str) -> None:
        from hexawyn.domain.services.pod_security.violation_classifier import classify_severity

        assert classify_severity(violation_type) == "critical"  # type: ignore[arg-type]

    def test_run_as_root_is_high(self) -> None:
        from hexawyn.domain.services.pod_security.violation_classifier import classify_severity

        assert classify_severity("run_as_root") == "high"

    def test_dangerous_capability_is_high(self) -> None:
        from hexawyn.domain.services.pod_security.violation_classifier import classify_severity

        assert classify_severity("dangerous_capability", capability="SYS_ADMIN") == "high"

    def test_net_bind_service_capability_is_medium_not_critical(self) -> None:
        """Ticket edge case + Checker case 6: NET_BIND_SERVICE must never be
        classified critical/high — it's a narrowly-scoped, non-dangerous cap."""
        from hexawyn.domain.services.pod_security.violation_classifier import classify_severity

        assert classify_severity("dangerous_capability", capability="NET_BIND_SERVICE") == "medium"

    def test_allow_privilege_escalation_is_medium(self) -> None:
        from hexawyn.domain.services.pod_security.violation_classifier import classify_severity

        assert classify_severity("allow_privilege_escalation") == "medium"


class TestClassifyPSSLevel:
    @pytest.mark.parametrize(
        "violation_type", ["privileged", "host_pid", "host_network", "host_ipc"]
    )
    def test_baseline_violation_types(self, violation_type: str) -> None:
        from hexawyn.domain.services.pod_security.violation_classifier import classify_pss_level

        assert classify_pss_level(violation_type) == "Baseline"  # type: ignore[arg-type]

    @pytest.mark.parametrize(
        "violation_type",
        ["run_as_root", "allow_privilege_escalation", "dangerous_capability"],
    )
    def test_restricted_violation_types(self, violation_type: str) -> None:
        """Checker case 2: runAsNonRoot violations are Restricted, not
        Baseline — a common LLM mix-up this matrix must prevent."""
        from hexawyn.domain.services.pod_security.violation_classifier import classify_pss_level

        assert classify_pss_level(violation_type) == "Restricted"  # type: ignore[arg-type]
