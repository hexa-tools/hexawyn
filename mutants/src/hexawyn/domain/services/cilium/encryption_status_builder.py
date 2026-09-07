"""Pure Cilium wire-encryption status building — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumEncryptionStatusResult

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"
_UNKNOWN_NOTE = "Cilium encryption configuration could not be established"

_ENCRYPTION_MODES = ("wireguard", "ipsec")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_deduce_encryption_mode__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_deduce_encryption_mode__mutmut)
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


def x_deduce_encryption_mode__mutmut_orig(encryption_type: str | None, encryption_enabled: str | None) -> str:
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


def x_deduce_encryption_mode__mutmut_1(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None or encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_2(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is not None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_3(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is not None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_4(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "XXUNKNOWNXX"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_5(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "unknown"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_6(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = None
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_7(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().upper()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_8(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type and "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_9(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "XXXX").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_10(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value not in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_11(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = None
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_12(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().upper() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_13(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled and "").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_14(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "XXXX").strip().lower() in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_15(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() not in ("true", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_16(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("XXtrueXX", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_17(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("TRUE", "1", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_18(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "XX1XX", "yes", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_19(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "XXyesXX", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_20(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "YES", "enabled")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_21(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "XXenabledXX")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_22(encryption_type: str | None, encryption_enabled: str | None) -> str:
    """Observed encryption mode from cilium-config keys (never inferred).

    ``encryption-type`` wireguard/ipsec wins; an empty/unset value with
    encryption disabled maps to ``none``; anything else stays ``UNKNOWN``.
    """
    if encryption_type is None and encryption_enabled is None:
        return "UNKNOWN"
    value = (encryption_type or "").strip().lower()
    if value in _ENCRYPTION_MODES:
        return value
    enabled = (encryption_enabled or "").strip().lower() in ("true", "1", "yes", "ENABLED")
    if enabled:
        return "UNKNOWN"
    return "none"


def x_deduce_encryption_mode__mutmut_23(encryption_type: str | None, encryption_enabled: str | None) -> str:
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
        return "XXUNKNOWNXX"
    return "none"


def x_deduce_encryption_mode__mutmut_24(encryption_type: str | None, encryption_enabled: str | None) -> str:
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
        return "unknown"
    return "none"


def x_deduce_encryption_mode__mutmut_25(encryption_type: str | None, encryption_enabled: str | None) -> str:
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
    return "XXnoneXX"


def x_deduce_encryption_mode__mutmut_26(encryption_type: str | None, encryption_enabled: str | None) -> str:
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
    return "NONE"

mutants_x_deduce_encryption_mode__mutmut['_mutmut_orig'] = x_deduce_encryption_mode__mutmut_orig # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_1'] = x_deduce_encryption_mode__mutmut_1 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_2'] = x_deduce_encryption_mode__mutmut_2 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_3'] = x_deduce_encryption_mode__mutmut_3 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_4'] = x_deduce_encryption_mode__mutmut_4 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_5'] = x_deduce_encryption_mode__mutmut_5 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_6'] = x_deduce_encryption_mode__mutmut_6 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_7'] = x_deduce_encryption_mode__mutmut_7 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_8'] = x_deduce_encryption_mode__mutmut_8 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_9'] = x_deduce_encryption_mode__mutmut_9 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_10'] = x_deduce_encryption_mode__mutmut_10 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_11'] = x_deduce_encryption_mode__mutmut_11 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_12'] = x_deduce_encryption_mode__mutmut_12 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_13'] = x_deduce_encryption_mode__mutmut_13 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_14'] = x_deduce_encryption_mode__mutmut_14 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_15'] = x_deduce_encryption_mode__mutmut_15 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_16'] = x_deduce_encryption_mode__mutmut_16 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_17'] = x_deduce_encryption_mode__mutmut_17 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_18'] = x_deduce_encryption_mode__mutmut_18 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_19'] = x_deduce_encryption_mode__mutmut_19 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_20'] = x_deduce_encryption_mode__mutmut_20 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_21'] = x_deduce_encryption_mode__mutmut_21 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_22'] = x_deduce_encryption_mode__mutmut_22 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_23'] = x_deduce_encryption_mode__mutmut_23 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_24'] = x_deduce_encryption_mode__mutmut_24 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_25'] = x_deduce_encryption_mode__mutmut_25 # type: ignore # mutmut generated
mutants_x_deduce_encryption_mode__mutmut['x_deduce_encryption_mode__mutmut_26'] = x_deduce_encryption_mode__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_encryption_status__mutmut)
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


def x_build_encryption_status__mutmut_orig(
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


def x_build_encryption_status__mutmut_1(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode != "none":
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


def x_build_encryption_status__mutmut_2(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "XXnoneXX":
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


def x_build_encryption_status__mutmut_3(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "NONE":
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


def x_build_encryption_status__mutmut_4(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = None
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


def x_build_encryption_status__mutmut_5(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "XXdisabledXX"
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


def x_build_encryption_status__mutmut_6(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "DISABLED"
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


def x_build_encryption_status__mutmut_7(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "disabled"
        encrypted_nodes = None
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


def x_build_encryption_status__mutmut_8(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "disabled"
        encrypted_nodes = 1
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


def x_build_encryption_status__mutmut_9(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "disabled"
        encrypted_nodes = 0
    elif mode not in _ENCRYPTION_MODES:
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


def x_build_encryption_status__mutmut_10(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "disabled"
        encrypted_nodes = 0
    elif mode in _ENCRYPTION_MODES:
        status = None
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


def x_build_encryption_status__mutmut_11(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "disabled"
        encrypted_nodes = 0
    elif mode in _ENCRYPTION_MODES:
        status = "XXenabledXX"
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


def x_build_encryption_status__mutmut_12(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "disabled"
        encrypted_nodes = 0
    elif mode in _ENCRYPTION_MODES:
        status = "ENABLED"
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


def x_build_encryption_status__mutmut_13(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "disabled"
        encrypted_nodes = 0
    elif mode in _ENCRYPTION_MODES:
        status = "enabled"
    else:
        status = None
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


def x_build_encryption_status__mutmut_14(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "disabled"
        encrypted_nodes = 0
    elif mode in _ENCRYPTION_MODES:
        status = "enabled"
    else:
        status = "XXunknownXX"
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


def x_build_encryption_status__mutmut_15(
    mode: str, encrypted_nodes: int, total_nodes: int
) -> CiliumEncryptionStatusResult:
    """Build the observed encryption status with node coverage."""
    if mode == "none":
        status = "disabled"
        encrypted_nodes = 0
    elif mode in _ENCRYPTION_MODES:
        status = "enabled"
    else:
        status = "UNKNOWN"
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


def x_build_encryption_status__mutmut_16(
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
    coverage = None
    return CiliumEncryptionStatusResult(
        installed=True,
        status=status,
        mode=mode,
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_17(
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
    coverage = f"{encrypted_nodes}/{total_nodes}" if total_nodes >= 0 else None
    return CiliumEncryptionStatusResult(
        installed=True,
        status=status,
        mode=mode,
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_18(
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
    coverage = f"{encrypted_nodes}/{total_nodes}" if total_nodes > 1 else None
    return CiliumEncryptionStatusResult(
        installed=True,
        status=status,
        mode=mode,
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_19(
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
        installed=None,
        status=status,
        mode=mode,
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_20(
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
        status=None,
        mode=mode,
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_21(
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
        mode=None,
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_22(
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
        encrypted_nodes=None,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_23(
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
        total_nodes=None,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_24(
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
        coverage=None,
        note=None,
    )


def x_build_encryption_status__mutmut_25(
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
        status=status,
        mode=mode,
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_26(
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
        mode=mode,
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_27(
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
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_28(
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
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_29(
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
        coverage=coverage,
        note=None,
    )


def x_build_encryption_status__mutmut_30(
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
        note=None,
    )


def x_build_encryption_status__mutmut_31(
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
        )


def x_build_encryption_status__mutmut_32(
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
        installed=False,
        status=status,
        mode=mode,
        encrypted_nodes=encrypted_nodes,
        total_nodes=total_nodes,
        coverage=coverage,
        note=None,
    )

mutants_x_build_encryption_status__mutmut['_mutmut_orig'] = x_build_encryption_status__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_1'] = x_build_encryption_status__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_2'] = x_build_encryption_status__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_3'] = x_build_encryption_status__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_4'] = x_build_encryption_status__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_5'] = x_build_encryption_status__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_6'] = x_build_encryption_status__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_7'] = x_build_encryption_status__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_8'] = x_build_encryption_status__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_9'] = x_build_encryption_status__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_10'] = x_build_encryption_status__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_11'] = x_build_encryption_status__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_12'] = x_build_encryption_status__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_13'] = x_build_encryption_status__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_14'] = x_build_encryption_status__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_15'] = x_build_encryption_status__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_16'] = x_build_encryption_status__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_17'] = x_build_encryption_status__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_18'] = x_build_encryption_status__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_19'] = x_build_encryption_status__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_20'] = x_build_encryption_status__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_21'] = x_build_encryption_status__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_22'] = x_build_encryption_status__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_23'] = x_build_encryption_status__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_24'] = x_build_encryption_status__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_25'] = x_build_encryption_status__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_26'] = x_build_encryption_status__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_27'] = x_build_encryption_status__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_28'] = x_build_encryption_status__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_29'] = x_build_encryption_status__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_30'] = x_build_encryption_status__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_31'] = x_build_encryption_status__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_encryption_status__mutmut['x_build_encryption_status__mutmut_32'] = x_build_encryption_status__mutmut_32 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_not_installed_encryption_status__mutmut)
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


def x_not_installed_encryption_status__mutmut_orig() -> CiliumEncryptionStatusResult:
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


def x_not_installed_encryption_status__mutmut_1() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=None,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_2() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status=None,
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_3() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode=None,
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_4() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=None,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_5() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=None,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_6() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=None,
    )


def x_not_installed_encryption_status__mutmut_7() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_8() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_9() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_10() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="UNKNOWN",
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_11() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_12() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_13() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        )


def x_not_installed_encryption_status__mutmut_14() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_15() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="XXnot_installedXX",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_16() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="NOT_INSTALLED",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_17() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="XXUNKNOWNXX",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_18() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="unknown",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_19() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=1,
        total_nodes=0,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_encryption_status__mutmut_20() -> CiliumEncryptionStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated encryption mode."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="not_installed",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=1,
        coverage=None,
        note=_NOT_INSTALLED_NOTE,
    )

mutants_x_not_installed_encryption_status__mutmut['_mutmut_orig'] = x_not_installed_encryption_status__mutmut_orig # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_1'] = x_not_installed_encryption_status__mutmut_1 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_2'] = x_not_installed_encryption_status__mutmut_2 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_3'] = x_not_installed_encryption_status__mutmut_3 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_4'] = x_not_installed_encryption_status__mutmut_4 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_5'] = x_not_installed_encryption_status__mutmut_5 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_6'] = x_not_installed_encryption_status__mutmut_6 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_7'] = x_not_installed_encryption_status__mutmut_7 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_8'] = x_not_installed_encryption_status__mutmut_8 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_9'] = x_not_installed_encryption_status__mutmut_9 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_10'] = x_not_installed_encryption_status__mutmut_10 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_11'] = x_not_installed_encryption_status__mutmut_11 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_12'] = x_not_installed_encryption_status__mutmut_12 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_13'] = x_not_installed_encryption_status__mutmut_13 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_14'] = x_not_installed_encryption_status__mutmut_14 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_15'] = x_not_installed_encryption_status__mutmut_15 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_16'] = x_not_installed_encryption_status__mutmut_16 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_17'] = x_not_installed_encryption_status__mutmut_17 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_18'] = x_not_installed_encryption_status__mutmut_18 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_19'] = x_not_installed_encryption_status__mutmut_19 # type: ignore # mutmut generated
mutants_x_not_installed_encryption_status__mutmut['x_not_installed_encryption_status__mutmut_20'] = x_not_installed_encryption_status__mutmut_20 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_unknown_encryption_status__mutmut)
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


def x_unknown_encryption_status__mutmut_orig() -> CiliumEncryptionStatusResult:
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


def x_unknown_encryption_status__mutmut_1() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=None,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_2() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status=None,
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_3() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode=None,
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_4() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=None,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_5() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=None,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_6() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=None,
    )


def x_unknown_encryption_status__mutmut_7() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_8() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_9() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_10() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="UNKNOWN",
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_11() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_12() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_13() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        )


def x_unknown_encryption_status__mutmut_14() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=False,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_15() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="XXunknownXX",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_16() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="UNKNOWN",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_17() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="XXUNKNOWNXX",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_18() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="unknown",
        encrypted_nodes=0,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_19() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=1,
        total_nodes=0,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )


def x_unknown_encryption_status__mutmut_20() -> CiliumEncryptionStatusResult:
    """Cilium installed but encryption state could not be established."""
    return CiliumEncryptionStatusResult(
        installed=True,
        status="unknown",
        mode="UNKNOWN",
        encrypted_nodes=0,
        total_nodes=1,
        coverage=None,
        note=_UNKNOWN_NOTE,
    )

mutants_x_unknown_encryption_status__mutmut['_mutmut_orig'] = x_unknown_encryption_status__mutmut_orig # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_1'] = x_unknown_encryption_status__mutmut_1 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_2'] = x_unknown_encryption_status__mutmut_2 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_3'] = x_unknown_encryption_status__mutmut_3 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_4'] = x_unknown_encryption_status__mutmut_4 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_5'] = x_unknown_encryption_status__mutmut_5 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_6'] = x_unknown_encryption_status__mutmut_6 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_7'] = x_unknown_encryption_status__mutmut_7 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_8'] = x_unknown_encryption_status__mutmut_8 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_9'] = x_unknown_encryption_status__mutmut_9 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_10'] = x_unknown_encryption_status__mutmut_10 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_11'] = x_unknown_encryption_status__mutmut_11 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_12'] = x_unknown_encryption_status__mutmut_12 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_13'] = x_unknown_encryption_status__mutmut_13 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_14'] = x_unknown_encryption_status__mutmut_14 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_15'] = x_unknown_encryption_status__mutmut_15 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_16'] = x_unknown_encryption_status__mutmut_16 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_17'] = x_unknown_encryption_status__mutmut_17 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_18'] = x_unknown_encryption_status__mutmut_18 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_19'] = x_unknown_encryption_status__mutmut_19 # type: ignore # mutmut generated
mutants_x_unknown_encryption_status__mutmut['x_unknown_encryption_status__mutmut_20'] = x_unknown_encryption_status__mutmut_20 # type: ignore # mutmut generated
