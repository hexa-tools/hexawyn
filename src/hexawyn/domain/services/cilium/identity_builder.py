"""Pure Cilium security-identity listing — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumIdentitiesResult,
    CiliumIdentityInfo,
)

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"


def _as_dict(value: object) -> dict[str, object]:
    return value if isinstance(value, dict) else {}


def build_identities_result(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def not_installed_identities_result() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="not_installed",
        total_identities=0,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def _extract_labels(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def _count_endpoint_ids(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, 0) + 1
    return counts


def _endpoint_identity_id(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None
