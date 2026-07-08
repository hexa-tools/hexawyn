from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    Finding,
    K8sPort,
    PodInfo,
)
from hexawyn.application.ports.driven.logs_port import LogEntry, LogsPort
from hexawyn.application.ports.driven.runtime_port import InvestigationOutput, RuntimePort
from hexawyn.application.use_case.chat_cli.chat_cli_command import ChatCliCommand
from hexawyn.application.use_case.chat_cli.chat_cli_response import ChatCliResponse
from hexawyn.application.use_case.chat_cli.chat_cli_use_case import ChatCliUseCase
from hexawyn.domain.models.cluster import ClusterContext as DomainClusterContext


class ChatCliService(ChatCliUseCase):
    def __init__(
        self,
        k8s_port: K8sPort,
        runtime: RuntimePort,
        logs_port: LogsPort | None = None,
    ) -> None:
        self._k8s = k8s_port
        self._runtime = runtime
        self._logs = logs_port

    def execute(self, command: ChatCliCommand) -> ChatCliResponse:
        normalized = command.query.strip().lower()
        if not normalized:
            return ChatCliResponse(
                kind="unknown",
                lines=[("Type a command or click a suggestion.", "dim")],
            )
        return self._investigate(normalized, command.conversation_history)

    def _investigate(
        self, query: str, conversation_history: list[dict[str, str]] | None = None
    ) -> ChatCliResponse:
        k8s_ctx: ClusterContext = self._k8s.get_cluster_context()
        domain_ctx = DomainClusterContext(
            name=k8s_ctx["name"],
            namespace=k8s_ctx["namespace"],
        )
        self._runtime.set_adapter(self._k8s)
        output: InvestigationOutput = self._runtime.run_investigation(
            query, domain_ctx, conversation_history
        )
        return _build_response(output)

    def list_pods(self) -> ChatCliResponse:
        pods = self._k8s.list_pods()
        return ChatCliResponse(
            kind="pods",
            pods=pods,
            summary=_pods_summary(pods),
            suggestions=_suggested_chips(pods),
        )

    def show_logs(self, query: str) -> ChatCliResponse:
        if self._logs is None:
            return ChatCliResponse(
                kind="unknown",
                lines=[("Logs are not available for this cluster.", "yellow")],
            )
        pods = self._k8s.list_pods()
        pod = find_pod(query, pods)
        pattern = service_name(pod["name"]) if pod else query
        entries: list[LogEntry] = self._logs.search_logs(pattern=pattern, time_window_minutes=15)
        if not entries:
            return ChatCliResponse(
                kind="logs",
                lines=[(f'No logs found for "{pattern}".', "dim")],
            )
        lines = [(f"[{e['severity']}] {e['timestamp']}  {e['message']}", "dim") for e in entries]
        return ChatCliResponse(kind="logs", lines=lines)

    def explain_pending(self, findings: list[Finding]) -> ChatCliResponse:
        pods = [p for p in self._k8s.list_pods() if p["status"] == "Pending"]
        if not pods:
            return ChatCliResponse(kind="pending", lines=[("No pending pods.", "green")])
        lines: list[tuple[str, str]] = []
        for pod in pods:
            lines.append((f"{pod['name']} is waiting to be scheduled (Pending).", "yellow"))
            svc = service_name(pod["name"]).lower()
            for finding in findings:
                if svc in finding["message"].lower():
                    lines.append((f"  → {finding['remediation']}", "dim"))
        return ChatCliResponse(kind="pending", lines=lines)


def service_name(pod_name: str) -> str:
    parts = pod_name.split("-")
    if len(parts) <= 2:
        return pod_name
    return "-".join(parts[:-2])


def find_pod(normalized_text: str, pods: list[PodInfo]) -> PodInfo | None:
    for pod in pods:
        svc = service_name(pod["name"])
        if svc.lower() in normalized_text or pod["name"].lower() in normalized_text:
            return pod
    return None


def _pods_summary(pods: list[PodInfo]) -> str:
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


def _suggested_chips(pods: list[PodInfo]) -> list[str]:
    chips: list[str] = []
    crashed = next((p for p in pods if p["status"] == "CrashLoop"), None)
    pending = next((p for p in pods if p["status"] == "Pending"), None)
    running = next((p for p in pods if p["status"] == "Running"), None)
    if crashed:
        chips.append(f"debug {service_name(crashed['name'])}")
    if pending:
        chips.append(f"why is {service_name(pending['name'])} pending?")
    if running:
        chips.append(f"show logs for {service_name(running['name'])}")
    return chips


def _build_response(output: InvestigationOutput) -> ChatCliResponse:
    lines: list[tuple[str, str]] = []
    answer = output["answer"]
    if answer:
        lines.append((answer, "white"))
    error_msg = output["error"]
    if error_msg:
        lines.append((f"Error: {error_msg}", "red"))
    raw_suggestions = output["suggestions"]
    suggestions = list(raw_suggestions)[:4] if raw_suggestions else []
    return ChatCliResponse(kind="debug", lines=lines, suggestions=suggestions)
