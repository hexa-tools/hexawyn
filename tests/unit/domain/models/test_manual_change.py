"""Unit tests for the Manual Change Outside GitOps domain models."""

from __future__ import annotations


class TestManualChange:
    def test_creates_manual_change_with_expected_fields(self) -> None:
        from hexawyn.domain.models.manual_change import ManualChange

        change = ManualChange(
            kind="Secret",
            name="db-password",
            namespace="production",
            timestamp="2026-06-12T09:11:00Z",
            actor="user:jane.ops@company.com",
            actor_type="human",
            changed_fields=["data.password"],
            severity="critical",
            is_limited_actor_info=False,
        )

        assert change.kind == "Secret"
        assert change.name == "db-password"
        assert change.namespace == "production"
        assert change.actor_type == "human"
        assert change.changed_fields == ["data.password"]
        assert change.severity == "critical"
        assert change.is_limited_actor_info is False

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.manual_change import ManualChange

        change = ManualChange(
            kind="ConfigMap",
            name="app-config",
            namespace="production",
            timestamp="2026-06-14T14:23:00Z",
            actor="user:john.doe@company.com",
            actor_type="human",
            changed_fields=["data.DATABASE_URL"],
            severity="warning",
            is_limited_actor_info=False,
        )

        import dataclasses

        with __import__("pytest").raises(dataclasses.FrozenInstanceError):
            change.severity = "critical"  # type: ignore[misc]


class TestManualChangeOutsideGitOpsRequest:
    def test_defaults_window_days_to_seven(self) -> None:
        from hexawyn.domain.models.manual_change import ManualChangeOutsideGitOpsRequest

        request = ManualChangeOutsideGitOpsRequest(namespace="production")

        assert request.namespace == "production"
        assert request.window_days == 7  # noqa: PLR2004

    def test_accepts_custom_window_days(self) -> None:
        from hexawyn.domain.models.manual_change import ManualChangeOutsideGitOpsRequest

        request = ManualChangeOutsideGitOpsRequest(namespace="production", window_days=3)

        assert request.window_days == 3  # noqa: PLR2004


class TestManualChangeOutsideGitOpsReport:
    def test_creates_report_with_expected_fields(self) -> None:
        from hexawyn.domain.models.manual_change import (
            ManualChange,
            ManualChangeOutsideGitOpsReport,
        )

        change = ManualChange(
            kind="ConfigMap",
            name="app-config",
            namespace="production",
            timestamp="2026-06-14T14:23:00Z",
            actor="user:john.doe@company.com",
            actor_type="human",
            changed_fields=["data.DATABASE_URL"],
            severity="warning",
            is_limited_actor_info=False,
        )
        report = ManualChangeOutsideGitOpsReport(
            manual_changes=[change],
            total_manual_changes=1,
            excluded_gitops_change_count=1,
            used_managed_fields_fallback=False,
            partial_window=False,
            notes=[],
        )

        assert report.manual_changes == [change]
        assert report.total_manual_changes == 1
        assert report.excluded_gitops_change_count == 1
        assert report.used_managed_fields_fallback is False
        assert report.partial_window is False
        assert report.notes == []
