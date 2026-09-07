# mypy: ignore-errors
"""GitOpsAdapter — queries real ArgoCD Applications via VanillaAdapter."""

from __future__ import annotations

from typing import cast

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.domain.models.gitops import (
    GitOpsApp,
    GitOpsDetectionResult,
    GitOpsEngine,
    GitOpsSource,
    HealthStatus,
    SyncStatus,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

_ARGO_GROUP = "argoproj.io"
_ARGO_VERSION = "v1alpha1"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGitOpsAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsAdapterǁlist_apps__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsAdapterǁget_app__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsAdapterǁlist_sources__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsAdapterǁget_source__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut: MutantDict = {}  # type: ignore


class GitOpsAdapter(GitOpsPort):
    """Real GitOps adapter using VanillaAdapter's CustomObjectsApi for ArgoCD."""

    @_mutmut_mutated(mutants_xǁGitOpsAdapterǁ__init____mutmut)
    def __init__(self, vanilla: VanillaAdapter) -> None:
        self._vanilla = vanilla

    def xǁGitOpsAdapterǁ__init____mutmut_orig(self, vanilla: VanillaAdapter) -> None:
        self._vanilla = vanilla

    def xǁGitOpsAdapterǁ__init____mutmut_1(self, vanilla: VanillaAdapter) -> None:
        self._vanilla = None

    def _crd(self):  # type: ignore
        return self._vanilla._crd_api_client()

    @_mutmut_mutated(mutants_xǁGitOpsAdapterǁdetect_engine__mutmut)
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_orig(self) -> GitOpsDetectionResult:
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_1(self) -> GitOpsDetectionResult:
        try:
            apps = None
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_2(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=None,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_3(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=None,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_4(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=None,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_5(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=None,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_6(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_7(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_8(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_9(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_10(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_11(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_12(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=1,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_13(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=1,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_14(self) -> GitOpsDetectionResult:
        try:
            apps = self._list_apps_raw()
        except Exception:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=1,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_15(self) -> GitOpsDetectionResult:
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

        if apps:
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_16(self) -> GitOpsDetectionResult:
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
                engine=None,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_17(self) -> GitOpsDetectionResult:
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
                apps_count=None,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_18(self) -> GitOpsDetectionResult:
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
                out_of_sync_count=None,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_19(self) -> GitOpsDetectionResult:
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
                failed_count=None,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_20(self) -> GitOpsDetectionResult:
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_21(self) -> GitOpsDetectionResult:
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_22(self) -> GitOpsDetectionResult:
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_23(self) -> GitOpsDetectionResult:
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_24(self) -> GitOpsDetectionResult:
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_25(self) -> GitOpsDetectionResult:
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_26(self) -> GitOpsDetectionResult:
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
                apps_count=1,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_27(self) -> GitOpsDetectionResult:
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
                out_of_sync_count=1,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_28(self) -> GitOpsDetectionResult:
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
                failed_count=1,
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_29(self) -> GitOpsDetectionResult:
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

        parsed = None
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_30(self) -> GitOpsDetectionResult:
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

        parsed = [self._parse_app(None) for a in apps]
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_31(self) -> GitOpsDetectionResult:
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
        out_of_sync = None
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_32(self) -> GitOpsDetectionResult:
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
        out_of_sync = sum(None)
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_33(self) -> GitOpsDetectionResult:
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
        out_of_sync = sum(2 for a in parsed if a.sync_status not in (SyncStatus.SYNCED,))
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_34(self) -> GitOpsDetectionResult:
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
        out_of_sync = sum(1 for a in parsed if a.sync_status in (SyncStatus.SYNCED,))
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

    def xǁGitOpsAdapterǁdetect_engine__mutmut_35(self) -> GitOpsDetectionResult:
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
        failed = None

        return GitOpsDetectionResult(
            engine=GitOpsEngine.ARGOCD,
            version=None,
            namespace="argocd",
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_36(self) -> GitOpsDetectionResult:
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
            None
        )

        return GitOpsDetectionResult(
            engine=GitOpsEngine.ARGOCD,
            version=None,
            namespace="argocd",
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_37(self) -> GitOpsDetectionResult:
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
            2 for a in parsed if a.health_status in (HealthStatus.DEGRADED, HealthStatus.MISSING)
        )

        return GitOpsDetectionResult(
            engine=GitOpsEngine.ARGOCD,
            version=None,
            namespace="argocd",
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_38(self) -> GitOpsDetectionResult:
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
            1 for a in parsed if a.health_status not in (HealthStatus.DEGRADED, HealthStatus.MISSING)
        )

        return GitOpsDetectionResult(
            engine=GitOpsEngine.ARGOCD,
            version=None,
            namespace="argocd",
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_39(self) -> GitOpsDetectionResult:
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
            engine=None,
            version=None,
            namespace="argocd",
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_40(self) -> GitOpsDetectionResult:
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
            namespace=None,
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_41(self) -> GitOpsDetectionResult:
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
            apps_count=None,
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_42(self) -> GitOpsDetectionResult:
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
            out_of_sync_count=None,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_43(self) -> GitOpsDetectionResult:
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
            failed_count=None,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_44(self) -> GitOpsDetectionResult:
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
            version=None,
            namespace="argocd",
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_45(self) -> GitOpsDetectionResult:
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
            namespace="argocd",
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_46(self) -> GitOpsDetectionResult:
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
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_47(self) -> GitOpsDetectionResult:
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
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_48(self) -> GitOpsDetectionResult:
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
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_49(self) -> GitOpsDetectionResult:
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
            )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_50(self) -> GitOpsDetectionResult:
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
            namespace="XXargocdXX",
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    def xǁGitOpsAdapterǁdetect_engine__mutmut_51(self) -> GitOpsDetectionResult:
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
            namespace="ARGOCD",
            apps_count=len(parsed),
            out_of_sync_count=out_of_sync,
            failed_count=failed,
        )

    @_mutmut_mutated(mutants_xǁGitOpsAdapterǁlist_apps__mutmut)
    def list_apps(self, namespace: str | None = None) -> list[GitOpsApp]:
        apps = self._list_apps_raw(namespace)
        return [self._parse_app(a) for a in apps]

    def xǁGitOpsAdapterǁlist_apps__mutmut_orig(self, namespace: str | None = None) -> list[GitOpsApp]:
        apps = self._list_apps_raw(namespace)
        return [self._parse_app(a) for a in apps]

    def xǁGitOpsAdapterǁlist_apps__mutmut_1(self, namespace: str | None = None) -> list[GitOpsApp]:
        apps = None
        return [self._parse_app(a) for a in apps]

    def xǁGitOpsAdapterǁlist_apps__mutmut_2(self, namespace: str | None = None) -> list[GitOpsApp]:
        apps = self._list_apps_raw(None)
        return [self._parse_app(a) for a in apps]

    def xǁGitOpsAdapterǁlist_apps__mutmut_3(self, namespace: str | None = None) -> list[GitOpsApp]:
        apps = self._list_apps_raw(namespace)
        return [self._parse_app(None) for a in apps]

    @_mutmut_mutated(mutants_xǁGitOpsAdapterǁget_app__mutmut)
    def get_app(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_orig(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_1(self, name: str, namespace: str) -> GitOpsApp:
        raw = None
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_2(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=None,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_3(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=None,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_4(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=None,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_5(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural=None,
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_6(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=None,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_7(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_8(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_9(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_10(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_11(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_12(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="XXapplicationsXX",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_13(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="APPLICATIONS",
            name=name,
        )
        return self._parse_app(cast(dict, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_14(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(None)  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_15(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(None, raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_16(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, None))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_17(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(raw))  # type: ignore

    def xǁGitOpsAdapterǁget_app__mutmut_18(self, name: str, namespace: str) -> GitOpsApp:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_ARGO_GROUP,
            version=_ARGO_VERSION,
            namespace=namespace,
            plural="applications",
            name=name,
        )
        return self._parse_app(cast(dict, ))  # type: ignore

    @_mutmut_mutated(mutants_xǁGitOpsAdapterǁlist_sources__mutmut)
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_orig(self, namespace: str | None = None) -> list[GitOpsSource]:
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_1(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = None
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_2(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(None)
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_3(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = None
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_4(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = None
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_5(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = None
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_6(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get(None, {}) if isinstance(a.get("spec"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_7(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", None) if isinstance(a.get("spec"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_8(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get({}) if isinstance(a.get("spec"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_9(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", ) if isinstance(a.get("spec"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_10(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("XXspecXX", {}) if isinstance(a.get("spec"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_11(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("SPEC", {}) if isinstance(a.get("spec"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_12(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = None
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_13(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get(None, {}) if isinstance(spec.get("source"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_14(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", None) if isinstance(spec.get("source"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_15(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get({}) if isinstance(spec.get("source"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_16(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", ) if isinstance(spec.get("source"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_17(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("XXsourceXX", {}) if isinstance(spec.get("source"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_18(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("SOURCE", {}) if isinstance(spec.get("source"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_19(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = None
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_20(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(None)
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_21(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get(None, ""))
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_22(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", None))
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_23(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get(""))
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_24(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ))
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_25(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("XXrepoURLXX", ""))
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_26(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repourl", ""))
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_27(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("REPOURL", ""))
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_28(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", "XXXX"))
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_29(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url or url not in seen:
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_30(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url and url in seen:
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_31(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url and url not in seen:
                seen.add(None)
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_32(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url and url not in seen:
                seen.add(url)
                meta = None
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_33(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url and url not in seen:
                seen.add(url)
                meta = a.get(None, {}) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_34(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url and url not in seen:
                seen.add(url)
                meta = a.get("metadata", None) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_35(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url and url not in seen:
                seen.add(url)
                meta = a.get({}) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_36(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url and url not in seen:
                seen.add(url)
                meta = a.get("metadata", ) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_37(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url and url not in seen:
                seen.add(url)
                meta = a.get("XXmetadataXX", {}) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_38(self, namespace: str | None = None) -> list[GitOpsSource]:
        apps = self._list_apps_raw(namespace)
        seen: set[str] = set()
        sources: list[GitOpsSource] = []
        for a in apps:
            spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
            source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
            url = str(source.get("repoURL", ""))
            if url and url not in seen:
                seen.add(url)
                meta = a.get("METADATA", {}) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁlist_sources__mutmut_39(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                    None
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_40(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        name=None,
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_41(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=None,
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_42(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        kind=None,
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_43(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        url=None,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_44(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        ready=None,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_45(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_46(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_47(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_48(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_49(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_50(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        name=str(None),
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_51(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        name=str(meta.get(None, "")),
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_52(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        name=str(meta.get("name", None)),
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_53(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        name=str(meta.get("")),
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_54(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        name=str(meta.get("name", )),
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_55(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        name=str(meta.get("XXnameXX", "")),
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_56(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        name=str(meta.get("NAME", "")),
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_57(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        name=str(meta.get("name", "XXXX")),
                        namespace=str(meta.get("namespace", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_58(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=str(None),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_59(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=str(meta.get(None, "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_60(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=str(meta.get("namespace", None)),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_61(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=str(meta.get("argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_62(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=str(meta.get("namespace", )),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_63(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=str(meta.get("XXnamespaceXX", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_64(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=str(meta.get("NAMESPACE", "argocd")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_65(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=str(meta.get("namespace", "XXargocdXX")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_66(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        namespace=str(meta.get("namespace", "ARGOCD")),
                        kind="GitRepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_67(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        kind="XXGitRepositoryXX",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_68(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        kind="gitrepository",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_69(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        kind="GITREPOSITORY",
                        url=url,
                        ready=True,
                    )
                )
        return sources

    def xǁGitOpsAdapterǁlist_sources__mutmut_70(self, namespace: str | None = None) -> list[GitOpsSource]:
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
                        ready=False,
                    )
                )
        return sources

    @_mutmut_mutated(mutants_xǁGitOpsAdapterǁget_source__mutmut)
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

    def xǁGitOpsAdapterǁget_source__mutmut_orig(self, name: str, namespace: str) -> GitOpsSource:
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

    def xǁGitOpsAdapterǁget_source__mutmut_1(self, name: str, namespace: str) -> GitOpsSource:
        apps = None
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

    def xǁGitOpsAdapterǁget_source__mutmut_2(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(None)
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

    def xǁGitOpsAdapterǁget_source__mutmut_3(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = None
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

    def xǁGitOpsAdapterǁget_source__mutmut_4(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get(None, {}) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁget_source__mutmut_5(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", None) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁget_source__mutmut_6(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get({}) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁget_source__mutmut_7(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", ) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁget_source__mutmut_8(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("XXmetadataXX", {}) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁget_source__mutmut_9(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("METADATA", {}) if isinstance(a.get("metadata"), dict) else {}
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

    def xǁGitOpsAdapterǁget_source__mutmut_10(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(None) == name:
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

    def xǁGitOpsAdapterǁget_source__mutmut_11(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get(None, "")) == name:
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

    def xǁGitOpsAdapterǁget_source__mutmut_12(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", None)) == name:
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

    def xǁGitOpsAdapterǁget_source__mutmut_13(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("")) == name:
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

    def xǁGitOpsAdapterǁget_source__mutmut_14(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", )) == name:
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

    def xǁGitOpsAdapterǁget_source__mutmut_15(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("XXnameXX", "")) == name:
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

    def xǁGitOpsAdapterǁget_source__mutmut_16(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("NAME", "")) == name:
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

    def xǁGitOpsAdapterǁget_source__mutmut_17(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "XXXX")) == name:
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

    def xǁGitOpsAdapterǁget_source__mutmut_18(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) != name:
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

    def xǁGitOpsAdapterǁget_source__mutmut_19(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = None
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_20(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get(None, {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_21(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", None) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_22(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get({}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_23(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", ) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_24(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("XXspecXX", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_25(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("SPEC", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_26(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = None
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_27(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get(None, {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_28(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", None) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_29(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get({}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_30(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", ) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_31(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("XXsourceXX", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_32(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("SOURCE", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_33(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=None,
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_34(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=None,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_35(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind=None,
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_36(self, name: str, namespace: str) -> GitOpsSource:
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
                    url=None,
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_37(self, name: str, namespace: str) -> GitOpsSource:
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
                    ready=None,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_38(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    namespace=namespace,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_39(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    kind="GitRepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_40(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_41(self, name: str, namespace: str) -> GitOpsSource:
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
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_42(self, name: str, namespace: str) -> GitOpsSource:
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
                    )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_43(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="XXGitRepositoryXX",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_44(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="gitrepository",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_45(self, name: str, namespace: str) -> GitOpsSource:
        apps = self._list_apps_raw(namespace)
        for a in apps:
            meta = a.get("metadata", {}) if isinstance(a.get("metadata"), dict) else {}
            if str(meta.get("name", "")) == name:
                spec = a.get("spec", {}) if isinstance(a.get("spec"), dict) else {}
                source = spec.get("source", {}) if isinstance(spec.get("source"), dict) else {}
                return GitOpsSource(
                    name=name,
                    namespace=namespace,
                    kind="GITREPOSITORY",
                    url=str(source.get("repoURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_46(self, name: str, namespace: str) -> GitOpsSource:
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
                    url=str(None),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_47(self, name: str, namespace: str) -> GitOpsSource:
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
                    url=str(source.get(None, "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_48(self, name: str, namespace: str) -> GitOpsSource:
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
                    url=str(source.get("repoURL", None)),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_49(self, name: str, namespace: str) -> GitOpsSource:
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
                    url=str(source.get("")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_50(self, name: str, namespace: str) -> GitOpsSource:
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
                    url=str(source.get("repoURL", )),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_51(self, name: str, namespace: str) -> GitOpsSource:
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
                    url=str(source.get("XXrepoURLXX", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_52(self, name: str, namespace: str) -> GitOpsSource:
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
                    url=str(source.get("repourl", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_53(self, name: str, namespace: str) -> GitOpsSource:
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
                    url=str(source.get("REPOURL", "")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_54(self, name: str, namespace: str) -> GitOpsSource:
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
                    url=str(source.get("repoURL", "XXXX")),
                    ready=True,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_55(self, name: str, namespace: str) -> GitOpsSource:
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
                    ready=False,
                )
        raise ValueError(f"Source {name} not found in {namespace}")

    def xǁGitOpsAdapterǁget_source__mutmut_56(self, name: str, namespace: str) -> GitOpsSource:
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
        raise ValueError(None)

    @_mutmut_mutated(mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut)
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_orig(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_1(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = None
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_2(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=None,
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_3(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
                    version=None,
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_4(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
                    version=_ARGO_VERSION,
                    namespace=None,
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_5(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
                    version=_ARGO_VERSION,
                    namespace=namespace,
                    plural=None,
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_6(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_7(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_8(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
                    version=_ARGO_VERSION,
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_9(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
                    version=_ARGO_VERSION,
                    namespace=namespace,
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_10(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
                    version=_ARGO_VERSION,
                    namespace=namespace,
                    plural="XXapplicationsXX",
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_11(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
                    version=_ARGO_VERSION,
                    namespace=namespace,
                    plural="APPLICATIONS",
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

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_12(self, namespace: str | None = None) -> list[dict]:  # type: ignore
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_ARGO_GROUP,
                    version=_ARGO_VERSION,
                    namespace=namespace,
                    plural="applications",
                )
            else:
                raw = None
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_13(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
                    group=None,
                    version=_ARGO_VERSION,
                    plural="applications",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_14(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
                    version=None,
                    plural="applications",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_15(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
                    plural=None,
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_16(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
                    version=_ARGO_VERSION,
                    plural="applications",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_17(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
                    plural="applications",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_18(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
                    )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_19(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
                    plural="XXapplicationsXX",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_20(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
                    plural="APPLICATIONS",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_21(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = None  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_22(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = cast(dict, raw).get(None, [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_23(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = cast(dict, raw).get("items", None)  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_24(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = cast(dict, raw).get([])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_25(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = cast(dict, raw).get("items", )  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_26(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = cast(None, raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_27(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = cast(dict, None).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_28(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = cast(raw).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_29(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = cast(dict, ).get("items", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_30(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = cast(dict, raw).get("XXitemsXX", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    def xǁGitOpsAdapterǁ_list_apps_raw__mutmut_31(self, namespace: str | None = None) -> list[dict]:  # type: ignore
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
        items = cast(dict, raw).get("ITEMS", [])  # type: ignore
        return [item for item in items if isinstance(item, dict)]

    @staticmethod
    @_mutmut_mutated(mutants_xǁGitOpsAdapterǁ_parse_app__mutmut)
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_orig(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_1(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_2(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get(None, {}) if isinstance(obj.get("metadata"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_3(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", None) if isinstance(obj.get("metadata"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_4(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get({}) if isinstance(obj.get("metadata"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_5(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", ) if isinstance(obj.get("metadata"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_6(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("XXmetadataXX", {}) if isinstance(obj.get("metadata"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_7(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("METADATA", {}) if isinstance(obj.get("metadata"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_8(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_9(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get(None, {}) if isinstance(obj.get("spec"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_10(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", None) if isinstance(obj.get("spec"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_11(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get({}) if isinstance(obj.get("spec"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_12(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", ) if isinstance(obj.get("spec"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_13(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("XXspecXX", {}) if isinstance(obj.get("spec"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_14(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("SPEC", {}) if isinstance(obj.get("spec"), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_15(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = None

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_16(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get(None, {}) if isinstance(obj.get("status"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_17(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", None) if isinstance(obj.get("status"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_18(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get({}) if isinstance(obj.get("status"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_19(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", ) if isinstance(obj.get("status"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_20(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("XXstatusXX", {}) if isinstance(obj.get("status"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_21(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("STATUS", {}) if isinstance(obj.get("status"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_22(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_23(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_24(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("XXsyncXX", None), ("health", None)]:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_25(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("SYNC", None), ("health", None)]:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_26(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("XXhealthXX", None)]:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_27(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("HEALTH", None)]:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_28(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_29(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(None, {}) if isinstance(status_data.get(field), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_30(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, None) if isinstance(status_data.get(field), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_31(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get({}) if isinstance(status_data.get(field), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_32(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, ) if isinstance(status_data.get(field), dict) else {}
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_33(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_34(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = str(field_data.get("status", "")).upper()
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_35(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = str(None).lower()
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_36(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = str(field_data.get(None, "")).lower()
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_37(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = str(field_data.get("status", None)).lower()
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_38(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = str(field_data.get("")).lower()
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_39(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = str(field_data.get("status", )).lower()
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_40(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = str(field_data.get("XXstatusXX", "")).lower()
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_41(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = str(field_data.get("STATUS", "")).lower()
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_42(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status_data = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        sync = SyncStatus.UNKNOWN
        health = HealthStatus.HEALTHY
        for field, st in [("sync", None), ("health", None)]:
            field_data = (
                status_data.get(field, {}) if isinstance(status_data.get(field), dict) else {}
            )
            status_val = str(field_data.get("status", "XXXX")).lower()
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_43(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            if field != "sync":
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_44(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            if field == "XXsyncXX":
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_45(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            if field == "SYNC":
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_46(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                if "XXsyncedXX" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_47(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                if "SYNCED" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_48(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                if "synced" not in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_49(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                    sync = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_50(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "XXoutofsyncXX" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_51(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "OUTOFSYNC" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_52(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "outofsync" not in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_53(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                    sync = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_54(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                    sync = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_55(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            elif field != "health":
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_56(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            elif field == "XXhealthXX":
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_57(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            elif field == "HEALTH":
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_58(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                if "XXhealthyXX" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_59(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                if "HEALTHY" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_60(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                if "healthy" not in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_61(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                    health = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_62(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "XXdegradedXX" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_63(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "DEGRADED" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_64(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "degraded" not in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_65(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                    health = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_66(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "XXprogressingXX" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_67(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "PROGRESSING" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_68(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "progressing" not in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_69(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                    health = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_70(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "XXsuspendedXX" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_71(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "SUSPENDED" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_72(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "suspended" not in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_73(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                    health = None
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_74(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "XXmissingXX" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_75(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "MISSING" in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_76(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                elif "missing" not in status_val:
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_77(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
                    health = None

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_78(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

        source = None

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_79(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

        source = spec.get(None, {}) if isinstance(spec.get("source"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_80(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

        source = spec.get("source", None) if isinstance(spec.get("source"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_81(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

        source = spec.get({}) if isinstance(spec.get("source"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_82(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

        source = spec.get("source", ) if isinstance(spec.get("source"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_83(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

        source = spec.get("XXsourceXX", {}) if isinstance(spec.get("source"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_84(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

        source = spec.get("SOURCE", {}) if isinstance(spec.get("source"), dict) else {}

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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_85(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            name=None,
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_86(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            namespace=None,
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_87(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            engine=None,
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_88(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            kind=None,
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_89(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            sync_status=None,
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_90(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            health_status=None,
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_91(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_92(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_93(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_94(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_95(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_96(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_97(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_98(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_99(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_100(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_101(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_102(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_103(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_104(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_105(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_106(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_107(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            name=str(None),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_108(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            name=str(meta.get(None, "")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_109(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            name=str(meta.get("name", None)),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_110(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            name=str(meta.get("")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_111(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            name=str(meta.get("name", )),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_112(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            name=str(meta.get("XXnameXX", "")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_113(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            name=str(meta.get("NAME", "")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_114(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            name=str(meta.get("name", "XXXX")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_115(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            namespace=str(None),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_116(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            namespace=str(meta.get(None, "argocd")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_117(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            namespace=str(meta.get("namespace", None)),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_118(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            namespace=str(meta.get("argocd")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_119(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            namespace=str(meta.get("namespace", )),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_120(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            namespace=str(meta.get("XXnamespaceXX", "argocd")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_121(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            namespace=str(meta.get("NAMESPACE", "argocd")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_122(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            namespace=str(meta.get("namespace", "XXargocdXX")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_123(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            namespace=str(meta.get("namespace", "ARGOCD")),
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_124(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            kind="XXApplicationXX",
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_125(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            kind="application",
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_126(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            kind="APPLICATION",
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

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_127(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=str(status_data.get("reconciledAt", "")) and None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_128(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=str(None) or None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_129(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=str(status_data.get(None, "")) or None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_130(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=str(status_data.get("reconciledAt", None)) or None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_131(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=str(status_data.get("")) or None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_132(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=str(status_data.get("reconciledAt", )) or None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_133(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=str(status_data.get("XXreconciledAtXX", "")) or None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_134(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=str(status_data.get("reconciledat", "")) or None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_135(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=str(status_data.get("RECONCILEDAT", "")) or None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_136(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_synced_at=str(status_data.get("reconciledAt", "XXXX")) or None,
            last_commit=str(status_data.get("sync", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_137(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", {}).get("revision", "")) and None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_138(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(None) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_139(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", {}).get(None, "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_140(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", {}).get("revision", None)) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_141(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", {}).get("")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_142(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", {}).get("revision", )) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_143(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get(None, {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_144(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", None).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_145(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get({}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_146(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", ).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_147(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("XXsyncXX", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_148(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("SYNC", {}).get("revision", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_149(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", {}).get("XXrevisionXX", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_150(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", {}).get("REVISION", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_151(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            last_commit=str(status_data.get("sync", {}).get("revision", "XXXX")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
            source_url=str(source.get("repoURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_152(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(source.get("repoURL", "")) and None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_153(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(None) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_154(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(source.get(None, "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_155(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(source.get("repoURL", None)) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_156(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(source.get("")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_157(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(source.get("repoURL", )) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_158(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(source.get("XXrepoURLXX", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_159(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(source.get("repourl", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_160(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(source.get("REPOURL", "")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_161(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            source_url=str(source.get("repoURL", "XXXX")) or None,
            revision=str(source.get("targetRevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_162(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(source.get("targetRevision", "")) and None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_163(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(None) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_164(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(source.get(None, "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_165(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(source.get("targetRevision", None)) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_166(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(source.get("")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_167(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(source.get("targetRevision", )) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_168(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(source.get("XXtargetRevisionXX", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_169(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(source.get("targetrevision", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_170(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(source.get("TARGETREVISION", "")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_171(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            revision=str(source.get("targetRevision", "XXXX")) or None,
            message=str(status_data.get("sync", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_172(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", {}).get("message", "")) and None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_173(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(None) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_174(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", {}).get(None, "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_175(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", {}).get("message", None)) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_176(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", {}).get("")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_177(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", {}).get("message", )) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_178(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get(None, {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_179(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", None).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_180(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get({}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_181(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", ).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_182(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("XXsyncXX", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_183(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("SYNC", {}).get("message", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_184(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", {}).get("XXmessageXX", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_185(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", {}).get("MESSAGE", "")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

    @staticmethod
    def xǁGitOpsAdapterǁ_parse_app__mutmut_186(obj: dict) -> GitOpsApp:  # noqa: C901  # type: ignore
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
            message=str(status_data.get("sync", {}).get("message", "XXXX")) or None
            if isinstance(status_data.get("sync"), dict)
            else None,
        )

mutants_xǁGitOpsAdapterǁ__init____mutmut['_mutmut_orig'] = GitOpsAdapter.xǁGitOpsAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ__init____mutmut['xǁGitOpsAdapterǁ__init____mutmut_1'] = GitOpsAdapter.xǁGitOpsAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['_mutmut_orig'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_1'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_2'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_3'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_4'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_5'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_6'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_7'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_8'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_9'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_10'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_11'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_12'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_13'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_14'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_15'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_16'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_17'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_18'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_19'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_20'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_21'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_22'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_23'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_24'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_25'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_26'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_27'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_28'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_29'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_30'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_31'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_32'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_33'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_34'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_35'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_36'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_37'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_38'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_39'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_40'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_41'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_42'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_43'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_44'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_45'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_46'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_47'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_48'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_49'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_50'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁdetect_engine__mutmut['xǁGitOpsAdapterǁdetect_engine__mutmut_51'] = GitOpsAdapter.xǁGitOpsAdapterǁdetect_engine__mutmut_51 # type: ignore # mutmut generated

mutants_xǁGitOpsAdapterǁlist_apps__mutmut['_mutmut_orig'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_apps__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_apps__mutmut['xǁGitOpsAdapterǁlist_apps__mutmut_1'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_apps__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_apps__mutmut['xǁGitOpsAdapterǁlist_apps__mutmut_2'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_apps__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_apps__mutmut['xǁGitOpsAdapterǁlist_apps__mutmut_3'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_apps__mutmut_3 # type: ignore # mutmut generated

mutants_xǁGitOpsAdapterǁget_app__mutmut['_mutmut_orig'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_1'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_2'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_3'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_4'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_5'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_6'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_7'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_8'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_9'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_10'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_11'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_12'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_13'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_14'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_15'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_16'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_17'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_app__mutmut['xǁGitOpsAdapterǁget_app__mutmut_18'] = GitOpsAdapter.xǁGitOpsAdapterǁget_app__mutmut_18 # type: ignore # mutmut generated

mutants_xǁGitOpsAdapterǁlist_sources__mutmut['_mutmut_orig'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_1'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_2'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_3'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_4'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_5'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_6'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_7'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_8'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_9'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_10'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_11'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_12'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_13'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_14'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_15'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_16'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_17'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_18'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_19'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_20'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_21'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_22'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_23'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_24'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_25'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_26'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_27'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_28'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_29'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_30'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_31'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_32'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_33'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_34'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_35'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_36'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_37'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_38'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_39'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_40'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_41'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_42'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_43'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_44'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_45'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_46'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_47'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_48'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_49'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_50'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_51'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_52'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_53'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_54'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_55'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_56'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_57'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_58'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_58 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_59'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_59 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_60'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_60 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_61'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_61 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_62'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_62 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_63'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_63 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_64'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_64 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_65'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_65 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_66'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_66 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_67'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_67 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_68'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_68 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_69'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_69 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁlist_sources__mutmut['xǁGitOpsAdapterǁlist_sources__mutmut_70'] = GitOpsAdapter.xǁGitOpsAdapterǁlist_sources__mutmut_70 # type: ignore # mutmut generated

mutants_xǁGitOpsAdapterǁget_source__mutmut['_mutmut_orig'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_1'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_2'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_3'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_4'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_5'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_6'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_7'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_8'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_9'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_10'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_11'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_12'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_13'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_14'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_15'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_16'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_17'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_18'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_19'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_20'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_21'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_22'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_23'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_24'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_25'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_26'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_27'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_28'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_29'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_30'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_31'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_32'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_33'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_34'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_35'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_36'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_37'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_38'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_39'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_40'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_41'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_42'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_43'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_44'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_45'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_46'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_47'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_48'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_49'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_50'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_51'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_52'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_53'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_54'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_55'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁget_source__mutmut['xǁGitOpsAdapterǁget_source__mutmut_56'] = GitOpsAdapter.xǁGitOpsAdapterǁget_source__mutmut_56 # type: ignore # mutmut generated

mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['_mutmut_orig'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_1'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_2'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_3'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_4'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_5'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_6'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_7'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_8'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_9'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_10'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_11'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_12'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_13'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_14'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_15'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_16'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_17'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_18'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_19'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_20'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_21'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_22'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_23'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_24'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_25'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_26'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_27'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_28'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_29'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_30'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_list_apps_raw__mutmut['xǁGitOpsAdapterǁ_list_apps_raw__mutmut_31'] = GitOpsAdapter.xǁGitOpsAdapterǁ_list_apps_raw__mutmut_31 # type: ignore # mutmut generated

mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['_mutmut_orig'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_1'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_2'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_3'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_4'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_5'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_6'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_7'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_8'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_9'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_10'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_11'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_12'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_13'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_14'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_15'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_16'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_17'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_18'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_19'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_20'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_21'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_22'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_23'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_24'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_25'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_26'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_27'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_28'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_29'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_30'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_31'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_32'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_33'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_34'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_35'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_36'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_37'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_38'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_39'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_40'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_41'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_42'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_43'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_44'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_45'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_46'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_47'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_48'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_49'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_50'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_51'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_52'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_53'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_54'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_55'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_56'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_57'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_58'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_58 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_59'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_59 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_60'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_60 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_61'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_61 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_62'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_62 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_63'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_63 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_64'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_64 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_65'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_65 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_66'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_66 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_67'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_67 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_68'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_68 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_69'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_69 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_70'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_70 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_71'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_71 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_72'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_72 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_73'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_73 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_74'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_74 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_75'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_75 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_76'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_76 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_77'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_77 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_78'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_78 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_79'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_79 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_80'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_80 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_81'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_81 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_82'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_82 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_83'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_83 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_84'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_84 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_85'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_85 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_86'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_86 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_87'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_87 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_88'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_88 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_89'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_89 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_90'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_90 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_91'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_91 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_92'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_92 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_93'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_93 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_94'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_94 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_95'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_95 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_96'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_96 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_97'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_97 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_98'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_98 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_99'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_99 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_100'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_100 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_101'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_101 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_102'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_102 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_103'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_103 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_104'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_104 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_105'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_105 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_106'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_106 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_107'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_107 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_108'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_108 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_109'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_109 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_110'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_110 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_111'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_111 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_112'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_112 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_113'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_113 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_114'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_114 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_115'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_115 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_116'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_116 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_117'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_117 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_118'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_118 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_119'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_119 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_120'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_120 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_121'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_121 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_122'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_122 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_123'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_123 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_124'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_124 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_125'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_125 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_126'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_126 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_127'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_127 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_128'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_128 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_129'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_129 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_130'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_130 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_131'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_131 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_132'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_132 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_133'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_133 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_134'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_134 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_135'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_135 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_136'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_136 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_137'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_137 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_138'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_138 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_139'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_139 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_140'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_140 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_141'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_141 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_142'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_142 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_143'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_143 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_144'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_144 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_145'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_145 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_146'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_146 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_147'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_147 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_148'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_148 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_149'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_149 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_150'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_150 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_151'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_151 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_152'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_152 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_153'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_153 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_154'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_154 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_155'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_155 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_156'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_156 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_157'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_157 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_158'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_158 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_159'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_159 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_160'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_160 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_161'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_161 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_162'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_162 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_163'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_163 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_164'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_164 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_165'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_165 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_166'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_166 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_167'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_167 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_168'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_168 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_169'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_169 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_170'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_170 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_171'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_171 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_172'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_172 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_173'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_173 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_174'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_174 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_175'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_175 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_176'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_176 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_177'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_177 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_178'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_178 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_179'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_179 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_180'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_180 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_181'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_181 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_182'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_182 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_183'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_183 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_184'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_184 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_185'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_185 # type: ignore # mutmut generated
mutants_xǁGitOpsAdapterǁ_parse_app__mutmut['xǁGitOpsAdapterǁ_parse_app__mutmut_186'] = GitOpsAdapter.xǁGitOpsAdapterǁ_parse_app__mutmut_186 # type: ignore # mutmut generated
