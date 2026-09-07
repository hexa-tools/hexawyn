from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁRunbookSuggestionEngineǁsuggest__mutmut: MutantDict = {}  # type: ignore


class RunbookSuggestionEngine:
    """Maps a Kubernetes event REASON to the most relevant runbook. Pure
    Python, no I/O — unknown reasons fall back to generic troubleshooting
    steps rather than raising."""

    @_mutmut_mutated(mutants_xǁRunbookSuggestionEngineǁsuggest__mutmut)
    def suggest(self, reason: str) -> RunbookSuggestion:
        return _RUNBOOKS.get(reason, _GENERIC_FALLBACK)

    def xǁRunbookSuggestionEngineǁsuggest__mutmut_orig(self, reason: str) -> RunbookSuggestion:
        return _RUNBOOKS.get(reason, _GENERIC_FALLBACK)

    def xǁRunbookSuggestionEngineǁsuggest__mutmut_1(self, reason: str) -> RunbookSuggestion:
        return _RUNBOOKS.get(None, _GENERIC_FALLBACK)

    def xǁRunbookSuggestionEngineǁsuggest__mutmut_2(self, reason: str) -> RunbookSuggestion:
        return _RUNBOOKS.get(reason, None)

    def xǁRunbookSuggestionEngineǁsuggest__mutmut_3(self, reason: str) -> RunbookSuggestion:
        return _RUNBOOKS.get(_GENERIC_FALLBACK)

    def xǁRunbookSuggestionEngineǁsuggest__mutmut_4(self, reason: str) -> RunbookSuggestion:
        return _RUNBOOKS.get(reason, )

mutants_xǁRunbookSuggestionEngineǁsuggest__mutmut['_mutmut_orig'] = RunbookSuggestionEngine.xǁRunbookSuggestionEngineǁsuggest__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRunbookSuggestionEngineǁsuggest__mutmut['xǁRunbookSuggestionEngineǁsuggest__mutmut_1'] = RunbookSuggestionEngine.xǁRunbookSuggestionEngineǁsuggest__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRunbookSuggestionEngineǁsuggest__mutmut['xǁRunbookSuggestionEngineǁsuggest__mutmut_2'] = RunbookSuggestionEngine.xǁRunbookSuggestionEngineǁsuggest__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRunbookSuggestionEngineǁsuggest__mutmut['xǁRunbookSuggestionEngineǁsuggest__mutmut_3'] = RunbookSuggestionEngine.xǁRunbookSuggestionEngineǁsuggest__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRunbookSuggestionEngineǁsuggest__mutmut['xǁRunbookSuggestionEngineǁsuggest__mutmut_4'] = RunbookSuggestionEngine.xǁRunbookSuggestionEngineǁsuggest__mutmut_4 # type: ignore # mutmut generated
