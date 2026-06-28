from collections.abc import Mapping
from typing import Any


def safe_findings(adapter: Any) -> list[Any]:
    if not hasattr(adapter, "get_findings"):
        return []
    try:
        findings = adapter.get_findings()
    except Exception:
        return []
    return list(findings)


def safe_pods(adapter: Any) -> list[Mapping[object, object]]:
    if not hasattr(adapter, "list_pods"):
        return []
    try:
        pods = adapter.list_pods()
    except Exception:
        return []
    return [pod for pod in pods if isinstance(pod, Mapping)]


def safe_metrics(adapter: Any) -> Mapping[object, object]:
    if not hasattr(adapter, "get_cluster_metrics"):
        return {}
    try:
        metrics = adapter.get_cluster_metrics()
    except Exception:
        return {}
    return metrics if isinstance(metrics, Mapping) else {}


def kubectl_current_context() -> str:
    try:
        import subprocess

        result = subprocess.run(
            ["kubectl", "config", "current-context"], capture_output=True, text=True, timeout=3
        )
        return result.stdout.strip() or "?"
    except Exception:
        return "?"


def safe_health_score(adapter: Any) -> int:
    if not hasattr(adapter, "get_health_score"):
        return 100
    try:
        score = adapter.get_health_score()
    except Exception:
        return 100
    return score if isinstance(score, int) else 100


def safe_suggestions(adapter: Any) -> list[str]:
    if not hasattr(adapter, "get_suggestion_chips"):
        return []
    try:
        suggestions = adapter.get_suggestion_chips()
    except Exception:
        return []
    return [str(suggestion) for suggestion in suggestions][:3]


def mapping_text(mapping: Mapping[object, object], key: str, default: str) -> str:
    value = mapping.get(key)
    return value if isinstance(value, str) else default


def mapping_int(mapping: Mapping[object, object], key: str, default: int) -> int:
    value = mapping.get(key)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return default


def running_pod_count(pods: list[Mapping[object, object]]) -> int:
    return sum(1 for pod in pods if mapping_text(pod, "status", "") == "Running")


def pending_pod_count(pods: list[Mapping[object, object]]) -> int:
    return sum(1 for pod in pods if mapping_text(pod, "status", "") == "Pending")


def failed_pod_count(pods: list[Mapping[object, object]]) -> int:
    failed_statuses = {"Failed", "Error", "CrashLoop", "CrashLoopBackOff"}
    return sum(1 for pod in pods if mapping_text(pod, "status", "") in failed_statuses)


def namespace_count(pods: list[Mapping[object, object]], fallback_namespace: str) -> int:
    namespaces = {
        mapping_text(pod, "namespace", fallback_namespace)
        for pod in pods
        if mapping_text(pod, "namespace", fallback_namespace)
    }
    return len(namespaces) if namespaces else 1


def crashloop_finding_count(findings: list[Any]) -> int:
    return sum(1 for finding in findings if "CrashLoopBackOff" in str(finding))


def restarting_finding_count(findings: list[Any]) -> int:
    return sum(1 for finding in findings if "restarted" in str(finding).lower())


def issue_name(finding: Any) -> str:
    message = finding_message(finding)
    if message.startswith("Pod "):
        resource = message.split()[1]
        return resource.split("/", maxsplit=1)[-1]
    return message.split(maxsplit=1)[0] if message else "unknown"


def issue_reason(finding: Any) -> str:
    message = finding_message(finding)
    if "CrashLoopBackOff" in message:
        return "CrashLoopBackOff"
    if "restarted" in message:
        return message.split(" restarted ", maxsplit=1)[-1].replace(" times", " restarts")
    return message


def finding_message(finding: Any) -> str:
    if isinstance(finding, Mapping):
        message = finding.get("message")
        return message if isinstance(message, str) else ""
    return str(finding)
