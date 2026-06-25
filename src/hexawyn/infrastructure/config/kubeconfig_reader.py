import os
from pathlib import Path

import yaml
from kubernetes import client, config

from hexawyn.domain.errors import ClusterUnreachableError

DEFAULT_KUBECONFIG = os.path.expanduser("~/.kube/config")


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

    valid_paths = [
        p for p in kubeconfig_path.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0
    ]
    if valid_paths:
        merged_path = os.pathsep.join(valid_paths)
        try:
            config.load_kube_config(config_file=merged_path, context=context)
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
        except Exception as e:
            raise ClusterUnreachableError(
                "No kubeconfig found and not running in-cluster. "
                "Mount your kubeconfig or set KUBECONFIG env var.",
                context={"kubeconfig_path": kubeconfig_path, "error": str(e)},
            ) from e

    return client.CoreV1Api()


def list_available_contexts() -> list[dict[str, str]]:
    """
    List all contexts available in the current kubeconfig.
    Used by the SetupWizard cluster selector and /cluster command.
    Never raises — returns empty list if kubeconfig is unavailable.

    Returns:
        List of dicts with keys: name, cluster, namespace.
    """
    try:
        contexts, _ = config.list_kube_config_contexts()
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
        _, active = config.list_kube_config_contexts()
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


def get_kubeconfig_stable_content() -> bytes | None:
    """
    Extract stable parts of the kubeconfig for encryption key derivation.

    Reads the CA certificate data and server URLs from all clusters in the
    kubeconfig file. These parts are stable across token refreshes and
    uniquely identify the cluster.

    Returns:
        Bytes of concatenated stable content, or None if no kubeconfig found.
    """
    kubeconfig_path = os.environ.get("KUBECONFIG", DEFAULT_KUBECONFIG)

    valid_paths = [
        p for p in kubeconfig_path.split(os.pathsep) if os.path.isfile(p) and os.path.getsize(p) > 0
    ]
    if not valid_paths:
        return None

    try:
        raw = Path(valid_paths[0]).read_text(encoding="utf-8")
        config_data = yaml.safe_load(raw)

        if not isinstance(config_data, dict):
            return raw.encode("utf-8")

        clusters = config_data.get("clusters")
        if not isinstance(clusters, list):
            return raw.encode("utf-8")

        stable_parts: list[str] = []
        for cluster_entry in clusters:
            if isinstance(cluster_entry, dict):
                cluster_info = cluster_entry.get("cluster")
                if isinstance(cluster_info, dict):
                    server = str(cluster_info.get("server", ""))
                    ca_data = str(cluster_info.get("certificate-authority-data", ""))
                    if server or ca_data:
                        stable_parts.append(f"{server}|{ca_data}")

        if not stable_parts:
            return raw.encode("utf-8")

        return "@".join(stable_parts).encode("utf-8")
    except Exception:
        return None
