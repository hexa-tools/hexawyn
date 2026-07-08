from __future__ import annotations

from hexawyn.domain.models.incident_triage import IncidentCauseCategory

_DATABASE_KEYWORDS = ("connection pool", "database", "postgres", "mysql", "db connection")
_RESOURCE_EXHAUSTION_KEYWORDS = ("oomkill", "out of memory", "memory", "evicted", "disk pressure")
_NETWORK_KEYWORDS = (
    "connection refused",
    "connection reset",
    "dial tcp",
    "no route to host",
    "dns",
)
_IMAGE_OR_CONFIG_KEYWORDS = (
    "imagepullbackoff",
    "errimagepull",
    "invalid configuration",
    "config file not found",
    "missing required field",
)
_DEPLOYMENT_KEYWORDS = ("crashloopbackoff", "back-off", "backoff", "failed scheduling")

_REMEDIATION: dict[IncidentCauseCategory, str] = {
    IncidentCauseCategory.DATABASE: (
        "Restore database connectivity — check the connection pool, credentials, "
        "and DB service/network path."
    ),
    IncidentCauseCategory.RESOURCE_EXHAUSTION: (
        "Increase memory/CPU limits or investigate a memory leak; consider "
        "rescheduling to a less saturated node."
    ),
    IncidentCauseCategory.NETWORK: (
        "Check network policies, DNS, and downstream service availability; "
        "verify the target endpoint is reachable."
    ),
    IncidentCauseCategory.IMAGE_OR_CONFIG: (
        "Verify the image tag/registry access and review the workload's "
        "configuration/environment variables."
    ),
    IncidentCauseCategory.DEPLOYMENT: (
        "Review the most recent deployment/rollout for this workload; " "consider rolling back."
    ),
    IncidentCauseCategory.UNKNOWN: (
        "Investigate the affected objects' events and logs; no known failure " "pattern matched."
    ),
}


def classify_incident_cause(text: str) -> IncidentCauseCategory:
    """Keyword classification of incident root-cause text (event reason/message,
    log line) into a functional category — same pattern as
    `failure_analysis.rca._classify_by_message`, checked most-specific first."""
    lower = text.lower()
    if any(keyword in lower for keyword in _DATABASE_KEYWORDS):
        return IncidentCauseCategory.DATABASE
    if any(keyword in lower for keyword in _RESOURCE_EXHAUSTION_KEYWORDS):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(keyword in lower for keyword in _NETWORK_KEYWORDS):
        return IncidentCauseCategory.NETWORK
    if any(keyword in lower for keyword in _IMAGE_OR_CONFIG_KEYWORDS):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(keyword in lower for keyword in _DEPLOYMENT_KEYWORDS):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def remediation_for(category: IncidentCauseCategory) -> str:
    return _REMEDIATION[category]
