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
        import os

        kubeconfig_env = os.environ.get("KUBECONFIG", os.path.expanduser("~/.kube/config"))
        import yaml

        for path in kubeconfig_env.split(os.pathsep):
            try:
                with open(path) as f:
                    config = yaml.safe_load(f)
                if config and isinstance(config, dict) and config.get("current-context"):
                    return str(config["current-context"])
            except Exception:
                continue
        return "?"
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


def schedule_summary_lines() -> list[str]:
    """Format the enabled scheduled checks for the aside.

    Returns an empty list when there are no enabled checks (or the schedule
    cannot be read), so callers can omit the section entirely.
    """
    from hexawyn.domain.services.schedule.cron_shortcut import cron_to_minutes
    from hexawyn.infrastructure.config.schedule_source import YamlScheduleSource

    try:
        checks = [c for c in YamlScheduleSource().load_checks() if c.enabled]
    except Exception:
        return []
    if not checks:
        return []

    lines = ["", "[bold]SCHEDULED CHECKS[/bold]"]
    for check in checks:
        interval = cron_to_minutes(check.schedule)
        cadence = f"~{interval}min" if interval > 0 else check.schedule
        lines.append(f"  {check.name}  [dim]{cadence}[/dim]")
    return lines
