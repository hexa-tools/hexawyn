import os
from pathlib import Path

from kubernetes import client, config

from hexawyn.domain.errors import ClusterUnreachableError

DEFAULT_KUBECONFIG = os.path.expanduser("~/.kube/config")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__kube_config_path__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__kube_config_path__mutmut)
def _kube_config_path() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_orig() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_1() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = None
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_2() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get(None)
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_3() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("XXKUBECONFIGXX")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_4() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("kubeconfig")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_5() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = None
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_6() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = None
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_7() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(None) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_8() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) or os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_9() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(None) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_10() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(None) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_11() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) >= 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_12() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 1]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_13() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid or env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_14() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_15() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is not None:
        valid = _scan_kube_configs()
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_16() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = None
    return os.pathsep.join(valid)


def x__kube_config_path__mutmut_17() -> str:
    """Merged kubeconfig path(s), excluding 0-byte files.

    The Kubernetes python client treats an empty file as invalid and aborts the
    whole KUBECONFIG merge, so any empty file is dropped here. When the
    ``KUBECONFIG`` env var is unset and the default path yields nothing usable,
    fall back to discovering a kubeconfig autonomously under ``$HOME`` — this
    makes a cluster reachable to a spawned MCP server that does not inherit
    ``KUBECONFIG``. When ``KUBECONFIG`` is explicitly set, it is honored as-is
    (no fallback).
    """
    env_kubeconfig = os.environ.get("KUBECONFIG")
    raw = env_kubeconfig if env_kubeconfig else DEFAULT_KUBECONFIG
    valid = [p for p in raw.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0]
    if not valid and env_kubeconfig is None:
        valid = _scan_kube_configs()
    return os.pathsep.join(None)

mutants_x__kube_config_path__mutmut['_mutmut_orig'] = x__kube_config_path__mutmut_orig # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_1'] = x__kube_config_path__mutmut_1 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_2'] = x__kube_config_path__mutmut_2 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_3'] = x__kube_config_path__mutmut_3 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_4'] = x__kube_config_path__mutmut_4 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_5'] = x__kube_config_path__mutmut_5 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_6'] = x__kube_config_path__mutmut_6 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_7'] = x__kube_config_path__mutmut_7 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_8'] = x__kube_config_path__mutmut_8 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_9'] = x__kube_config_path__mutmut_9 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_10'] = x__kube_config_path__mutmut_10 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_11'] = x__kube_config_path__mutmut_11 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_12'] = x__kube_config_path__mutmut_12 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_13'] = x__kube_config_path__mutmut_13 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_14'] = x__kube_config_path__mutmut_14 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_15'] = x__kube_config_path__mutmut_15 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_16'] = x__kube_config_path__mutmut_16 # type: ignore # mutmut generated
mutants_x__kube_config_path__mutmut['x__kube_config_path__mutmut_17'] = x__kube_config_path__mutmut_17 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__home_kube_dirs__mutmut)
def _home_kube_dirs() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_orig() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_1() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = None
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_2() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(None)
        for p in (
            home / ".kube",
            home / ".config" / "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_3() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home * ".kube",
            home / ".config" / "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_4() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / "XX.kubeXX",
            home / ".config" / "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_5() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".KUBE",
            home / ".config" / "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_6() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" * "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_7() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home * ".config" / "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_8() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / "XX.configXX" / "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_9() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".CONFIG" / "kube",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_10() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "XXkubeXX",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_11() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "KUBE",
            home / ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_12() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "kube",
            home / ".config" * "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_13() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "kube",
            home * ".config" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_14() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "kube",
            home / "XX.configXX" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_15() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "kube",
            home / ".CONFIG" / "kubernetes",
        )
    ]


def x__home_kube_dirs__mutmut_16() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "kube",
            home / ".config" / "XXkubernetesXX",
        )
    ]


