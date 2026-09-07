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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__windows_machine_guid__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__windows_machine_guid__mutmut)
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


def x__windows_machine_guid__mutmut_orig() -> str | None:
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


def x__windows_machine_guid__mutmut_1() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = None
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_2() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            None,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_3() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            None,
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_4() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_5() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_6() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"XXSOFTWARE\Microsoft\CryptographyXX",
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_7() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"software\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_8() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\MICROSOFT\CRYPTOGRAPHY",
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_9() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = None  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_10() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(None, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_11() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, None)  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_12() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx("MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_13() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, )  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_14() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, "XXMachineGuidXX")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_15() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, "machineguid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_16() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, "MACHINEGUID")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_17() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(None)  # type: ignore[attr-defined]
        return str(value)
    except Exception:
        return None


def x__windows_machine_guid__mutmut_18() -> str | None:
    """Read MachineGuid from Windows registry."""
    try:
        import winreg

        key = winreg.OpenKey(  # type: ignore[attr-defined]
            winreg.HKEY_LOCAL_MACHINE,  # type: ignore[attr-defined]
            r"SOFTWARE\Microsoft\Cryptography",
        )
        value, _ = winreg.QueryValueEx(key, "MachineGuid")  # type: ignore[attr-defined]
        winreg.CloseKey(key)  # type: ignore[attr-defined]
        return str(None)
    except Exception:
        return None

mutants_x__windows_machine_guid__mutmut['_mutmut_orig'] = x__windows_machine_guid__mutmut_orig # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_1'] = x__windows_machine_guid__mutmut_1 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_2'] = x__windows_machine_guid__mutmut_2 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_3'] = x__windows_machine_guid__mutmut_3 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_4'] = x__windows_machine_guid__mutmut_4 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_5'] = x__windows_machine_guid__mutmut_5 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_6'] = x__windows_machine_guid__mutmut_6 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_7'] = x__windows_machine_guid__mutmut_7 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_8'] = x__windows_machine_guid__mutmut_8 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_9'] = x__windows_machine_guid__mutmut_9 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_10'] = x__windows_machine_guid__mutmut_10 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_11'] = x__windows_machine_guid__mutmut_11 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_12'] = x__windows_machine_guid__mutmut_12 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_13'] = x__windows_machine_guid__mutmut_13 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_14'] = x__windows_machine_guid__mutmut_14 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_15'] = x__windows_machine_guid__mutmut_15 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_16'] = x__windows_machine_guid__mutmut_16 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_17'] = x__windows_machine_guid__mutmut_17 # type: ignore # mutmut generated
mutants_x__windows_machine_guid__mutmut['x__windows_machine_guid__mutmut_18'] = x__windows_machine_guid__mutmut_18 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__macos_platform_uuid__mutmut)
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


def x__macos_platform_uuid__mutmut_orig() -> str | None:
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


def x__macos_platform_uuid__mutmut_1() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = None
        for line in result.stdout.splitlines():
            if "IOPlatformUUID" in line:
                parts = line.strip().split('"')
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_2() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            None,
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


def x__macos_platform_uuid__mutmut_3() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPlatformExpertDevice"],
            capture_output=None,
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


def x__macos_platform_uuid__mutmut_4() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPlatformExpertDevice"],
            capture_output=True,
            text=None,
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


def x__macos_platform_uuid__mutmut_5() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPlatformExpertDevice"],
            capture_output=True,
            text=True,
            timeout=None,
        )
        for line in result.stdout.splitlines():
            if "IOPlatformUUID" in line:
                parts = line.strip().split('"')
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_6() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
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


def x__macos_platform_uuid__mutmut_7() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPlatformExpertDevice"],
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


def x__macos_platform_uuid__mutmut_8() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPlatformExpertDevice"],
            capture_output=True,
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


def x__macos_platform_uuid__mutmut_9() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPlatformExpertDevice"],
            capture_output=True,
            text=True,
            )
        for line in result.stdout.splitlines():
            if "IOPlatformUUID" in line:
                parts = line.strip().split('"')
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_10() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["XXioregXX", "-d2", "-c", "IOPlatformExpertDevice"],
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


def x__macos_platform_uuid__mutmut_11() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["IOREG", "-d2", "-c", "IOPlatformExpertDevice"],
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


def x__macos_platform_uuid__mutmut_12() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "XX-d2XX", "-c", "IOPlatformExpertDevice"],
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


