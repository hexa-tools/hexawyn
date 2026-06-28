from dataclasses import dataclass, field
from typing import Any

from hexawyn.application.ports.driven.runtime_port import InvestigationOutput
from hexawyn.application.service.runtime_adapter import get_runtime


@dataclass
class CommandResult:
    kind: str
    lines: list[tuple[str, str]] = field(default_factory=list)
    pods: list[dict[str, Any]] | None = None
    summary: str | None = None
    chips: list[str] = field(default_factory=list)


def _service_name(pod_name: str) -> str:
    """Strip the trailing replica/pod-hash segments from a k8s pod name."""
    parts = pod_name.split("-")
    if len(parts) <= 2:
        return pod_name
    return "-".join(parts[:-2])


def _find_pod(normalized_text: str, pods: list[dict[str, Any]]) -> dict[str, Any] | None:
    for pod in pods:
        svc = _service_name(str(pod["name"]))
        if svc.lower() in normalized_text or str(pod["name"]).lower() in normalized_text:
            return pod
    return None


def _pods_summary(pods: list[dict[str, Any]]) -> str:
    running = sum(1 for p in pods if p["status"] == "Running")
    crashloop = sum(1 for p in pods if p["status"] == "CrashLoop")
    pending = sum(1 for p in pods if p["status"] == "Pending")
    other = len(pods) - running - crashloop - pending
    parts = [f"{len(pods)} pods", f"{running} running"]
    if crashloop:
        parts.append(f"{crashloop} crashloop")
    if pending:
        parts.append(f"{pending} pending")
    if other:
        parts.append(f"{other} other")
    return " · ".join(parts)


def _suggested_chips(pods: list[dict[str, Any]]) -> list[str]:
    chips: list[str] = []
    crashed = next((p for p in pods if p["status"] == "CrashLoop"), None)
    pending = next((p for p in pods if p["status"] == "Pending"), None)
    running = next((p for p in pods if p["status"] == "Running"), None)
    if crashed:
        chips.append(f"debug {_service_name(str(crashed['name']))}")
    if pending:
        chips.append(f"why is {_service_name(str(pending['name']))} pending?")
    if running:
        chips.append(f"show logs for {_service_name(str(running['name']))}")
    return chips


def _list_pods(adapter: Any) -> CommandResult:
    pods = adapter.list_pods()
    return CommandResult(
        kind="pods",
        pods=pods,
        summary=_pods_summary(pods),
        chips=_suggested_chips(pods),
    )


def _debug_pod(adapter: Any, normalized_text: str) -> CommandResult:
    pods = adapter.list_pods()
    pod = _find_pod(normalized_text, pods)
    if pod is None:
        return CommandResult(
            kind="unknown",
            lines=[("No pod matching that request found.", "yellow")],
        )

    return _investigate(
        adapter=adapter,
        query=f"debug {_service_name(str(pod['name']))}",
        pod=pod,
    )


def _investigate(adapter: Any, query: str, pod: dict[str, Any] | None = None) -> CommandResult:
    ctx = adapter.get_cluster_context()
    runtime = get_runtime()
    runtime.set_adapter(adapter)

    output: InvestigationOutput = {
        "answer": "",
        "cause": "",
        "solution": "",
        "status": "error",
        "suggestions": [],
        "error": "Unknown error",
    }

    try:
        output = runtime.run_investigation(query, ctx)
    except Exception as exc:
        output = InvestigationOutput(
            answer="",
            cause="",
            solution="",
            status="error",
            suggestions=[],
            error=str(exc),
        )

    lines: list[tuple[str, str]] = []

    answer = output["answer"]
    if answer:
        lines.append((answer, "white"))

    if pod is not None:
        lines.insert(
            0,
            (
                f"{pod['name']}  ·  {pod['status']}  ·  {pod['restarts']} restarts",
                "bold",
            ),
        )

    error_msg = output["error"]
    if error_msg:
        lines.append((f"Error: {error_msg}", "red"))

    status = output["status"]
    if str(status) == "degraded":
        lines.append(("[UNVERIFIED — results may be incomplete]", "yellow"))

    suggestions = output["suggestions"]

    return CommandResult(
        kind="debug",
        lines=lines,
        chips=list(suggestions) if suggestions else [],
    )


def _show_logs(adapter: Any, normalized_text: str) -> CommandResult:
    if not hasattr(adapter, "search_logs"):
        return CommandResult(
            kind="unknown",
            lines=[("Logs are not available for this cluster.", "yellow")],
        )

    pods = adapter.list_pods()
    pod = _find_pod(normalized_text, pods)
    pattern = _service_name(str(pod["name"])) if pod else normalized_text

    entries = adapter.search_logs(pattern=pattern, time_window_minutes=15)
    if not entries:
        return CommandResult(kind="logs", lines=[(f'No logs found for "{pattern}".', "dim")])

    lines = [(f"[{e['severity']}] {e['timestamp']}  {e['message']}", "dim") for e in entries]
    return CommandResult(kind="logs", lines=lines)


def _explain_pending(adapter: Any) -> CommandResult:
    pods = [p for p in adapter.list_pods() if p["status"] == "Pending"]
    if not pods:
        return CommandResult(kind="pending", lines=[("No pending pods.", "green")])

    lines: list[tuple[str, str]] = []
    for pod in pods:
        lines.append((f"{pod['name']} is waiting to be scheduled (Pending).", "yellow"))
        if hasattr(adapter, "get_findings"):
            svc = _service_name(str(pod["name"])).lower()
            for finding in adapter.get_findings():
                if svc in finding["message"].lower():
                    lines.append((f"  → {finding['remediation']}", "dim"))
    return CommandResult(kind="pending", lines=lines)


def route_command(text: str, adapter: Any) -> CommandResult:
    normalized = text.strip().lower()
    if not normalized:
        return CommandResult(
            kind="unknown",
            lines=[("Type a command or click a suggestion.", "dim")],
        )

    return _investigate(adapter, normalized)
