"""Pure Cilium wire-encryption status building — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumEncryptionStatusResult

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"
_UNKNOWN_NOTE = "Cilium encryption configuration could not be established"

_ENCRYPTION_MODES = ("wireguard", "ipsec")


def deduce_encryption_mode(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def build_encryption_status(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "disabled"
        encrypted_nodes = 0
    elif mode in _ENCRYPTION_MODES:
        status = "enabled"
    else:
        status = "unknown"
    coverage = f"{encrypted_nodes}/{total_nodes}" if total_nodes > 0 else None
    return CiliumEncryptionStatusResult(
        installed=True,
        status=status,
        mode=mode,
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def not_installed_encryption_status() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def unknown_encryption_status() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )
