"""VolumeSnapshot tools — query snapshot.storage.k8s.io CRDs."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def snapshots_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
                version="v1",
                namespace=namespace,
                plural="volumesnapshots",
            )
        else:
            raw = crd.list_cluster_custom_object(  # type: ignore
                group="snapshot.storage.k8s.io",
                version="v1",
                plural="volumesnapshots",
            )
    except Exception as exc:
        return {"snapshots": [], "error": str(exc)}

    items = raw.get("items", []) if isinstance(raw, dict) else []
    results: list[dict[str, object]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        meta = item.get("metadata", {}) if isinstance(item.get("metadata"), dict) else {}
        spec = item.get("spec", {}) if isinstance(item.get("spec"), dict) else {}
        status = item.get("status", {}) if isinstance(item.get("status"), dict) else {}
        ready = status.get("readyToUse", False)
        results.append(
            {
                "name": str(meta.get("name", "")),
                "namespace": str(meta.get("namespace", "default")),
                "snapshot_class": str(spec.get("volumeSnapshotClassName", "")),
                "source_pvc": str(spec.get("source", {}).get("persistentVolumeClaimName", ""))
                if isinstance(spec.get("source"), dict)
                else "",
                "ready": bool(ready),
                "creation_time": str(meta.get("creationTimestamp", "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def snapshot_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="v1",
            namespace=namespace,
            plural="volumesnapshots",
            name=name,
        )
    except Exception as exc:
        return {"name": "", "namespace": "", "error": str(exc)}

    if not isinstance(raw, dict):
        return {"name": "", "namespace": "", "error": "Not found"}
    meta = raw.get("metadata", {}) if isinstance(raw.get("metadata"), dict) else {}
    spec = raw.get("spec", {}) if isinstance(raw.get("spec"), dict) else {}
    status = raw.get("status", {}) if isinstance(raw.get("status"), dict) else {}
    return {
        "name": str(meta.get("name", "")),
        "namespace": str(meta.get("namespace", "default")),
        "snapshot_class": str(spec.get("volumeSnapshotClassName", "")),
        "source_pvc": str(spec.get("source", {}).get("persistentVolumeClaimName", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(snapshots_list)
    mcp.tool()(snapshot_get)
