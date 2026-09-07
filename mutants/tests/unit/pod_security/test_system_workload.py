"""Unit tests for is_known_system_daemonset — Edge Cases 1 & 4: a DaemonSet
pod with a legitimate hostPID (e.g. node-exporter) is still reported at its
real severity, but annotated as an expected system workload."""

from __future__ import annotations


class TestIsKnownSystemDaemonset:
    def test_known_daemonset_name_fragment_matches(self) -> None:
        from hexawyn.domain.services.pod_security.system_workload import (
            is_known_system_daemonset,
        )

        result = is_known_system_daemonset(
            owner_kind="DaemonSet",
            pod_name="node-exporter-abc123",
            known_name_fragments=("node-exporter", "kube-proxy"),
        )

        assert result is True

    def test_non_daemonset_owner_is_never_a_system_workload(self) -> None:
        from hexawyn.domain.services.pod_security.system_workload import (
            is_known_system_daemonset,
        )

        result = is_known_system_daemonset(
            owner_kind="ReplicaSet",
            pod_name="node-exporter-abc123",
            known_name_fragments=("node-exporter",),
        )

        assert result is False

    def test_daemonset_with_unrecognized_name_is_not_a_system_workload(self) -> None:
        from hexawyn.domain.services.pod_security.system_workload import (
            is_known_system_daemonset,
        )

        result = is_known_system_daemonset(
            owner_kind="DaemonSet",
            pod_name="custom-agent-abc123",
            known_name_fragments=("node-exporter", "kube-proxy"),
        )

        assert result is False

    def test_no_owner_is_not_a_system_workload(self) -> None:
        from hexawyn.domain.services.pod_security.system_workload import (
            is_known_system_daemonset,
        )

        result = is_known_system_daemonset(
            owner_kind=None,
            pod_name="node-exporter-abc123",
            known_name_fragments=("node-exporter",),
        )

        assert result is False
