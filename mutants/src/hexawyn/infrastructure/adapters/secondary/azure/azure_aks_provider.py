from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
from hexawyn.infrastructure.adapters.provider_registry import CloudProvider
from hexawyn.infrastructure.adapters.secondary.azure.aks_adapter import AzureAKSAdapter
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAzureAKSProviderǁsupports__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureAKSProviderǁbuild__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureAKSProviderǁprovider_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureAKSProviderǁprovider_badge__mutmut: MutantDict = {}  # type: ignore


class AzureAKSProvider(CloudProvider):
    """CloudProvider plugin for Azure AKS clusters.

    Selected automatically by the adapter factory when the azure dependencies
    are installed and the cluster context looks like AKS.
    """

    @classmethod
    @_mutmut_mutated(mutants_xǁAzureAKSProviderǁsupports__mutmut, is_classmethod = True)
    def supports(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_orig(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_1(cls, context: ClusterContext) -> bool:
        if detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_2(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get(None, False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_3(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", None):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_4(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get(False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_5(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", ):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_6(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("XXazureXX", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_7(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("AZURE", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_8(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", True):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_9(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return True
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_10(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = None
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_11(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").upper()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_12(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get(None, "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_13(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", None).lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_14(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_15(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", ).lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_16(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("XXnameXX", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_17(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("NAME", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_18(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "XXXX").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_19(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = None
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_20(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").upper()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_21(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get(None, "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_22(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", None).lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_23(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_24(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", ).lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_25(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("XXproviderXX", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_26(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("PROVIDER", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_27(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "XXXX").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_28(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name and provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_29(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "XXaksXX" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_30(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "AKS" in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_31(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" not in name or provider == "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_32(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider != "azure"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_33(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "XXazureXX"

    @classmethod
    def xǁAzureAKSProviderǁsupports__mutmut_34(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "AZURE"

    @classmethod
    @_mutmut_mutated(mutants_xǁAzureAKSProviderǁbuild__mutmut, is_classmethod = True)
    def build(cls, context: ClusterContext) -> K8sPort:
        return AzureAKSAdapter(context)

    @classmethod
    def xǁAzureAKSProviderǁbuild__mutmut_orig(cls, context: ClusterContext) -> K8sPort:
        return AzureAKSAdapter(context)

    @classmethod
    def xǁAzureAKSProviderǁbuild__mutmut_1(cls, context: ClusterContext) -> K8sPort:
        return AzureAKSAdapter(None)

    @classmethod
    @_mutmut_mutated(mutants_xǁAzureAKSProviderǁprovider_name__mutmut, is_classmethod = True)
    def provider_name(cls) -> str:
        return "Azure AKS"

    @classmethod
    def xǁAzureAKSProviderǁprovider_name__mutmut_orig(cls) -> str:
        return "Azure AKS"

    @classmethod
    def xǁAzureAKSProviderǁprovider_name__mutmut_1(cls) -> str:
        return "XXAzure AKSXX"

    @classmethod
    def xǁAzureAKSProviderǁprovider_name__mutmut_2(cls) -> str:
        return "azure aks"

    @classmethod
    def xǁAzureAKSProviderǁprovider_name__mutmut_3(cls) -> str:
        return "AZURE AKS"

    @classmethod
    @_mutmut_mutated(mutants_xǁAzureAKSProviderǁprovider_badge__mutmut, is_classmethod = True)
    def provider_badge(cls) -> str:
        return "☁ Azure"

    @classmethod
    def xǁAzureAKSProviderǁprovider_badge__mutmut_orig(cls) -> str:
        return "☁ Azure"

    @classmethod
    def xǁAzureAKSProviderǁprovider_badge__mutmut_1(cls) -> str:
        return "XX☁ AzureXX"

    @classmethod
    def xǁAzureAKSProviderǁprovider_badge__mutmut_2(cls) -> str:
        return "☁ azure"

    @classmethod
    def xǁAzureAKSProviderǁprovider_badge__mutmut_3(cls) -> str:
        return "☁ AZURE"

mutants_xǁAzureAKSProviderǁsupports__mutmut['_mutmut_orig'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_1'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_2'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_3'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_4'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_5'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_6'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_7'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_8'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_9'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_10'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_11'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_12'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_13'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_14'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_15'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_16'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_17'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_18'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_19'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_20'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_21'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_22'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_23'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_24'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_25'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_26'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_27'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_28'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_29'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_30'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_31'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_32'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_33'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁsupports__mutmut['xǁAzureAKSProviderǁsupports__mutmut_34'] = AzureAKSProvider.xǁAzureAKSProviderǁsupports__mutmut_34 # type: ignore # mutmut generated

mutants_xǁAzureAKSProviderǁbuild__mutmut['_mutmut_orig'] = AzureAKSProvider.xǁAzureAKSProviderǁbuild__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁbuild__mutmut['xǁAzureAKSProviderǁbuild__mutmut_1'] = AzureAKSProvider.xǁAzureAKSProviderǁbuild__mutmut_1 # type: ignore # mutmut generated

mutants_xǁAzureAKSProviderǁprovider_name__mutmut['_mutmut_orig'] = AzureAKSProvider.xǁAzureAKSProviderǁprovider_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁprovider_name__mutmut['xǁAzureAKSProviderǁprovider_name__mutmut_1'] = AzureAKSProvider.xǁAzureAKSProviderǁprovider_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁprovider_name__mutmut['xǁAzureAKSProviderǁprovider_name__mutmut_2'] = AzureAKSProvider.xǁAzureAKSProviderǁprovider_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁprovider_name__mutmut['xǁAzureAKSProviderǁprovider_name__mutmut_3'] = AzureAKSProvider.xǁAzureAKSProviderǁprovider_name__mutmut_3 # type: ignore # mutmut generated

mutants_xǁAzureAKSProviderǁprovider_badge__mutmut['_mutmut_orig'] = AzureAKSProvider.xǁAzureAKSProviderǁprovider_badge__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁprovider_badge__mutmut['xǁAzureAKSProviderǁprovider_badge__mutmut_1'] = AzureAKSProvider.xǁAzureAKSProviderǁprovider_badge__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁprovider_badge__mutmut['xǁAzureAKSProviderǁprovider_badge__mutmut_2'] = AzureAKSProvider.xǁAzureAKSProviderǁprovider_badge__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureAKSProviderǁprovider_badge__mutmut['xǁAzureAKSProviderǁprovider_badge__mutmut_3'] = AzureAKSProvider.xǁAzureAKSProviderǁprovider_badge__mutmut_3 # type: ignore # mutmut generated
