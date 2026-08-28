"""Pure Calico WireGuard encryption status — no infrastructure imports.

Combines the observed FelixConfiguration (cluster WireGuard flag + per-node
values) with the dataplane mode. Encryption is never invented: it reflects only
what FelixConfiguration reports; when no configuration is observed the flag is
reported ``None`` (not a fabricated enabled/disabled).
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoDetectionResult,
    CalicoEncryptionNodeStatus,
    CalicoEncryptionStatusResult,
)


def build_calico_encryption_status(
    *,
    detection: CalicoDetectionResult,
    config: Mapping[str, object],
) -> CalicoEncryptionStatusResult:
    """Compose the WireGuard status from FelixConfiguration + dataplane mode."""
    if not detection.installed:
        return CalicoEncryptionStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            wireguard_enabled=None,
            mode=None,
            per_node=[],
            summary=None,
            error=detection.error,
        )

    wireguard_enabled = config.get("wireguard_enabled")
    enabled_flag = bool(wireguard_enabled) if wireguard_enabled is not None else None
    per_node = _parse_per_node(config.get("per_node"))
    summary = _summary(enabled_flag, detection.mode, len(per_node))
    return CalicoEncryptionStatusResult(
        installed=True,
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def _parse_per_node(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = entry.get("node")
        if node is None:
            continue
        enabled = entry.get("wireguard_enabled")
        result.append(
            CalicoEncryptionNodeStatus(
                node=str(node),
                wireguard_enabled=bool(enabled) if enabled is not None else False,
            )
        )
    return result


def _summary(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "enabled"
        if wireguard_enabled is True
        else "disabled"
        if wireguard_enabled is False
        else "not configured"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"
