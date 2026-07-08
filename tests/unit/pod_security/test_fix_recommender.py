"""Unit tests for recommend_fix — one specific securityContext fix sentence
per violation type (Acceptance Criteria: "recommends the specific security
context fix for each violation")."""

from __future__ import annotations


class TestRecommendFix:
    def test_privileged(self) -> None:
        from hexawyn.domain.services.pod_security.fix_recommender import recommend_fix

        fix = recommend_fix("privileged")

        assert "privileged: false" in fix

    def test_host_pid(self) -> None:
        from hexawyn.domain.services.pod_security.fix_recommender import recommend_fix

        fix = recommend_fix("host_pid")

        assert "hostPID: false" in fix

    def test_host_network(self) -> None:
        from hexawyn.domain.services.pod_security.fix_recommender import recommend_fix

        fix = recommend_fix("host_network")

        assert "hostNetwork: false" in fix

    def test_host_ipc(self) -> None:
        from hexawyn.domain.services.pod_security.fix_recommender import recommend_fix

        fix = recommend_fix("host_ipc")

        assert "hostIPC: false" in fix

    def test_run_as_root(self) -> None:
        from hexawyn.domain.services.pod_security.fix_recommender import recommend_fix

        fix = recommend_fix("run_as_root")

        assert "runAsNonRoot: true" in fix

    def test_allow_privilege_escalation(self) -> None:
        from hexawyn.domain.services.pod_security.fix_recommender import recommend_fix

        fix = recommend_fix("allow_privilege_escalation")

        assert "allowPrivilegeEscalation: false" in fix

    def test_dangerous_capability_names_the_capability(self) -> None:
        from hexawyn.domain.services.pod_security.fix_recommender import recommend_fix

        fix = recommend_fix("dangerous_capability", capability="SYS_ADMIN")

        assert "SYS_ADMIN" in fix
