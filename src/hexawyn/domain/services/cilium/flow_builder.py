"""Pure Hubble flow mapping and filtering — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumFlowEntry,
    CiliumFlowQuery,
    CiliumFlowsResult,
)

_NOT_INSTALLED_NOTE = "Hubble relay is not available in this cluster"


def build_flows(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def not_installed_flows_result() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="not_installed",
        total_flows=0,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def _to_entry(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def _extract_policy(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def _matches(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def _any_namespace(entry: CiliumFlowEntry, namespace: str) -> bool:
    return namespace in (entry.source_namespace, entry.destination_namespace)


def _as_dict(value: object) -> dict[str, object]:
    return value if isinstance(value, dict) else {}


def _as_str(value: object) -> str | None:
    return str(value) if value is not None else None
