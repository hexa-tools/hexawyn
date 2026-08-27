import os
from pathlib import Path

from kubernetes import client, config

from hexawyn.domain.errors import ClusterUnreachableError

DEFAULT_KUBECONFIG = os.path.expanduser("~/.kube/config")


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
            raise ClusterUnreachableError(
                "Unable to load kubeconfig.",
                context={"kubeconfig_path": merged_path, "error": str(exc)},
            ) from exc
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
