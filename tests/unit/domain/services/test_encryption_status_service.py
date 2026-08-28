"""Tests for domain/services/calico/encryption_status_service."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    DataplaneMode,
)
from hexawyn.domain.services.calico.encryption_status_service import (
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

    def test_wireguard_on(self) -> None:
        config = {"wireguard_enabled": True, "per_node": []}
        result = build_calico_encryption_status(detection=self._detection(), config=config)
        assert result.installed is True
        assert result.wireguard_enabled is True
        assert result.mode == DataplaneMode.IPIP

    def test_wireguard_off(self) -> None:
        config = {"wireguard_enabled": False, "per_node": []}
        result = build_calico_encryption_status(detection=self._detection(), config=config)
        assert result.wireguard_enabled is False

    def test_no_configuration_defaults_as_is(self) -> None:
        result = build_calico_encryption_status(detection=self._detection(), config={})
        assert result.wireguard_enabled is None

    def test_per_node_observed(self) -> None:
        config = {
            "wireguard_enabled": True,
            "per_node": [
                {"node": "node-1", "wireguard_enabled": True},
                {"node": "node-2", "wireguard_enabled": False},
            ],
        }
        result = build_calico_encryption_status(detection=self._detection(), config=config)
        assert [n.node for n in result.per_node] == ["node-1", "node-2"]
        assert result.per_node[1].wireguard_enabled is False

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
        assert [n.node for n in result.per_node] == ["node-1"]

    def test_not_installed(self) -> None:
        detection = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            total_nodes=0,
            ready_agents=0,
            mode=DataplaneMode.UNKNOWN,
        )
        result = build_calico_encryption_status(detection=detection, config={})
        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.wireguard_enabled is None

    def test_summary_reflects_state(self) -> None:
        config = {"wireguard_enabled": True, "per_node": []}
        result = build_calico_encryption_status(detection=self._detection(), config=config)
        assert result.summary is not None
        assert "WireGuard" in result.summary
