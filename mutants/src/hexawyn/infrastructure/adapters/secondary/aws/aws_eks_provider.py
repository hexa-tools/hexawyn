from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
from hexawyn.infrastructure.adapters.provider_registry import CloudProvider
from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers

_EKS_ARN_PREFIX = "arn:aws:eks:"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAWSEKSProviderǁsupports__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSEKSProviderǁbuild__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSEKSProviderǁprovider_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSEKSProviderǁprovider_badge__mutmut: MutantDict = {}  # type: ignore


class AWSEKSProvider(CloudProvider):
    """CloudProvider plugin for AWS EKS clusters.

    Selected automatically by the adapter factory when the boto3 dependency is
    installed and the cluster context looks like an EKS cluster.
    """

    @classmethod
    @_mutmut_mutated(mutants_xǁAWSEKSProviderǁsupports__mutmut, is_classmethod = True)
    def supports(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_orig(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_1(cls, context: ClusterContext) -> bool:
        if detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_2(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get(None, False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_3(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", None):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_4(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get(False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_5(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", ):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_6(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("XXawsXX", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_7(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("AWS", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_8(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", True):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_9(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return True
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_10(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = None
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_11(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").upper()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_12(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get(None, "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_13(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", None).lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_14(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_15(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", ).lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_16(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("XXnameXX", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_17(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("NAME", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_18(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "XXXX").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_19(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = None
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_20(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").upper()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_21(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get(None, "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_22(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", None).lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_23(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_24(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", ).lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_25(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("XXproviderXX", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_26(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("PROVIDER", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_27(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "XXXX").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_28(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" and name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_29(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name and provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_30(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "XXeksXX" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_31(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "EKS" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_32(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" not in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_33(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider != "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_34(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "XXawsXX" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_35(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "AWS" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def xǁAWSEKSProviderǁsupports__mutmut_36(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(None)

    @classmethod
    @_mutmut_mutated(mutants_xǁAWSEKSProviderǁbuild__mutmut, is_classmethod = True)
    def build(cls, context: ClusterContext) -> K8sPort:
        return AWSEKSAdapter(context)

    @classmethod
    def xǁAWSEKSProviderǁbuild__mutmut_orig(cls, context: ClusterContext) -> K8sPort:
        return AWSEKSAdapter(context)

    @classmethod
    def xǁAWSEKSProviderǁbuild__mutmut_1(cls, context: ClusterContext) -> K8sPort:
        return AWSEKSAdapter(None)

    @classmethod
    @_mutmut_mutated(mutants_xǁAWSEKSProviderǁprovider_name__mutmut, is_classmethod = True)
    def provider_name(cls) -> str:
        return "AWS EKS"

    @classmethod
    def xǁAWSEKSProviderǁprovider_name__mutmut_orig(cls) -> str:
        return "AWS EKS"

    @classmethod
    def xǁAWSEKSProviderǁprovider_name__mutmut_1(cls) -> str:
        return "XXAWS EKSXX"

    @classmethod
    def xǁAWSEKSProviderǁprovider_name__mutmut_2(cls) -> str:
        return "aws eks"

    @classmethod
    @_mutmut_mutated(mutants_xǁAWSEKSProviderǁprovider_badge__mutmut, is_classmethod = True)
    def provider_badge(cls) -> str:
        return "☁ AWS"

    @classmethod
    def xǁAWSEKSProviderǁprovider_badge__mutmut_orig(cls) -> str:
        return "☁ AWS"

    @classmethod
    def xǁAWSEKSProviderǁprovider_badge__mutmut_1(cls) -> str:
        return "XX☁ AWSXX"

    @classmethod
    def xǁAWSEKSProviderǁprovider_badge__mutmut_2(cls) -> str:
        return "☁ aws"

mutants_xǁAWSEKSProviderǁsupports__mutmut['_mutmut_orig'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_1'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_2'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_3'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_4'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_5'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_6'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_7'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_8'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_9'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_10'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_11'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_12'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_13'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_14'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_15'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_16'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_17'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_18'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_19'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_20'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_21'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_22'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_23'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_24'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_25'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_26'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_27'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_28'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_29'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_30'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_31'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_32'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_33'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_34'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_35'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁsupports__mutmut['xǁAWSEKSProviderǁsupports__mutmut_36'] = AWSEKSProvider.xǁAWSEKSProviderǁsupports__mutmut_36 # type: ignore # mutmut generated

mutants_xǁAWSEKSProviderǁbuild__mutmut['_mutmut_orig'] = AWSEKSProvider.xǁAWSEKSProviderǁbuild__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁbuild__mutmut['xǁAWSEKSProviderǁbuild__mutmut_1'] = AWSEKSProvider.xǁAWSEKSProviderǁbuild__mutmut_1 # type: ignore # mutmut generated

mutants_xǁAWSEKSProviderǁprovider_name__mutmut['_mutmut_orig'] = AWSEKSProvider.xǁAWSEKSProviderǁprovider_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁprovider_name__mutmut['xǁAWSEKSProviderǁprovider_name__mutmut_1'] = AWSEKSProvider.xǁAWSEKSProviderǁprovider_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁprovider_name__mutmut['xǁAWSEKSProviderǁprovider_name__mutmut_2'] = AWSEKSProvider.xǁAWSEKSProviderǁprovider_name__mutmut_2 # type: ignore # mutmut generated

mutants_xǁAWSEKSProviderǁprovider_badge__mutmut['_mutmut_orig'] = AWSEKSProvider.xǁAWSEKSProviderǁprovider_badge__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁprovider_badge__mutmut['xǁAWSEKSProviderǁprovider_badge__mutmut_1'] = AWSEKSProvider.xǁAWSEKSProviderǁprovider_badge__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSEKSProviderǁprovider_badge__mutmut['xǁAWSEKSProviderǁprovider_badge__mutmut_2'] = AWSEKSProvider.xǁAWSEKSProviderǁprovider_badge__mutmut_2 # type: ignore # mutmut generated