def x__macos_platform_uuid__mutmut_13() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-D2", "-c", "IOPlatformExpertDevice"],
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


def x__macos_platform_uuid__mutmut_14() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "XX-cXX", "IOPlatformExpertDevice"],
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


def x__macos_platform_uuid__mutmut_15() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-C", "IOPlatformExpertDevice"],
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


def x__macos_platform_uuid__mutmut_16() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "XXIOPlatformExpertDeviceXX"],
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


def x__macos_platform_uuid__mutmut_17() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "ioplatformexpertdevice"],
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


def x__macos_platform_uuid__mutmut_18() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPLATFORMEXPERTDEVICE"],
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


def x__macos_platform_uuid__mutmut_19() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPlatformExpertDevice"],
            capture_output=False,
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


def x__macos_platform_uuid__mutmut_20() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPlatformExpertDevice"],
            capture_output=True,
            text=False,
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


def x__macos_platform_uuid__mutmut_21() -> str | None:
    """Read IOPlatformUUID via ioreg on macOS."""
    try:
        import subprocess

        result = subprocess.run(
            ["ioreg", "-d2", "-c", "IOPlatformExpertDevice"],
            capture_output=True,
            text=True,
            timeout=6,
        )
        for line in result.stdout.splitlines():
            if "IOPlatformUUID" in line:
                parts = line.strip().split('"')
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_22() -> str | None:
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
            if "XXIOPlatformUUIDXX" in line:
                parts = line.strip().split('"')
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_23() -> str | None:
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
            if "ioplatformuuid" in line:
                parts = line.strip().split('"')
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_24() -> str | None:
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
            if "IOPLATFORMUUID" in line:
                parts = line.strip().split('"')
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_25() -> str | None:
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
            if "IOPlatformUUID" not in line:
                parts = line.strip().split('"')
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_26() -> str | None:
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
                parts = None
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_27() -> str | None:
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
                parts = line.strip().split(None)
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_28() -> str | None:
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
                parts = line.strip().split('XX"XX')
                if len(parts) >= 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_29() -> str | None:
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
                if len(parts) > 3:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_30() -> str | None:
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
                if len(parts) >= 4:  # noqa: PLR2004
                    return parts[-2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_31() -> str | None:
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
                    return parts[+2]
    except Exception:
        pass
    return None


def x__macos_platform_uuid__mutmut_32() -> str | None:
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
                    return parts[-3]
    except Exception:
        pass
    return None

mutants_x__macos_platform_uuid__mutmut['_mutmut_orig'] = x__macos_platform_uuid__mutmut_orig # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_1'] = x__macos_platform_uuid__mutmut_1 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_2'] = x__macos_platform_uuid__mutmut_2 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_3'] = x__macos_platform_uuid__mutmut_3 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_4'] = x__macos_platform_uuid__mutmut_4 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_5'] = x__macos_platform_uuid__mutmut_5 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_6'] = x__macos_platform_uuid__mutmut_6 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_7'] = x__macos_platform_uuid__mutmut_7 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_8'] = x__macos_platform_uuid__mutmut_8 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_9'] = x__macos_platform_uuid__mutmut_9 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_10'] = x__macos_platform_uuid__mutmut_10 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_11'] = x__macos_platform_uuid__mutmut_11 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_12'] = x__macos_platform_uuid__mutmut_12 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_13'] = x__macos_platform_uuid__mutmut_13 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_14'] = x__macos_platform_uuid__mutmut_14 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_15'] = x__macos_platform_uuid__mutmut_15 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_16'] = x__macos_platform_uuid__mutmut_16 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_17'] = x__macos_platform_uuid__mutmut_17 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_18'] = x__macos_platform_uuid__mutmut_18 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_19'] = x__macos_platform_uuid__mutmut_19 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_20'] = x__macos_platform_uuid__mutmut_20 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_21'] = x__macos_platform_uuid__mutmut_21 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_22'] = x__macos_platform_uuid__mutmut_22 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_23'] = x__macos_platform_uuid__mutmut_23 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_24'] = x__macos_platform_uuid__mutmut_24 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_25'] = x__macos_platform_uuid__mutmut_25 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_26'] = x__macos_platform_uuid__mutmut_26 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_27'] = x__macos_platform_uuid__mutmut_27 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_28'] = x__macos_platform_uuid__mutmut_28 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_29'] = x__macos_platform_uuid__mutmut_29 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_30'] = x__macos_platform_uuid__mutmut_30 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_31'] = x__macos_platform_uuid__mutmut_31 # type: ignore # mutmut generated
mutants_x__macos_platform_uuid__mutmut['x__macos_platform_uuid__mutmut_32'] = x__macos_platform_uuid__mutmut_32 # type: ignore # mutmut generated
mutants_x__linux_machine_id__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__linux_machine_id__mutmut)
def _linux_machine_id() -> str | None:
    for p in ("/etc/machine-id", "/var/lib/dbus/machine-id"):
        path = Path(p)
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    return None


