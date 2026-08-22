#!/usr/bin/env python3
"""Sync intent_examples.yaml from hexa-control-plane into hexawyn.

Copies the `description` field for every shared use case key and adds
missing descriptions for hexawyn-only use cases. Control-plane is the
source of truth for descriptions.

Usage:
    poetry run python scripts/sync_intent_examples.py
"""

from __future__ import annotations

from pathlib import Path

import yaml

HEXAWYN_PATH = Path(__file__).parent.parent / "datasets" / "intent_examples.yaml"
CONTROL_PLANE_PATH = (
    Path.home() / "sites" / "hexa-control-plane" / "datasets" / "intent_examples.yaml"
)

# hexawyn-only use cases -> hand-written descriptions (not in control-plane)
_HEXAWYN_ONLY_DESCRIPTIONS = {
    "container_image_vulnerability_scanning": (
        "Scan container images for known vulnerabilities, including EOL base images, "
        "critical CVEs and missing patch levels, and flag production workloads."
    ),
    "pod_security_standards_audit": (
        "Audit pods against Pod Security Standards, flagging privileged pods, "
        "host-network usage and dangerous capabilities."
    ),
}

# Registered MCP tools with no intent entry anywhere -> full hand-written entries.
_EXTRA_USE_CASES = {
    "list_openshift_projects": {
        "tool": "list_openshift_projects",
        "description": (
            "OpenShift-only. List OpenShift projects (namespaces) with their status and "
            "display name, the full project inventory of the OCP cluster. For non-OpenShift "
            "clusters, use list_namespaces directly."
        ),
        "questions": [
            "List all OpenShift projects and their current status.",
            "What projects exist on this OCP cluster and how are they doing?",
            "Show me every project with its display name on the OpenShift cluster.",
            "Which OpenShift projects are in the cluster right now?",
            "Give me the full project inventory of the OpenShift cluster.",
        ],
    },
    "list_openshift_routes": {
        "tool": "list_openshift_routes",
        "description": (
            "OpenShift-only. List OpenShift Routes and ingresses exposed in a namespace, "
            "their target services, hostnames, and whether TLS termination is enabled. "
            "For non-OpenShift clusters, use list_ingresses directly."
        ),
        "questions": [
            "Which routes are exposed in the payments namespace, and are they TLS-enabled?",
            "List all OpenShift routes targeting the checkout service.",
            "Show me the hostnames and TLS status of routes in production.",
            "Are there any OpenShift routes without TLS termination in staging?",
            "List the routes and their backend services in the default namespace.",
        ],
    },
    "list_openshift_sccs": {
        "tool": "list_openshift_sccs",
        "description": (
            "OpenShift-only. List SecurityContextConstraints (SCC) in the cluster, showing "
            "which ones allow privileged containers, host namespaces or run-as-any user. "
            "SCCs are an OpenShift concept and do not apply to vanilla Kubernetes."
        ),
        "questions": [
            "List all SecurityContextConstraints on this OpenShift cluster.",
            "Which SCCs allow privileged containers or host namespaces?",
            "Show me the most permissive SCCs and what they allow.",
            "Is there an SCC granting run-as-any user on the cluster?",
            "Audit the SCCs for privilege escalation risks.",
        ],
    },
    "list_openshift_imagestreams": {
        "tool": "list_openshift_imagestreams",
        "description": (
            "OpenShift-only. List ImageStreams in a namespace or the whole cluster, showing "
            "image tags and their tracked build sources. ImageStreams are an OpenShift "
            "concept and do not apply to vanilla Kubernetes."
        ),
        "questions": [
            "List the ImageStreams in the checkout namespace.",
            "Show me all ImageStreams on the OpenShift cluster.",
            "How many image tags are tracked in the frontend ImageStream?",
            "List ImageStreams and their build sources in production.",
            "Which image streams exist in the default namespace?",
        ],
    },
    "get_quota_usage": {
        "tool": "get_quota_usage",
        "description": (
            "Generate a usage ledger for billing — how many investigations were run this "
            "month, which tools consume the most SLM time, average investigation duration, "
            "and token consumption."
        ),
        "questions": [
            "How many investigations did I run this month?",
            "Which tools consume the most SLM time?",
            "What is my average investigation duration this month?",
            "Show me my token consumption and quota usage.",
            "Generate a usage ledger report for billing.",
        ],
    },
}


def _load(path: Path) -> dict[str, dict[str, object]]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return {k: v for k, v in data.items() if isinstance(v, dict)}


def _dump(path: Path, data: dict[str, dict[str, object]]) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False, width=100), encoding="utf-8")


def sync() -> int:
    control = _load(CONTROL_PLANE_PATH)
    local = _load(HEXAWYN_PATH)

    updated = 0
    for use_case, entry in local.items():
        control_entry = control.get(use_case)
        if control_entry and control_entry.get("description"):
            description = str(control_entry["description"])
        else:
            description = _HEXAWYN_ONLY_DESCRIPTIONS.get(use_case, "")
        if description and entry.get("description") != description:
            entry["description"] = description
            updated += 1

    # Copy over use cases that exist in control-plane but are missing locally
    # (their MCP tools are registered, so their intent examples must exist too).
    for use_case, control_entry in control.items():
        if use_case in local:
            continue
        if not isinstance(control_entry, dict) or not control_entry.get("tool"):
            continue
        local[use_case] = dict(control_entry)
        updated += 1

    # Add registered tools that have no intent entry anywhere (OpenShift + quota).
    for use_case, entry in _EXTRA_USE_CASES.items():
        existing = local.get(use_case)
        is_canonical = existing and existing.get("tool") == entry["tool"]
        if not existing or not is_canonical:
            local[use_case] = dict(entry)
            updated += 1

    _dump(HEXAWYN_PATH, local)
    return updated


if __name__ == "__main__":
    count = sync()
    print(f"✅ Synced {count} descriptions into datasets/intent_examples.yaml")
