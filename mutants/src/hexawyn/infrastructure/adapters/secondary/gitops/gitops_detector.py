from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.domain.models.gitops import (
    GitOpsApp,
    GitOpsDetectionResult,
    GitOpsEngine,
    GitOpsSource,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGitOpsDetectorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsDetectorǁ_ensure_detected__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsDetectorǁlist_apps__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsDetectorǁget_app__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsDetectorǁlist_sources__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitOpsDetectorǁget_source__mutmut: MutantDict = {}  # type: ignore


class GitOpsDetector(GitOpsPort):
    """Auto-detects Flux CD or Argo CD by checking for CRDs in the cluster.

    Delegates to FluxAdapter or ArgoCDAdapter once the engine is detected.
    Detection order: Flux CRDs first, then Argo CD CRDs.
    """

    @_mutmut_mutated(mutants_xǁGitOpsDetectorǁ__init____mutmut)
    def __init__(self) -> None:
        self._delegate: GitOpsPort | None = None

    def xǁGitOpsDetectorǁ__init____mutmut_orig(self) -> None:
        self._delegate: GitOpsPort | None = None

    def xǁGitOpsDetectorǁ__init____mutmut_1(self) -> None:
        self._delegate: GitOpsPort | None = ""

    @_mutmut_mutated(mutants_xǁGitOpsDetectorǁ_ensure_detected__mutmut)
    def _ensure_detected(self) -> GitOpsPort:
        if self._delegate is not None:
            return self._delegate
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        raise GitOpsEngineNotFoundError()

    def xǁGitOpsDetectorǁ_ensure_detected__mutmut_orig(self) -> GitOpsPort:
        if self._delegate is not None:
            return self._delegate
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        raise GitOpsEngineNotFoundError()

    def xǁGitOpsDetectorǁ_ensure_detected__mutmut_1(self) -> GitOpsPort:
        if self._delegate is None:
            return self._delegate
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        raise GitOpsEngineNotFoundError()

    @_mutmut_mutated(mutants_xǁGitOpsDetectorǁdetect_engine__mutmut)
    def detect_engine(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_orig(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_1(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=None,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_2(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=None,
                out_of_sync_count=0,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_3(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=None,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_4(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=None,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_5(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_6(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_7(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_8(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                out_of_sync_count=0,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_9(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_10(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_11(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=1,
                out_of_sync_count=0,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_12(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=1,
                failed_count=0,
            )

    def xǁGitOpsDetectorǁdetect_engine__mutmut_13(self) -> GitOpsDetectionResult:
        from hexawyn.domain.errors import GitOpsEngineNotFoundError

        try:
            self._ensure_detected()
            return self._delegate.detect_engine()  # type: ignore[union-attr]
        except GitOpsEngineNotFoundError:
            return GitOpsDetectionResult(
                engine=GitOpsEngine.NONE,
                version=None,
                namespace=None,
                apps_count=0,
                out_of_sync_count=0,
                failed_count=1,
            )

    @_mutmut_mutated(mutants_xǁGitOpsDetectorǁlist_apps__mutmut)
    def list_apps(self, namespace: str | None = None) -> list[GitOpsApp]:
        return self._ensure_detected().list_apps(namespace=namespace)

    def xǁGitOpsDetectorǁlist_apps__mutmut_orig(self, namespace: str | None = None) -> list[GitOpsApp]:
        return self._ensure_detected().list_apps(namespace=namespace)

    def xǁGitOpsDetectorǁlist_apps__mutmut_1(self, namespace: str | None = None) -> list[GitOpsApp]:
        return self._ensure_detected().list_apps(namespace=None)

    @_mutmut_mutated(mutants_xǁGitOpsDetectorǁget_app__mutmut)
    def get_app(self, name: str, namespace: str) -> GitOpsApp:
        return self._ensure_detected().get_app(name=name, namespace=namespace)

    def xǁGitOpsDetectorǁget_app__mutmut_orig(self, name: str, namespace: str) -> GitOpsApp:
        return self._ensure_detected().get_app(name=name, namespace=namespace)

    def xǁGitOpsDetectorǁget_app__mutmut_1(self, name: str, namespace: str) -> GitOpsApp:
        return self._ensure_detected().get_app(name=None, namespace=namespace)

    def xǁGitOpsDetectorǁget_app__mutmut_2(self, name: str, namespace: str) -> GitOpsApp:
        return self._ensure_detected().get_app(name=name, namespace=None)

    def xǁGitOpsDetectorǁget_app__mutmut_3(self, name: str, namespace: str) -> GitOpsApp:
        return self._ensure_detected().get_app(namespace=namespace)

    def xǁGitOpsDetectorǁget_app__mutmut_4(self, name: str, namespace: str) -> GitOpsApp:
        return self._ensure_detected().get_app(name=name, )

    @_mutmut_mutated(mutants_xǁGitOpsDetectorǁlist_sources__mutmut)
    def list_sources(self, namespace: str | None = None) -> list[GitOpsSource]:
        return self._ensure_detected().list_sources(namespace=namespace)

    def xǁGitOpsDetectorǁlist_sources__mutmut_orig(self, namespace: str | None = None) -> list[GitOpsSource]:
        return self._ensure_detected().list_sources(namespace=namespace)

    def xǁGitOpsDetectorǁlist_sources__mutmut_1(self, namespace: str | None = None) -> list[GitOpsSource]:
        return self._ensure_detected().list_sources(namespace=None)

    @_mutmut_mutated(mutants_xǁGitOpsDetectorǁget_source__mutmut)
    def get_source(self, name: str, namespace: str) -> GitOpsSource:
        return self._ensure_detected().get_source(name=name, namespace=namespace)

    def xǁGitOpsDetectorǁget_source__mutmut_orig(self, name: str, namespace: str) -> GitOpsSource:
        return self._ensure_detected().get_source(name=name, namespace=namespace)

    def xǁGitOpsDetectorǁget_source__mutmut_1(self, name: str, namespace: str) -> GitOpsSource:
        return self._ensure_detected().get_source(name=None, namespace=namespace)

    def xǁGitOpsDetectorǁget_source__mutmut_2(self, name: str, namespace: str) -> GitOpsSource:
        return self._ensure_detected().get_source(name=name, namespace=None)

    def xǁGitOpsDetectorǁget_source__mutmut_3(self, name: str, namespace: str) -> GitOpsSource:
        return self._ensure_detected().get_source(namespace=namespace)

    def xǁGitOpsDetectorǁget_source__mutmut_4(self, name: str, namespace: str) -> GitOpsSource:
        return self._ensure_detected().get_source(name=name, )

mutants_xǁGitOpsDetectorǁ__init____mutmut['_mutmut_orig'] = GitOpsDetector.xǁGitOpsDetectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁ__init____mutmut['xǁGitOpsDetectorǁ__init____mutmut_1'] = GitOpsDetector.xǁGitOpsDetectorǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitOpsDetectorǁ_ensure_detected__mutmut['_mutmut_orig'] = GitOpsDetector.xǁGitOpsDetectorǁ_ensure_detected__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁ_ensure_detected__mutmut['xǁGitOpsDetectorǁ_ensure_detected__mutmut_1'] = GitOpsDetector.xǁGitOpsDetectorǁ_ensure_detected__mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['_mutmut_orig'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_1'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_2'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_3'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_4'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_5'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_6'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_7'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_8'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_9'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_10'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_11'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_12'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁdetect_engine__mutmut['xǁGitOpsDetectorǁdetect_engine__mutmut_13'] = GitOpsDetector.xǁGitOpsDetectorǁdetect_engine__mutmut_13 # type: ignore # mutmut generated

mutants_xǁGitOpsDetectorǁlist_apps__mutmut['_mutmut_orig'] = GitOpsDetector.xǁGitOpsDetectorǁlist_apps__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁlist_apps__mutmut['xǁGitOpsDetectorǁlist_apps__mutmut_1'] = GitOpsDetector.xǁGitOpsDetectorǁlist_apps__mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitOpsDetectorǁget_app__mutmut['_mutmut_orig'] = GitOpsDetector.xǁGitOpsDetectorǁget_app__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁget_app__mutmut['xǁGitOpsDetectorǁget_app__mutmut_1'] = GitOpsDetector.xǁGitOpsDetectorǁget_app__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁget_app__mutmut['xǁGitOpsDetectorǁget_app__mutmut_2'] = GitOpsDetector.xǁGitOpsDetectorǁget_app__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁget_app__mutmut['xǁGitOpsDetectorǁget_app__mutmut_3'] = GitOpsDetector.xǁGitOpsDetectorǁget_app__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁget_app__mutmut['xǁGitOpsDetectorǁget_app__mutmut_4'] = GitOpsDetector.xǁGitOpsDetectorǁget_app__mutmut_4 # type: ignore # mutmut generated

mutants_xǁGitOpsDetectorǁlist_sources__mutmut['_mutmut_orig'] = GitOpsDetector.xǁGitOpsDetectorǁlist_sources__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁlist_sources__mutmut['xǁGitOpsDetectorǁlist_sources__mutmut_1'] = GitOpsDetector.xǁGitOpsDetectorǁlist_sources__mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitOpsDetectorǁget_source__mutmut['_mutmut_orig'] = GitOpsDetector.xǁGitOpsDetectorǁget_source__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁget_source__mutmut['xǁGitOpsDetectorǁget_source__mutmut_1'] = GitOpsDetector.xǁGitOpsDetectorǁget_source__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁget_source__mutmut['xǁGitOpsDetectorǁget_source__mutmut_2'] = GitOpsDetector.xǁGitOpsDetectorǁget_source__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁget_source__mutmut['xǁGitOpsDetectorǁget_source__mutmut_3'] = GitOpsDetector.xǁGitOpsDetectorǁget_source__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitOpsDetectorǁget_source__mutmut['xǁGitOpsDetectorǁget_source__mutmut_4'] = GitOpsDetector.xǁGitOpsDetectorǁget_source__mutmut_4 # type: ignore # mutmut generated