def x__home_kube_dirs__mutmut_17() -> list[str]:
    """Standard kubeconfig directories under the user's home (multi-OS).

    Uses ``Path.home()`` which resolves ``HOME`` on POSIX and ``USERPROFILE`` on
    Windows — no absolute path is hardcoded. ``os.pathsep`` (``:`` / ``;``)
    already splits ``KUBECONFIG`` correctly per OS.
    """
    home = Path.home()
    return [
        str(p)
        for p in (
            home / ".kube",
            home / ".config" / "kube",
            home / ".config" / "KUBERNETES",
        )
    ]

mutants_x__home_kube_dirs__mutmut['_mutmut_orig'] = x__home_kube_dirs__mutmut_orig # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_1'] = x__home_kube_dirs__mutmut_1 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_2'] = x__home_kube_dirs__mutmut_2 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_3'] = x__home_kube_dirs__mutmut_3 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_4'] = x__home_kube_dirs__mutmut_4 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_5'] = x__home_kube_dirs__mutmut_5 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_6'] = x__home_kube_dirs__mutmut_6 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_7'] = x__home_kube_dirs__mutmut_7 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_8'] = x__home_kube_dirs__mutmut_8 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_9'] = x__home_kube_dirs__mutmut_9 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_10'] = x__home_kube_dirs__mutmut_10 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_11'] = x__home_kube_dirs__mutmut_11 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_12'] = x__home_kube_dirs__mutmut_12 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_13'] = x__home_kube_dirs__mutmut_13 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_14'] = x__home_kube_dirs__mutmut_14 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_15'] = x__home_kube_dirs__mutmut_15 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_16'] = x__home_kube_dirs__mutmut_16 # type: ignore # mutmut generated
mutants_x__home_kube_dirs__mutmut['x__home_kube_dirs__mutmut_17'] = x__home_kube_dirs__mutmut_17 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__scan_kube_configs__mutmut)
def _scan_kube_configs() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_orig() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_1() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = None
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_2() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_3() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(None):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_4() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            break
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_5() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(None):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_6() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(None)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_7() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_8() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") and filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_9() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" and filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_10() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename != "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_11() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "XXconfigXX" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_12() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "CONFIG" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_13() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(None) or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_14() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith("XX.yamlXX") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_15() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".YAML") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_16() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(None)
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_17() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith("XX.ymlXX")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_18() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".YML")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_19() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                break
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_20() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = None
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_21() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(None, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_22() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, None)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_23() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_24() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, )
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_25() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) or os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_26() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(None) and os.path.getsize(full) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_27() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(None) > 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_28() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) >= 0:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_29() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 1:
                found.append(full)
    return found