def x__linux_machine_id__mutmut_orig() -> str | None:
    for p in ("/etc/machine-id", "/var/lib/dbus/machine-id"):
        path = Path(p)
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    return None


def x__linux_machine_id__mutmut_1() -> str | None:
    for p in ("XX/etc/machine-idXX", "/var/lib/dbus/machine-id"):
        path = Path(p)
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    return None


def x__linux_machine_id__mutmut_2() -> str | None:
    for p in ("/ETC/MACHINE-ID", "/var/lib/dbus/machine-id"):
        path = Path(p)
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    return None


def x__linux_machine_id__mutmut_3() -> str | None:
    for p in ("/etc/machine-id", "XX/var/lib/dbus/machine-idXX"):
        path = Path(p)
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    return None


def x__linux_machine_id__mutmut_4() -> str | None:
    for p in ("/etc/machine-id", "/VAR/LIB/DBUS/MACHINE-ID"):
        path = Path(p)
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    return None


def x__linux_machine_id__mutmut_5() -> str | None:
    for p in ("/etc/machine-id", "/var/lib/dbus/machine-id"):
        path = None
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    return None


def x__linux_machine_id__mutmut_6() -> str | None:
    for p in ("/etc/machine-id", "/var/lib/dbus/machine-id"):
        path = Path(None)
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    return None


def x__linux_machine_id__mutmut_7() -> str | None:
    for p in ("/etc/machine-id", "/var/lib/dbus/machine-id"):
        path = Path(p)
        if path.exists():
            return path.read_text(encoding=None).strip()
    return None


def x__linux_machine_id__mutmut_8() -> str | None:
    for p in ("/etc/machine-id", "/var/lib/dbus/machine-id"):
        path = Path(p)
        if path.exists():
            return path.read_text(encoding="XXutf-8XX").strip()
    return None


def x__linux_machine_id__mutmut_9() -> str | None:
    for p in ("/etc/machine-id", "/var/lib/dbus/machine-id"):
        path = Path(p)
        if path.exists():
            return path.read_text(encoding="UTF-8").strip()
    return None

mutants_x__linux_machine_id__mutmut['_mutmut_orig'] = x__linux_machine_id__mutmut_orig # type: ignore # mutmut generated
mutants_x__linux_machine_id__mutmut['x__linux_machine_id__mutmut_1'] = x__linux_machine_id__mutmut_1 # type: ignore # mutmut generated
mutants_x__linux_machine_id__mutmut['x__linux_machine_id__mutmut_2'] = x__linux_machine_id__mutmut_2 # type: ignore # mutmut generated
mutants_x__linux_machine_id__mutmut['x__linux_machine_id__mutmut_3'] = x__linux_machine_id__mutmut_3 # type: ignore # mutmut generated
mutants_x__linux_machine_id__mutmut['x__linux_machine_id__mutmut_4'] = x__linux_machine_id__mutmut_4 # type: ignore # mutmut generated
mutants_x__linux_machine_id__mutmut['x__linux_machine_id__mutmut_5'] = x__linux_machine_id__mutmut_5 # type: ignore # mutmut generated
mutants_x__linux_machine_id__mutmut['x__linux_machine_id__mutmut_6'] = x__linux_machine_id__mutmut_6 # type: ignore # mutmut generated
mutants_x__linux_machine_id__mutmut['x__linux_machine_id__mutmut_7'] = x__linux_machine_id__mutmut_7 # type: ignore # mutmut generated
mutants_x__linux_machine_id__mutmut['x__linux_machine_id__mutmut_8'] = x__linux_machine_id__mutmut_8 # type: ignore # mutmut generated
mutants_x__linux_machine_id__mutmut['x__linux_machine_id__mutmut_9'] = x__linux_machine_id__mutmut_9 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__hardware_fingerprint__mutmut)
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


