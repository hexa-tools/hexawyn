from __future__ import annotations

from unittest.mock import MagicMock


def _make_manual_change(**overrides: object) -> object:
    from hexawyn.domain.models.manual_change import ManualChange

    defaults: dict[str, object] = {
        "kind": "Deployment",
        "name": "my-app",
        "namespace": "default",
        "timestamp": "2026-07-27T10:00:00Z",
        "actor": "kubectl-set",
        "actor_type": "human",
        "changed_fields": ["spec.replicas"],
        "severity": "warning",
        "is_limited_actor_info": False,
    }
    defaults.update(overrides)
    return ManualChange(**defaults)  # type: ignore[arg-type]


class TestManualChangeOutsideGitopsUseCase:
    def test_detect_manual_changes_returns_response_type(self) -> None:
        from hexawyn.application.use_case.gitops.manual_change_outside_gitops.command import (
            ManualChangeOutsideGitopsCommand,
        )
        from hexawyn.application.use_case.gitops.manual_change_outside_gitops.manual_change_outside_gitops_use_case import (  # noqa: E501
            ManualChangeOutsideGitopsUseCase,
        )
        from hexawyn.application.use_case.gitops.manual_change_outside_gitops.response import (
            ManualChangeOutsideGitopsResponse,
        )

        mock_port = MagicMock()
        mock_port.list_live_config_resources.return_value = []
        mock_port.fetch_audit_log_events.return_value = {
            "events": [],
            "available": False,
            "earliest_timestamp": None,
        }

        use_case = ManualChangeOutsideGitopsUseCase(audit_port=mock_port)
        result = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace="default")
        )

        assert isinstance(result, ManualChangeOutsideGitopsResponse)
        assert result.error is None

    def test_detect_manual_changes_uses_namespace_from_command(self) -> None:
        from hexawyn.application.use_case.gitops.manual_change_outside_gitops.command import (
            ManualChangeOutsideGitopsCommand,
        )
        from hexawyn.application.use_case.gitops.manual_change_outside_gitops.manual_change_outside_gitops_use_case import (  # noqa: E501
            ManualChangeOutsideGitopsUseCase,
        )

        mock_port = MagicMock()
        mock_port.list_live_config_resources.return_value = []
        mock_port.fetch_audit_log_events.return_value = {
            "events": [],
            "available": False,
            "earliest_timestamp": None,
        }

        use_case = ManualChangeOutsideGitopsUseCase(audit_port=mock_port)
        use_case.detect_manual_changes(ManualChangeOutsideGitopsCommand(namespace="production"))

        mock_port.list_live_config_resources.assert_called_once_with("production")
        mock_port.fetch_audit_log_events.assert_called_once_with("production", 7)

    def test_detect_manual_changes_uses_window_days_from_command(self) -> None:
        from hexawyn.application.use_case.gitops.manual_change_outside_gitops.command import (
            ManualChangeOutsideGitopsCommand,
        )
        from hexawyn.application.use_case.gitops.manual_change_outside_gitops.manual_change_outside_gitops_use_case import (  # noqa: E501
            ManualChangeOutsideGitopsUseCase,
        )

        mock_port = MagicMock()
        mock_port.list_live_config_resources.return_value = []
        mock_port.fetch_audit_log_events.return_value = {
            "events": [],
            "available": False,
            "earliest_timestamp": None,
        }

        use_case = ManualChangeOutsideGitopsUseCase(audit_port=mock_port)
        use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace="default", window_days=30)
        )

        mock_port.fetch_audit_log_events.assert_called_once_with("default", 30)

    def test_detect_manual_changes_includes_report_fields(self) -> None:
        from hexawyn.application.use_case.gitops.manual_change_outside_gitops.command import (
            ManualChangeOutsideGitopsCommand,
        )
        from hexawyn.application.use_case.gitops.manual_change_outside_gitops.manual_change_outside_gitops_use_case import (  # noqa: E501
            ManualChangeOutsideGitopsUseCase,
        )

        mock_port = MagicMock()
        mock_port.list_live_config_resources.return_value = []
        mock_port.fetch_audit_log_events.return_value = {
            "events": [],
            "available": False,
            "earliest_timestamp": None,
        }

        use_case = ManualChangeOutsideGitopsUseCase(audit_port=mock_port)
        result = use_case.detect_manual_changes(
            ManualChangeOutsideGitopsCommand(namespace="default")
        )

        assert hasattr(result, "manual_changes")
        assert hasattr(result, "total_manual_changes")
        assert hasattr(result, "excluded_gitops_change_count")
        assert hasattr(result, "used_managed_fields_fallback")
        assert hasattr(result, "partial_window")
        assert hasattr(result, "notes")