def x__scan_kube_configs__mutmut_30() -> list[str]:
    """Discover kubeconfig files autonomously: non-empty ``config``/``*.yaml``/
    ``*.yml`` files under the standard ``$HOME`` kubeconfig directories."""
    found: list[str] = []
    for directory in _home_kube_dirs():
        if not os.path.isdir(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not (
                filename == "config" or filename.endswith(".yaml") or filename.endswith(".yml")
            ):
                continue
            full = os.path.join(directory, filename)
            if os.path.isfile(full) and os.path.getsize(full) > 0:
                found.append(None)
    return found

mutants_x__scan_kube_configs__mutmut['_mutmut_orig'] = x__scan_kube_configs__mutmut_orig # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_1'] = x__scan_kube_configs__mutmut_1 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_2'] = x__scan_kube_configs__mutmut_2 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_3'] = x__scan_kube_configs__mutmut_3 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_4'] = x__scan_kube_configs__mutmut_4 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_5'] = x__scan_kube_configs__mutmut_5 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_6'] = x__scan_kube_configs__mutmut_6 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_7'] = x__scan_kube_configs__mutmut_7 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_8'] = x__scan_kube_configs__mutmut_8 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_9'] = x__scan_kube_configs__mutmut_9 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_10'] = x__scan_kube_configs__mutmut_10 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_11'] = x__scan_kube_configs__mutmut_11 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_12'] = x__scan_kube_configs__mutmut_12 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_13'] = x__scan_kube_configs__mutmut_13 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_14'] = x__scan_kube_configs__mutmut_14 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_15'] = x__scan_kube_configs__mutmut_15 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_16'] = x__scan_kube_configs__mutmut_16 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_17'] = x__scan_kube_configs__mutmut_17 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_18'] = x__scan_kube_configs__mutmut_18 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_19'] = x__scan_kube_configs__mutmut_19 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_20'] = x__scan_kube_configs__mutmut_20 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_21'] = x__scan_kube_configs__mutmut_21 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_22'] = x__scan_kube_configs__mutmut_22 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_23'] = x__scan_kube_configs__mutmut_23 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_24'] = x__scan_kube_configs__mutmut_24 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_25'] = x__scan_kube_configs__mutmut_25 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_26'] = x__scan_kube_configs__mutmut_26 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_27'] = x__scan_kube_configs__mutmut_27 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_28'] = x__scan_kube_configs__mutmut_28 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_29'] = x__scan_kube_configs__mutmut_29 # type: ignore # mutmut generated
mutants_x__scan_kube_configs__mutmut['x__scan_kube_configs__mutmut_30'] = x__scan_kube_configs__mutmut_30 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_load_kubeconfig__mutmut)
def load_kubeconfig(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_orig(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_1(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = None
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_2(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get(None, DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_3(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", None)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_4(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get(DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_5(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", )
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_6(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("XXKUBECONFIGXX", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_7(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("kubeconfig", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_8(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = None

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_9(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = None
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_10(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=None,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_11(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=None,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_12(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=None,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_13(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_14(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_15(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_16(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is not None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_17(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    None,
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_18(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context=None,
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_19(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_20(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_21(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "XXUnable to load kubeconfig.XX",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_22(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_23(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "UNABLE TO LOAD KUBECONFIG.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_24(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"XXkubeconfig_pathXX": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_25(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"KUBECONFIG_PATH": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_26(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "XXerrorXX": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_27(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "ERROR": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_28(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(None)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_29(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = None
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_30(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=None,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_31(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=None,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_32(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_33(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_34(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_35(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    None,
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_36(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context=None,
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_37(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_38(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_39(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "XXUnable to load kubeconfig.XX",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_40(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_41(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "UNABLE TO LOAD KUBECONFIG.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_42(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"XXkubeconfig_pathXX": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_43(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"KUBECONFIG_PATH": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_44(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "XXerrorXX": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_45(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "ERROR": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_46(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(None)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_47(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = None
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_48(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = None
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_49(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get(None, {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_50(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", None)
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_51(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get({})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_52(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", )
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_53(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("XXcontextXX", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_54(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("CONTEXT", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_55(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = None
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_56(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(None)
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_57(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get(None, "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_58(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", None))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_59(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_60(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", ))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_61(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("XXclusterXX", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_62(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("CLUSTER", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_63(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "XXunknownXX"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_64(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "UNKNOWN"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_65(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = None
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_66(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "XXunknownXX"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_67(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "UNKNOWN"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_68(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(None)
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_69(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['XXnameXX']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_70(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['NAME']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_71(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print(None)
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_72(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("XX[hexawyn] Running in-cluster mode (ServiceAccount)XX")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_73(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] running in-cluster mode (serviceaccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_74(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[HEXAWYN] RUNNING IN-CLUSTER MODE (SERVICEACCOUNT)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_75(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                None,
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_76(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context=None,
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_77(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_78(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_79(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "XXNo kubeconfig found and not running in-cluster. XX"
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_80(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "no kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_81(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "NO KUBECONFIG FOUND AND NOT RUNNING IN-CLUSTER. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_82(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "XXMount your kubeconfig or set KUBECONFIG env var.XX",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_83(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "mount your kubeconfig or set kubeconfig env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_84(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "MOUNT YOUR KUBECONFIG OR SET KUBECONFIG ENV VAR.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_85(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"XXkubeconfig_pathXX": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_86(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"KUBECONFIG_PATH": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_87(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "XXerrorXX": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_88(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "ERROR": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_89(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(None)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_90(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = None
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_91(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=None)
    return client.CoreV1Api(api_client=api_client)


def x_load_kubeconfig__mutmut_92(context: str | None = None) -> client.CoreV1Api:
    """
    Load kubeconfig and return a CoreV1Api client.

    Priority:
    1. KUBECONFIG env var (if set and file exists)
    2. ~/.kube/config (default path)
    3. In-cluster ServiceAccount token (when running inside a pod)

    Args:
        context: optional context name override.
                 If None, uses the active context from kubeconfig.

    Returns:
        CoreV1Api client ready to use.

    Raises:
        ClusterUnreachableError: if no kubeconfig found and not running in-cluster.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)
    merged_path = _kube_config_path()

    if merged_path:
        try:
            cfg = client.Configuration()
            config.load_kube_config(
                config_file=merged_path,
                context=context,
                client_configuration=cfg,
            )
        except Exception as exc:
            if context is None:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(exc)},
                ) from exc
            # Edge case: the explicit context fails to resolve (kubernetes
            # raises at set_active_context). Retry with the config's own
            # current context so the call still succeeds.
            cfg = client.Configuration()
            try:
                config.load_kube_config(
                    config_file=merged_path,
                    context=None,
                    client_configuration=cfg,
                )
            except Exception as retry_exc:
                raise ClusterUnreachableError(
                    "Unable to load kubeconfig.",
                    context={"kubeconfig_path": merged_path, "error": str(retry_exc)},
                ) from retry_exc
        active = get_active_context()
        if active:
            context_data = active.get("context", {})
            if isinstance(context_data, dict):
                cluster_name = str(context_data.get("cluster", "unknown"))
            else:
                cluster_name = "unknown"
            print(f"[hexawyn] Active context: {active['name']} → {cluster_name}")
    else:
        try:
            config.load_incluster_config()
            print("[hexawyn] Running in-cluster mode (ServiceAccount)")
            return client.CoreV1Api()
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    api_client = client.ApiClient(configuration=cfg)
    return client.CoreV1Api(api_client=None)

mutants_x_load_kubeconfig__mutmut['_mutmut_orig'] = x_load_kubeconfig__mutmut_orig # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_1'] = x_load_kubeconfig__mutmut_1 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_2'] = x_load_kubeconfig__mutmut_2 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_3'] = x_load_kubeconfig__mutmut_3 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_4'] = x_load_kubeconfig__mutmut_4 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_5'] = x_load_kubeconfig__mutmut_5 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_6'] = x_load_kubeconfig__mutmut_6 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_7'] = x_load_kubeconfig__mutmut_7 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_8'] = x_load_kubeconfig__mutmut_8 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_9'] = x_load_kubeconfig__mutmut_9 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_10'] = x_load_kubeconfig__mutmut_10 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_11'] = x_load_kubeconfig__mutmut_11 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_12'] = x_load_kubeconfig__mutmut_12 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_13'] = x_load_kubeconfig__mutmut_13 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_14'] = x_load_kubeconfig__mutmut_14 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_15'] = x_load_kubeconfig__mutmut_15 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_16'] = x_load_kubeconfig__mutmut_16 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_17'] = x_load_kubeconfig__mutmut_17 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_18'] = x_load_kubeconfig__mutmut_18 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_19'] = x_load_kubeconfig__mutmut_19 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_20'] = x_load_kubeconfig__mutmut_20 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_21'] = x_load_kubeconfig__mutmut_21 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_22'] = x_load_kubeconfig__mutmut_22 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_23'] = x_load_kubeconfig__mutmut_23 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_24'] = x_load_kubeconfig__mutmut_24 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_25'] = x_load_kubeconfig__mutmut_25 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_26'] = x_load_kubeconfig__mutmut_26 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_27'] = x_load_kubeconfig__mutmut_27 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_28'] = x_load_kubeconfig__mutmut_28 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_29'] = x_load_kubeconfig__mutmut_29 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_30'] = x_load_kubeconfig__mutmut_30 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_31'] = x_load_kubeconfig__mutmut_31 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_32'] = x_load_kubeconfig__mutmut_32 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_33'] = x_load_kubeconfig__mutmut_33 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_34'] = x_load_kubeconfig__mutmut_34 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_35'] = x_load_kubeconfig__mutmut_35 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_36'] = x_load_kubeconfig__mutmut_36 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_37'] = x_load_kubeconfig__mutmut_37 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_38'] = x_load_kubeconfig__mutmut_38 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_39'] = x_load_kubeconfig__mutmut_39 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_40'] = x_load_kubeconfig__mutmut_40 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_41'] = x_load_kubeconfig__mutmut_41 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_42'] = x_load_kubeconfig__mutmut_42 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_43'] = x_load_kubeconfig__mutmut_43 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_44'] = x_load_kubeconfig__mutmut_44 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_45'] = x_load_kubeconfig__mutmut_45 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_46'] = x_load_kubeconfig__mutmut_46 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_47'] = x_load_kubeconfig__mutmut_47 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_48'] = x_load_kubeconfig__mutmut_48 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_49'] = x_load_kubeconfig__mutmut_49 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_50'] = x_load_kubeconfig__mutmut_50 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_51'] = x_load_kubeconfig__mutmut_51 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_52'] = x_load_kubeconfig__mutmut_52 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_53'] = x_load_kubeconfig__mutmut_53 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_54'] = x_load_kubeconfig__mutmut_54 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_55'] = x_load_kubeconfig__mutmut_55 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_56'] = x_load_kubeconfig__mutmut_56 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_57'] = x_load_kubeconfig__mutmut_57 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_58'] = x_load_kubeconfig__mutmut_58 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_59'] = x_load_kubeconfig__mutmut_59 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_60'] = x_load_kubeconfig__mutmut_60 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_61'] = x_load_kubeconfig__mutmut_61 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_62'] = x_load_kubeconfig__mutmut_62 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_63'] = x_load_kubeconfig__mutmut_63 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_64'] = x_load_kubeconfig__mutmut_64 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_65'] = x_load_kubeconfig__mutmut_65 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_66'] = x_load_kubeconfig__mutmut_66 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_67'] = x_load_kubeconfig__mutmut_67 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_68'] = x_load_kubeconfig__mutmut_68 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_69'] = x_load_kubeconfig__mutmut_69 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_70'] = x_load_kubeconfig__mutmut_70 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_71'] = x_load_kubeconfig__mutmut_71 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_72'] = x_load_kubeconfig__mutmut_72 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_73'] = x_load_kubeconfig__mutmut_73 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_74'] = x_load_kubeconfig__mutmut_74 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_75'] = x_load_kubeconfig__mutmut_75 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_76'] = x_load_kubeconfig__mutmut_76 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_77'] = x_load_kubeconfig__mutmut_77 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_78'] = x_load_kubeconfig__mutmut_78 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_79'] = x_load_kubeconfig__mutmut_79 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_80'] = x_load_kubeconfig__mutmut_80 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_81'] = x_load_kubeconfig__mutmut_81 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_82'] = x_load_kubeconfig__mutmut_82 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_83'] = x_load_kubeconfig__mutmut_83 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_84'] = x_load_kubeconfig__mutmut_84 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_85'] = x_load_kubeconfig__mutmut_85 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_86'] = x_load_kubeconfig__mutmut_86 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_87'] = x_load_kubeconfig__mutmut_87 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_88'] = x_load_kubeconfig__mutmut_88 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_89'] = x_load_kubeconfig__mutmut_89 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_90'] = x_load_kubeconfig__mutmut_90 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_91'] = x_load_kubeconfig__mutmut_91 # type: ignore # mutmut generated
mutants_x_load_kubeconfig__mutmut['x_load_kubeconfig__mutmut_92'] = x_load_kubeconfig__mutmut_92 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_available_contexts__mutmut)
def list_available_contexts() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_orig() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_1() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = None
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_2() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=None)
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_3() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "XXnameXX": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_4() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "NAME": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_5() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["XXnameXX"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_6() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["NAME"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_7() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "XXclusterXX": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_8() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "CLUSTER": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_9() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get(None, "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_10() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", None),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_11() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_12() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", ),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_13() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["XXcontextXX"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_14() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["CONTEXT"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_15() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("XXclusterXX", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_16() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("CLUSTER", "unknown"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_17() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "XXunknownXX"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_18() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "UNKNOWN"),
                "namespace": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_19() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "XXnamespaceXX": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_20() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "NAMESPACE": ctx["context"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_21() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get(None, "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_22() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", None),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_23() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_24() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", ),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_25() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["XXcontextXX"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_26() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["CONTEXT"].get("namespace", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_27() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("XXnamespaceXX", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_28() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("NAMESPACE", "default"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_29() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "XXdefaultXX"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []


def x_list_available_contexts__mutmut_30() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=_kube_config_path())
        return [
            {
                "name": ctx["name"],
                "cluster": ctx["context"].get("cluster", "unknown"),
                "namespace": ctx["context"].get("namespace", "DEFAULT"),
            }
            for ctx in contexts
        ]
    except Exception:
        return []

mutants_x_list_available_contexts__mutmut['_mutmut_orig'] = x_list_available_contexts__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_1'] = x_list_available_contexts__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_2'] = x_list_available_contexts__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_3'] = x_list_available_contexts__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_4'] = x_list_available_contexts__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_5'] = x_list_available_contexts__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_6'] = x_list_available_contexts__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_7'] = x_list_available_contexts__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_8'] = x_list_available_contexts__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_9'] = x_list_available_contexts__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_10'] = x_list_available_contexts__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_11'] = x_list_available_contexts__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_12'] = x_list_available_contexts__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_13'] = x_list_available_contexts__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_14'] = x_list_available_contexts__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_15'] = x_list_available_contexts__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_16'] = x_list_available_contexts__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_17'] = x_list_available_contexts__mutmut_17 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_18'] = x_list_available_contexts__mutmut_18 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_19'] = x_list_available_contexts__mutmut_19 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_20'] = x_list_available_contexts__mutmut_20 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_21'] = x_list_available_contexts__mutmut_21 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_22'] = x_list_available_contexts__mutmut_22 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_23'] = x_list_available_contexts__mutmut_23 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_24'] = x_list_available_contexts__mutmut_24 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_25'] = x_list_available_contexts__mutmut_25 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_26'] = x_list_available_contexts__mutmut_26 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_27'] = x_list_available_contexts__mutmut_27 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_28'] = x_list_available_contexts__mutmut_28 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_29'] = x_list_available_contexts__mutmut_29 # type: ignore # mutmut generated
mutants_x_list_available_contexts__mutmut['x_list_available_contexts__mutmut_30'] = x_list_available_contexts__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_active_context__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_active_context__mutmut)
def get_active_context() -> dict[str, object] | None:
    """
    Get the currently active kubeconfig context.
    Never raises — returns None if kubeconfig is unavailable.

    Returns:
        Dict with keys: name, cluster, namespace. Or None.
    """
    try:
        _, active = config.list_kube_config_contexts(config_file=_kube_config_path())
        return active if isinstance(active, dict) else None
    except Exception:
        return None


def x_get_active_context__mutmut_orig() -> dict[str, object] | None:
    """
    Get the currently active kubeconfig context.
    Never raises — returns None if kubeconfig is unavailable.

    Returns:
        Dict with keys: name, cluster, namespace. Or None.
    """
    try:
        _, active = config.list_kube_config_contexts(config_file=_kube_config_path())
        return active if isinstance(active, dict) else None
    except Exception:
        return None


def x_get_active_context__mutmut_1() -> dict[str, object] | None:
    """
    Get the currently active kubeconfig context.
    Never raises — returns None if kubeconfig is unavailable.

    Returns:
        Dict with keys: name, cluster, namespace. Or None.
    """
    try:
        _, active = None
        return active if isinstance(active, dict) else None
    except Exception:
        return None


def x_get_active_context__mutmut_2() -> dict[str, object] | None:
    """
    Get the currently active kubeconfig context.
    Never raises — returns None if kubeconfig is unavailable.

    Returns:
        Dict with keys: name, cluster, namespace. Or None.
    """
    try:
        _, active = config.list_kube_config_contexts(config_file=None)
        return active if isinstance(active, dict) else None
    except Exception:
        return None

mutants_x_get_active_context__mutmut['_mutmut_orig'] = x_get_active_context__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_active_context__mutmut['x_get_active_context__mutmut_1'] = x_get_active_context__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_active_context__mutmut['x_get_active_context__mutmut_2'] = x_get_active_context__mutmut_2 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_validate_connection__mutmut)
def validate_connection(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_orig(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_1(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=None, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_2(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=None)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_3(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_4(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, )
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_5(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=2, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_6(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=6)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_7(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"XXstatusXX": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_8(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"STATUS": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_9(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "XXconnectedXX", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_10(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "CONNECTED", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_11(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "XXcontextXX": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_12(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "CONTEXT": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_13(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "XXstatusXX": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_14(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "STATUS": "unreachable",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_15(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "XXunreachableXX",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_16(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "UNREACHABLE",
            "context": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_17(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "XXcontextXX": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_18(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "CONTEXT": context_name,
            "error": str(e),
        }


def x_validate_connection__mutmut_19(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "XXerrorXX": str(e),
        }


def x_validate_connection__mutmut_20(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "ERROR": str(e),
        }


def x_validate_connection__mutmut_21(
    api: client.CoreV1Api,
    context_name: str,
) -> dict[str, str]:
    """
    Lightweight connectivity check — lists namespaces with a 5s timeout.
    Called at startup to confirm the cluster is reachable.
    Never raises — returns a status dict.

    Returns:
        {"status": "connected", "context": context_name}
        or
        {"status": "unreachable", "context": context_name, "error": str}
    """
    try:
        api.list_namespace(limit=1, timeout_seconds=5)
        return {"status": "connected", "context": context_name}
    except Exception as e:
        return {
            "status": "unreachable",
            "context": context_name,
            "error": str(None),
        }

mutants_x_validate_connection__mutmut['_mutmut_orig'] = x_validate_connection__mutmut_orig # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_1'] = x_validate_connection__mutmut_1 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_2'] = x_validate_connection__mutmut_2 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_3'] = x_validate_connection__mutmut_3 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_4'] = x_validate_connection__mutmut_4 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_5'] = x_validate_connection__mutmut_5 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_6'] = x_validate_connection__mutmut_6 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_7'] = x_validate_connection__mutmut_7 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_8'] = x_validate_connection__mutmut_8 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_9'] = x_validate_connection__mutmut_9 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_10'] = x_validate_connection__mutmut_10 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_11'] = x_validate_connection__mutmut_11 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_12'] = x_validate_connection__mutmut_12 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_13'] = x_validate_connection__mutmut_13 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_14'] = x_validate_connection__mutmut_14 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_15'] = x_validate_connection__mutmut_15 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_16'] = x_validate_connection__mutmut_16 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_17'] = x_validate_connection__mutmut_17 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_18'] = x_validate_connection__mutmut_18 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_19'] = x_validate_connection__mutmut_19 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_20'] = x_validate_connection__mutmut_20 # type: ignore # mutmut generated
mutants_x_validate_connection__mutmut['x_validate_connection__mutmut_21'] = x_validate_connection__mutmut_21 # type: ignore # mutmut generated