def x__hardware_fingerprint__mutmut_orig() -> str:
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


def x__hardware_fingerprint__mutmut_1() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = None
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


def x__hardware_fingerprint__mutmut_2() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = None

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


def x__hardware_fingerprint__mutmut_3() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system != "Windows":
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


def x__hardware_fingerprint__mutmut_4() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "XXWindowsXX":
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


def x__hardware_fingerprint__mutmut_5() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "windows":
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


def x__hardware_fingerprint__mutmut_6() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "WINDOWS":
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


def x__hardware_fingerprint__mutmut_7() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "Windows":
        guid = None
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


def x__hardware_fingerprint__mutmut_8() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "Windows":
        guid = _windows_machine_guid()
        if guid:
            parts.append(None)
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


def x__hardware_fingerprint__mutmut_9() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "Windows":
        guid = _windows_machine_guid()
        if guid:
            parts.append(guid)
    elif system != "Darwin":
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


def x__hardware_fingerprint__mutmut_10() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "Windows":
        guid = _windows_machine_guid()
        if guid:
            parts.append(guid)
    elif system == "XXDarwinXX":
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


def x__hardware_fingerprint__mutmut_11() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "Windows":
        guid = _windows_machine_guid()
        if guid:
            parts.append(guid)
    elif system == "darwin":
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


def x__hardware_fingerprint__mutmut_12() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "Windows":
        guid = _windows_machine_guid()
        if guid:
            parts.append(guid)
    elif system == "DARWIN":
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


def x__hardware_fingerprint__mutmut_13() -> str:
    """Build a SHA-256 fingerprint from OS-specific machine ID + network identity."""
    system = platform.system()
    parts: list[str] = []

    if system == "Windows":
        guid = _windows_machine_guid()
        if guid:
            parts.append(guid)
    elif system == "Darwin":
        puuid = None
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


def x__hardware_fingerprint__mutmut_14() -> str:
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
            parts.append(None)
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


def x__hardware_fingerprint__mutmut_15() -> str:
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
        mid = None
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


def x__hardware_fingerprint__mutmut_16() -> str:
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
            parts.append(None)

    parts.append(platform.node() or socket.gethostname())

    try:
        parts.append(str(uuid.getnode()))
    except Exception:
        pass

    parts.append(platform.machine())
    parts.append(system)

    combined = "|".join(parts)
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_17() -> str:
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

    parts.append(None)

    try:
        parts.append(str(uuid.getnode()))
    except Exception:
        pass

    parts.append(platform.machine())
    parts.append(system)

    combined = "|".join(parts)
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_18() -> str:
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

    parts.append(platform.node() and socket.gethostname())

    try:
        parts.append(str(uuid.getnode()))
    except Exception:
        pass

    parts.append(platform.machine())
    parts.append(system)

    combined = "|".join(parts)
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_19() -> str:
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
        parts.append(None)
    except Exception:
        pass

    parts.append(platform.machine())
    parts.append(system)

    combined = "|".join(parts)
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_20() -> str:
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
        parts.append(str(None))
    except Exception:
        pass

    parts.append(platform.machine())
    parts.append(system)

    combined = "|".join(parts)
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_21() -> str:
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

    parts.append(None)
    parts.append(system)

    combined = "|".join(parts)
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_22() -> str:
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
    parts.append(None)

    combined = "|".join(parts)
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_23() -> str:
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

    combined = None
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_24() -> str:
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

    combined = "|".join(None)
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_25() -> str:
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

    combined = "XX|XX".join(parts)
    return hashlib.sha256(combined.encode()).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_26() -> str:
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
    return hashlib.sha256(None).hexdigest()[:24]


def x__hardware_fingerprint__mutmut_27() -> str:
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
    return hashlib.sha256(combined.encode()).hexdigest()[:25]

