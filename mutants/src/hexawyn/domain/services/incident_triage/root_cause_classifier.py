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
        "Review the most recent deployment/rollout for this workload; consider rolling back."
    ),
    IncidentCauseCategory.UNKNOWN: (
        "Investigate the affected objects' events and logs; no known failure pattern matched."
    ),
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_incident_cause__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_incident_cause__mutmut)
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


def x_classify_incident_cause__mutmut_orig(text: str) -> IncidentCauseCategory:
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


def x_classify_incident_cause__mutmut_1(text: str) -> IncidentCauseCategory:
    """Keyword classification of incident root-cause text (event reason/message,
    log line) into a functional category — same pattern as
    `failure_analysis.rca._classify_by_message`, checked most-specific first."""
    lower = None
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


def x_classify_incident_cause__mutmut_2(text: str) -> IncidentCauseCategory:
    """Keyword classification of incident root-cause text (event reason/message,
    log line) into a functional category — same pattern as
    `failure_analysis.rca._classify_by_message`, checked most-specific first."""
    lower = text.upper()
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


def x_classify_incident_cause__mutmut_3(text: str) -> IncidentCauseCategory:
    """Keyword classification of incident root-cause text (event reason/message,
    log line) into a functional category — same pattern as
    `failure_analysis.rca._classify_by_message`, checked most-specific first."""
    lower = text.lower()
    if any(None):
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


def x_classify_incident_cause__mutmut_4(text: str) -> IncidentCauseCategory:
    """Keyword classification of incident root-cause text (event reason/message,
    log line) into a functional category — same pattern as
    `failure_analysis.rca._classify_by_message`, checked most-specific first."""
    lower = text.lower()
    if any(keyword not in lower for keyword in _DATABASE_KEYWORDS):
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


def x_classify_incident_cause__mutmut_5(text: str) -> IncidentCauseCategory:
    """Keyword classification of incident root-cause text (event reason/message,
    log line) into a functional category — same pattern as
    `failure_analysis.rca._classify_by_message`, checked most-specific first."""
    lower = text.lower()
    if any(keyword in lower for keyword in _DATABASE_KEYWORDS):
        return IncidentCauseCategory.DATABASE
    if any(None):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(keyword in lower for keyword in _NETWORK_KEYWORDS):
        return IncidentCauseCategory.NETWORK
    if any(keyword in lower for keyword in _IMAGE_OR_CONFIG_KEYWORDS):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(keyword in lower for keyword in _DEPLOYMENT_KEYWORDS):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x_classify_incident_cause__mutmut_6(text: str) -> IncidentCauseCategory:
    """Keyword classification of incident root-cause text (event reason/message,
    log line) into a functional category — same pattern as
    `failure_analysis.rca._classify_by_message`, checked most-specific first."""
    lower = text.lower()
    if any(keyword in lower for keyword in _DATABASE_KEYWORDS):
        return IncidentCauseCategory.DATABASE
    if any(keyword not in lower for keyword in _RESOURCE_EXHAUSTION_KEYWORDS):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(keyword in lower for keyword in _NETWORK_KEYWORDS):
        return IncidentCauseCategory.NETWORK
    if any(keyword in lower for keyword in _IMAGE_OR_CONFIG_KEYWORDS):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(keyword in lower for keyword in _DEPLOYMENT_KEYWORDS):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x_classify_incident_cause__mutmut_7(text: str) -> IncidentCauseCategory:
    """Keyword classification of incident root-cause text (event reason/message,
    log line) into a functional category — same pattern as
    `failure_analysis.rca._classify_by_message`, checked most-specific first."""
    lower = text.lower()
    if any(keyword in lower for keyword in _DATABASE_KEYWORDS):
        return IncidentCauseCategory.DATABASE
    if any(keyword in lower for keyword in _RESOURCE_EXHAUSTION_KEYWORDS):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(None):
        return IncidentCauseCategory.NETWORK
    if any(keyword in lower for keyword in _IMAGE_OR_CONFIG_KEYWORDS):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(keyword in lower for keyword in _DEPLOYMENT_KEYWORDS):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x_classify_incident_cause__mutmut_8(text: str) -> IncidentCauseCategory:
    """Keyword classification of incident root-cause text (event reason/message,
    log line) into a functional category — same pattern as
    `failure_analysis.rca._classify_by_message`, checked most-specific first."""
    lower = text.lower()
    if any(keyword in lower for keyword in _DATABASE_KEYWORDS):
        return IncidentCauseCategory.DATABASE
    if any(keyword in lower for keyword in _RESOURCE_EXHAUSTION_KEYWORDS):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(keyword not in lower for keyword in _NETWORK_KEYWORDS):
        return IncidentCauseCategory.NETWORK
    if any(keyword in lower for keyword in _IMAGE_OR_CONFIG_KEYWORDS):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(keyword in lower for keyword in _DEPLOYMENT_KEYWORDS):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x_classify_incident_cause__mutmut_9(text: str) -> IncidentCauseCategory:
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
    if any(None):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(keyword in lower for keyword in _DEPLOYMENT_KEYWORDS):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x_classify_incident_cause__mutmut_10(text: str) -> IncidentCauseCategory:
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
    if any(keyword not in lower for keyword in _IMAGE_OR_CONFIG_KEYWORDS):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(keyword in lower for keyword in _DEPLOYMENT_KEYWORDS):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x_classify_incident_cause__mutmut_11(text: str) -> IncidentCauseCategory:
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
    if any(None):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x_classify_incident_cause__mutmut_12(text: str) -> IncidentCauseCategory:
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
    if any(keyword not in lower for keyword in _DEPLOYMENT_KEYWORDS):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN

mutants_x_classify_incident_cause__mutmut['_mutmut_orig'] = x_classify_incident_cause__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_1'] = x_classify_incident_cause__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_2'] = x_classify_incident_cause__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_3'] = x_classify_incident_cause__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_4'] = x_classify_incident_cause__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_5'] = x_classify_incident_cause__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_6'] = x_classify_incident_cause__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_7'] = x_classify_incident_cause__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_8'] = x_classify_incident_cause__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_9'] = x_classify_incident_cause__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_10'] = x_classify_incident_cause__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_11'] = x_classify_incident_cause__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_incident_cause__mutmut['x_classify_incident_cause__mutmut_12'] = x_classify_incident_cause__mutmut_12 # type: ignore # mutmut generated


def remediation_for(category: IncidentCauseCategory) -> str:
    return _REMEDIATION[category]
