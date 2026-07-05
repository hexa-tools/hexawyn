from __future__ import annotations


class TestManualChangeOutsideGitOpsResponse:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_response import (
            ManualChangeOutsideGitOpsResponse,
        )

        response = ManualChangeOutsideGitOpsResponse()

        assert response.manual_changes == []
        assert response.total_manual_changes == 0
        assert response.excluded_gitops_change_count == 0
        assert response.used_managed_fields_fallback is False
        assert response.partial_window is False
        assert response.notes == []
        assert response.error is None

    def test_accepts_explicit_values(self) -> None:
        from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_response import (
            ManualChangeDict,
            ManualChangeOutsideGitOpsResponse,
        )

        change: ManualChangeDict = {
            "kind": "Secret",
            "name": "db-password",
            "namespace": "production",
            "timestamp": "2026-06-12T09:11:00Z",
            "actor": "user:jane.ops@company.com",
            "actor_type": "human",
            "changed_fields": ["data.password"],
            "severity": "critical",
            "is_limited_actor_info": False,
        }
        response = ManualChangeOutsideGitOpsResponse(
            manual_changes=[change],
            total_manual_changes=1,
            excluded_gitops_change_count=2,
            used_managed_fields_fallback=True,
            partial_window=True,
            notes=["note"],
            error=None,
        )

        assert response.manual_changes == [change]
        assert response.total_manual_changes == 1
        assert response.excluded_gitops_change_count == 2
        assert response.used_managed_fields_fallback is True
        assert response.partial_window is True
        assert response.notes == ["note"]