mutants_x__hardware_fingerprint__mutmut['_mutmut_orig'] = x__hardware_fingerprint__mutmut_orig # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_1'] = x__hardware_fingerprint__mutmut_1 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_2'] = x__hardware_fingerprint__mutmut_2 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_3'] = x__hardware_fingerprint__mutmut_3 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_4'] = x__hardware_fingerprint__mutmut_4 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_5'] = x__hardware_fingerprint__mutmut_5 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_6'] = x__hardware_fingerprint__mutmut_6 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_7'] = x__hardware_fingerprint__mutmut_7 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_8'] = x__hardware_fingerprint__mutmut_8 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_9'] = x__hardware_fingerprint__mutmut_9 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_10'] = x__hardware_fingerprint__mutmut_10 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_11'] = x__hardware_fingerprint__mutmut_11 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_12'] = x__hardware_fingerprint__mutmut_12 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_13'] = x__hardware_fingerprint__mutmut_13 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_14'] = x__hardware_fingerprint__mutmut_14 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_15'] = x__hardware_fingerprint__mutmut_15 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_16'] = x__hardware_fingerprint__mutmut_16 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_17'] = x__hardware_fingerprint__mutmut_17 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_18'] = x__hardware_fingerprint__mutmut_18 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_19'] = x__hardware_fingerprint__mutmut_19 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_20'] = x__hardware_fingerprint__mutmut_20 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_21'] = x__hardware_fingerprint__mutmut_21 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_22'] = x__hardware_fingerprint__mutmut_22 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_23'] = x__hardware_fingerprint__mutmut_23 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_24'] = x__hardware_fingerprint__mutmut_24 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_25'] = x__hardware_fingerprint__mutmut_25 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_26'] = x__hardware_fingerprint__mutmut_26 # type: ignore # mutmut generated
mutants_x__hardware_fingerprint__mutmut['x__hardware_fingerprint__mutmut_27'] = x__hardware_fingerprint__mutmut_27 # type: ignore # mutmut generated
mutants_x__read_stored__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__read_stored__mutmut)
def _read_stored() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="utf-8").strip().split("\n")[0]
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_orig() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="utf-8").strip().split("\n")[0]
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_1() -> str | None:
    if MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="utf-8").strip().split("\n")[0]
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_2() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = None
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_3() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="utf-8").strip().split(None)[0]
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_4() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding=None).strip().split("\n")[0]
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_5() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="XXutf-8XX").strip().split("\n")[0]
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_6() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="UTF-8").strip().split("\n")[0]
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_7() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="utf-8").strip().split("XX\nXX")[0]
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_8() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="utf-8").strip().split("\n")[1]
    return stored if len(stored) >= 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_9() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="utf-8").strip().split("\n")[0]
    return stored if len(stored) > 20 else None  # noqa: PLR2004


def x__read_stored__mutmut_10() -> str | None:
    if not MACHINE_ID_PATH.exists():
        return None
    stored = MACHINE_ID_PATH.read_text(encoding="utf-8").strip().split("\n")[0]
    return stored if len(stored) >= 21 else None  # noqa: PLR2004

