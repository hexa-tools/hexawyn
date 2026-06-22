import os

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

    if os.path.exists(kubeconfig_path):
        config.load_kube_config(config_file=kubeconfig_path, context=context)
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
