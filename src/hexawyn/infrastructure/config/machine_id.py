"""Machine fingerprint — hardware-bound identity, persisted across restarts.

Cross-platform: Linux (/etc/machine-id), Windows (MachineGuid registry),
macOS (IOPlatformUUID). Falls back to hostname + MAC + architecture.

The fingerprint is stored in ~/.hexawyn/.machine_id (chmod 600) and
re-validated on every call. Same hardware → same fingerprint.
"""

from __future__ import annotations

import hashlib
import platform
import socket
import uuid
from pathlib import Path

MACHINE_ID_PATH = Path.home() / ".hexawyn" / ".machine_id"


def _windows_machine_guid() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def _macos_platform_uuid() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPlatformExpertDevice"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        for line in result.stdout.splitlines():
            if "IOPlatformUUID" in line:
                parts = line.strip().split('"')
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def _linux_machine_id() -> str | None:
    for p in ("/etc/machine-id", "/var/lib/dbus/machine-id"):
        path = Path(p)
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    return None


def _hardware_fingerprint() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "Windows":
        guid = _windows_machine_guid()
        if guid:
            parts.append(guid)
    elif system == "Darwin":
        puuid = _macos_platform_uuid()
        if puuid:
            parts.append(puuid)
    else:
        mid = _linux_machine_id()
        if mid:
            parts.append(mid)

    parts.append(platform.node() or socket.gethostname())

    try:
        parts.append(str(uuid.getnode()))
    except Exception:
        pass

    parts.append(platform.machine())
    parts.append(system)

    combined = "|".join(parts)
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def _read_stored() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="utf-8").strip().split("\n")[0]
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def _validate_or_repair(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def get_machine_id() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def get_machine_id_short() -> str:
    """Return first 12 chars of the fingerprint for display/logging."""
    return get_machine_id()[:12]
