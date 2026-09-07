from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
from hexawyn.infrastructure.adapters.provider_registry import CloudProvider
from hexawyn.infrastructure.adapters.secondary.openshift.openshift_adapter import OpenShiftAdapter
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOpenShiftProviderǁsupports__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftProviderǁbuild__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftProviderǁprovider_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftProviderǁprovider_badge__mutmut: MutantDict = {}  # type: ignore


class OpenShiftProvider(CloudProvider):
    """CloudProvider plugin for Red Hat OpenShift clusters.

    Selected automatically by the adapter factory when the openshift dependency
    is installed and the cluster context looks like OpenShift (CRC included).
    """

    @classmethod
    @_mutmut_mutated(mutants_xǁOpenShiftProviderǁsupports__mutmut, is_classmethod = True)
    def supports(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_orig(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_1(cls, context: ClusterContext) -> bool:
        if detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_2(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get(None, False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_3(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", None):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_4(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get(False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_5(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", ):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_6(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("XXopenshiftXX", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_7(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("OPENSHIFT", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_8(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", True):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_9(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return True
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_10(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = None
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_11(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").upper()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_12(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get(None, "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_13(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", None).lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_14(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_15(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", ).lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_16(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("XXnameXX", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_17(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("NAME", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_18(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "XXXX").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_19(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = None
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_20(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").upper()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_21(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get(None, "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_22(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", None).lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_23(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_24(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", ).lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_25(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("XXproviderXX", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_26(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("PROVIDER", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_27(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "XXXX").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_28(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name and provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_29(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name and "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_30(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "XXopenshiftXX" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_31(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "OPENSHIFT" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_32(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" not in name or "ocp" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_33(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "XXocpXX" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_34(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "OCP" in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_35(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" not in name or provider == "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_36(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider != "openshift"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_37(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "XXopenshiftXX"

    @classmethod
    def xǁOpenShiftProviderǁsupports__mutmut_38(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "OPENSHIFT"

    @classmethod
    @_mutmut_mutated(mutants_xǁOpenShiftProviderǁbuild__mutmut, is_classmethod = True)
    def build(cls, context: ClusterContext) -> K8sPort:
        return OpenShiftAdapter(context)

    @classmethod
    def xǁOpenShiftProviderǁbuild__mutmut_orig(cls, context: ClusterContext) -> K8sPort:
        return OpenShiftAdapter(context)

    @classmethod
    def xǁOpenShiftProviderǁbuild__mutmut_1(cls, context: ClusterContext) -> K8sPort:
        return OpenShiftAdapter(None)

    @classmethod
    @_mutmut_mutated(mutants_xǁOpenShiftProviderǁprovider_name__mutmut, is_classmethod = True)
    def provider_name(cls) -> str:
        return "OpenShift"

    @classmethod
    def xǁOpenShiftProviderǁprovider_name__mutmut_orig(cls) -> str:
        return "OpenShift"

    @classmethod
    def xǁOpenShiftProviderǁprovider_name__mutmut_1(cls) -> str:
        return "XXOpenShiftXX"

    @classmethod
    def xǁOpenShiftProviderǁprovider_name__mutmut_2(cls) -> str:
        return "openshift"

    @classmethod
    def xǁOpenShiftProviderǁprovider_name__mutmut_3(cls) -> str:
        return "OPENSHIFT"

    @classmethod
    @_mutmut_mutated(mutants_xǁOpenShiftProviderǁprovider_badge__mutmut, is_classmethod = True)
    def provider_badge(cls) -> str:
        return "⛑ OpenShift"

    @classmethod
    def xǁOpenShiftProviderǁprovider_badge__mutmut_orig(cls) -> str:
        return "⛑ OpenShift"

    @classmethod
    def xǁOpenShiftProviderǁprovider_badge__mutmut_1(cls) -> str:
        return "XX⛑ OpenShiftXX"

    @classmethod
    def xǁOpenShiftProviderǁprovider_badge__mutmut_2(cls) -> str:
        return "⛑ openshift"

    @classmethod
    def xǁOpenShiftProviderǁprovider_badge__mutmut_3(cls) -> str:
        return "⛑ OPENSHIFT"

mutants_xǁOpenShiftProviderǁsupports__mutmut['_mutmut_orig'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_1'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_2'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_3'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_4'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_5'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_6'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_7'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_8'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_9'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_10'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_11'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_12'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_13'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_14'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_15'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_16'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_17'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_18'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_19'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_20'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_21'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_22'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_23'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_24'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_25'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_26'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_27'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_28'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_29'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_30'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_31'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_32'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_33'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_34'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_35'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_36'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_37'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁsupports__mutmut['xǁOpenShiftProviderǁsupports__mutmut_38'] = OpenShiftProvider.xǁOpenShiftProviderǁsupports__mutmut_38 # type: ignore # mutmut generated

mutants_xǁOpenShiftProviderǁbuild__mutmut['_mutmut_orig'] = OpenShiftProvider.xǁOpenShiftProviderǁbuild__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁbuild__mutmut['xǁOpenShiftProviderǁbuild__mutmut_1'] = OpenShiftProvider.xǁOpenShiftProviderǁbuild__mutmut_1 # type: ignore # mutmut generated

mutants_xǁOpenShiftProviderǁprovider_name__mutmut['_mutmut_orig'] = OpenShiftProvider.xǁOpenShiftProviderǁprovider_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁprovider_name__mutmut['xǁOpenShiftProviderǁprovider_name__mutmut_1'] = OpenShiftProvider.xǁOpenShiftProviderǁprovider_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁprovider_name__mutmut['xǁOpenShiftProviderǁprovider_name__mutmut_2'] = OpenShiftProvider.xǁOpenShiftProviderǁprovider_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁprovider_name__mutmut['xǁOpenShiftProviderǁprovider_name__mutmut_3'] = OpenShiftProvider.xǁOpenShiftProviderǁprovider_name__mutmut_3 # type: ignore # mutmut generated

mutants_xǁOpenShiftProviderǁprovider_badge__mutmut['_mutmut_orig'] = OpenShiftProvider.xǁOpenShiftProviderǁprovider_badge__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁprovider_badge__mutmut['xǁOpenShiftProviderǁprovider_badge__mutmut_1'] = OpenShiftProvider.xǁOpenShiftProviderǁprovider_badge__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁprovider_badge__mutmut['xǁOpenShiftProviderǁprovider_badge__mutmut_2'] = OpenShiftProvider.xǁOpenShiftProviderǁprovider_badge__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftProviderǁprovider_badge__mutmut['xǁOpenShiftProviderǁprovider_badge__mutmut_3'] = OpenShiftProvider.xǁOpenShiftProviderǁprovider_badge__mutmut_3 # type: ignore # mutmut generated
