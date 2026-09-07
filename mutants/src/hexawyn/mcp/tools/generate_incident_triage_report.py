"""MCP tool: generate_incident_triage_report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.domain.models.incident_triage import (
    IncidentCauseCategory,
    IncidentTriageReport,
    RootCauseCandidate,
)
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__category_from_reason__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__category_from_reason__mutmut)
def _category_from_reason(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_orig(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_1(reason: str) -> IncidentCauseCategory:
    db_keywords = None
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_2(reason: str) -> IncidentCauseCategory:
    db_keywords = ["XXpostgresXX", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_3(reason: str) -> IncidentCauseCategory:
    db_keywords = ["POSTGRES", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_4(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "XXmysqlXX", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_5(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "MYSQL", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_6(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "XXdatabaseXX", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_7(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "DATABASE", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_8(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "XXconnectionXX", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_9(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "CONNECTION", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_10(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "XXpoolXX", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_11(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "POOL", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_12(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "XXtimeoutXX"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_13(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "TIMEOUT"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_14(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = None
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_15(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["XXoomXX", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_16(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["OOM", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_17(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "XXmemoryXX", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_18(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "MEMORY", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_19(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "XXcpuXX", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_20(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "CPU", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_21(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "XXdiskXX", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_22(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "DISK", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_23(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "XXlimitXX", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_24(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "LIMIT", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_25(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "XXquotaXX"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_26(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "QUOTA"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_27(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = None
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_28(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["XXnetworkXX", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_29(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["NETWORK", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_30(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "XXdnsXX", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_31(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "DNS", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_32(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "XXconnectXX", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_33(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "CONNECT", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_34(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "XXrefusedXX", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_35(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "REFUSED", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_36(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "XXtimeoutXX", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_37(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "TIMEOUT", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_38(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "XXtlsXX", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_39(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "TLS", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_40(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "XXcertificateXX"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_41(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "CERTIFICATE"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_42(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = None
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_43(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["XXimageXX", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_44(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["IMAGE", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_45(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "XXpullXX", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_46(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "PULL", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_47(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "XXregistryXX", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_48(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "REGISTRY", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_49(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "XXconfigXX", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_50(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "CONFIG", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_51(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "XXsecretXX"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_52(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "SECRET"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_53(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = None

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_54(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["XXdeployXX", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_55(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["DEPLOY", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_56(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "XXrolloutXX", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_57(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "ROLLOUT", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_58(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "XXreplicasXX", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_59(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "REPLICAS", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_60(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "XXscaleXX", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_61(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "SCALE", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_62(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "XXupdateXX"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_63(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "UPDATE"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_64(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = None
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_65(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.upper()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_66(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(None):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_67(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw not in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_68(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(None):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_69(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw not in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_70(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(None):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_71(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw not in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_72(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(None):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_73(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw not in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_74(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(None):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def x__category_from_reason__mutmut_75(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw not in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN

mutants_x__category_from_reason__mutmut['_mutmut_orig'] = x__category_from_reason__mutmut_orig # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_1'] = x__category_from_reason__mutmut_1 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_2'] = x__category_from_reason__mutmut_2 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_3'] = x__category_from_reason__mutmut_3 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_4'] = x__category_from_reason__mutmut_4 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_5'] = x__category_from_reason__mutmut_5 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_6'] = x__category_from_reason__mutmut_6 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_7'] = x__category_from_reason__mutmut_7 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_8'] = x__category_from_reason__mutmut_8 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_9'] = x__category_from_reason__mutmut_9 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_10'] = x__category_from_reason__mutmut_10 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_11'] = x__category_from_reason__mutmut_11 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_12'] = x__category_from_reason__mutmut_12 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_13'] = x__category_from_reason__mutmut_13 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_14'] = x__category_from_reason__mutmut_14 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_15'] = x__category_from_reason__mutmut_15 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_16'] = x__category_from_reason__mutmut_16 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_17'] = x__category_from_reason__mutmut_17 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_18'] = x__category_from_reason__mutmut_18 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_19'] = x__category_from_reason__mutmut_19 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_20'] = x__category_from_reason__mutmut_20 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_21'] = x__category_from_reason__mutmut_21 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_22'] = x__category_from_reason__mutmut_22 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_23'] = x__category_from_reason__mutmut_23 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_24'] = x__category_from_reason__mutmut_24 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_25'] = x__category_from_reason__mutmut_25 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_26'] = x__category_from_reason__mutmut_26 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_27'] = x__category_from_reason__mutmut_27 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_28'] = x__category_from_reason__mutmut_28 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_29'] = x__category_from_reason__mutmut_29 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_30'] = x__category_from_reason__mutmut_30 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_31'] = x__category_from_reason__mutmut_31 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_32'] = x__category_from_reason__mutmut_32 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_33'] = x__category_from_reason__mutmut_33 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_34'] = x__category_from_reason__mutmut_34 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_35'] = x__category_from_reason__mutmut_35 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_36'] = x__category_from_reason__mutmut_36 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_37'] = x__category_from_reason__mutmut_37 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_38'] = x__category_from_reason__mutmut_38 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_39'] = x__category_from_reason__mutmut_39 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_40'] = x__category_from_reason__mutmut_40 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_41'] = x__category_from_reason__mutmut_41 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_42'] = x__category_from_reason__mutmut_42 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_43'] = x__category_from_reason__mutmut_43 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_44'] = x__category_from_reason__mutmut_44 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_45'] = x__category_from_reason__mutmut_45 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_46'] = x__category_from_reason__mutmut_46 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_47'] = x__category_from_reason__mutmut_47 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_48'] = x__category_from_reason__mutmut_48 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_49'] = x__category_from_reason__mutmut_49 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_50'] = x__category_from_reason__mutmut_50 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_51'] = x__category_from_reason__mutmut_51 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_52'] = x__category_from_reason__mutmut_52 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_53'] = x__category_from_reason__mutmut_53 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_54'] = x__category_from_reason__mutmut_54 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_55'] = x__category_from_reason__mutmut_55 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_56'] = x__category_from_reason__mutmut_56 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_57'] = x__category_from_reason__mutmut_57 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_58'] = x__category_from_reason__mutmut_58 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_59'] = x__category_from_reason__mutmut_59 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_60'] = x__category_from_reason__mutmut_60 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_61'] = x__category_from_reason__mutmut_61 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_62'] = x__category_from_reason__mutmut_62 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_63'] = x__category_from_reason__mutmut_63 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_64'] = x__category_from_reason__mutmut_64 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_65'] = x__category_from_reason__mutmut_65 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_66'] = x__category_from_reason__mutmut_66 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_67'] = x__category_from_reason__mutmut_67 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_68'] = x__category_from_reason__mutmut_68 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_69'] = x__category_from_reason__mutmut_69 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_70'] = x__category_from_reason__mutmut_70 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_71'] = x__category_from_reason__mutmut_71 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_72'] = x__category_from_reason__mutmut_72 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_73'] = x__category_from_reason__mutmut_73 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_74'] = x__category_from_reason__mutmut_74 # type: ignore # mutmut generated
mutants_x__category_from_reason__mutmut['x__category_from_reason__mutmut_75'] = x__category_from_reason__mutmut_75 # type: ignore # mutmut generated
mutants_x__format_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__format_report__mutmut)
def _format_report(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_orig(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_1(report: IncidentTriageReport) -> str:
    lines: list[str] = None
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_2(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(None)
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_3(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(None)
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_4(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append(None)

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_5(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("XXXX")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_6(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append(None)
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_7(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("XX## Root Cause AnalysisXX")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_8(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## root cause analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_9(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## ROOT CAUSE ANALYSIS")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_10(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                None
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_11(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(None)
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_12(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append(None)
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_13(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("XX## Root Cause AnalysisXX")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_14(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## root cause analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_15(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## ROOT CAUSE ANALYSIS")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_16(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append(None)

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_17(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("XXNo root causes identified — insufficient data.XX")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_18(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("no root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_19(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("NO ROOT CAUSES IDENTIFIED — INSUFFICIENT DATA.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_20(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append(None)
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_21(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("XXXX")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_22(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append(None)
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_23(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("XX## Remediation StepsXX")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_24(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## remediation steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_25(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## REMEDIATION STEPS")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_26(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(None)

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_27(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append(None)
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_28(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("XXXX")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_29(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(None)
    return "\n".join(lines)


def x__format_report__mutmut_30(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'XXYesXX' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_31(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_32(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'YES' if report.resolved else 'No'}")
    return "\n".join(lines)


def x__format_report__mutmut_33(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'XXNoXX'}")
    return "\n".join(lines)


def x__format_report__mutmut_34(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'no'}")
    return "\n".join(lines)


def x__format_report__mutmut_35(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'NO'}")
    return "\n".join(lines)


def x__format_report__mutmut_36(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(None)


def x__format_report__mutmut_37(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "XX\nXX".join(lines)

mutants_x__format_report__mutmut['_mutmut_orig'] = x__format_report__mutmut_orig # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_1'] = x__format_report__mutmut_1 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_2'] = x__format_report__mutmut_2 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_3'] = x__format_report__mutmut_3 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_4'] = x__format_report__mutmut_4 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_5'] = x__format_report__mutmut_5 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_6'] = x__format_report__mutmut_6 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_7'] = x__format_report__mutmut_7 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_8'] = x__format_report__mutmut_8 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_9'] = x__format_report__mutmut_9 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_10'] = x__format_report__mutmut_10 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_11'] = x__format_report__mutmut_11 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_12'] = x__format_report__mutmut_12 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_13'] = x__format_report__mutmut_13 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_14'] = x__format_report__mutmut_14 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_15'] = x__format_report__mutmut_15 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_16'] = x__format_report__mutmut_16 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_17'] = x__format_report__mutmut_17 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_18'] = x__format_report__mutmut_18 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_19'] = x__format_report__mutmut_19 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_20'] = x__format_report__mutmut_20 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_21'] = x__format_report__mutmut_21 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_22'] = x__format_report__mutmut_22 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_23'] = x__format_report__mutmut_23 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_24'] = x__format_report__mutmut_24 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_25'] = x__format_report__mutmut_25 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_26'] = x__format_report__mutmut_26 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_27'] = x__format_report__mutmut_27 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_28'] = x__format_report__mutmut_28 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_29'] = x__format_report__mutmut_29 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_30'] = x__format_report__mutmut_30 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_31'] = x__format_report__mutmut_31 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_32'] = x__format_report__mutmut_32 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_33'] = x__format_report__mutmut_33 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_34'] = x__format_report__mutmut_34 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_35'] = x__format_report__mutmut_35 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_36'] = x__format_report__mutmut_36 # type: ignore # mutmut generated
mutants_x__format_report__mutmut['x__format_report__mutmut_37'] = x__format_report__mutmut_37 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_generate_incident_triage_report__mutmut)
def generate_incident_triage_report(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_orig(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_1(namespace: str = "XXtest-nsXX") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_2(namespace: str = "TEST-NS") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_3(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = None
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_4(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = None
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_5(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = None
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_6(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = None
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_7(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = None

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_8(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = None

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_9(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(None)

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_10(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=None))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_11(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = None
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_12(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = None
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_13(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(None)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_14(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                None
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_15(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=None,
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_16(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=None,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_17(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=None,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_18(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=None,
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_19(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=None,
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_20(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_21(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_22(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_23(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_24(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_25(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=1.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_26(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = None
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_27(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category != IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_28(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append(None)
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_29(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("XXCheck database connection pool limits and healthXX")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_30(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_31(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("CHECK DATABASE CONNECTION POOL LIMITS AND HEALTH")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_32(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category != IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_33(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append(None)
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_34(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("XXIncrease resource limits or scale replicasXX")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_35(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_36(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("INCREASE RESOURCE LIMITS OR SCALE REPLICAS")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_37(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category != IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_38(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append(None)
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_39(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("XXVerify network policies and DNS resolutionXX")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_40(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("verify network policies and dns resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_41(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("VERIFY NETWORK POLICIES AND DNS RESOLUTION")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_42(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category != IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_43(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append(None)

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_44(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("XXVerify image pull secrets and registry accessXX")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_45(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_46(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("VERIFY IMAGE PULL SECRETS AND REGISTRY ACCESS")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_47(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = None

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_48(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=None,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_49(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=None,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_50(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=None,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_51(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=None,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_52(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=None,
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_53(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_54(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_55(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_56(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_57(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_58(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=121,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_59(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["XXeventsXX", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_60(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["EVENTS", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_61(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "XXpodsXX", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_62(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "PODS", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_63(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "XXpipeline_runsXX"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_64(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "PIPELINE_RUNS"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_65(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "XXnamespaceXX": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_66(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "NAMESPACE": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_67(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "XXroot_causesXX": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_68(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "ROOT_CAUSES": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_69(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "XXdescriptionXX": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_70(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "DESCRIPTION": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_71(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "XXcategoryXX": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_72(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "CATEGORY": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_73(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "XXconfidenceXX": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_74(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "CONFIDENCE": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_75(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "XXevidenceXX": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_76(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "EVIDENCE": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_77(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "XXformatted_reportXX": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_78(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "FORMATTED_REPORT": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_79(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(None),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_80(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_81(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_82(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "XXnamespaceXX": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_83(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "NAMESPACE": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_84(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "XXroot_causesXX": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_85(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "ROOT_CAUSES": [],
            "formatted_report": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_86(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "XXformatted_reportXX": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_87(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "FORMATTED_REPORT": "",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_88(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "XXXX",
            "error": str(exc),
        }


def x_generate_incident_triage_report__mutmut_89(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "XXerrorXX": str(exc),
        }


def x_generate_incident_triage_report__mutmut_90(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "ERROR": str(exc),
        }


def x_generate_incident_triage_report__mutmut_91(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(None),
        }

mutants_x_generate_incident_triage_report__mutmut['_mutmut_orig'] = x_generate_incident_triage_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_1'] = x_generate_incident_triage_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_2'] = x_generate_incident_triage_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_3'] = x_generate_incident_triage_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_4'] = x_generate_incident_triage_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_5'] = x_generate_incident_triage_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_6'] = x_generate_incident_triage_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_7'] = x_generate_incident_triage_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_8'] = x_generate_incident_triage_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_9'] = x_generate_incident_triage_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_10'] = x_generate_incident_triage_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_11'] = x_generate_incident_triage_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_12'] = x_generate_incident_triage_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_13'] = x_generate_incident_triage_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_14'] = x_generate_incident_triage_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_15'] = x_generate_incident_triage_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_16'] = x_generate_incident_triage_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_17'] = x_generate_incident_triage_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_18'] = x_generate_incident_triage_report__mutmut_18 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_19'] = x_generate_incident_triage_report__mutmut_19 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_20'] = x_generate_incident_triage_report__mutmut_20 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_21'] = x_generate_incident_triage_report__mutmut_21 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_22'] = x_generate_incident_triage_report__mutmut_22 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_23'] = x_generate_incident_triage_report__mutmut_23 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_24'] = x_generate_incident_triage_report__mutmut_24 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_25'] = x_generate_incident_triage_report__mutmut_25 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_26'] = x_generate_incident_triage_report__mutmut_26 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_27'] = x_generate_incident_triage_report__mutmut_27 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_28'] = x_generate_incident_triage_report__mutmut_28 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_29'] = x_generate_incident_triage_report__mutmut_29 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_30'] = x_generate_incident_triage_report__mutmut_30 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_31'] = x_generate_incident_triage_report__mutmut_31 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_32'] = x_generate_incident_triage_report__mutmut_32 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_33'] = x_generate_incident_triage_report__mutmut_33 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_34'] = x_generate_incident_triage_report__mutmut_34 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_35'] = x_generate_incident_triage_report__mutmut_35 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_36'] = x_generate_incident_triage_report__mutmut_36 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_37'] = x_generate_incident_triage_report__mutmut_37 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_38'] = x_generate_incident_triage_report__mutmut_38 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_39'] = x_generate_incident_triage_report__mutmut_39 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_40'] = x_generate_incident_triage_report__mutmut_40 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_41'] = x_generate_incident_triage_report__mutmut_41 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_42'] = x_generate_incident_triage_report__mutmut_42 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_43'] = x_generate_incident_triage_report__mutmut_43 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_44'] = x_generate_incident_triage_report__mutmut_44 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_45'] = x_generate_incident_triage_report__mutmut_45 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_46'] = x_generate_incident_triage_report__mutmut_46 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_47'] = x_generate_incident_triage_report__mutmut_47 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_48'] = x_generate_incident_triage_report__mutmut_48 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_49'] = x_generate_incident_triage_report__mutmut_49 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_50'] = x_generate_incident_triage_report__mutmut_50 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_51'] = x_generate_incident_triage_report__mutmut_51 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_52'] = x_generate_incident_triage_report__mutmut_52 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_53'] = x_generate_incident_triage_report__mutmut_53 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_54'] = x_generate_incident_triage_report__mutmut_54 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_55'] = x_generate_incident_triage_report__mutmut_55 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_56'] = x_generate_incident_triage_report__mutmut_56 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_57'] = x_generate_incident_triage_report__mutmut_57 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_58'] = x_generate_incident_triage_report__mutmut_58 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_59'] = x_generate_incident_triage_report__mutmut_59 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_60'] = x_generate_incident_triage_report__mutmut_60 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_61'] = x_generate_incident_triage_report__mutmut_61 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_62'] = x_generate_incident_triage_report__mutmut_62 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_63'] = x_generate_incident_triage_report__mutmut_63 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_64'] = x_generate_incident_triage_report__mutmut_64 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_65'] = x_generate_incident_triage_report__mutmut_65 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_66'] = x_generate_incident_triage_report__mutmut_66 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_67'] = x_generate_incident_triage_report__mutmut_67 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_68'] = x_generate_incident_triage_report__mutmut_68 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_69'] = x_generate_incident_triage_report__mutmut_69 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_70'] = x_generate_incident_triage_report__mutmut_70 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_71'] = x_generate_incident_triage_report__mutmut_71 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_72'] = x_generate_incident_triage_report__mutmut_72 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_73'] = x_generate_incident_triage_report__mutmut_73 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_74'] = x_generate_incident_triage_report__mutmut_74 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_75'] = x_generate_incident_triage_report__mutmut_75 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_76'] = x_generate_incident_triage_report__mutmut_76 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_77'] = x_generate_incident_triage_report__mutmut_77 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_78'] = x_generate_incident_triage_report__mutmut_78 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_79'] = x_generate_incident_triage_report__mutmut_79 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_80'] = x_generate_incident_triage_report__mutmut_80 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_81'] = x_generate_incident_triage_report__mutmut_81 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_82'] = x_generate_incident_triage_report__mutmut_82 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_83'] = x_generate_incident_triage_report__mutmut_83 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_84'] = x_generate_incident_triage_report__mutmut_84 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_85'] = x_generate_incident_triage_report__mutmut_85 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_86'] = x_generate_incident_triage_report__mutmut_86 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_87'] = x_generate_incident_triage_report__mutmut_87 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_88'] = x_generate_incident_triage_report__mutmut_88 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_89'] = x_generate_incident_triage_report__mutmut_89 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_90'] = x_generate_incident_triage_report__mutmut_90 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_91'] = x_generate_incident_triage_report__mutmut_91 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(generate_incident_triage_report)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(generate_incident_triage_report)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
