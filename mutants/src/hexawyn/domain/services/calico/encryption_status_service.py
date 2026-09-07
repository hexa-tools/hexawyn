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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_calico_encryption_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_calico_encryption_status__mutmut)
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


def x_build_calico_encryption_status__mutmut_orig(
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


def x_build_calico_encryption_status__mutmut_1(
    *,
    detection: CalicoDetectionResult,
    config: Mapping[str, object],
) -> CalicoEncryptionStatusResult:
    """Compose the WireGuard status from FelixConfiguration + dataplane mode."""
    if detection.installed:
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


def x_build_calico_encryption_status__mutmut_2(
    *,
    detection: CalicoDetectionResult,
    config: Mapping[str, object],
) -> CalicoEncryptionStatusResult:
    """Compose the WireGuard status from FelixConfiguration + dataplane mode."""
    if not detection.installed:
        return CalicoEncryptionStatusResult(
            installed=None,
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


def x_build_calico_encryption_status__mutmut_3(
    *,
    detection: CalicoDetectionResult,
    config: Mapping[str, object],
) -> CalicoEncryptionStatusResult:
    """Compose the WireGuard status from FelixConfiguration + dataplane mode."""
    if not detection.installed:
        return CalicoEncryptionStatusResult(
            installed=False,
            not_installed_marker=None,
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


def x_build_calico_encryption_status__mutmut_4(
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
            per_node=None,
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


def x_build_calico_encryption_status__mutmut_5(
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
            error=None,
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


def x_build_calico_encryption_status__mutmut_6(
    *,
    detection: CalicoDetectionResult,
    config: Mapping[str, object],
) -> CalicoEncryptionStatusResult:
    """Compose the WireGuard status from FelixConfiguration + dataplane mode."""
    if not detection.installed:
        return CalicoEncryptionStatusResult(
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


def x_build_calico_encryption_status__mutmut_7(
    *,
    detection: CalicoDetectionResult,
    config: Mapping[str, object],
) -> CalicoEncryptionStatusResult:
    """Compose the WireGuard status from FelixConfiguration + dataplane mode."""
    if not detection.installed:
        return CalicoEncryptionStatusResult(
            installed=False,
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


def x_build_calico_encryption_status__mutmut_8(
    *,
    detection: CalicoDetectionResult,
    config: Mapping[str, object],
) -> CalicoEncryptionStatusResult:
    """Compose the WireGuard status from FelixConfiguration + dataplane mode."""
    if not detection.installed:
        return CalicoEncryptionStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
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


def x_build_calico_encryption_status__mutmut_9(
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


def x_build_calico_encryption_status__mutmut_10(
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


def x_build_calico_encryption_status__mutmut_11(
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


def x_build_calico_encryption_status__mutmut_12(
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


def x_build_calico_encryption_status__mutmut_13(
    *,
    detection: CalicoDetectionResult,
    config: Mapping[str, object],
) -> CalicoEncryptionStatusResult:
    """Compose the WireGuard status from FelixConfiguration + dataplane mode."""
    if not detection.installed:
        return CalicoEncryptionStatusResult(
            installed=True,
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


def x_build_calico_encryption_status__mutmut_14(
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

    wireguard_enabled = None
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


def x_build_calico_encryption_status__mutmut_15(
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

    wireguard_enabled = config.get(None)
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


def x_build_calico_encryption_status__mutmut_16(
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

    wireguard_enabled = config.get("XXwireguard_enabledXX")
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


def x_build_calico_encryption_status__mutmut_17(
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

    wireguard_enabled = config.get("WIREGUARD_ENABLED")
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


def x_build_calico_encryption_status__mutmut_18(
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
    enabled_flag = None
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


def x_build_calico_encryption_status__mutmut_19(
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
    enabled_flag = bool(None) if wireguard_enabled is not None else None
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


def x_build_calico_encryption_status__mutmut_20(
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
    enabled_flag = bool(wireguard_enabled) if wireguard_enabled is None else None
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


def x_build_calico_encryption_status__mutmut_21(
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
    per_node = None
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


def x_build_calico_encryption_status__mutmut_22(
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
    per_node = _parse_per_node(None)
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


def x_build_calico_encryption_status__mutmut_23(
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
    per_node = _parse_per_node(config.get(None))
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


def x_build_calico_encryption_status__mutmut_24(
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
    per_node = _parse_per_node(config.get("XXper_nodeXX"))
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


def x_build_calico_encryption_status__mutmut_25(
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
    per_node = _parse_per_node(config.get("PER_NODE"))
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


def x_build_calico_encryption_status__mutmut_26(
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
    summary = None
    return CalicoEncryptionStatusResult(
        installed=True,
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_27(
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
    summary = _summary(None, detection.mode, len(per_node))
    return CalicoEncryptionStatusResult(
        installed=True,
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_28(
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
    summary = _summary(enabled_flag, None, len(per_node))
    return CalicoEncryptionStatusResult(
        installed=True,
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_29(
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
    summary = _summary(enabled_flag, detection.mode, None)
    return CalicoEncryptionStatusResult(
        installed=True,
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_30(
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
    summary = _summary(detection.mode, len(per_node))
    return CalicoEncryptionStatusResult(
        installed=True,
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_31(
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
    summary = _summary(enabled_flag, len(per_node))
    return CalicoEncryptionStatusResult(
        installed=True,
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_32(
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
    summary = _summary(enabled_flag, detection.mode, )
    return CalicoEncryptionStatusResult(
        installed=True,
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_33(
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
        installed=None,
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_34(
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
        wireguard_enabled=None,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_35(
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
        mode=None,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_36(
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
        per_node=None,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_37(
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
        summary=None,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_38(
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
        error=None,
    )


def x_build_calico_encryption_status__mutmut_39(
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
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_40(
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
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_41(
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
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_42(
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
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_43(
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
        summary=summary,
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_44(
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
        error=detection.error,
    )


def x_build_calico_encryption_status__mutmut_45(
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
        )


def x_build_calico_encryption_status__mutmut_46(
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
        installed=False,
        not_installed_marker=None,
        wireguard_enabled=enabled_flag,
        mode=detection.mode,
        per_node=per_node,
        summary=summary,
        error=detection.error,
    )

mutants_x_build_calico_encryption_status__mutmut['_mutmut_orig'] = x_build_calico_encryption_status__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_1'] = x_build_calico_encryption_status__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_2'] = x_build_calico_encryption_status__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_3'] = x_build_calico_encryption_status__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_4'] = x_build_calico_encryption_status__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_5'] = x_build_calico_encryption_status__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_6'] = x_build_calico_encryption_status__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_7'] = x_build_calico_encryption_status__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_8'] = x_build_calico_encryption_status__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_9'] = x_build_calico_encryption_status__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_10'] = x_build_calico_encryption_status__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_11'] = x_build_calico_encryption_status__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_12'] = x_build_calico_encryption_status__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_13'] = x_build_calico_encryption_status__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_14'] = x_build_calico_encryption_status__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_15'] = x_build_calico_encryption_status__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_16'] = x_build_calico_encryption_status__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_17'] = x_build_calico_encryption_status__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_18'] = x_build_calico_encryption_status__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_19'] = x_build_calico_encryption_status__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_20'] = x_build_calico_encryption_status__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_21'] = x_build_calico_encryption_status__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_22'] = x_build_calico_encryption_status__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_23'] = x_build_calico_encryption_status__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_24'] = x_build_calico_encryption_status__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_25'] = x_build_calico_encryption_status__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_26'] = x_build_calico_encryption_status__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_27'] = x_build_calico_encryption_status__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_28'] = x_build_calico_encryption_status__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_29'] = x_build_calico_encryption_status__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_30'] = x_build_calico_encryption_status__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_31'] = x_build_calico_encryption_status__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_32'] = x_build_calico_encryption_status__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_33'] = x_build_calico_encryption_status__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_34'] = x_build_calico_encryption_status__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_35'] = x_build_calico_encryption_status__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_36'] = x_build_calico_encryption_status__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_37'] = x_build_calico_encryption_status__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_38'] = x_build_calico_encryption_status__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_39'] = x_build_calico_encryption_status__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_40'] = x_build_calico_encryption_status__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_41'] = x_build_calico_encryption_status__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_42'] = x_build_calico_encryption_status__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_43'] = x_build_calico_encryption_status__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_44'] = x_build_calico_encryption_status__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_45'] = x_build_calico_encryption_status__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_calico_encryption_status__mutmut['x_build_calico_encryption_status__mutmut_46'] = x_build_calico_encryption_status__mutmut_46 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_per_node__mutmut)
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


def x__parse_per_node__mutmut_orig(raw: object) -> list[CalicoEncryptionNodeStatus]:
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


def x__parse_per_node__mutmut_1(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if isinstance(raw, Sequence):
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


def x__parse_per_node__mutmut_2(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = None
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


def x__parse_per_node__mutmut_3(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if isinstance(entry, Mapping):
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


def x__parse_per_node__mutmut_4(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            break
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


def x__parse_per_node__mutmut_5(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = None
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


def x__parse_per_node__mutmut_6(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = entry.get(None)
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


def x__parse_per_node__mutmut_7(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = entry.get("XXnodeXX")
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


def x__parse_per_node__mutmut_8(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = entry.get("NODE")
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


def x__parse_per_node__mutmut_9(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = entry.get("node")
        if node is not None:
            continue
        enabled = entry.get("wireguard_enabled")
        result.append(
            CalicoEncryptionNodeStatus(
                node=str(node),
                wireguard_enabled=bool(enabled) if enabled is not None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_10(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = entry.get("node")
        if node is None:
            break
        enabled = entry.get("wireguard_enabled")
        result.append(
            CalicoEncryptionNodeStatus(
                node=str(node),
                wireguard_enabled=bool(enabled) if enabled is not None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_11(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = entry.get("node")
        if node is None:
            continue
        enabled = None
        result.append(
            CalicoEncryptionNodeStatus(
                node=str(node),
                wireguard_enabled=bool(enabled) if enabled is not None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_12(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = entry.get("node")
        if node is None:
            continue
        enabled = entry.get(None)
        result.append(
            CalicoEncryptionNodeStatus(
                node=str(node),
                wireguard_enabled=bool(enabled) if enabled is not None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_13(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = entry.get("node")
        if node is None:
            continue
        enabled = entry.get("XXwireguard_enabledXX")
        result.append(
            CalicoEncryptionNodeStatus(
                node=str(node),
                wireguard_enabled=bool(enabled) if enabled is not None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_14(raw: object) -> list[CalicoEncryptionNodeStatus]:
    if not isinstance(raw, Sequence):
        return []
    result: list[CalicoEncryptionNodeStatus] = []
    for entry in raw:
        if not isinstance(entry, Mapping):
            continue
        node = entry.get("node")
        if node is None:
            continue
        enabled = entry.get("WIREGUARD_ENABLED")
        result.append(
            CalicoEncryptionNodeStatus(
                node=str(node),
                wireguard_enabled=bool(enabled) if enabled is not None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_15(raw: object) -> list[CalicoEncryptionNodeStatus]:
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
            None
        )
    return result


def x__parse_per_node__mutmut_16(raw: object) -> list[CalicoEncryptionNodeStatus]:
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
                node=None,
                wireguard_enabled=bool(enabled) if enabled is not None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_17(raw: object) -> list[CalicoEncryptionNodeStatus]:
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
                wireguard_enabled=None,
            )
        )
    return result


def x__parse_per_node__mutmut_18(raw: object) -> list[CalicoEncryptionNodeStatus]:
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
                wireguard_enabled=bool(enabled) if enabled is not None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_19(raw: object) -> list[CalicoEncryptionNodeStatus]:
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
                )
        )
    return result


def x__parse_per_node__mutmut_20(raw: object) -> list[CalicoEncryptionNodeStatus]:
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
                node=str(None),
                wireguard_enabled=bool(enabled) if enabled is not None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_21(raw: object) -> list[CalicoEncryptionNodeStatus]:
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
                wireguard_enabled=bool(None) if enabled is not None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_22(raw: object) -> list[CalicoEncryptionNodeStatus]:
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
                wireguard_enabled=bool(enabled) if enabled is None else False,
            )
        )
    return result


def x__parse_per_node__mutmut_23(raw: object) -> list[CalicoEncryptionNodeStatus]:
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
                wireguard_enabled=bool(enabled) if enabled is not None else True,
            )
        )
    return result

mutants_x__parse_per_node__mutmut['_mutmut_orig'] = x__parse_per_node__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_1'] = x__parse_per_node__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_2'] = x__parse_per_node__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_3'] = x__parse_per_node__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_4'] = x__parse_per_node__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_5'] = x__parse_per_node__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_6'] = x__parse_per_node__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_7'] = x__parse_per_node__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_8'] = x__parse_per_node__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_9'] = x__parse_per_node__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_10'] = x__parse_per_node__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_11'] = x__parse_per_node__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_12'] = x__parse_per_node__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_13'] = x__parse_per_node__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_14'] = x__parse_per_node__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_15'] = x__parse_per_node__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_16'] = x__parse_per_node__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_17'] = x__parse_per_node__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_18'] = x__parse_per_node__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_19'] = x__parse_per_node__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_20'] = x__parse_per_node__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_21'] = x__parse_per_node__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_22'] = x__parse_per_node__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_per_node__mutmut['x__parse_per_node__mutmut_23'] = x__parse_per_node__mutmut_23 # type: ignore # mutmut generated
mutants_x__summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summary__mutmut)
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


def x__summary__mutmut_orig(
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


def x__summary__mutmut_1(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = None
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_2(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "XXenabledXX"
        if wireguard_enabled is True
        else "disabled"
        if wireguard_enabled is False
        else "not configured"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_3(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "ENABLED"
        if wireguard_enabled is True
        else "disabled"
        if wireguard_enabled is False
        else "not configured"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_4(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "enabled"
        if wireguard_enabled is not True
        else "disabled"
        if wireguard_enabled is False
        else "not configured"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_5(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "enabled"
        if wireguard_enabled is False
        else "disabled"
        if wireguard_enabled is False
        else "not configured"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_6(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "enabled"
        if wireguard_enabled is True
        else "XXdisabledXX"
        if wireguard_enabled is False
        else "not configured"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_7(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "enabled"
        if wireguard_enabled is True
        else "DISABLED"
        if wireguard_enabled is False
        else "not configured"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_8(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "enabled"
        if wireguard_enabled is True
        else "disabled"
        if wireguard_enabled is not False
        else "not configured"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_9(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "enabled"
        if wireguard_enabled is True
        else "disabled"
        if wireguard_enabled is True
        else "not configured"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_10(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "enabled"
        if wireguard_enabled is True
        else "disabled"
        if wireguard_enabled is False
        else "XXnot configuredXX"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_11(
    wireguard_enabled: bool | None,
    mode: object | None,
    per_node_count: int,
) -> str:
    state = (
        "enabled"
        if wireguard_enabled is True
        else "disabled"
        if wireguard_enabled is False
        else "NOT CONFIGURED"
    )
    mode_value = getattr(mode, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_12(
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
    mode_value = None
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_13(
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
    mode_value = getattr(None, "value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_14(
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
    mode_value = getattr(mode, None, mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_15(
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
    mode_value = getattr(mode, "value", None)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_16(
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
    mode_value = getattr("value", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_17(
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
    mode_value = getattr(mode, mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_18(
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
    mode_value = getattr(mode, "value", )
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_19(
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
    mode_value = getattr(mode, "XXvalueXX", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_20(
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
    mode_value = getattr(mode, "VALUE", mode)
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else ""
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_21(
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
    suffix = None
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"


def x__summary__mutmut_22(
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
    suffix = f" ({per_node_count} per-node override(s))" if per_node_count else "XXXX"
    return f"WireGuard {state} (dataplane mode: {mode_value}){suffix}"

mutants_x__summary__mutmut['_mutmut_orig'] = x__summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_1'] = x__summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_2'] = x__summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_3'] = x__summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_4'] = x__summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_5'] = x__summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_6'] = x__summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_7'] = x__summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_8'] = x__summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_9'] = x__summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_10'] = x__summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_11'] = x__summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_12'] = x__summary__mutmut_12 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_13'] = x__summary__mutmut_13 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_14'] = x__summary__mutmut_14 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_15'] = x__summary__mutmut_15 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_16'] = x__summary__mutmut_16 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_17'] = x__summary__mutmut_17 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_18'] = x__summary__mutmut_18 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_19'] = x__summary__mutmut_19 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_20'] = x__summary__mutmut_20 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_21'] = x__summary__mutmut_21 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_22'] = x__summary__mutmut_22 # type: ignore # mutmut generated
