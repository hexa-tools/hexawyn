from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
from hexawyn.infrastructure.adapters.provider_registry import CloudProvider
from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGCPGKEProviderǁsupports__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPGKEProviderǁbuild__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPGKEProviderǁprovider_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPGKEProviderǁprovider_badge__mutmut: MutantDict = {}  # type: ignore


class GCPGKEProvider(CloudProvider):
    """CloudProvider plugin for GCP GKE clusters.

    Selected automatically by the adapter factory when the google-cloud
    dependencies are installed and the cluster context looks like GKE.
    """

    @classmethod
    @_mutmut_mutated(mutants_xǁGCPGKEProviderǁsupports__mutmut, is_classmethod = True)
    def supports(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_orig(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_1(cls, context: ClusterContext) -> bool:
        if detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_2(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get(None, False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_3(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", None):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_4(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get(False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_5(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", ):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_6(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("XXgcpXX", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_7(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("GCP", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_8(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", True):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_9(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return True
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_10(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = None
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_11(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").upper()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_12(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get(None, "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_13(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", None).lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_14(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_15(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", ).lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_16(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("XXnameXX", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_17(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("NAME", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_18(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "XXXX").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_19(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = None
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_20(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").upper()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_21(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get(None, "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_22(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", None).lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_23(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_24(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", ).lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_25(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("XXproviderXX", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_26(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("PROVIDER", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_27(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "XXXX").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_28(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name and provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_29(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "XXgkeXX" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_30(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "GKE" in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_31(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" not in name or provider == "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_32(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider != "gcp"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_33(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "XXgcpXX"

    @classmethod
    def xǁGCPGKEProviderǁsupports__mutmut_34(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "GCP"

    @classmethod
    @_mutmut_mutated(mutants_xǁGCPGKEProviderǁbuild__mutmut, is_classmethod = True)
    def build(cls, context: ClusterContext) -> K8sPort:
        return GCPGKEAdapter(context)

    @classmethod
    def xǁGCPGKEProviderǁbuild__mutmut_orig(cls, context: ClusterContext) -> K8sPort:
        return GCPGKEAdapter(context)

    @classmethod
    def xǁGCPGKEProviderǁbuild__mutmut_1(cls, context: ClusterContext) -> K8sPort:
        return GCPGKEAdapter(None)

    @classmethod
    @_mutmut_mutated(mutants_xǁGCPGKEProviderǁprovider_name__mutmut, is_classmethod = True)
    def provider_name(cls) -> str:
        return "GCP GKE"

    @classmethod
    def xǁGCPGKEProviderǁprovider_name__mutmut_orig(cls) -> str:
        return "GCP GKE"

    @classmethod
    def xǁGCPGKEProviderǁprovider_name__mutmut_1(cls) -> str:
        return "XXGCP GKEXX"

    @classmethod
    def xǁGCPGKEProviderǁprovider_name__mutmut_2(cls) -> str:
        return "gcp gke"

    @classmethod
    @_mutmut_mutated(mutants_xǁGCPGKEProviderǁprovider_badge__mutmut, is_classmethod = True)
    def provider_badge(cls) -> str:
        return "☁ GCP"

    @classmethod
    def xǁGCPGKEProviderǁprovider_badge__mutmut_orig(cls) -> str:
        return "☁ GCP"

    @classmethod
    def xǁGCPGKEProviderǁprovider_badge__mutmut_1(cls) -> str:
        return "XX☁ GCPXX"

    @classmethod
    def xǁGCPGKEProviderǁprovider_badge__mutmut_2(cls) -> str:
        return "☁ gcp"

mutants_xǁGCPGKEProviderǁsupports__mutmut['_mutmut_orig'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_1'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_2'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_3'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_4'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_5'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_6'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_7'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_8'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_9'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_10'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_11'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_12'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_13'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_14'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_15'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_16'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_17'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_18'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_19'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_20'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_21'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_22'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_23'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_24'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_25'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_26'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_27'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_28'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_29'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_30'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_31'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_32'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_33'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁsupports__mutmut['xǁGCPGKEProviderǁsupports__mutmut_34'] = GCPGKEProvider.xǁGCPGKEProviderǁsupports__mutmut_34 # type: ignore # mutmut generated

mutants_xǁGCPGKEProviderǁbuild__mutmut['_mutmut_orig'] = GCPGKEProvider.xǁGCPGKEProviderǁbuild__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁbuild__mutmut['xǁGCPGKEProviderǁbuild__mutmut_1'] = GCPGKEProvider.xǁGCPGKEProviderǁbuild__mutmut_1 # type: ignore # mutmut generated

mutants_xǁGCPGKEProviderǁprovider_name__mutmut['_mutmut_orig'] = GCPGKEProvider.xǁGCPGKEProviderǁprovider_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁprovider_name__mutmut['xǁGCPGKEProviderǁprovider_name__mutmut_1'] = GCPGKEProvider.xǁGCPGKEProviderǁprovider_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁprovider_name__mutmut['xǁGCPGKEProviderǁprovider_name__mutmut_2'] = GCPGKEProvider.xǁGCPGKEProviderǁprovider_name__mutmut_2 # type: ignore # mutmut generated

mutants_xǁGCPGKEProviderǁprovider_badge__mutmut['_mutmut_orig'] = GCPGKEProvider.xǁGCPGKEProviderǁprovider_badge__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁprovider_badge__mutmut['xǁGCPGKEProviderǁprovider_badge__mutmut_1'] = GCPGKEProvider.xǁGCPGKEProviderǁprovider_badge__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPGKEProviderǁprovider_badge__mutmut['xǁGCPGKEProviderǁprovider_badge__mutmut_2'] = GCPGKEProvider.xǁGCPGKEProviderǁprovider_badge__mutmut_2 # type: ignore # mutmut generated
