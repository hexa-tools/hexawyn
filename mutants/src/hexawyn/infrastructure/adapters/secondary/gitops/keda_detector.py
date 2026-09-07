from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.domain.errors import ComponentNotInstalledError
from hexawyn.domain.models.keda import (
    KedaDetectionResult,
    KedaScaledJob,
    KedaScaledObject,
    KedaTriggerAuth,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKedaDetectorǁdetect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaDetectorǁget_scaledobject__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaDetectorǁget_trigger_auth__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKedaDetectorǁget_scaledjob__mutmut: MutantDict = {}  # type: ignore


class KedaDetector(KedaPort):
    """Auto-detects KEDA via CRDs. All read-only — never triggers scale."""

    @_mutmut_mutated(mutants_xǁKedaDetectorǁdetect__mutmut)
    def detect(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_orig(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_1(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=None,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_2(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=None,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_3(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=None,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_4(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=None,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_5(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=None,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_6(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=None,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_7(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=None,
        )

    def xǁKedaDetectorǁdetect__mutmut_8(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_9(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_10(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_11(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_12(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_13(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_14(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_15(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_16(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            )

    def xǁKedaDetectorǁdetect__mutmut_17(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=True,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_18(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=1,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_19(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=1,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_20(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=1,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_21(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=1,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def xǁKedaDetectorǁdetect__mutmut_22(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=1,
            managed_namespaces=[],
        )

    @_mutmut_mutated(mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut)
    def list_scaledobjects(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledobjects__mutmut_orig(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledobjects__mutmut_1(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise ComponentNotInstalledError(None, "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledobjects__mutmut_2(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise ComponentNotInstalledError("KEDA", None)

    def xǁKedaDetectorǁlist_scaledobjects__mutmut_3(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise ComponentNotInstalledError("https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledobjects__mutmut_4(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise ComponentNotInstalledError("KEDA", )

    def xǁKedaDetectorǁlist_scaledobjects__mutmut_5(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise ComponentNotInstalledError("XXKEDAXX", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledobjects__mutmut_6(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise ComponentNotInstalledError("keda", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledobjects__mutmut_7(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise ComponentNotInstalledError("KEDA", "XXhttps://keda.sh/docs/deploy/XX")

    def xǁKedaDetectorǁlist_scaledobjects__mutmut_8(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise ComponentNotInstalledError("KEDA", "HTTPS://KEDA.SH/DOCS/DEPLOY/")

    @_mutmut_mutated(mutants_xǁKedaDetectorǁget_scaledobject__mutmut)
    def get_scaledobject(self, name: str, namespace: str) -> KedaScaledObject:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledobject__mutmut_orig(self, name: str, namespace: str) -> KedaScaledObject:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledobject__mutmut_1(self, name: str, namespace: str) -> KedaScaledObject:
        raise ComponentNotInstalledError(None, "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledobject__mutmut_2(self, name: str, namespace: str) -> KedaScaledObject:
        raise ComponentNotInstalledError("KEDA", None)

    def xǁKedaDetectorǁget_scaledobject__mutmut_3(self, name: str, namespace: str) -> KedaScaledObject:
        raise ComponentNotInstalledError("https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledobject__mutmut_4(self, name: str, namespace: str) -> KedaScaledObject:
        raise ComponentNotInstalledError("KEDA", )

    def xǁKedaDetectorǁget_scaledobject__mutmut_5(self, name: str, namespace: str) -> KedaScaledObject:
        raise ComponentNotInstalledError("XXKEDAXX", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledobject__mutmut_6(self, name: str, namespace: str) -> KedaScaledObject:
        raise ComponentNotInstalledError("keda", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledobject__mutmut_7(self, name: str, namespace: str) -> KedaScaledObject:
        raise ComponentNotInstalledError("KEDA", "XXhttps://keda.sh/docs/deploy/XX")

    def xǁKedaDetectorǁget_scaledobject__mutmut_8(self, name: str, namespace: str) -> KedaScaledObject:
        raise ComponentNotInstalledError("KEDA", "HTTPS://KEDA.SH/DOCS/DEPLOY/")

    @_mutmut_mutated(mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut)
    def list_trigger_auths(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_trigger_auths__mutmut_orig(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_trigger_auths__mutmut_1(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise ComponentNotInstalledError(None, "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_trigger_auths__mutmut_2(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise ComponentNotInstalledError("KEDA", None)

    def xǁKedaDetectorǁlist_trigger_auths__mutmut_3(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise ComponentNotInstalledError("https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_trigger_auths__mutmut_4(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise ComponentNotInstalledError("KEDA", )

    def xǁKedaDetectorǁlist_trigger_auths__mutmut_5(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise ComponentNotInstalledError("XXKEDAXX", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_trigger_auths__mutmut_6(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise ComponentNotInstalledError("keda", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_trigger_auths__mutmut_7(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise ComponentNotInstalledError("KEDA", "XXhttps://keda.sh/docs/deploy/XX")

    def xǁKedaDetectorǁlist_trigger_auths__mutmut_8(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise ComponentNotInstalledError("KEDA", "HTTPS://KEDA.SH/DOCS/DEPLOY/")

    @_mutmut_mutated(mutants_xǁKedaDetectorǁget_trigger_auth__mutmut)
    def get_trigger_auth(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_trigger_auth__mutmut_orig(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_trigger_auth__mutmut_1(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise ComponentNotInstalledError(None, "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_trigger_auth__mutmut_2(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise ComponentNotInstalledError("KEDA", None)

    def xǁKedaDetectorǁget_trigger_auth__mutmut_3(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise ComponentNotInstalledError("https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_trigger_auth__mutmut_4(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise ComponentNotInstalledError("KEDA", )

    def xǁKedaDetectorǁget_trigger_auth__mutmut_5(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise ComponentNotInstalledError("XXKEDAXX", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_trigger_auth__mutmut_6(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise ComponentNotInstalledError("keda", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_trigger_auth__mutmut_7(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise ComponentNotInstalledError("KEDA", "XXhttps://keda.sh/docs/deploy/XX")

    def xǁKedaDetectorǁget_trigger_auth__mutmut_8(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise ComponentNotInstalledError("KEDA", "HTTPS://KEDA.SH/DOCS/DEPLOY/")

    @_mutmut_mutated(mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut)
    def list_scaledjobs(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledjobs__mutmut_orig(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledjobs__mutmut_1(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise ComponentNotInstalledError(None, "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledjobs__mutmut_2(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise ComponentNotInstalledError("KEDA", None)

    def xǁKedaDetectorǁlist_scaledjobs__mutmut_3(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise ComponentNotInstalledError("https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledjobs__mutmut_4(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise ComponentNotInstalledError("KEDA", )

    def xǁKedaDetectorǁlist_scaledjobs__mutmut_5(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise ComponentNotInstalledError("XXKEDAXX", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledjobs__mutmut_6(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise ComponentNotInstalledError("keda", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁlist_scaledjobs__mutmut_7(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise ComponentNotInstalledError("KEDA", "XXhttps://keda.sh/docs/deploy/XX")

    def xǁKedaDetectorǁlist_scaledjobs__mutmut_8(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise ComponentNotInstalledError("KEDA", "HTTPS://KEDA.SH/DOCS/DEPLOY/")

    @_mutmut_mutated(mutants_xǁKedaDetectorǁget_scaledjob__mutmut)
    def get_scaledjob(self, name: str, namespace: str) -> KedaScaledJob:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledjob__mutmut_orig(self, name: str, namespace: str) -> KedaScaledJob:
        raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledjob__mutmut_1(self, name: str, namespace: str) -> KedaScaledJob:
        raise ComponentNotInstalledError(None, "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledjob__mutmut_2(self, name: str, namespace: str) -> KedaScaledJob:
        raise ComponentNotInstalledError("KEDA", None)

    def xǁKedaDetectorǁget_scaledjob__mutmut_3(self, name: str, namespace: str) -> KedaScaledJob:
        raise ComponentNotInstalledError("https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledjob__mutmut_4(self, name: str, namespace: str) -> KedaScaledJob:
        raise ComponentNotInstalledError("KEDA", )

    def xǁKedaDetectorǁget_scaledjob__mutmut_5(self, name: str, namespace: str) -> KedaScaledJob:
        raise ComponentNotInstalledError("XXKEDAXX", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledjob__mutmut_6(self, name: str, namespace: str) -> KedaScaledJob:
        raise ComponentNotInstalledError("keda", "https://keda.sh/docs/deploy/")

    def xǁKedaDetectorǁget_scaledjob__mutmut_7(self, name: str, namespace: str) -> KedaScaledJob:
        raise ComponentNotInstalledError("KEDA", "XXhttps://keda.sh/docs/deploy/XX")

    def xǁKedaDetectorǁget_scaledjob__mutmut_8(self, name: str, namespace: str) -> KedaScaledJob:
        raise ComponentNotInstalledError("KEDA", "HTTPS://KEDA.SH/DOCS/DEPLOY/")

mutants_xǁKedaDetectorǁdetect__mutmut['_mutmut_orig'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_1'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_2'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_3'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_4'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_5'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_6'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_7'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_8'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_9'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_10'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_11'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_12'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_13'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_14'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_15'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_16'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_17'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_18'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_19'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_20'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_21'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁdetect__mutmut['xǁKedaDetectorǁdetect__mutmut_22'] = KedaDetector.xǁKedaDetectorǁdetect__mutmut_22 # type: ignore # mutmut generated

mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut['_mutmut_orig'] = KedaDetector.xǁKedaDetectorǁlist_scaledobjects__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut['xǁKedaDetectorǁlist_scaledobjects__mutmut_1'] = KedaDetector.xǁKedaDetectorǁlist_scaledobjects__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut['xǁKedaDetectorǁlist_scaledobjects__mutmut_2'] = KedaDetector.xǁKedaDetectorǁlist_scaledobjects__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut['xǁKedaDetectorǁlist_scaledobjects__mutmut_3'] = KedaDetector.xǁKedaDetectorǁlist_scaledobjects__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut['xǁKedaDetectorǁlist_scaledobjects__mutmut_4'] = KedaDetector.xǁKedaDetectorǁlist_scaledobjects__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut['xǁKedaDetectorǁlist_scaledobjects__mutmut_5'] = KedaDetector.xǁKedaDetectorǁlist_scaledobjects__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut['xǁKedaDetectorǁlist_scaledobjects__mutmut_6'] = KedaDetector.xǁKedaDetectorǁlist_scaledobjects__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut['xǁKedaDetectorǁlist_scaledobjects__mutmut_7'] = KedaDetector.xǁKedaDetectorǁlist_scaledobjects__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledobjects__mutmut['xǁKedaDetectorǁlist_scaledobjects__mutmut_8'] = KedaDetector.xǁKedaDetectorǁlist_scaledobjects__mutmut_8 # type: ignore # mutmut generated

mutants_xǁKedaDetectorǁget_scaledobject__mutmut['_mutmut_orig'] = KedaDetector.xǁKedaDetectorǁget_scaledobject__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledobject__mutmut['xǁKedaDetectorǁget_scaledobject__mutmut_1'] = KedaDetector.xǁKedaDetectorǁget_scaledobject__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledobject__mutmut['xǁKedaDetectorǁget_scaledobject__mutmut_2'] = KedaDetector.xǁKedaDetectorǁget_scaledobject__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledobject__mutmut['xǁKedaDetectorǁget_scaledobject__mutmut_3'] = KedaDetector.xǁKedaDetectorǁget_scaledobject__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledobject__mutmut['xǁKedaDetectorǁget_scaledobject__mutmut_4'] = KedaDetector.xǁKedaDetectorǁget_scaledobject__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledobject__mutmut['xǁKedaDetectorǁget_scaledobject__mutmut_5'] = KedaDetector.xǁKedaDetectorǁget_scaledobject__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledobject__mutmut['xǁKedaDetectorǁget_scaledobject__mutmut_6'] = KedaDetector.xǁKedaDetectorǁget_scaledobject__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledobject__mutmut['xǁKedaDetectorǁget_scaledobject__mutmut_7'] = KedaDetector.xǁKedaDetectorǁget_scaledobject__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledobject__mutmut['xǁKedaDetectorǁget_scaledobject__mutmut_8'] = KedaDetector.xǁKedaDetectorǁget_scaledobject__mutmut_8 # type: ignore # mutmut generated

mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut['_mutmut_orig'] = KedaDetector.xǁKedaDetectorǁlist_trigger_auths__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut['xǁKedaDetectorǁlist_trigger_auths__mutmut_1'] = KedaDetector.xǁKedaDetectorǁlist_trigger_auths__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut['xǁKedaDetectorǁlist_trigger_auths__mutmut_2'] = KedaDetector.xǁKedaDetectorǁlist_trigger_auths__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut['xǁKedaDetectorǁlist_trigger_auths__mutmut_3'] = KedaDetector.xǁKedaDetectorǁlist_trigger_auths__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut['xǁKedaDetectorǁlist_trigger_auths__mutmut_4'] = KedaDetector.xǁKedaDetectorǁlist_trigger_auths__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut['xǁKedaDetectorǁlist_trigger_auths__mutmut_5'] = KedaDetector.xǁKedaDetectorǁlist_trigger_auths__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut['xǁKedaDetectorǁlist_trigger_auths__mutmut_6'] = KedaDetector.xǁKedaDetectorǁlist_trigger_auths__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut['xǁKedaDetectorǁlist_trigger_auths__mutmut_7'] = KedaDetector.xǁKedaDetectorǁlist_trigger_auths__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_trigger_auths__mutmut['xǁKedaDetectorǁlist_trigger_auths__mutmut_8'] = KedaDetector.xǁKedaDetectorǁlist_trigger_auths__mutmut_8 # type: ignore # mutmut generated

mutants_xǁKedaDetectorǁget_trigger_auth__mutmut['_mutmut_orig'] = KedaDetector.xǁKedaDetectorǁget_trigger_auth__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_trigger_auth__mutmut['xǁKedaDetectorǁget_trigger_auth__mutmut_1'] = KedaDetector.xǁKedaDetectorǁget_trigger_auth__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_trigger_auth__mutmut['xǁKedaDetectorǁget_trigger_auth__mutmut_2'] = KedaDetector.xǁKedaDetectorǁget_trigger_auth__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_trigger_auth__mutmut['xǁKedaDetectorǁget_trigger_auth__mutmut_3'] = KedaDetector.xǁKedaDetectorǁget_trigger_auth__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_trigger_auth__mutmut['xǁKedaDetectorǁget_trigger_auth__mutmut_4'] = KedaDetector.xǁKedaDetectorǁget_trigger_auth__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_trigger_auth__mutmut['xǁKedaDetectorǁget_trigger_auth__mutmut_5'] = KedaDetector.xǁKedaDetectorǁget_trigger_auth__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_trigger_auth__mutmut['xǁKedaDetectorǁget_trigger_auth__mutmut_6'] = KedaDetector.xǁKedaDetectorǁget_trigger_auth__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_trigger_auth__mutmut['xǁKedaDetectorǁget_trigger_auth__mutmut_7'] = KedaDetector.xǁKedaDetectorǁget_trigger_auth__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_trigger_auth__mutmut['xǁKedaDetectorǁget_trigger_auth__mutmut_8'] = KedaDetector.xǁKedaDetectorǁget_trigger_auth__mutmut_8 # type: ignore # mutmut generated

mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut['_mutmut_orig'] = KedaDetector.xǁKedaDetectorǁlist_scaledjobs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut['xǁKedaDetectorǁlist_scaledjobs__mutmut_1'] = KedaDetector.xǁKedaDetectorǁlist_scaledjobs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut['xǁKedaDetectorǁlist_scaledjobs__mutmut_2'] = KedaDetector.xǁKedaDetectorǁlist_scaledjobs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut['xǁKedaDetectorǁlist_scaledjobs__mutmut_3'] = KedaDetector.xǁKedaDetectorǁlist_scaledjobs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut['xǁKedaDetectorǁlist_scaledjobs__mutmut_4'] = KedaDetector.xǁKedaDetectorǁlist_scaledjobs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut['xǁKedaDetectorǁlist_scaledjobs__mutmut_5'] = KedaDetector.xǁKedaDetectorǁlist_scaledjobs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut['xǁKedaDetectorǁlist_scaledjobs__mutmut_6'] = KedaDetector.xǁKedaDetectorǁlist_scaledjobs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut['xǁKedaDetectorǁlist_scaledjobs__mutmut_7'] = KedaDetector.xǁKedaDetectorǁlist_scaledjobs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁlist_scaledjobs__mutmut['xǁKedaDetectorǁlist_scaledjobs__mutmut_8'] = KedaDetector.xǁKedaDetectorǁlist_scaledjobs__mutmut_8 # type: ignore # mutmut generated

mutants_xǁKedaDetectorǁget_scaledjob__mutmut['_mutmut_orig'] = KedaDetector.xǁKedaDetectorǁget_scaledjob__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledjob__mutmut['xǁKedaDetectorǁget_scaledjob__mutmut_1'] = KedaDetector.xǁKedaDetectorǁget_scaledjob__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledjob__mutmut['xǁKedaDetectorǁget_scaledjob__mutmut_2'] = KedaDetector.xǁKedaDetectorǁget_scaledjob__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledjob__mutmut['xǁKedaDetectorǁget_scaledjob__mutmut_3'] = KedaDetector.xǁKedaDetectorǁget_scaledjob__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledjob__mutmut['xǁKedaDetectorǁget_scaledjob__mutmut_4'] = KedaDetector.xǁKedaDetectorǁget_scaledjob__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledjob__mutmut['xǁKedaDetectorǁget_scaledjob__mutmut_5'] = KedaDetector.xǁKedaDetectorǁget_scaledjob__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledjob__mutmut['xǁKedaDetectorǁget_scaledjob__mutmut_6'] = KedaDetector.xǁKedaDetectorǁget_scaledjob__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledjob__mutmut['xǁKedaDetectorǁget_scaledjob__mutmut_7'] = KedaDetector.xǁKedaDetectorǁget_scaledjob__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKedaDetectorǁget_scaledjob__mutmut['xǁKedaDetectorǁget_scaledjob__mutmut_8'] = KedaDetector.xǁKedaDetectorǁget_scaledjob__mutmut_8 # type: ignore # mutmut generated
