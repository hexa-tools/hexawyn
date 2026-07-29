from __future__ import annotations

import json
from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
    _parse_audit_line,
)
from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
    _node_allocatable,
    _node_allocatable_cpu,
    _node_allocatable_memory_gb,
)


class TestParseAuditLine:
    def test_valid_configmap(self) -> None:
        line = json.dumps(
            {
                "objectRef": {
                    "resource": "configmaps",
                    "namespace": "default",
                    "name": "my-config",
                },
                "user": {"username": "admin"},
                "requestReceivedTimestamp": "2026-01-01T00:00:00Z",
                "verb": "update",
            }
        )
        result = _parse_audit_line(line, "default")
        assert result is not None
        assert result["kind"] == "ConfigMap"

    def test_valid_secret(self) -> None:
        line = json.dumps(
            {
                "objectRef": {"resource": "secrets", "namespace": "prod", "name": "db-pass"},
                "user": {"username": "sa"},
                "requestReceivedTimestamp": "2026-01-01T00:00:00Z",
                "verb": "get",
            }
        )
        result = _parse_audit_line(line, "prod")
        assert result is not None
        assert result["kind"] == "Secret"

    def test_invalid_json(self) -> None:
        assert _parse_audit_line("bad json", "ns") is None

    def test_wrong_namespace(self) -> None:
        line = json.dumps(
            {
                "objectRef": {"resource": "configmaps", "namespace": "other", "name": "x"},
                "user": {"username": "admin"},
                "requestReceivedTimestamp": "2026-01-01T00:00:00Z",
                "verb": "get",
            }
        )
        assert _parse_audit_line(line, "default") is None


class TestNodeAllocatable:
    def test_with_data(self) -> None:
        node = Mock(status=Mock(allocatable={"cpu": "4", "memory": "16Gi"}))
        assert _node_allocatable(node) == {"cpu": "4", "memory": "16Gi"}

    def test_no_allocatable(self) -> None:
        node = Mock(status=None)
        assert _node_allocatable(node) == {}


class TestNodeAllocatableCpu:
    def test(self) -> None:
        node = Mock(status=Mock(allocatable={"cpu": "2000m"}))
        assert _node_allocatable_cpu(node) == 2.0  # noqa: PLR2004

    def test_zero(self) -> None:
        node = Mock(status=Mock(allocatable={"cpu": "0"}))
        assert _node_allocatable_cpu(node) == 0.0


class TestNodeAllocatableMemory:
    def test_1gib(self) -> None:
        node = Mock(status=Mock(allocatable={"memory": "1Gi"}))
        assert _node_allocatable_memory_gb(node) == 1.0

    def test_zero(self) -> None:
        node = Mock(status=Mock(allocatable={"memory": "0"}))
        assert _node_allocatable_memory_gb(node) == 0.0
