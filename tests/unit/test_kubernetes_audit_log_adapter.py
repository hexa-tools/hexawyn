"""Unit tests for KubernetesAuditLogAdapter — mocks kubernetes.client.CoreV1Api
for list_live_config_resources, uses real tmp_path files for
fetch_audit_log_events (no k8s audit-log-API precedent exists to mock)."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.gitops_drift_audit_port import GitOpsDriftAuditPort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _managed_fields_entry(
    manager: str,
    operation: str = "Update",
    time: datetime | None = None,
    fields_v1: dict | None = None,
) -> MagicMock:
    entry = MagicMock()
    entry.manager = manager
    entry.operation = operation
    entry.time = time if time is not None else datetime(2026, 6, 14, 14, 23, tzinfo=UTC)
    entry.fields_v1 = fields_v1 if fields_v1 is not None else {"f:data": {"f:KEY": {}}}
    return entry


def _item(
    name: str, namespace: str = "production", managed_fields: list | None = None
) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.metadata.managed_fields = managed_fields if managed_fields is not None else []
    return item


def _list_response(*items: MagicMock) -> MagicMock:
    response = MagicMock()
    response.items = list(items)
    return response


class TestKubernetesAuditLogAdapterIsPort:
    def test_is_gitops_drift_audit_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        assert isinstance(KubernetesAuditLogAdapter(), GitOpsDriftAuditPort)


class TestListLiveConfigResources:
    def test_returns_configmaps_and_secrets_with_managed_fields(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespaced_config_map.return_value = _list_response(
            _item("app-config", managed_fields=[_managed_fields_entry("kubectl-client-side-apply")])
        )
        core_api.list_namespaced_secret.return_value = _list_response(
            _item(
                "db-password",
                managed_fields=[_managed_fields_entry("argocd-application-controller")],
            )
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAuditLogAdapter()
            resources = adapter.list_live_config_resources("production")

        by_kind = {r["kind"]: r for r in resources}
        assert by_kind["ConfigMap"]["name"] == "app-config"
        assert by_kind["Secret"]["name"] == "db-password"
        entry = by_kind["ConfigMap"]["managed_fields"][0]
        assert entry["manager"] == "kubectl-client-side-apply"
        assert entry["operation"] == "Update"
        assert entry["time"] == "2026-06-14T14:23:00+00:00"
        assert entry["fields_v1_raw"] == {"f:data": {"f:KEY": {}}}

    def test_no_managed_fields_returns_empty_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespaced_config_map.return_value = _list_response(
            _item("app-config", managed_fields=None)
        )
        core_api.list_namespaced_secret.return_value = _list_response()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAuditLogAdapter()
            resources = adapter.list_live_config_resources("production")

        assert resources[0]["managed_fields"] == []

    def test_non_dict_fields_v1_defaults_to_empty_mapping(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespaced_config_map.return_value = _list_response(
            _item(
                "app-config",
                managed_fields=[_managed_fields_entry("kubectl-edit", fields_v1="not-a-dict")],
            )
        )
        core_api.list_namespaced_secret.return_value = _list_response()

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAuditLogAdapter()
            resources = adapter.list_live_config_resources("production")

        assert resources[0]["managed_fields"][0]["fields_v1_raw"] == {}

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        core_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        core_api.list_namespaced_config_map.side_effect = error

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAuditLogAdapter()
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_live_config_resources("production")

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespaced_config_map.side_effect = Exception("connection refused")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            adapter = KubernetesAuditLogAdapter()
            with pytest.raises(ClusterUnreachableError):
                adapter.list_live_config_resources("production")


class TestFetchAuditLogEvents:
    def test_missing_file_returns_unavailable(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(tmp_path / "does-not-exist.log"))
        adapter = KubernetesAuditLogAdapter()

        result = adapter.fetch_audit_log_events("production", 7)

        assert result["available"] is False
        assert result["events"] == []
        assert result["earliest_timestamp"] is None

    def test_valid_ndjson_parsed_into_events(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        log_path = tmp_path / "audit.log"
        lines = [
            {
                "verb": "update",
                "objectRef": {
                    "resource": "configmaps",
                    "namespace": "production",
                    "name": "app-config",
                },
                "user": {"username": "user:john.doe@company.com"},
                "requestReceivedTimestamp": "2026-06-14T14:23:00.000000Z",
            },
            {
                "verb": "patch",
                "objectRef": {
                    "resource": "secrets",
                    "namespace": "production",
                    "name": "db-password",
                },
                "user": {"username": "user:jane.ops@company.com"},
                "requestReceivedTimestamp": "2026-06-12T09:11:00.000000Z",
            },
        ]
        log_path.write_text("\n".join(json.dumps(line) for line in lines))
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))
        adapter = KubernetesAuditLogAdapter()

        result = adapter.fetch_audit_log_events("production", 7)

        assert result["available"] is True
        assert len(result["events"]) == 2
        actors = {event["name"]: event["actor"] for event in result["events"]}
        assert actors["app-config"] == "user:john.doe@company.com"
        assert actors["db-password"] == "user:jane.ops@company.com"
        assert result["earliest_timestamp"] == "2026-06-12T09:11:00.000000Z"

    def test_malformed_line_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        log_path = tmp_path / "audit.log"
        valid_line = json.dumps(
            {
                "verb": "update",
                "objectRef": {
                    "resource": "configmaps",
                    "namespace": "production",
                    "name": "app-config",
                },
                "user": {"username": "user:john.doe@company.com"},
                "requestReceivedTimestamp": "2026-06-14T14:23:00.000000Z",
            }
        )
        log_path.write_text("not-json\n" + valid_line)
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))
        adapter = KubernetesAuditLogAdapter()

        result = adapter.fetch_audit_log_events("production", 7)

        assert len(result["events"]) == 1

    def test_other_namespace_and_resource_kind_are_filtered_out(
        self, tmp_path, monkeypatch
    ) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        log_path = tmp_path / "audit.log"
        lines = [
            {
                "verb": "update",
                "objectRef": {
                    "resource": "configmaps",
                    "namespace": "staging",
                    "name": "other-config",
                },
                "user": {"username": "user:a@company.com"},
                "requestReceivedTimestamp": "2026-06-14T14:23:00.000000Z",
            },
            {
                "verb": "update",
                "objectRef": {"resource": "pods", "namespace": "production", "name": "some-pod"},
                "user": {"username": "user:b@company.com"},
                "requestReceivedTimestamp": "2026-06-14T14:23:00.000000Z",
            },
        ]
        log_path.write_text("\n".join(json.dumps(line) for line in lines))
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))
        adapter = KubernetesAuditLogAdapter()

        result = adapter.fetch_audit_log_events("production", 7)

        assert result["events"] == []
        assert result["earliest_timestamp"] is None

    def test_non_dict_json_line_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        log_path = tmp_path / "audit.log"
        log_path.write_text(json.dumps(["not", "a", "dict"]))
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))
        adapter = KubernetesAuditLogAdapter()

        result = adapter.fetch_audit_log_events("production", 7)

        assert result["events"] == []

    def test_object_ref_missing_fields_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        log_path = tmp_path / "audit.log"
        log_path.write_text(json.dumps({"verb": "update", "objectRef": "not-a-dict"}))
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))
        adapter = KubernetesAuditLogAdapter()

        result = adapter.fetch_audit_log_events("production", 7)

        assert result["events"] == []

    def test_non_string_resource_field_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        log_path = tmp_path / "audit.log"
        log_path.write_text(
            json.dumps(
                {
                    "verb": "update",
                    "objectRef": {"resource": 123, "namespace": "production", "name": "app-config"},
                }
            )
        )
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))
        adapter = KubernetesAuditLogAdapter()

        result = adapter.fetch_audit_log_events("production", 7)

        assert result["events"] == []

    def test_missing_user_or_timestamp_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        log_path = tmp_path / "audit.log"
        log_path.write_text(
            json.dumps(
                {
                    "verb": "update",
                    "objectRef": {
                        "resource": "configmaps",
                        "namespace": "production",
                        "name": "app-config",
                    },
                }
            )
        )
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))
        adapter = KubernetesAuditLogAdapter()

        result = adapter.fetch_audit_log_events("production", 7)

        assert result["events"] == []

    def test_default_path_used_when_env_var_not_set(self, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
            KubernetesAuditLogAdapter,
        )

        monkeypatch.delenv("K8S_AUDIT_LOG_PATH", raising=False)
        adapter = KubernetesAuditLogAdapter()

        result = adapter.fetch_audit_log_events("production", 7)

        assert result["available"] is False
