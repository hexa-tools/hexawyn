from __future__ import annotations

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.domain.errors import ComponentNotInstalledError
from hexawyn.domain.models.rollouts import (
    AnalysisRun,
    Rollout,
    RolloutsDetectionResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut: MutantDict = {}  # type: ignore
mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut: MutantDict = {}  # type: ignore
mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut: MutantDict = {}  # type: ignore
mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut: MutantDict = {}  # type: ignore


class ArgoRolloutsDetector(RolloutsPort):
    """Detects Argo Rollouts by checking for CRDs and provides read-only access.

    All tools are read-only — promote, abort, and retry are never triggered.
    """

    @_mutmut_mutated(mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut)
    def detect_rollouts(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_orig(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_1(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=None,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_2(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=None,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_3(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=None,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_4(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=None,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_5(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=None,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_6(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=None,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_7(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_8(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_9(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_10(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_11(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_12(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_13(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_14(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_15(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=True,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_16(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=1,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_17(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=1,
            progressing=0,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_18(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=1,
            degraded=0,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_19(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=1,
            paused=0,
        )

    def xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_20(self) -> RolloutsDetectionResult:
        return RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=1,
        )

    @_mutmut_mutated(mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut)
    def list_rollouts(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_orig(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_1(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            None, "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_2(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", None
        )

    def xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_3(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_4(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", )

    def xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_5(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "XXArgo RolloutsXX", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_6(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "argo rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_7(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "ARGO ROLLOUTS", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_8(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "XXhttps://argo-rollouts.readthedocs.io/en/stable/installation/XX"
        )

    def xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_9(self, namespace: str | None = None) -> list[Rollout]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "HTTPS://ARGO-ROLLOUTS.READTHEDOCS.IO/EN/STABLE/INSTALLATION/"
        )

    @_mutmut_mutated(mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut)
    def get_rollout(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁget_rollout__mutmut_orig(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁget_rollout__mutmut_1(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            None, "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁget_rollout__mutmut_2(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "Argo Rollouts", None
        )

    def xǁArgoRolloutsDetectorǁget_rollout__mutmut_3(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁget_rollout__mutmut_4(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "Argo Rollouts", )

    def xǁArgoRolloutsDetectorǁget_rollout__mutmut_5(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "XXArgo RolloutsXX", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁget_rollout__mutmut_6(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "argo rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁget_rollout__mutmut_7(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "ARGO ROLLOUTS", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁget_rollout__mutmut_8(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "XXhttps://argo-rollouts.readthedocs.io/en/stable/installation/XX"
        )

    def xǁArgoRolloutsDetectorǁget_rollout__mutmut_9(self, name: str, namespace: str) -> Rollout:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "HTTPS://ARGO-ROLLOUTS.READTHEDOCS.IO/EN/STABLE/INSTALLATION/"
        )

    @_mutmut_mutated(mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut)
    def list_analysis_runs(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_orig(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_1(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            None, "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_2(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", None
        )

    def xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_3(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_4(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", )

    def xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_5(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "XXArgo RolloutsXX", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_6(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "argo rollouts", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_7(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "ARGO ROLLOUTS", "https://argo-rollouts.readthedocs.io/en/stable/installation/"
        )

    def xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_8(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "XXhttps://argo-rollouts.readthedocs.io/en/stable/installation/XX"
        )

    def xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_9(
        self, namespace: str | None = None, rollout_name: str | None = None
    ) -> list[AnalysisRun]:
        raise ComponentNotInstalledError(
            "Argo Rollouts", "HTTPS://ARGO-ROLLOUTS.READTHEDOCS.IO/EN/STABLE/INSTALLATION/"
        )

mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['_mutmut_orig'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_orig # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_1'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_1 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_2'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_2 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_3'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_3 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_4'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_4 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_5'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_5 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_6'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_6 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_7'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_7 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_8'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_8 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_9'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_9 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_10'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_10 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_11'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_11 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_12'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_12 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_13'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_13 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_14'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_14 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_15'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_15 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_16'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_16 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_17'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_17 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_18'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_18 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_19'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_19 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut['xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_20'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁdetect_rollouts__mutmut_20 # type: ignore # mutmut generated

mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut['_mutmut_orig'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_orig # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut['xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_1'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_1 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut['xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_2'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_2 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut['xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_3'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_3 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut['xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_4'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_4 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut['xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_5'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_5 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut['xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_6'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_6 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut['xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_7'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_7 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut['xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_8'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_8 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_rollouts__mutmut['xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_9'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_rollouts__mutmut_9 # type: ignore # mutmut generated

mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut['_mutmut_orig'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁget_rollout__mutmut_orig # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut['xǁArgoRolloutsDetectorǁget_rollout__mutmut_1'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁget_rollout__mutmut_1 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut['xǁArgoRolloutsDetectorǁget_rollout__mutmut_2'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁget_rollout__mutmut_2 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut['xǁArgoRolloutsDetectorǁget_rollout__mutmut_3'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁget_rollout__mutmut_3 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut['xǁArgoRolloutsDetectorǁget_rollout__mutmut_4'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁget_rollout__mutmut_4 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut['xǁArgoRolloutsDetectorǁget_rollout__mutmut_5'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁget_rollout__mutmut_5 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut['xǁArgoRolloutsDetectorǁget_rollout__mutmut_6'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁget_rollout__mutmut_6 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut['xǁArgoRolloutsDetectorǁget_rollout__mutmut_7'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁget_rollout__mutmut_7 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut['xǁArgoRolloutsDetectorǁget_rollout__mutmut_8'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁget_rollout__mutmut_8 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁget_rollout__mutmut['xǁArgoRolloutsDetectorǁget_rollout__mutmut_9'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁget_rollout__mutmut_9 # type: ignore # mutmut generated

mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut['_mutmut_orig'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut['xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_1'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut['xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_2'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut['xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_3'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut['xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_4'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut['xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_5'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut['xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_6'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut['xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_7'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut['xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_8'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut['xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_9'] = ArgoRolloutsDetector.xǁArgoRolloutsDetectorǁlist_analysis_runs__mutmut_9 # type: ignore # mutmut generated