mutants_x__read_stored__mutmut['_mutmut_orig'] = x__read_stored__mutmut_orig # type: ignore # mutmut generated
mutants_x__read_stored__mutmut['x__read_stored__mutmut_1'] = x__read_stored__mutmut_1 # type: ignore # mutmut generated
mutants_x__read_stored__mutmut['x__read_stored__mutmut_2'] = x__read_stored__mutmut_2 # type: ignore # mutmut generated
mutants_x__read_stored__mutmut['x__read_stored__mutmut_3'] = x__read_stored__mutmut_3 # type: ignore # mutmut generated
mutants_x__read_stored__mutmut['x__read_stored__mutmut_4'] = x__read_stored__mutmut_4 # type: ignore # mutmut generated
mutants_x__read_stored__mutmut['x__read_stored__mutmut_5'] = x__read_stored__mutmut_5 # type: ignore # mutmut generated
mutants_x__read_stored__mutmut['x__read_stored__mutmut_6'] = x__read_stored__mutmut_6 # type: ignore # mutmut generated
mutants_x__read_stored__mutmut['x__read_stored__mutmut_7'] = x__read_stored__mutmut_7 # type: ignore # mutmut generated
mutants_x__read_stored__mutmut['x__read_stored__mutmut_8'] = x__read_stored__mutmut_8 # type: ignore # mutmut generated
mutants_x__read_stored__mutmut['x__read_stored__mutmut_9'] = x__read_stored__mutmut_9 # type: ignore # mutmut generated
mutants_x__read_stored__mutmut['x__read_stored__mutmut_10'] = x__read_stored__mutmut_10 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__validate_or_repair__mutmut)
def _validate_or_repair(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_orig(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_1(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = None

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_2(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current != stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_3(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=None, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_4(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=None)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_5(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_6(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, )
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_7(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=False, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_8(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=False)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_9(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(None, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_10(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding=None)
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_11(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_12(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, )
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_13(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="XXutf-8XX")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_14(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="UTF-8")
    MACHINE_ID_PATH.chmod(0o600)
    return current


def x__validate_or_repair__mutmut_15(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(None)
    return current


def x__validate_or_repair__mutmut_16(stored: str) -> str:
    """If the hardware matches what's stored, keep it. Otherwise regenerate."""
    current = _hardware_fingerprint()

    if current == stored:
        return stored

    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(current, encoding="utf-8")
    MACHINE_ID_PATH.chmod(385)
    return current

mutants_x__validate_or_repair__mutmut['_mutmut_orig'] = x__validate_or_repair__mutmut_orig # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_1'] = x__validate_or_repair__mutmut_1 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_2'] = x__validate_or_repair__mutmut_2 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_3'] = x__validate_or_repair__mutmut_3 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_4'] = x__validate_or_repair__mutmut_4 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_5'] = x__validate_or_repair__mutmut_5 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_6'] = x__validate_or_repair__mutmut_6 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_7'] = x__validate_or_repair__mutmut_7 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_8'] = x__validate_or_repair__mutmut_8 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_9'] = x__validate_or_repair__mutmut_9 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_10'] = x__validate_or_repair__mutmut_10 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_11'] = x__validate_or_repair__mutmut_11 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_12'] = x__validate_or_repair__mutmut_12 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_13'] = x__validate_or_repair__mutmut_13 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_14'] = x__validate_or_repair__mutmut_14 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_15'] = x__validate_or_repair__mutmut_15 # type: ignore # mutmut generated
mutants_x__validate_or_repair__mutmut['x__validate_or_repair__mutmut_16'] = x__validate_or_repair__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_machine_id__mutmut)
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


def x_get_machine_id__mutmut_orig() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_1() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = None
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_2() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_3() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(None)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_4() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = None
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_5() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=None, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_6() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=None)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_7() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_8() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, )
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_9() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=False, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_10() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=False)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_11() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(None, encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_12() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding=None)
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_13() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(encoding="utf-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_14() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, )
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_15() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="XXutf-8XX")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_16() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="UTF-8")
    MACHINE_ID_PATH.chmod(0o600)
    return fingerprint


def x_get_machine_id__mutmut_17() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(None)
    return fingerprint


def x_get_machine_id__mutmut_18() -> str:
    """Return the machine fingerprint, creating it on first call."""
    stored = _read_stored()
    if stored is not None:
        return _validate_or_repair(stored)

    fingerprint = _hardware_fingerprint()
    MACHINE_ID_PATH.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_ID_PATH.write_text(fingerprint, encoding="utf-8")
    MACHINE_ID_PATH.chmod(385)
    return fingerprint

mutants_x_get_machine_id__mutmut['_mutmut_orig'] = x_get_machine_id__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_1'] = x_get_machine_id__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_2'] = x_get_machine_id__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_3'] = x_get_machine_id__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_4'] = x_get_machine_id__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_5'] = x_get_machine_id__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_6'] = x_get_machine_id__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_7'] = x_get_machine_id__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_8'] = x_get_machine_id__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_9'] = x_get_machine_id__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_10'] = x_get_machine_id__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_11'] = x_get_machine_id__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_12'] = x_get_machine_id__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_13'] = x_get_machine_id__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_14'] = x_get_machine_id__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_15'] = x_get_machine_id__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_16'] = x_get_machine_id__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_17'] = x_get_machine_id__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_machine_id__mutmut['x_get_machine_id__mutmut_18'] = x_get_machine_id__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_machine_id_short__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_machine_id_short__mutmut)
def get_machine_id_short() -> str:
    """Return first 12 chars of the fingerprint for display/logging."""
    return get_machine_id()[:12]


def x_get_machine_id_short__mutmut_orig() -> str:
    """Return first 12 chars of the fingerprint for display/logging."""
    return get_machine_id()[:12]


def x_get_machine_id_short__mutmut_1() -> str:
    """Return first 12 chars of the fingerprint for display/logging."""
    return get_machine_id()[:13]

mutants_x_get_machine_id_short__mutmut['_mutmut_orig'] = x_get_machine_id_short__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_machine_id_short__mutmut['x_get_machine_id_short__mutmut_1'] = x_get_machine_id_short__mutmut_1 # type: ignore # mutmut generated
