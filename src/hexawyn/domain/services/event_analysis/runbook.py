from dataclasses import dataclass, field


@dataclass(frozen=True)
class RunbookSuggestion:
    """A runbook suggested for a given event REASON."""

    runbook_id: str
    title: str
    steps: list[str] = field(default_factory=list)


_GENERIC_FALLBACK = RunbookSuggestion(
    runbook_id="runbook-generic-001",
    title="Generic troubleshooting steps",
    steps=[
        "Check pod logs for the affected object",
        "Check recent deployments and configuration changes",
        "Check resource utilization (CPU, memory, disk) on the node",
    ],
)

_RUNBOOKS: dict[str, RunbookSuggestion] = {
    "OOMKilling": RunbookSuggestion(
        runbook_id="runbook-memory-001",
        title="Increase memory limit or investigate memory leak",
        steps=[
            "Check container memory usage trend before the OOM kill",
            "Increase the pod's memory limit if usage is legitimate",
            "Profile the application for a memory leak if usage keeps climbing",
        ],
    ),
    "OOMKilled": RunbookSuggestion(
        runbook_id="runbook-memory-001",
        title="Increase memory limit or investigate memory leak",
        steps=[
            "Check container memory usage trend before the OOM kill",
            "Increase the pod's memory limit if usage is legitimate",
            "Profile the application for a memory leak if usage keeps climbing",
        ],
    ),
    "BackOff": RunbookSuggestion(
        runbook_id="runbook-crashloop-001",
        title="Investigate container crash loop",
        steps=[
            "Check container logs for the crash reason",
            "Verify the startup command and image pull policy",
            "Check readiness/liveness probe configuration",
        ],
    ),
    "CrashLoopBackOff": RunbookSuggestion(
        runbook_id="runbook-crashloop-001",
        title="Investigate container crash loop",
        steps=[
            "Check container logs for the crash reason",
            "Verify the startup command and image pull policy",
            "Check readiness/liveness probe configuration",
        ],
    ),
    "FailedScheduling": RunbookSuggestion(
        runbook_id="runbook-scheduling-001",
        title="Resolve pod scheduling failure",
        steps=[
            "Check node resource capacity and taints/tolerations",
            "Verify node affinity and anti-affinity rules",
            "Check for insufficient CPU/memory across the cluster",
        ],
    ),
    "FailedMount": RunbookSuggestion(
        runbook_id="runbook-storage-001",
        title="Resolve volume mount failure",
        steps=[
            "Verify the PVC is bound and the storage class exists",
            "Check the CSI driver logs for mount errors",
            "Confirm the volume is not already attached to another node",
        ],
    ),
}


class RunbookSuggestionEngine:
    """Maps a Kubernetes event REASON to the most relevant runbook. Pure
    Python, no I/O — unknown reasons fall back to generic troubleshooting
    steps rather than raising."""

    def suggest(self, reason: str) -> RunbookSuggestion:
        return _RUNBOOKS.get(reason, _GENERIC_FALLBACK)
