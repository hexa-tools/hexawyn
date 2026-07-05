"""Unit tests for ManualChangeOutsideGitOpsService — mocks GitOpsDriftAuditPort.

Timestamps are computed relative to datetime.now(UTC) (the same pattern used
in test_server.py's stuck-pipeline-run tests) so the tests stay deterministic
regardless of the actual current date.
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_command import (
    ManualChangeOutsideGitOpsCommand,
)
from hexawyn.application.service.manual_change_outside_gitops_service import (
    ManualChangeOutsideGitOpsService,
)


def _ts(days_ago: float) -> str:
    return (datetime.now(UTC) - timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")


def _resource(
    kind: str, name: str, managed_fields: list[dict], namespace: str = "production"
) -> dict:
    return {"kind": kind, "name": name, "namespace": namespace, "managed_fields": managed_fields}


def _entry(manager: str, time: str, fields_v1_raw: dict) -> dict:
    return {"manager": manager, "operation": "Update", "time": time, "fields_v1_raw": fields_v1_raw}


def _no_audit_log() -> dict:
    return {"available": False, "events": [], "earliest_timestamp": None}


def _make_service(
    audit_port: MagicMock | None = None,
) -> tuple[ManualChangeOutsideGitOpsService, MagicMock]:
    if audit_port is None:
        audit_port = MagicMock()
        audit_port.list_live_config_resources.return_value = []
        audit_port.fetch_audit_log_events.return_value = _no_audit_log()
    return ManualChangeOutsideGitOpsService(audit_port=audit_port), audit_port


class TestHumanConfigMapChange:
    def test_tc1_configmap_modified_by_human_is_flagged_manual_with_warning(self) -> None:
        """TC1: ConfigMap app-config modified by user:john (not ArgoCD)."""
        ts = _ts(1)
        audit_port = MagicMock()
        audit_port.list_live_config_resources.return_value = [
            _resource(
                "ConfigMap",
                "app-config",
                [_entry("kubectl-client-side-apply", ts, {"f:data": {"f:DATABASE_URL": {}}})],
            )
        ]
        audit_port.fetch_audit_log_events.return_value = {
            "available": True,
            "events": [
                {
                    "kind": "ConfigMap",
                    "name": "app-config",
                    "namespace": "production",
                    "actor": "user:john.doe@company.com",
                    "verb": "update",
                    "timestamp": ts,
                }
            ],
            "earliest_timestamp": _ts(6),
        }
        service, _ = _make_service(audit_port)

        response = service.detect_manual_changes(
            ManualChangeOutsideGitOpsCommand(namespace="production")
        )

        assert response.error is None
        assert len(response.manual_changes) == 1
        change = response.manual_changes[0]
        assert change["actor"] == "user:john.doe@company.com"
        assert change["actor_type"] == "human"
        assert change["severity"] == "warning"
        assert change["changed_fields"] == ["data.DATABASE_URL"]
        assert change["is_limited_actor_info"] is False


class TestSecretCriticalSeverity:
    def test_tc2_secret_modified_by_human_is_critical(self) -> None:
        """TC2: Secret db-password modified by human 3 days ago."""
        ts = _ts(3)
        audit_port = MagicMock()
        audit_port.list_live_config_resources.return_value = [
            _resource(
                "Secret",
                "db-password",
                [_entry("kubectl-client-side-apply", ts, {"f:data": {"f:password": {}}})],
            )
        ]
        audit_port.fetch_audit_log_events.return_value = {
            "available": True,
            "events": [
                {
                    "kind": "Secret",
                    "name": "db-password",
                    "namespace": "production",
                    "actor": "user:jane.ops@company.com",
                    "verb": "update",
                    "timestamp": ts,
                }
            ],
            "earliest_timestamp": _ts(6),
        }
        service, _ = _make_service(audit_port)

        response = service.detect_manual_changes(
            ManualChangeOutsideGitOpsCommand(namespace="production")
        )

        assert len(response.manual_changes) == 1
        assert response.manual_changes[0]["severity"] == "critical"
        assert response.manual_changes[0]["actor"] == "user:jane.ops@company.com"


class TestAllChangesByGitOpsController:
    def test_tc3_all_argocd_changes_produce_no_manual_changes(self) -> None:
        ts = _ts(2)
        audit_port = MagicMock()
        audit_port.list_live_config_resources.return_value = [
            _resource(
                "ConfigMap",
                "app-config",
                [_entry("argocd-application-controller", ts, {"f:data": {"f:DATABASE_URL": {}}})],
            )
        ]
        audit_port.fetch_audit_log_events.return_value = _no_audit_log()
        service, _ = _make_service(audit_port)

        response = service.detect_manual_changes(
            ManualChangeOutsideGitOpsCommand(namespace="production")
        )

        assert response.manual_changes == []
        assert response.excluded_gitops_change_count == 1


class TestFiveManualChangesListed:
    def test_tc4_five_manual_changes_all_listed(self) -> None:
        entries = [
            _entry("kubectl-client-side-apply", _ts(i), {"f:data": {"f:KEY": {}}}) for i in range(5)
        ]
        audit_port = MagicMock()
        audit_port.list_live_config_resources.return_value = [
            _resource("ConfigMap", "app-config", entries)
        ]
        audit_port.fetch_audit_log_events.return_value = _no_audit_log()
        service, _ = _make_service(audit_port)

        response = service.detect_manual_changes(
            ManualChangeOutsideGitOpsCommand(namespace="production")
        )

        assert len(response.manual_changes) == 5
        assert response.total_manual_changes == 5


class TestMixedGitOpsAndHumanChange:
    def test_tc5_configmap_changed_by_argocd_then_human_only_human_flagged(self) -> None:
        argocd_ts = _ts(5)
        human_ts = _ts(1)
        audit_port = MagicMock()
        audit_port.list_live_config_resources.return_value = [
            _resource(
                "ConfigMap",
                "app-config",
                [
                    _entry(
                        "argocd-application-controller", argocd_ts, {"f:data": {"f:REPLICAS": {}}}
                    ),
                    _entry(
                        "kubectl-client-side-apply", human_ts, {"f:data": {"f:DATABASE_URL": {}}}
                    ),
                ],
            )
        ]
        audit_port.fetch_audit_log_events.return_value = _no_audit_log()
        service, _ = _make_service(audit_port)

        response = service.detect_manual_changes(
            ManualChangeOutsideGitOpsCommand(namespace="production")
        )

        assert len(response.manual_changes) == 1
        assert response.manual_changes[0]["timestamp"] == human_ts
        assert response.excluded_gitops_change_count == 1


class TestAuditLogFallback:
    def test_no_audit_log_falls_back_to_managed_fields_with_limited_actor_info(self) -> None:
        ts = _ts(1)
        audit_port = MagicMock()
        audit_port.list_live_config_resources.return_value = [
            _resource(
                "ConfigMap",
                "app-config",
                [_entry("kubectl-client-side-apply", ts, {"f:data": {"f:DATABASE_URL": {}}})],
            )
        ]
        audit_port.fetch_audit_log_events.return_value = _no_audit_log()
        service, _ = _make_service(audit_port)

        response = service.detect_manual_changes(
            ManualChangeOutsideGitOpsCommand(namespace="production")
        )

        assert len(response.manual_changes) == 1
        assert response.manual_changes[0]["actor"] == "kubectl-client-side-apply"
        assert response.manual_changes[0]["is_limited_actor_info"] is True
        assert response.used_managed_fields_fallback is True
        assert any("managedFields" in note for note in response.notes)


class TestPartialWindowNote:
    def test_earliest_audit_timestamp_newer_than_window_start_flags_partial(self) -> None:
        ts = _ts(1)
        audit_port = MagicMock()
        audit_port.list_live_config_resources.return_value = [
            _resource(
                "ConfigMap",
                "app-config",
                [_entry("kubectl-client-side-apply", ts, {"f:data": {"f:DATABASE_URL": {}}})],
            )
        ]
        audit_port.fetch_audit_log_events.return_value = {
            "available": True,
            "events": [],
            "earliest_timestamp": _ts(2),
        }
        service, _ = _make_service(audit_port)

        response = service.detect_manual_changes(
            ManualChangeOutsideGitOpsCommand(namespace="production")
        )

        assert response.partial_window is True


class TestCIServiceAccountVsHumanDifferentiation:
    def test_ci_service_account_and_human_both_manual_but_differentiated(self) -> None:
        ci_ts = _ts(1)
        human_ts = _ts(2)
        audit_port = MagicMock()
        audit_port.list_live_config_resources.return_value = [
            _resource(
                "ConfigMap",
                "app-config",
                [
                    _entry(
                        "system:serviceaccount:ci:pipeline-runner", ci_ts, {"f:data": {"f:A": {}}}
                    ),
                    _entry("kubectl-client-side-apply", human_ts, {"f:data": {"f:B": {}}}),
                ],
            )
        ]
        audit_port.fetch_audit_log_events.return_value = _no_audit_log()
        service, _ = _make_service(audit_port)

        response = service.detect_manual_changes(
            ManualChangeOutsideGitOpsCommand(namespace="production")
        )

        assert len(response.manual_changes) == 2
        actor_types = {c["timestamp"]: c["actor_type"] for c in response.manual_changes}
        assert actor_types[ci_ts] == "service_account"
        assert actor_types[human_ts] == "human"


class TestOutsideWindowExcluded:
    def test_entry_older_than_window_is_excluded(self) -> None:
        old_ts = _ts(10)
        audit_port = MagicMock()
        audit_port.list_live_config_resources.return_value = [
            _resource(
                "ConfigMap",
                "app-config",
                [_entry("kubectl-client-side-apply", old_ts, {"f:data": {"f:DATABASE_URL": {}}})],
            )
        ]
        audit_port.fetch_audit_log_events.return_value = _no_audit_log()
        service, _ = _make_service(audit_port)

        response = service.detect_manual_changes(
            ManualChangeOutsideGitOpsCommand(namespace="production", window_days=7)
        )

        assert response.manual_changes == []


class TestNoLiveResources:
    def test_empty_namespace_produces_empty_report(self) -> None:
        service, _ = _make_service()

        response = service.detect_manual_changes(
            ManualChangeOutsideGitOpsCommand(namespace="production")
        )

        assert response.error is None
        assert response.manual_changes == []
        assert response.total_manual_changes == 0
