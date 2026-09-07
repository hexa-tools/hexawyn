"""VolumeSnapshot tools — query snapshot.storage.k8s.io CRDs."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_snapshots_list__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_snapshots_list__mutmut)
def snapshots_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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


def x_snapshots_list__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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


def x_snapshots_list__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = None
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


def x_snapshots_list__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name=None)
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


def x_snapshots_list__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="XXdefaultXX")
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


def x_snapshots_list__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="DEFAULT")
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


def x_snapshots_list__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = None
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


def x_snapshots_list__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = None
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


def x_snapshots_list__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group=None,
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


def x_snapshots_list__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
                version=None,
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


def x_snapshots_list__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
                version="v1",
                namespace=None,
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


def x_snapshots_list__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
                version="v1",
                namespace=namespace,
                plural=None,
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


def x_snapshots_list__mutmut_11(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
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


def x_snapshots_list__mutmut_12(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
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


def x_snapshots_list__mutmut_13(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
                version="v1",
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


def x_snapshots_list__mutmut_14(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
                version="v1",
                namespace=namespace,
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


def x_snapshots_list__mutmut_15(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="XXsnapshot.storage.k8s.ioXX",
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


def x_snapshots_list__mutmut_16(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="SNAPSHOT.STORAGE.K8S.IO",
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


def x_snapshots_list__mutmut_17(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
                version="XXv1XX",
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


def x_snapshots_list__mutmut_18(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
                version="V1",
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


def x_snapshots_list__mutmut_19(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
                version="v1",
                namespace=namespace,
                plural="XXvolumesnapshotsXX",
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


def x_snapshots_list__mutmut_20(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        if namespace:
            raw = crd.list_namespaced_custom_object(
                group="snapshot.storage.k8s.io",
                version="v1",
                namespace=namespace,
                plural="VOLUMESNAPSHOTS",
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


def x_snapshots_list__mutmut_21(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
            raw = None
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


def x_snapshots_list__mutmut_22(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                group=None,
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


def x_snapshots_list__mutmut_23(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                version=None,
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


def x_snapshots_list__mutmut_24(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                plural=None,
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


def x_snapshots_list__mutmut_25(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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


def x_snapshots_list__mutmut_26(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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


def x_snapshots_list__mutmut_27(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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


def x_snapshots_list__mutmut_28(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                group="XXsnapshot.storage.k8s.ioXX",
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


def x_snapshots_list__mutmut_29(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                group="SNAPSHOT.STORAGE.K8S.IO",
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


def x_snapshots_list__mutmut_30(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                version="XXv1XX",
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


def x_snapshots_list__mutmut_31(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                version="V1",
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


def x_snapshots_list__mutmut_32(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                plural="XXvolumesnapshotsXX",
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


def x_snapshots_list__mutmut_33(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                plural="VOLUMESNAPSHOTS",
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


def x_snapshots_list__mutmut_34(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"XXsnapshotsXX": [], "error": str(exc)}

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


def x_snapshots_list__mutmut_35(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"SNAPSHOTS": [], "error": str(exc)}

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


def x_snapshots_list__mutmut_36(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"snapshots": [], "XXerrorXX": str(exc)}

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


def x_snapshots_list__mutmut_37(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"snapshots": [], "ERROR": str(exc)}

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


def x_snapshots_list__mutmut_38(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"snapshots": [], "error": str(None)}

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


def x_snapshots_list__mutmut_39(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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

    items = None
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


def x_snapshots_list__mutmut_40(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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

    items = raw.get(None, []) if isinstance(raw, dict) else []
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


def x_snapshots_list__mutmut_41(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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

    items = raw.get("items", None) if isinstance(raw, dict) else []
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


def x_snapshots_list__mutmut_42(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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

    items = raw.get([]) if isinstance(raw, dict) else []
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


def x_snapshots_list__mutmut_43(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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

    items = raw.get("items", ) if isinstance(raw, dict) else []
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


def x_snapshots_list__mutmut_44(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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

    items = raw.get("XXitemsXX", []) if isinstance(raw, dict) else []
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


def x_snapshots_list__mutmut_45(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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

    items = raw.get("ITEMS", []) if isinstance(raw, dict) else []
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


def x_snapshots_list__mutmut_46(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    results: list[dict[str, object]] = None
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


def x_snapshots_list__mutmut_47(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        if isinstance(item, dict):
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


def x_snapshots_list__mutmut_48(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
            break
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


def x_snapshots_list__mutmut_49(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        meta = None
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


def x_snapshots_list__mutmut_50(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        meta = item.get(None, {}) if isinstance(item.get("metadata"), dict) else {}
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


def x_snapshots_list__mutmut_51(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        meta = item.get("metadata", None) if isinstance(item.get("metadata"), dict) else {}
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


def x_snapshots_list__mutmut_52(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        meta = item.get({}) if isinstance(item.get("metadata"), dict) else {}
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


def x_snapshots_list__mutmut_53(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        meta = item.get("metadata", ) if isinstance(item.get("metadata"), dict) else {}
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


def x_snapshots_list__mutmut_54(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        meta = item.get("XXmetadataXX", {}) if isinstance(item.get("metadata"), dict) else {}
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


def x_snapshots_list__mutmut_55(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        meta = item.get("METADATA", {}) if isinstance(item.get("metadata"), dict) else {}
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


def x_snapshots_list__mutmut_56(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        spec = None
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


def x_snapshots_list__mutmut_57(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        spec = item.get(None, {}) if isinstance(item.get("spec"), dict) else {}
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


def x_snapshots_list__mutmut_58(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        spec = item.get("spec", None) if isinstance(item.get("spec"), dict) else {}
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


def x_snapshots_list__mutmut_59(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        spec = item.get({}) if isinstance(item.get("spec"), dict) else {}
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


def x_snapshots_list__mutmut_60(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        spec = item.get("spec", ) if isinstance(item.get("spec"), dict) else {}
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


def x_snapshots_list__mutmut_61(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        spec = item.get("XXspecXX", {}) if isinstance(item.get("spec"), dict) else {}
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


def x_snapshots_list__mutmut_62(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        spec = item.get("SPEC", {}) if isinstance(item.get("spec"), dict) else {}
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


def x_snapshots_list__mutmut_63(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        status = None
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


def x_snapshots_list__mutmut_64(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        status = item.get(None, {}) if isinstance(item.get("status"), dict) else {}
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


def x_snapshots_list__mutmut_65(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        status = item.get("status", None) if isinstance(item.get("status"), dict) else {}
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


def x_snapshots_list__mutmut_66(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        status = item.get({}) if isinstance(item.get("status"), dict) else {}
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


def x_snapshots_list__mutmut_67(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        status = item.get("status", ) if isinstance(item.get("status"), dict) else {}
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


def x_snapshots_list__mutmut_68(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        status = item.get("XXstatusXX", {}) if isinstance(item.get("status"), dict) else {}
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


def x_snapshots_list__mutmut_69(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        status = item.get("STATUS", {}) if isinstance(item.get("status"), dict) else {}
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


def x_snapshots_list__mutmut_70(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        ready = None
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


def x_snapshots_list__mutmut_71(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        ready = status.get(None, False)
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


def x_snapshots_list__mutmut_72(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        ready = status.get("readyToUse", None)
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


def x_snapshots_list__mutmut_73(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        ready = status.get(False)
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


def x_snapshots_list__mutmut_74(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        ready = status.get("readyToUse", )
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


def x_snapshots_list__mutmut_75(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        ready = status.get("XXreadyToUseXX", False)
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


def x_snapshots_list__mutmut_76(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        ready = status.get("readytouse", False)
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


def x_snapshots_list__mutmut_77(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        ready = status.get("READYTOUSE", False)
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


def x_snapshots_list__mutmut_78(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        ready = status.get("readyToUse", True)
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


def x_snapshots_list__mutmut_79(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
            None
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_80(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "XXnameXX": str(meta.get("name", "")),
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


def x_snapshots_list__mutmut_81(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "NAME": str(meta.get("name", "")),
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


def x_snapshots_list__mutmut_82(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "name": str(None),
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


def x_snapshots_list__mutmut_83(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "name": str(meta.get(None, "")),
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


def x_snapshots_list__mutmut_84(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "name": str(meta.get("name", None)),
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


def x_snapshots_list__mutmut_85(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "name": str(meta.get("")),
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


def x_snapshots_list__mutmut_86(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "name": str(meta.get("name", )),
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


def x_snapshots_list__mutmut_87(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "name": str(meta.get("XXnameXX", "")),
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


def x_snapshots_list__mutmut_88(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "name": str(meta.get("NAME", "")),
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


def x_snapshots_list__mutmut_89(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "name": str(meta.get("name", "XXXX")),
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


def x_snapshots_list__mutmut_90(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "XXnamespaceXX": str(meta.get("namespace", "default")),
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


def x_snapshots_list__mutmut_91(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "NAMESPACE": str(meta.get("namespace", "default")),
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


def x_snapshots_list__mutmut_92(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "namespace": str(None),
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


def x_snapshots_list__mutmut_93(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "namespace": str(meta.get(None, "default")),
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


def x_snapshots_list__mutmut_94(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "namespace": str(meta.get("namespace", None)),
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


def x_snapshots_list__mutmut_95(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "namespace": str(meta.get("default")),
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


def x_snapshots_list__mutmut_96(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "namespace": str(meta.get("namespace", )),
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


def x_snapshots_list__mutmut_97(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "namespace": str(meta.get("XXnamespaceXX", "default")),
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


def x_snapshots_list__mutmut_98(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "namespace": str(meta.get("NAMESPACE", "default")),
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


def x_snapshots_list__mutmut_99(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "namespace": str(meta.get("namespace", "XXdefaultXX")),
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


def x_snapshots_list__mutmut_100(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "namespace": str(meta.get("namespace", "DEFAULT")),
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


def x_snapshots_list__mutmut_101(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "XXsnapshot_classXX": str(spec.get("volumeSnapshotClassName", "")),
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


def x_snapshots_list__mutmut_102(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "SNAPSHOT_CLASS": str(spec.get("volumeSnapshotClassName", "")),
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


def x_snapshots_list__mutmut_103(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "snapshot_class": str(None),
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


def x_snapshots_list__mutmut_104(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "snapshot_class": str(spec.get(None, "")),
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


def x_snapshots_list__mutmut_105(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "snapshot_class": str(spec.get("volumeSnapshotClassName", None)),
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


def x_snapshots_list__mutmut_106(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "snapshot_class": str(spec.get("")),
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


def x_snapshots_list__mutmut_107(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "snapshot_class": str(spec.get("volumeSnapshotClassName", )),
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


def x_snapshots_list__mutmut_108(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "snapshot_class": str(spec.get("XXvolumeSnapshotClassNameXX", "")),
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


def x_snapshots_list__mutmut_109(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "snapshot_class": str(spec.get("volumesnapshotclassname", "")),
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


def x_snapshots_list__mutmut_110(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "snapshot_class": str(spec.get("VOLUMESNAPSHOTCLASSNAME", "")),
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


def x_snapshots_list__mutmut_111(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "snapshot_class": str(spec.get("volumeSnapshotClassName", "XXXX")),
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


def x_snapshots_list__mutmut_112(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "XXsource_pvcXX": str(spec.get("source", {}).get("persistentVolumeClaimName", ""))
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


def x_snapshots_list__mutmut_113(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "SOURCE_PVC": str(spec.get("source", {}).get("persistentVolumeClaimName", ""))
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


def x_snapshots_list__mutmut_114(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(None)
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


def x_snapshots_list__mutmut_115(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("source", {}).get(None, ""))
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


def x_snapshots_list__mutmut_116(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("source", {}).get("persistentVolumeClaimName", None))
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


def x_snapshots_list__mutmut_117(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("source", {}).get(""))
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


def x_snapshots_list__mutmut_118(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("source", {}).get("persistentVolumeClaimName", ))
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


def x_snapshots_list__mutmut_119(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get(None, {}).get("persistentVolumeClaimName", ""))
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


def x_snapshots_list__mutmut_120(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("source", None).get("persistentVolumeClaimName", ""))
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


def x_snapshots_list__mutmut_121(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get({}).get("persistentVolumeClaimName", ""))
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


def x_snapshots_list__mutmut_122(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("source", ).get("persistentVolumeClaimName", ""))
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


def x_snapshots_list__mutmut_123(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("XXsourceXX", {}).get("persistentVolumeClaimName", ""))
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


def x_snapshots_list__mutmut_124(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("SOURCE", {}).get("persistentVolumeClaimName", ""))
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


def x_snapshots_list__mutmut_125(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("source", {}).get("XXpersistentVolumeClaimNameXX", ""))
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


def x_snapshots_list__mutmut_126(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("source", {}).get("persistentvolumeclaimname", ""))
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


def x_snapshots_list__mutmut_127(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("source", {}).get("PERSISTENTVOLUMECLAIMNAME", ""))
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


def x_snapshots_list__mutmut_128(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "source_pvc": str(spec.get("source", {}).get("persistentVolumeClaimName", "XXXX"))
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


def x_snapshots_list__mutmut_129(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                else "XXXX",
                "ready": bool(ready),
                "creation_time": str(meta.get("creationTimestamp", "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_130(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "XXreadyXX": bool(ready),
                "creation_time": str(meta.get("creationTimestamp", "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_131(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "READY": bool(ready),
                "creation_time": str(meta.get("creationTimestamp", "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_132(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "ready": bool(None),
                "creation_time": str(meta.get("creationTimestamp", "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_133(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "XXcreation_timeXX": str(meta.get("creationTimestamp", "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_134(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "CREATION_TIME": str(meta.get("creationTimestamp", "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_135(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "creation_time": str(None),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_136(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "creation_time": str(meta.get(None, "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_137(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "creation_time": str(meta.get("creationTimestamp", None)),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_138(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "creation_time": str(meta.get("")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_139(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "creation_time": str(meta.get("creationTimestamp", )),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_140(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "creation_time": str(meta.get("XXcreationTimestampXX", "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_141(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "creation_time": str(meta.get("creationtimestamp", "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_142(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "creation_time": str(meta.get("CREATIONTIMESTAMP", "")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_143(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "creation_time": str(meta.get("creationTimestamp", "XXXX")),
                "restore_size": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_144(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "XXrestore_sizeXX": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_145(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "RESTORE_SIZE": str(status.get("restoreSize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_146(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "restore_size": str(None),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_147(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "restore_size": str(status.get(None, "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_148(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "restore_size": str(status.get("restoreSize", None)),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_149(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "restore_size": str(status.get("")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_150(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "restore_size": str(status.get("restoreSize", )),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_151(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "restore_size": str(status.get("XXrestoreSizeXX", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_152(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "restore_size": str(status.get("restoresize", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_153(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "restore_size": str(status.get("RESTORESIZE", "")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_154(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "restore_size": str(status.get("restoreSize", "XXXX")),
                "error": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_155(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "XXerrorXX": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_156(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "ERROR": str(status.get("error", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_157(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(None)
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_158(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("error", {}).get(None, ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_159(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("error", {}).get("message", None))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_160(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("error", {}).get(""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_161(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("error", {}).get("message", ))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_162(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get(None, {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_163(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("error", None).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_164(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get({}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_165(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("error", ).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_166(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("XXerrorXX", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_167(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("ERROR", {}).get("message", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_168(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("error", {}).get("XXmessageXX", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_169(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("error", {}).get("MESSAGE", ""))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_170(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                "error": str(status.get("error", {}).get("message", "XXXX"))
                if isinstance(status.get("error"), dict)
                else "",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_171(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
                else "XXXX",
            }
        )
    return {"snapshots": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_172(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    return {"XXsnapshotsXX": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_173(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    return {"SNAPSHOTS": results, "count": len(results), "error": ""}


def x_snapshots_list__mutmut_174(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    return {"snapshots": results, "XXcountXX": len(results), "error": ""}


def x_snapshots_list__mutmut_175(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    return {"snapshots": results, "COUNT": len(results), "error": ""}


def x_snapshots_list__mutmut_176(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    return {"snapshots": results, "count": len(results), "XXerrorXX": ""}


def x_snapshots_list__mutmut_177(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    return {"snapshots": results, "count": len(results), "ERROR": ""}


def x_snapshots_list__mutmut_178(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    return {"snapshots": results, "count": len(results), "error": "XXXX"}

mutants_x_snapshots_list__mutmut['_mutmut_orig'] = x_snapshots_list__mutmut_orig # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_1'] = x_snapshots_list__mutmut_1 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_2'] = x_snapshots_list__mutmut_2 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_3'] = x_snapshots_list__mutmut_3 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_4'] = x_snapshots_list__mutmut_4 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_5'] = x_snapshots_list__mutmut_5 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_6'] = x_snapshots_list__mutmut_6 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_7'] = x_snapshots_list__mutmut_7 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_8'] = x_snapshots_list__mutmut_8 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_9'] = x_snapshots_list__mutmut_9 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_10'] = x_snapshots_list__mutmut_10 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_11'] = x_snapshots_list__mutmut_11 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_12'] = x_snapshots_list__mutmut_12 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_13'] = x_snapshots_list__mutmut_13 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_14'] = x_snapshots_list__mutmut_14 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_15'] = x_snapshots_list__mutmut_15 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_16'] = x_snapshots_list__mutmut_16 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_17'] = x_snapshots_list__mutmut_17 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_18'] = x_snapshots_list__mutmut_18 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_19'] = x_snapshots_list__mutmut_19 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_20'] = x_snapshots_list__mutmut_20 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_21'] = x_snapshots_list__mutmut_21 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_22'] = x_snapshots_list__mutmut_22 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_23'] = x_snapshots_list__mutmut_23 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_24'] = x_snapshots_list__mutmut_24 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_25'] = x_snapshots_list__mutmut_25 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_26'] = x_snapshots_list__mutmut_26 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_27'] = x_snapshots_list__mutmut_27 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_28'] = x_snapshots_list__mutmut_28 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_29'] = x_snapshots_list__mutmut_29 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_30'] = x_snapshots_list__mutmut_30 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_31'] = x_snapshots_list__mutmut_31 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_32'] = x_snapshots_list__mutmut_32 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_33'] = x_snapshots_list__mutmut_33 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_34'] = x_snapshots_list__mutmut_34 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_35'] = x_snapshots_list__mutmut_35 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_36'] = x_snapshots_list__mutmut_36 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_37'] = x_snapshots_list__mutmut_37 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_38'] = x_snapshots_list__mutmut_38 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_39'] = x_snapshots_list__mutmut_39 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_40'] = x_snapshots_list__mutmut_40 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_41'] = x_snapshots_list__mutmut_41 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_42'] = x_snapshots_list__mutmut_42 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_43'] = x_snapshots_list__mutmut_43 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_44'] = x_snapshots_list__mutmut_44 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_45'] = x_snapshots_list__mutmut_45 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_46'] = x_snapshots_list__mutmut_46 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_47'] = x_snapshots_list__mutmut_47 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_48'] = x_snapshots_list__mutmut_48 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_49'] = x_snapshots_list__mutmut_49 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_50'] = x_snapshots_list__mutmut_50 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_51'] = x_snapshots_list__mutmut_51 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_52'] = x_snapshots_list__mutmut_52 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_53'] = x_snapshots_list__mutmut_53 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_54'] = x_snapshots_list__mutmut_54 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_55'] = x_snapshots_list__mutmut_55 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_56'] = x_snapshots_list__mutmut_56 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_57'] = x_snapshots_list__mutmut_57 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_58'] = x_snapshots_list__mutmut_58 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_59'] = x_snapshots_list__mutmut_59 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_60'] = x_snapshots_list__mutmut_60 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_61'] = x_snapshots_list__mutmut_61 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_62'] = x_snapshots_list__mutmut_62 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_63'] = x_snapshots_list__mutmut_63 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_64'] = x_snapshots_list__mutmut_64 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_65'] = x_snapshots_list__mutmut_65 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_66'] = x_snapshots_list__mutmut_66 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_67'] = x_snapshots_list__mutmut_67 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_68'] = x_snapshots_list__mutmut_68 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_69'] = x_snapshots_list__mutmut_69 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_70'] = x_snapshots_list__mutmut_70 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_71'] = x_snapshots_list__mutmut_71 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_72'] = x_snapshots_list__mutmut_72 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_73'] = x_snapshots_list__mutmut_73 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_74'] = x_snapshots_list__mutmut_74 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_75'] = x_snapshots_list__mutmut_75 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_76'] = x_snapshots_list__mutmut_76 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_77'] = x_snapshots_list__mutmut_77 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_78'] = x_snapshots_list__mutmut_78 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_79'] = x_snapshots_list__mutmut_79 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_80'] = x_snapshots_list__mutmut_80 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_81'] = x_snapshots_list__mutmut_81 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_82'] = x_snapshots_list__mutmut_82 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_83'] = x_snapshots_list__mutmut_83 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_84'] = x_snapshots_list__mutmut_84 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_85'] = x_snapshots_list__mutmut_85 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_86'] = x_snapshots_list__mutmut_86 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_87'] = x_snapshots_list__mutmut_87 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_88'] = x_snapshots_list__mutmut_88 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_89'] = x_snapshots_list__mutmut_89 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_90'] = x_snapshots_list__mutmut_90 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_91'] = x_snapshots_list__mutmut_91 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_92'] = x_snapshots_list__mutmut_92 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_93'] = x_snapshots_list__mutmut_93 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_94'] = x_snapshots_list__mutmut_94 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_95'] = x_snapshots_list__mutmut_95 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_96'] = x_snapshots_list__mutmut_96 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_97'] = x_snapshots_list__mutmut_97 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_98'] = x_snapshots_list__mutmut_98 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_99'] = x_snapshots_list__mutmut_99 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_100'] = x_snapshots_list__mutmut_100 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_101'] = x_snapshots_list__mutmut_101 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_102'] = x_snapshots_list__mutmut_102 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_103'] = x_snapshots_list__mutmut_103 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_104'] = x_snapshots_list__mutmut_104 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_105'] = x_snapshots_list__mutmut_105 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_106'] = x_snapshots_list__mutmut_106 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_107'] = x_snapshots_list__mutmut_107 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_108'] = x_snapshots_list__mutmut_108 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_109'] = x_snapshots_list__mutmut_109 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_110'] = x_snapshots_list__mutmut_110 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_111'] = x_snapshots_list__mutmut_111 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_112'] = x_snapshots_list__mutmut_112 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_113'] = x_snapshots_list__mutmut_113 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_114'] = x_snapshots_list__mutmut_114 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_115'] = x_snapshots_list__mutmut_115 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_116'] = x_snapshots_list__mutmut_116 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_117'] = x_snapshots_list__mutmut_117 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_118'] = x_snapshots_list__mutmut_118 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_119'] = x_snapshots_list__mutmut_119 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_120'] = x_snapshots_list__mutmut_120 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_121'] = x_snapshots_list__mutmut_121 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_122'] = x_snapshots_list__mutmut_122 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_123'] = x_snapshots_list__mutmut_123 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_124'] = x_snapshots_list__mutmut_124 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_125'] = x_snapshots_list__mutmut_125 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_126'] = x_snapshots_list__mutmut_126 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_127'] = x_snapshots_list__mutmut_127 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_128'] = x_snapshots_list__mutmut_128 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_129'] = x_snapshots_list__mutmut_129 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_130'] = x_snapshots_list__mutmut_130 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_131'] = x_snapshots_list__mutmut_131 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_132'] = x_snapshots_list__mutmut_132 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_133'] = x_snapshots_list__mutmut_133 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_134'] = x_snapshots_list__mutmut_134 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_135'] = x_snapshots_list__mutmut_135 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_136'] = x_snapshots_list__mutmut_136 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_137'] = x_snapshots_list__mutmut_137 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_138'] = x_snapshots_list__mutmut_138 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_139'] = x_snapshots_list__mutmut_139 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_140'] = x_snapshots_list__mutmut_140 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_141'] = x_snapshots_list__mutmut_141 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_142'] = x_snapshots_list__mutmut_142 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_143'] = x_snapshots_list__mutmut_143 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_144'] = x_snapshots_list__mutmut_144 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_145'] = x_snapshots_list__mutmut_145 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_146'] = x_snapshots_list__mutmut_146 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_147'] = x_snapshots_list__mutmut_147 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_148'] = x_snapshots_list__mutmut_148 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_149'] = x_snapshots_list__mutmut_149 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_150'] = x_snapshots_list__mutmut_150 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_151'] = x_snapshots_list__mutmut_151 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_152'] = x_snapshots_list__mutmut_152 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_153'] = x_snapshots_list__mutmut_153 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_154'] = x_snapshots_list__mutmut_154 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_155'] = x_snapshots_list__mutmut_155 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_156'] = x_snapshots_list__mutmut_156 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_157'] = x_snapshots_list__mutmut_157 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_158'] = x_snapshots_list__mutmut_158 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_159'] = x_snapshots_list__mutmut_159 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_160'] = x_snapshots_list__mutmut_160 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_161'] = x_snapshots_list__mutmut_161 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_162'] = x_snapshots_list__mutmut_162 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_163'] = x_snapshots_list__mutmut_163 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_164'] = x_snapshots_list__mutmut_164 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_165'] = x_snapshots_list__mutmut_165 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_166'] = x_snapshots_list__mutmut_166 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_167'] = x_snapshots_list__mutmut_167 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_168'] = x_snapshots_list__mutmut_168 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_169'] = x_snapshots_list__mutmut_169 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_170'] = x_snapshots_list__mutmut_170 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_171'] = x_snapshots_list__mutmut_171 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_172'] = x_snapshots_list__mutmut_172 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_173'] = x_snapshots_list__mutmut_173 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_174'] = x_snapshots_list__mutmut_174 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_175'] = x_snapshots_list__mutmut_175 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_176'] = x_snapshots_list__mutmut_176 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_177'] = x_snapshots_list__mutmut_177 # type: ignore # mutmut generated
mutants_x_snapshots_list__mutmut['x_snapshots_list__mutmut_178'] = x_snapshots_list__mutmut_178 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_snapshot_get__mutmut)
def snapshot_get(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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


def x_snapshot_get__mutmut_orig(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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


def x_snapshot_get__mutmut_1(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = None
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


def x_snapshot_get__mutmut_2(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name=None)
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


def x_snapshot_get__mutmut_3(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="XXdefaultXX")
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


def x_snapshot_get__mutmut_4(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="DEFAULT")
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


def x_snapshot_get__mutmut_5(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = None
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


def x_snapshot_get__mutmut_6(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = None
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


def x_snapshot_get__mutmut_7(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group=None,
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


def x_snapshot_get__mutmut_8(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version=None,
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


def x_snapshot_get__mutmut_9(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="v1",
            namespace=None,
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


def x_snapshot_get__mutmut_10(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="v1",
            namespace=namespace,
            plural=None,
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


def x_snapshot_get__mutmut_11(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="v1",
            namespace=namespace,
            plural="volumesnapshots",
            name=None,
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


def x_snapshot_get__mutmut_12(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
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


def x_snapshot_get__mutmut_13(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
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


def x_snapshot_get__mutmut_14(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="v1",
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


def x_snapshot_get__mutmut_15(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="v1",
            namespace=namespace,
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


def x_snapshot_get__mutmut_16(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="v1",
            namespace=namespace,
            plural="volumesnapshots",
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


def x_snapshot_get__mutmut_17(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="XXsnapshot.storage.k8s.ioXX",
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


def x_snapshot_get__mutmut_18(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="SNAPSHOT.STORAGE.K8S.IO",
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


def x_snapshot_get__mutmut_19(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="XXv1XX",
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


def x_snapshot_get__mutmut_20(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="V1",
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


def x_snapshot_get__mutmut_21(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="v1",
            namespace=namespace,
            plural="XXvolumesnapshotsXX",
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


def x_snapshot_get__mutmut_22(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    try:
        vanilla = VanillaAdapter(cluster_name="default")
        crd = vanilla._crd_api_client()
        raw = crd.get_namespaced_custom_object(  # type: ignore
            group="snapshot.storage.k8s.io",
            version="v1",
            namespace=namespace,
            plural="VOLUMESNAPSHOTS",
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


def x_snapshot_get__mutmut_23(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"XXnameXX": "", "namespace": "", "error": str(exc)}

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


def x_snapshot_get__mutmut_24(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"NAME": "", "namespace": "", "error": str(exc)}

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


def x_snapshot_get__mutmut_25(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "XXXX", "namespace": "", "error": str(exc)}

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


def x_snapshot_get__mutmut_26(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "XXnamespaceXX": "", "error": str(exc)}

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


def x_snapshot_get__mutmut_27(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "NAMESPACE": "", "error": str(exc)}

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


def x_snapshot_get__mutmut_28(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "namespace": "XXXX", "error": str(exc)}

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


def x_snapshot_get__mutmut_29(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "namespace": "", "XXerrorXX": str(exc)}

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


def x_snapshot_get__mutmut_30(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "namespace": "", "ERROR": str(exc)}

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


def x_snapshot_get__mutmut_31(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "namespace": "", "error": str(None)}

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


def x_snapshot_get__mutmut_32(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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

    if isinstance(raw, dict):
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


def x_snapshot_get__mutmut_33(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"XXnameXX": "", "namespace": "", "error": "Not found"}
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


def x_snapshot_get__mutmut_34(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"NAME": "", "namespace": "", "error": "Not found"}
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


def x_snapshot_get__mutmut_35(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "XXXX", "namespace": "", "error": "Not found"}
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


def x_snapshot_get__mutmut_36(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "XXnamespaceXX": "", "error": "Not found"}
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


def x_snapshot_get__mutmut_37(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "NAMESPACE": "", "error": "Not found"}
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


def x_snapshot_get__mutmut_38(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "namespace": "XXXX", "error": "Not found"}
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


def x_snapshot_get__mutmut_39(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "namespace": "", "XXerrorXX": "Not found"}
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


def x_snapshot_get__mutmut_40(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "namespace": "", "ERROR": "Not found"}
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


def x_snapshot_get__mutmut_41(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "namespace": "", "error": "XXNot foundXX"}
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


def x_snapshot_get__mutmut_42(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "namespace": "", "error": "not found"}
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


def x_snapshot_get__mutmut_43(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        return {"name": "", "namespace": "", "error": "NOT FOUND"}
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


def x_snapshot_get__mutmut_44(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    meta = None
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


def x_snapshot_get__mutmut_45(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    meta = raw.get(None, {}) if isinstance(raw.get("metadata"), dict) else {}
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


def x_snapshot_get__mutmut_46(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    meta = raw.get("metadata", None) if isinstance(raw.get("metadata"), dict) else {}
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


def x_snapshot_get__mutmut_47(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    meta = raw.get({}) if isinstance(raw.get("metadata"), dict) else {}
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


def x_snapshot_get__mutmut_48(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    meta = raw.get("metadata", ) if isinstance(raw.get("metadata"), dict) else {}
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


def x_snapshot_get__mutmut_49(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    meta = raw.get("XXmetadataXX", {}) if isinstance(raw.get("metadata"), dict) else {}
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


def x_snapshot_get__mutmut_50(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    meta = raw.get("METADATA", {}) if isinstance(raw.get("metadata"), dict) else {}
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


def x_snapshot_get__mutmut_51(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    spec = None
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


def x_snapshot_get__mutmut_52(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    spec = raw.get(None, {}) if isinstance(raw.get("spec"), dict) else {}
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


def x_snapshot_get__mutmut_53(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    spec = raw.get("spec", None) if isinstance(raw.get("spec"), dict) else {}
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


def x_snapshot_get__mutmut_54(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    spec = raw.get({}) if isinstance(raw.get("spec"), dict) else {}
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


def x_snapshot_get__mutmut_55(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    spec = raw.get("spec", ) if isinstance(raw.get("spec"), dict) else {}
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


def x_snapshot_get__mutmut_56(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    spec = raw.get("XXspecXX", {}) if isinstance(raw.get("spec"), dict) else {}
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


def x_snapshot_get__mutmut_57(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    spec = raw.get("SPEC", {}) if isinstance(raw.get("spec"), dict) else {}
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


def x_snapshot_get__mutmut_58(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    status = None
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


def x_snapshot_get__mutmut_59(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    status = raw.get(None, {}) if isinstance(raw.get("status"), dict) else {}
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


def x_snapshot_get__mutmut_60(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    status = raw.get("status", None) if isinstance(raw.get("status"), dict) else {}
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


def x_snapshot_get__mutmut_61(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    status = raw.get({}) if isinstance(raw.get("status"), dict) else {}
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


def x_snapshot_get__mutmut_62(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    status = raw.get("status", ) if isinstance(raw.get("status"), dict) else {}
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


def x_snapshot_get__mutmut_63(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    status = raw.get("XXstatusXX", {}) if isinstance(raw.get("status"), dict) else {}
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


def x_snapshot_get__mutmut_64(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
    status = raw.get("STATUS", {}) if isinstance(raw.get("status"), dict) else {}
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


def x_snapshot_get__mutmut_65(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "XXnameXX": str(meta.get("name", "")),
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


def x_snapshot_get__mutmut_66(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "NAME": str(meta.get("name", "")),
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


def x_snapshot_get__mutmut_67(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "name": str(None),
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


def x_snapshot_get__mutmut_68(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "name": str(meta.get(None, "")),
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


def x_snapshot_get__mutmut_69(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "name": str(meta.get("name", None)),
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


def x_snapshot_get__mutmut_70(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "name": str(meta.get("")),
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


def x_snapshot_get__mutmut_71(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "name": str(meta.get("name", )),
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


def x_snapshot_get__mutmut_72(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "name": str(meta.get("XXnameXX", "")),
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


def x_snapshot_get__mutmut_73(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "name": str(meta.get("NAME", "")),
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


def x_snapshot_get__mutmut_74(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "name": str(meta.get("name", "XXXX")),
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


def x_snapshot_get__mutmut_75(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "XXnamespaceXX": str(meta.get("namespace", "default")),
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


def x_snapshot_get__mutmut_76(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "NAMESPACE": str(meta.get("namespace", "default")),
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


def x_snapshot_get__mutmut_77(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "namespace": str(None),
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


def x_snapshot_get__mutmut_78(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "namespace": str(meta.get(None, "default")),
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


def x_snapshot_get__mutmut_79(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "namespace": str(meta.get("namespace", None)),
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


def x_snapshot_get__mutmut_80(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "namespace": str(meta.get("default")),
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


def x_snapshot_get__mutmut_81(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "namespace": str(meta.get("namespace", )),
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


def x_snapshot_get__mutmut_82(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "namespace": str(meta.get("XXnamespaceXX", "default")),
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


def x_snapshot_get__mutmut_83(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "namespace": str(meta.get("NAMESPACE", "default")),
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


def x_snapshot_get__mutmut_84(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "namespace": str(meta.get("namespace", "XXdefaultXX")),
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


def x_snapshot_get__mutmut_85(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "namespace": str(meta.get("namespace", "DEFAULT")),
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


def x_snapshot_get__mutmut_86(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "XXsnapshot_classXX": str(spec.get("volumeSnapshotClassName", "")),
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


def x_snapshot_get__mutmut_87(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "SNAPSHOT_CLASS": str(spec.get("volumeSnapshotClassName", "")),
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


def x_snapshot_get__mutmut_88(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "snapshot_class": str(None),
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


def x_snapshot_get__mutmut_89(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "snapshot_class": str(spec.get(None, "")),
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


def x_snapshot_get__mutmut_90(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "snapshot_class": str(spec.get("volumeSnapshotClassName", None)),
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


def x_snapshot_get__mutmut_91(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "snapshot_class": str(spec.get("")),
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


def x_snapshot_get__mutmut_92(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "snapshot_class": str(spec.get("volumeSnapshotClassName", )),
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


def x_snapshot_get__mutmut_93(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "snapshot_class": str(spec.get("XXvolumeSnapshotClassNameXX", "")),
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


def x_snapshot_get__mutmut_94(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "snapshot_class": str(spec.get("volumesnapshotclassname", "")),
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


def x_snapshot_get__mutmut_95(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "snapshot_class": str(spec.get("VOLUMESNAPSHOTCLASSNAME", "")),
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


def x_snapshot_get__mutmut_96(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "snapshot_class": str(spec.get("volumeSnapshotClassName", "XXXX")),
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


def x_snapshot_get__mutmut_97(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "XXsource_pvcXX": str(spec.get("source", {}).get("persistentVolumeClaimName", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_98(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "SOURCE_PVC": str(spec.get("source", {}).get("persistentVolumeClaimName", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_99(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(None)
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_100(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("source", {}).get(None, ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_101(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("source", {}).get("persistentVolumeClaimName", None))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_102(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("source", {}).get(""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_103(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("source", {}).get("persistentVolumeClaimName", ))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_104(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get(None, {}).get("persistentVolumeClaimName", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_105(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("source", None).get("persistentVolumeClaimName", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_106(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get({}).get("persistentVolumeClaimName", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_107(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("source", ).get("persistentVolumeClaimName", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_108(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("XXsourceXX", {}).get("persistentVolumeClaimName", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_109(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("SOURCE", {}).get("persistentVolumeClaimName", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_110(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("source", {}).get("XXpersistentVolumeClaimNameXX", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_111(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("source", {}).get("persistentvolumeclaimname", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_112(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("source", {}).get("PERSISTENTVOLUMECLAIMNAME", ""))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_113(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "source_pvc": str(spec.get("source", {}).get("persistentVolumeClaimName", "XXXX"))
        if isinstance(spec.get("source"), dict)
        else "",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_114(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        else "XXXX",
        "ready": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_115(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "XXreadyXX": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_116(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "READY": bool(status.get("readyToUse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_117(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "ready": bool(None),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_118(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "ready": bool(status.get(None, False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_119(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "ready": bool(status.get("readyToUse", None)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_120(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "ready": bool(status.get(False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_121(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "ready": bool(status.get("readyToUse", )),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_122(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "ready": bool(status.get("XXreadyToUseXX", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_123(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "ready": bool(status.get("readytouse", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_124(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "ready": bool(status.get("READYTOUSE", False)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_125(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "ready": bool(status.get("readyToUse", True)),
        "creation_time": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_126(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "XXcreation_timeXX": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_127(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "CREATION_TIME": str(meta.get("creationTimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_128(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "creation_time": str(None),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_129(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "creation_time": str(meta.get(None, "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_130(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "creation_time": str(meta.get("creationTimestamp", None)),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_131(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "creation_time": str(meta.get("")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_132(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "creation_time": str(meta.get("creationTimestamp", )),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_133(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "creation_time": str(meta.get("XXcreationTimestampXX", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_134(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "creation_time": str(meta.get("creationtimestamp", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_135(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "creation_time": str(meta.get("CREATIONTIMESTAMP", "")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_136(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "creation_time": str(meta.get("creationTimestamp", "XXXX")),
        "restore_size": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_137(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "XXrestore_sizeXX": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_138(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "RESTORE_SIZE": str(status.get("restoreSize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_139(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "restore_size": str(None),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_140(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "restore_size": str(status.get(None, "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_141(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "restore_size": str(status.get("restoreSize", None)),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_142(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "restore_size": str(status.get("")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_143(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "restore_size": str(status.get("restoreSize", )),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_144(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "restore_size": str(status.get("XXrestoreSizeXX", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_145(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "restore_size": str(status.get("restoresize", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_146(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "restore_size": str(status.get("RESTORESIZE", "")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_147(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "restore_size": str(status.get("restoreSize", "XXXX")),
        "error": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_148(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "XXerrorXX": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_149(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "ERROR": str(status.get("error", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_150(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(None)
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_151(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("error", {}).get(None, ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_152(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("error", {}).get("message", None))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_153(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("error", {}).get(""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_154(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("error", {}).get("message", ))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_155(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get(None, {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_156(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("error", None).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_157(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get({}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_158(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("error", ).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_159(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("XXerrorXX", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_160(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("ERROR", {}).get("message", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_161(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("error", {}).get("XXmessageXX", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_162(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("error", {}).get("MESSAGE", ""))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_163(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        "error": str(status.get("error", {}).get("message", "XXXX"))
        if isinstance(status.get("error"), dict)
        else "",
    }


def x_snapshot_get__mutmut_164(name: str, namespace: str) -> dict[str, object]:
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

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
        else "XXXX",
    }

mutants_x_snapshot_get__mutmut['_mutmut_orig'] = x_snapshot_get__mutmut_orig # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_1'] = x_snapshot_get__mutmut_1 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_2'] = x_snapshot_get__mutmut_2 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_3'] = x_snapshot_get__mutmut_3 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_4'] = x_snapshot_get__mutmut_4 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_5'] = x_snapshot_get__mutmut_5 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_6'] = x_snapshot_get__mutmut_6 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_7'] = x_snapshot_get__mutmut_7 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_8'] = x_snapshot_get__mutmut_8 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_9'] = x_snapshot_get__mutmut_9 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_10'] = x_snapshot_get__mutmut_10 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_11'] = x_snapshot_get__mutmut_11 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_12'] = x_snapshot_get__mutmut_12 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_13'] = x_snapshot_get__mutmut_13 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_14'] = x_snapshot_get__mutmut_14 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_15'] = x_snapshot_get__mutmut_15 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_16'] = x_snapshot_get__mutmut_16 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_17'] = x_snapshot_get__mutmut_17 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_18'] = x_snapshot_get__mutmut_18 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_19'] = x_snapshot_get__mutmut_19 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_20'] = x_snapshot_get__mutmut_20 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_21'] = x_snapshot_get__mutmut_21 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_22'] = x_snapshot_get__mutmut_22 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_23'] = x_snapshot_get__mutmut_23 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_24'] = x_snapshot_get__mutmut_24 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_25'] = x_snapshot_get__mutmut_25 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_26'] = x_snapshot_get__mutmut_26 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_27'] = x_snapshot_get__mutmut_27 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_28'] = x_snapshot_get__mutmut_28 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_29'] = x_snapshot_get__mutmut_29 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_30'] = x_snapshot_get__mutmut_30 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_31'] = x_snapshot_get__mutmut_31 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_32'] = x_snapshot_get__mutmut_32 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_33'] = x_snapshot_get__mutmut_33 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_34'] = x_snapshot_get__mutmut_34 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_35'] = x_snapshot_get__mutmut_35 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_36'] = x_snapshot_get__mutmut_36 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_37'] = x_snapshot_get__mutmut_37 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_38'] = x_snapshot_get__mutmut_38 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_39'] = x_snapshot_get__mutmut_39 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_40'] = x_snapshot_get__mutmut_40 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_41'] = x_snapshot_get__mutmut_41 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_42'] = x_snapshot_get__mutmut_42 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_43'] = x_snapshot_get__mutmut_43 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_44'] = x_snapshot_get__mutmut_44 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_45'] = x_snapshot_get__mutmut_45 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_46'] = x_snapshot_get__mutmut_46 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_47'] = x_snapshot_get__mutmut_47 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_48'] = x_snapshot_get__mutmut_48 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_49'] = x_snapshot_get__mutmut_49 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_50'] = x_snapshot_get__mutmut_50 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_51'] = x_snapshot_get__mutmut_51 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_52'] = x_snapshot_get__mutmut_52 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_53'] = x_snapshot_get__mutmut_53 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_54'] = x_snapshot_get__mutmut_54 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_55'] = x_snapshot_get__mutmut_55 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_56'] = x_snapshot_get__mutmut_56 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_57'] = x_snapshot_get__mutmut_57 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_58'] = x_snapshot_get__mutmut_58 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_59'] = x_snapshot_get__mutmut_59 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_60'] = x_snapshot_get__mutmut_60 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_61'] = x_snapshot_get__mutmut_61 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_62'] = x_snapshot_get__mutmut_62 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_63'] = x_snapshot_get__mutmut_63 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_64'] = x_snapshot_get__mutmut_64 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_65'] = x_snapshot_get__mutmut_65 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_66'] = x_snapshot_get__mutmut_66 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_67'] = x_snapshot_get__mutmut_67 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_68'] = x_snapshot_get__mutmut_68 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_69'] = x_snapshot_get__mutmut_69 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_70'] = x_snapshot_get__mutmut_70 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_71'] = x_snapshot_get__mutmut_71 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_72'] = x_snapshot_get__mutmut_72 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_73'] = x_snapshot_get__mutmut_73 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_74'] = x_snapshot_get__mutmut_74 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_75'] = x_snapshot_get__mutmut_75 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_76'] = x_snapshot_get__mutmut_76 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_77'] = x_snapshot_get__mutmut_77 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_78'] = x_snapshot_get__mutmut_78 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_79'] = x_snapshot_get__mutmut_79 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_80'] = x_snapshot_get__mutmut_80 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_81'] = x_snapshot_get__mutmut_81 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_82'] = x_snapshot_get__mutmut_82 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_83'] = x_snapshot_get__mutmut_83 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_84'] = x_snapshot_get__mutmut_84 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_85'] = x_snapshot_get__mutmut_85 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_86'] = x_snapshot_get__mutmut_86 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_87'] = x_snapshot_get__mutmut_87 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_88'] = x_snapshot_get__mutmut_88 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_89'] = x_snapshot_get__mutmut_89 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_90'] = x_snapshot_get__mutmut_90 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_91'] = x_snapshot_get__mutmut_91 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_92'] = x_snapshot_get__mutmut_92 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_93'] = x_snapshot_get__mutmut_93 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_94'] = x_snapshot_get__mutmut_94 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_95'] = x_snapshot_get__mutmut_95 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_96'] = x_snapshot_get__mutmut_96 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_97'] = x_snapshot_get__mutmut_97 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_98'] = x_snapshot_get__mutmut_98 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_99'] = x_snapshot_get__mutmut_99 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_100'] = x_snapshot_get__mutmut_100 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_101'] = x_snapshot_get__mutmut_101 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_102'] = x_snapshot_get__mutmut_102 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_103'] = x_snapshot_get__mutmut_103 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_104'] = x_snapshot_get__mutmut_104 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_105'] = x_snapshot_get__mutmut_105 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_106'] = x_snapshot_get__mutmut_106 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_107'] = x_snapshot_get__mutmut_107 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_108'] = x_snapshot_get__mutmut_108 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_109'] = x_snapshot_get__mutmut_109 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_110'] = x_snapshot_get__mutmut_110 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_111'] = x_snapshot_get__mutmut_111 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_112'] = x_snapshot_get__mutmut_112 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_113'] = x_snapshot_get__mutmut_113 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_114'] = x_snapshot_get__mutmut_114 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_115'] = x_snapshot_get__mutmut_115 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_116'] = x_snapshot_get__mutmut_116 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_117'] = x_snapshot_get__mutmut_117 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_118'] = x_snapshot_get__mutmut_118 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_119'] = x_snapshot_get__mutmut_119 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_120'] = x_snapshot_get__mutmut_120 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_121'] = x_snapshot_get__mutmut_121 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_122'] = x_snapshot_get__mutmut_122 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_123'] = x_snapshot_get__mutmut_123 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_124'] = x_snapshot_get__mutmut_124 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_125'] = x_snapshot_get__mutmut_125 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_126'] = x_snapshot_get__mutmut_126 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_127'] = x_snapshot_get__mutmut_127 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_128'] = x_snapshot_get__mutmut_128 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_129'] = x_snapshot_get__mutmut_129 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_130'] = x_snapshot_get__mutmut_130 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_131'] = x_snapshot_get__mutmut_131 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_132'] = x_snapshot_get__mutmut_132 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_133'] = x_snapshot_get__mutmut_133 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_134'] = x_snapshot_get__mutmut_134 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_135'] = x_snapshot_get__mutmut_135 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_136'] = x_snapshot_get__mutmut_136 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_137'] = x_snapshot_get__mutmut_137 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_138'] = x_snapshot_get__mutmut_138 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_139'] = x_snapshot_get__mutmut_139 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_140'] = x_snapshot_get__mutmut_140 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_141'] = x_snapshot_get__mutmut_141 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_142'] = x_snapshot_get__mutmut_142 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_143'] = x_snapshot_get__mutmut_143 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_144'] = x_snapshot_get__mutmut_144 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_145'] = x_snapshot_get__mutmut_145 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_146'] = x_snapshot_get__mutmut_146 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_147'] = x_snapshot_get__mutmut_147 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_148'] = x_snapshot_get__mutmut_148 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_149'] = x_snapshot_get__mutmut_149 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_150'] = x_snapshot_get__mutmut_150 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_151'] = x_snapshot_get__mutmut_151 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_152'] = x_snapshot_get__mutmut_152 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_153'] = x_snapshot_get__mutmut_153 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_154'] = x_snapshot_get__mutmut_154 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_155'] = x_snapshot_get__mutmut_155 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_156'] = x_snapshot_get__mutmut_156 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_157'] = x_snapshot_get__mutmut_157 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_158'] = x_snapshot_get__mutmut_158 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_159'] = x_snapshot_get__mutmut_159 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_160'] = x_snapshot_get__mutmut_160 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_161'] = x_snapshot_get__mutmut_161 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_162'] = x_snapshot_get__mutmut_162 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_163'] = x_snapshot_get__mutmut_163 # type: ignore # mutmut generated
mutants_x_snapshot_get__mutmut['x_snapshot_get__mutmut_164'] = x_snapshot_get__mutmut_164 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(snapshots_list)
    mcp.tool()(snapshot_get)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(snapshots_list)
    mcp.tool()(snapshot_get)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)
    mcp.tool()(snapshot_get)


def x_register__mutmut_2(mcp: FastMCP) -> None:
    mcp.tool()(snapshots_list)
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_2'] = x_register__mutmut_2 # type: ignore # mutmut generated
