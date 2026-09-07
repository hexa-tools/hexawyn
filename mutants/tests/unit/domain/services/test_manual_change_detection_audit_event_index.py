from __future__ import annotations

from hexawyn.application.ports.driven.gitops_drift_audit_port import AuditEventRaw


class TestIndexAuditEvents:
    def test_happy_path_returns_indexed_by_composite_key(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_index import (
            index_audit_events,
        )

        events: list[AuditEventRaw] = [
            {
                "kind": "ConfigMap",
                "name": "my-config",
                "namespace": "default",
                "actor": "admin",
                "verb": "update",
                "timestamp": "2026-01-01T00:00:00Z",
            },
            {
                "kind": "Secret",
                "name": "db-creds",
                "namespace": "production",
                "actor": "ci-bot",
                "verb": "patch",
                "timestamp": "2026-01-02T12:00:00Z",
            },
        ]

        result = index_audit_events(events)

        assert result[("ConfigMap", "my-config", "default", "2026-01-01T00:00:00Z")] == "admin"
        assert result[("Secret", "db-creds", "production", "2026-01-02T12:00:00Z")] == "ci-bot"

    def test_empty_list_returns_empty_dict(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_index import (
            index_audit_events,
        )

        result = index_audit_events([])

        assert result == {}
        assert isinstance(result, dict)

    def test_single_event_returns_single_entry(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_index import (
            index_audit_events,
        )

        events: list[AuditEventRaw] = [
            {
                "kind": "ConfigMap",
                "name": "sole-config",
                "namespace": "kube-system",
                "actor": "controller",
                "verb": "create",
                "timestamp": "2026-07-01T08:00:00Z",
            },
        ]

        result = index_audit_events(events)

        assert len(result) == 1

    def test_duplicate_keys_last_wins(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_index import (
            index_audit_events,
        )

        events: list[AuditEventRaw] = [
            {
                "kind": "ConfigMap",
                "name": "shared",
                "namespace": "default",
                "actor": "first",
                "verb": "update",
                "timestamp": "2026-01-01T00:00:00Z",
            },
            {
                "kind": "ConfigMap",
                "name": "shared",
                "namespace": "default",
                "actor": "second",
                "verb": "update",
                "timestamp": "2026-01-01T00:00:00Z",
            },
        ]

        result = index_audit_events(events)

        assert result[("ConfigMap", "shared", "default", "2026-01-01T00:00:00Z")] == "second"

    def test_empty_string_values_are_indexed(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_index import (
            index_audit_events,
        )

        events: list[AuditEventRaw] = [
            {
                "kind": "",
                "name": "",
                "namespace": "",
                "actor": "nobody",
                "verb": "delete",
                "timestamp": "",
            },
        ]

        result = index_audit_events(events)

        assert result[("", "", "", "")] == "nobody"

    def test_no_events_returns_dict_instance(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_index import (
            index_audit_events,
        )

        result = index_audit_events([])

        assert isinstance(result, dict)

    def test_many_events_correct_size(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_index import (
            index_audit_events,
        )

        events: list[AuditEventRaw] = [
            {
                "kind": "Secret",
                "name": f"secret-{i}",
                "namespace": "ns",
                "actor": f"user-{i}",
                "verb": "update",
                "timestamp": f"2026-01-01T{i:02d}:00:00Z",
            }
            for i in range(100)
        ]

        result = index_audit_events(events)

        assert len(result) == 100  # noqa: PLR2004
