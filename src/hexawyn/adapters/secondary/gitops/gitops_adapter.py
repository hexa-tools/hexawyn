# mypy: ignore-errors
"""GitOpsAdapter — queries real ArgoCD Applications via VanillaAdapter."""

from __future__ import annotations

from typing import cast

from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.domain.models.gitops import (
    GitOpsApp,
    GitOpsDetectionResult,
    GitOpsEngine,
    GitOpsSource,
    HealthStatus,
    SyncStatus,
)

_ARGO_GROUP = "argoproj.io"
_ARGO_VERSION = "v1alpha1"


class GitOpsAdapter(GitOpsPort):
    """Real GitOps adapter using VanillaAdapter's CustomObjectsApi for ArgoCD."""

    def __init__(self, vanilla: VanillaAdapter) -> None:
        self._vanilla = vanilla

    def _crd(self):  # type: ignore
        return self._vanilla._crd_api_client()

    def detect_engine(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=0,
            )

        if not apps:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=0,
            )

        parsed = [self._parse_app(a) for a in apps]
        out_of_sync = sum(1 for a in parsed if a.sync_status not in (SyncStatus.SYNCED,))
        failed = sum(
            1 for a in parsed if a.health_status in (HealthStatus.DEGRADED, HealthStatus.MISSING)
        )

        return GitOpsDetectionResult(
            engine=GitOpsEngine.ARGOCD,
            version=None,
            namespace="argocd",
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def list_apps(self, namespace: str | None = None) -> list[GitOpsApp]:
        apps = self._list_apps_raw(namespace)
        return [self._parse_app(a) for a in apps]

    def get_app(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def list_sources(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url and url not in seen:
                seen.add(url)
                meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
                sources.append(
                    GitOpsSource(
                        name=str(meta.get("name", "")),
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def get_source(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def _list_apps_raw(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
                    version=_ARGO_VERSION,
                    namespace=namespace,
                    plural="applications",
                )
            else:
                raw = self._crd().list_cluster_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
                    version=_ARGO_VERSION,
                    plural="applications",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    @staticmethod
    def _parse_app(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = str(field_data.get("status", "")).lower()
            if field == "sync":
                if "synced" in status_val:
                    sync = SyncStatus.SYNCED
                elif "outofsync" in status_val:
                    sync = SyncStatus.OUT_OF_SYNC
                elif status_val:
                    sync = SyncStatus.UNKNOWN
            elif field == "health":
                if "healthy" in status_val:
                    health = HealthStatus.HEALTHY
                elif "degraded" in status_val:
                    health = HealthStatus.DEGRADED
                elif "progressing" in status_val:
                    health = HealthStatus.PROGRESSING
                elif "suspended" in status_val:
                    health = HealthStatus.SUSPENDED
                elif "missing" in status_val:
                    health = HealthStatus.MISSING

        source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}

        return GitOpsApp(
            name=str(meta.get("name", "")),
            namespace=str(meta.get("namespace", "argocd")),
            engine=GitOpsEngine.ARGOCD,
            kind="Application",
            sync_status=sync,
            health_status=health,
            last_synced_at=str(status_data.get("reconciledAt", "")) or None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )
