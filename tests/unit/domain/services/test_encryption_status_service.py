"""Tests for domain/services/calico/encryption_status_service."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoEncryptionNodeStatus,
    DataplaneMode,
)
from hexawyn.domain.services.calico.encryption_status_service import (
    _parse_per_node,
    _summary,
    build_calico_encryption_status,
)


class TestBuildCalicoEncryptionStatus:
    def _detection(self, **overrides: object) -> CalicoDetectionResult:
        base: dict[str, object] = {
            "installed": True,
            "status": CalicoDetectionStatus.INSTALLED,
            "not_installed_marker": None,
            "version": "v3.26.1",
            "mode": DataplaneMode.IPIP,
            "namespace": "calico-system",
            "tigera_operator": False,
            "enterprise": False,
            "agents": [],
            "total_nodes": 3,
            "ready_agents": 3,
            "degraded_agents": 0,
            "degraded_summary": None,
            "error": None,
        }
        base.update(overrides)
        return CalicoDetectionResult(**base)  # type: ignore[arg-type]

    def test_wireguard_on_full_payload(self) -> None:
        config = {"wireguard_enabled": True, "per_node": []}
        result = build_calico_encryption_status(detection=self._detection(), config=config)
        assert result.installed is True
        assert result.not_installed_marker is None
        assert result.wireguard_enabled is True
        assert result.mode == DataplaneMode.IPIP
        assert result.per_node == []
        assert result.summary == "WireGuard enabled (dataplane mode: IPIP)"
        assert result.error is None

    def test_wireguard_off_summary(self) -> None:
        config = {"wireguard_enabled": False, "per_node": []}
        result = build_calico_encryption_status(detection=self._detection(), config=config)
        assert result.wireguard_enabled is False
        assert result.summary == "WireGuard disabled (dataplane mode: IPIP)"

    def test_no_configuration_summary_not_configured(self) -> None:
        result = build_calico_encryption_status(detection=self._detection(), config={})
        assert result.wireguard_enabled is None
        assert result.summary == "WireGuard not configured (dataplane mode: IPIP)"

    def test_per_node_override_suffix(self) -> None:
        config = {
            "wireguard_enabled": True,
            "per_node": [
                {"node": "node-1", "wireguard_enabled": True},
                {"node": "node-2", "wireguard_enabled": False},
            ],
        }
        result = build_calico_encryption_status(detection=self._detection(), config=config)
        assert result.per_node == [
            CalicoEncryptionNodeStatus(node="node-1", wireguard_enabled=True),
            CalicoEncryptionNodeStatus(node="node-2", wireguard_enabled=False),
        ]
        assert result.summary == (
            "WireGuard enabled (dataplane mode: IPIP) (2 per-node override(s))"
        )

    def test_per_node_without_flag_defaults_false(self) -> None:
        config = {
            "wireguard_enabled": True,
            "per_node": [{"node": "node-1"}],
        }
        result = build_calico_encryption_status(detection=self._detection(), config=config)
        assert result.per_node[0].wireguard_enabled is False

    def test_per_node_skips_junk_entries(self) -> None:
        config = {
            "wireguard_enabled": True,
            "per_node": [
                "not-a-mapping",
                {"wireguard_enabled": True},
                {"node": "node-1", "wireguard_enabled": True},
            ],
        }
        result = build_calico_encryption_status(detection=self._detection(), config=config)
        assert result.per_node == [
            CalicoEncryptionNodeStatus(node="node-1", wireguard_enabled=True)
        ]

    def test_not_installed_full_payload(self) -> None:
        detection = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            total_nodes=0,
            ready_agents=0,
            mode=DataplaneMode.UNKNOWN,
            error="kube api unreachable",
        )
        result = build_calico_encryption_status(detection=detection, config={})
        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.wireguard_enabled is None
        assert result.mode is None
        assert result.per_node == []
        assert result.summary is None
        assert result.error == "kube api unreachable"

    def test_installed_forwards_detection_error(self) -> None:
        detection = self._detection(error="no felix config")
        result = build_calico_encryption_status(detection=detection, config={})
        assert result.installed is True
        assert result.error == "no felix config"

    def test_unknown_mode_value_in_summary(self) -> None:
        detection = self._detection(mode=DataplaneMode.UNKNOWN)
        result = build_calico_encryption_status(
            detection=detection, config={"wireguard_enabled": True}
        )
        assert result.summary == "WireGuard enabled (dataplane mode: UNKNOWN)"


class TestParsePerNodeDirect:
    def test_non_sequence_returns_empty(self) -> None:
        assert _parse_per_node(None) == []
        assert _parse_per_node("nope") == []

    def test_empty_sequence(self) -> None:
        assert _parse_per_node([]) == []

    def test_non_mapping_entry_skipped(self) -> None:
        assert _parse_per_node(["junk", {"node": "n1"}]) == [
            CalicoEncryptionNodeStatus(node="n1", wireguard_enabled=False)
        ]

    def test_missing_node_skipped(self) -> None:
        assert _parse_per_node([{"wireguard_enabled": True}]) == []

    def test_enabled_true(self) -> None:
        assert _parse_per_node([{"node": "n1", "wireguard_enabled": True}]) == [
            CalicoEncryptionNodeStatus(node="n1", wireguard_enabled=True)
        ]

    def test_enabled_false(self) -> None:
        assert _parse_per_node([{"node": "n1", "wireguard_enabled": False}]) == [
            CalicoEncryptionNodeStatus(node="n1", wireguard_enabled=False)
        ]

    def test_node_non_string_coerced(self) -> None:
        assert _parse_per_node([{"node": 7, "wireguard_enabled": True}]) == [
            CalicoEncryptionNodeStatus(node="7", wireguard_enabled=True)
        ]


class TestSummaryDirect:
    def test_enabled_no_overrides(self) -> None:
        assert _summary(True, DataplaneMode.EBPF, 0) == "WireGuard enabled (dataplane mode: eBPF)"

    def test_disabled_no_overrides(self) -> None:
        assert _summary(False, DataplaneMode.IPIP, 0) == "WireGuard disabled (dataplane mode: IPIP)"

    def test_not_configured(self) -> None:
        assert _summary(None, DataplaneMode.UNKNOWN, 0) == (
            "WireGuard not configured (dataplane mode: UNKNOWN)"
        )

    def test_single_override_suffix(self) -> None:
        assert _summary(True, DataplaneMode.IPIP, 1) == (
            "WireGuard enabled (dataplane mode: IPIP) (1 per-node override(s))"
        )

    def test_multiple_overrides_suffix(self) -> None:
        assert _summary(False, DataplaneMode.IPIP, 3) == (
            "WireGuard disabled (dataplane mode: IPIP) (3 per-node override(s))"
        )

    def test_mode_passthrough_string(self) -> None:
        assert _summary(True, "custom-mode", 0) == "WireGuard enabled (dataplane mode: custom-mode)"
