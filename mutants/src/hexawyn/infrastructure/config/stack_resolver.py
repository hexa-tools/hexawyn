from typing import TypedDict

_AWS_PROVIDER = "aws-eks"
_GCP_PROVIDER = "gcp-gke"
_AZURE_PROVIDER = "azure-aks"
_DATADOG_PROVIDER = "datadog"
_VANILLA_PROVIDER = "vanilla"
_SOURCE_OVERRIDE = "override"
_SOURCE_AUTO = "auto"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class StackDescription(TypedDict):
    provider: str
    metrics: str
    traces: str
    logs: str
    source: str
mutants_x_resolve_stack__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resolve_stack__mutmut)
def resolve_stack(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_orig(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_1(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override != "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_2(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "XXdatadogXX":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_3(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "DATADOG":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_4(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(None)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_5(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override != "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_6(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "XXawsXX":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_7(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "AWS":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_8(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(None)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_9(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override != "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_10(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "XXgcpXX":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_11(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "GCP":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_12(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(None)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_13(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override != "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_14(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "XXazureXX":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_15(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "AZURE":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_16(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(None)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_17(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override != "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_18(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "XXvanillaXX":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_19(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "VANILLA":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_20(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(None)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_21(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(None)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_22(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(None)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_23(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(None)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_24(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(None)
    return _vanilla_stack(_SOURCE_AUTO)


def x_resolve_stack__mutmut_25(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
    datadog_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "datadog":
        return _datadog_stack(_SOURCE_OVERRIDE)
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if datadog_supported:
        return _datadog_stack(_SOURCE_AUTO)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(None)

mutants_x_resolve_stack__mutmut['_mutmut_orig'] = x_resolve_stack__mutmut_orig # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_1'] = x_resolve_stack__mutmut_1 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_2'] = x_resolve_stack__mutmut_2 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_3'] = x_resolve_stack__mutmut_3 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_4'] = x_resolve_stack__mutmut_4 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_5'] = x_resolve_stack__mutmut_5 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_6'] = x_resolve_stack__mutmut_6 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_7'] = x_resolve_stack__mutmut_7 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_8'] = x_resolve_stack__mutmut_8 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_9'] = x_resolve_stack__mutmut_9 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_10'] = x_resolve_stack__mutmut_10 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_11'] = x_resolve_stack__mutmut_11 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_12'] = x_resolve_stack__mutmut_12 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_13'] = x_resolve_stack__mutmut_13 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_14'] = x_resolve_stack__mutmut_14 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_15'] = x_resolve_stack__mutmut_15 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_16'] = x_resolve_stack__mutmut_16 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_17'] = x_resolve_stack__mutmut_17 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_18'] = x_resolve_stack__mutmut_18 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_19'] = x_resolve_stack__mutmut_19 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_20'] = x_resolve_stack__mutmut_20 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_21'] = x_resolve_stack__mutmut_21 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_22'] = x_resolve_stack__mutmut_22 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_23'] = x_resolve_stack__mutmut_23 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_24'] = x_resolve_stack__mutmut_24 # type: ignore # mutmut generated
mutants_x_resolve_stack__mutmut['x_resolve_stack__mutmut_25'] = x_resolve_stack__mutmut_25 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__aws_stack__mutmut)
def _aws_stack(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_orig(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_1(source: str) -> StackDescription:
    return {
        "XXproviderXX": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_2(source: str) -> StackDescription:
    return {
        "PROVIDER": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_3(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "XXmetricsXX": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_4(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "METRICS": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_5(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "XXCloudWatch Container InsightsXX",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_6(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "cloudwatch container insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_7(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CLOUDWATCH CONTAINER INSIGHTS",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_8(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "XXtracesXX": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_9(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "TRACES": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_10(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "XXAWS X-RayXX",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_11(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "aws x-ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_12(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-RAY",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_13(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "XXlogsXX": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_14(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "LOGS": "CloudWatch Logs",
        "source": source,
    }


def x__aws_stack__mutmut_15(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "XXCloudWatch LogsXX",
        "source": source,
    }


def x__aws_stack__mutmut_16(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "cloudwatch logs",
        "source": source,
    }


def x__aws_stack__mutmut_17(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CLOUDWATCH LOGS",
        "source": source,
    }


def x__aws_stack__mutmut_18(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "XXsourceXX": source,
    }


def x__aws_stack__mutmut_19(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "SOURCE": source,
    }

mutants_x__aws_stack__mutmut['_mutmut_orig'] = x__aws_stack__mutmut_orig # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_1'] = x__aws_stack__mutmut_1 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_2'] = x__aws_stack__mutmut_2 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_3'] = x__aws_stack__mutmut_3 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_4'] = x__aws_stack__mutmut_4 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_5'] = x__aws_stack__mutmut_5 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_6'] = x__aws_stack__mutmut_6 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_7'] = x__aws_stack__mutmut_7 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_8'] = x__aws_stack__mutmut_8 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_9'] = x__aws_stack__mutmut_9 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_10'] = x__aws_stack__mutmut_10 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_11'] = x__aws_stack__mutmut_11 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_12'] = x__aws_stack__mutmut_12 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_13'] = x__aws_stack__mutmut_13 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_14'] = x__aws_stack__mutmut_14 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_15'] = x__aws_stack__mutmut_15 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_16'] = x__aws_stack__mutmut_16 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_17'] = x__aws_stack__mutmut_17 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_18'] = x__aws_stack__mutmut_18 # type: ignore # mutmut generated
mutants_x__aws_stack__mutmut['x__aws_stack__mutmut_19'] = x__aws_stack__mutmut_19 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__gcp_stack__mutmut)
def _gcp_stack(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_orig(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_1(source: str) -> StackDescription:
    return {
        "XXproviderXX": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_2(source: str) -> StackDescription:
    return {
        "PROVIDER": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_3(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "XXmetricsXX": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_4(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "METRICS": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_5(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "XXGCP Managed PrometheusXX",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_6(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "gcp managed prometheus",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_7(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP MANAGED PROMETHEUS",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_8(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "XXtracesXX": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_9(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "TRACES": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_10(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "XXGoogle Cloud TraceXX",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_11(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "google cloud trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_12(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "GOOGLE CLOUD TRACE",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_13(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "XXlogsXX": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_14(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "LOGS": "Google Cloud Logging",
        "source": source,
    }


def x__gcp_stack__mutmut_15(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "XXGoogle Cloud LoggingXX",
        "source": source,
    }


def x__gcp_stack__mutmut_16(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "google cloud logging",
        "source": source,
    }


def x__gcp_stack__mutmut_17(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "GOOGLE CLOUD LOGGING",
        "source": source,
    }


def x__gcp_stack__mutmut_18(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "XXsourceXX": source,
    }


def x__gcp_stack__mutmut_19(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "SOURCE": source,
    }

mutants_x__gcp_stack__mutmut['_mutmut_orig'] = x__gcp_stack__mutmut_orig # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_1'] = x__gcp_stack__mutmut_1 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_2'] = x__gcp_stack__mutmut_2 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_3'] = x__gcp_stack__mutmut_3 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_4'] = x__gcp_stack__mutmut_4 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_5'] = x__gcp_stack__mutmut_5 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_6'] = x__gcp_stack__mutmut_6 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_7'] = x__gcp_stack__mutmut_7 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_8'] = x__gcp_stack__mutmut_8 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_9'] = x__gcp_stack__mutmut_9 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_10'] = x__gcp_stack__mutmut_10 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_11'] = x__gcp_stack__mutmut_11 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_12'] = x__gcp_stack__mutmut_12 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_13'] = x__gcp_stack__mutmut_13 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_14'] = x__gcp_stack__mutmut_14 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_15'] = x__gcp_stack__mutmut_15 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_16'] = x__gcp_stack__mutmut_16 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_17'] = x__gcp_stack__mutmut_17 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_18'] = x__gcp_stack__mutmut_18 # type: ignore # mutmut generated
mutants_x__gcp_stack__mutmut['x__gcp_stack__mutmut_19'] = x__gcp_stack__mutmut_19 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__azure_stack__mutmut)
def _azure_stack(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_orig(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_1(source: str) -> StackDescription:
    return {
        "XXproviderXX": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_2(source: str) -> StackDescription:
    return {
        "PROVIDER": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_3(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "XXmetricsXX": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_4(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "METRICS": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_5(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "XXAzure Monitor PrometheusXX",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_6(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "azure monitor prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_7(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "AZURE MONITOR PROMETHEUS",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_8(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "XXtracesXX": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_9(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "TRACES": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_10(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "XXAzure Monitor TracesXX",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_11(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "azure monitor traces",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_12(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "AZURE MONITOR TRACES",
        "logs": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_13(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "XXlogsXX": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_14(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "LOGS": "Azure Log Analytics",
        "source": source,
    }


def x__azure_stack__mutmut_15(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "XXAzure Log AnalyticsXX",
        "source": source,
    }


def x__azure_stack__mutmut_16(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "azure log analytics",
        "source": source,
    }


def x__azure_stack__mutmut_17(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "AZURE LOG ANALYTICS",
        "source": source,
    }


def x__azure_stack__mutmut_18(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "XXsourceXX": source,
    }


def x__azure_stack__mutmut_19(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
        "SOURCE": source,
    }

mutants_x__azure_stack__mutmut['_mutmut_orig'] = x__azure_stack__mutmut_orig # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_1'] = x__azure_stack__mutmut_1 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_2'] = x__azure_stack__mutmut_2 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_3'] = x__azure_stack__mutmut_3 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_4'] = x__azure_stack__mutmut_4 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_5'] = x__azure_stack__mutmut_5 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_6'] = x__azure_stack__mutmut_6 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_7'] = x__azure_stack__mutmut_7 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_8'] = x__azure_stack__mutmut_8 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_9'] = x__azure_stack__mutmut_9 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_10'] = x__azure_stack__mutmut_10 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_11'] = x__azure_stack__mutmut_11 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_12'] = x__azure_stack__mutmut_12 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_13'] = x__azure_stack__mutmut_13 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_14'] = x__azure_stack__mutmut_14 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_15'] = x__azure_stack__mutmut_15 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_16'] = x__azure_stack__mutmut_16 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_17'] = x__azure_stack__mutmut_17 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_18'] = x__azure_stack__mutmut_18 # type: ignore # mutmut generated
mutants_x__azure_stack__mutmut['x__azure_stack__mutmut_19'] = x__azure_stack__mutmut_19 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__datadog_stack__mutmut)
def _datadog_stack(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_orig(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_1(source: str) -> StackDescription:
    return {
        "XXproviderXX": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_2(source: str) -> StackDescription:
    return {
        "PROVIDER": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_3(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "XXmetricsXX": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_4(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "METRICS": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_5(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "XXDatadog MetricsXX",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_6(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "datadog metrics",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_7(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "DATADOG METRICS",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_8(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "XXtracesXX": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_9(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "TRACES": "Datadog APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_10(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "XXDatadog APMXX",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_11(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "datadog apm",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_12(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "DATADOG APM",
        "logs": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_13(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "XXlogsXX": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_14(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "LOGS": "Datadog Logs",
        "source": source,
    }


def x__datadog_stack__mutmut_15(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "XXDatadog LogsXX",
        "source": source,
    }


def x__datadog_stack__mutmut_16(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "datadog logs",
        "source": source,
    }


def x__datadog_stack__mutmut_17(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "DATADOG LOGS",
        "source": source,
    }


def x__datadog_stack__mutmut_18(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "XXsourceXX": source,
    }


def x__datadog_stack__mutmut_19(source: str) -> StackDescription:
    return {
        "provider": _DATADOG_PROVIDER,
        "metrics": "Datadog Metrics",
        "traces": "Datadog APM",
        "logs": "Datadog Logs",
        "SOURCE": source,
    }

mutants_x__datadog_stack__mutmut['_mutmut_orig'] = x__datadog_stack__mutmut_orig # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_1'] = x__datadog_stack__mutmut_1 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_2'] = x__datadog_stack__mutmut_2 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_3'] = x__datadog_stack__mutmut_3 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_4'] = x__datadog_stack__mutmut_4 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_5'] = x__datadog_stack__mutmut_5 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_6'] = x__datadog_stack__mutmut_6 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_7'] = x__datadog_stack__mutmut_7 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_8'] = x__datadog_stack__mutmut_8 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_9'] = x__datadog_stack__mutmut_9 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_10'] = x__datadog_stack__mutmut_10 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_11'] = x__datadog_stack__mutmut_11 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_12'] = x__datadog_stack__mutmut_12 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_13'] = x__datadog_stack__mutmut_13 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_14'] = x__datadog_stack__mutmut_14 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_15'] = x__datadog_stack__mutmut_15 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_16'] = x__datadog_stack__mutmut_16 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_17'] = x__datadog_stack__mutmut_17 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_18'] = x__datadog_stack__mutmut_18 # type: ignore # mutmut generated
mutants_x__datadog_stack__mutmut['x__datadog_stack__mutmut_19'] = x__datadog_stack__mutmut_19 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__vanilla_stack__mutmut)
def _vanilla_stack(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_orig(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_1(source: str) -> StackDescription:
    return {
        "XXproviderXX": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_2(source: str) -> StackDescription:
    return {
        "PROVIDER": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_3(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "XXmetricsXX": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_4(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "METRICS": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_5(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "XXPrometheusXX",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_6(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "prometheus",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_7(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "PROMETHEUS",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_8(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "XXtracesXX": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_9(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "TRACES": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_10(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "XXOpenTelemetryXX",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_11(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "opentelemetry",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_12(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OPENTELEMETRY",
        "logs": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_13(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "XXlogsXX": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_14(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "LOGS": "Kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_15(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "XXKubernetesXX",
        "source": source,
    }


def x__vanilla_stack__mutmut_16(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "kubernetes",
        "source": source,
    }


def x__vanilla_stack__mutmut_17(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "KUBERNETES",
        "source": source,
    }


def x__vanilla_stack__mutmut_18(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "XXsourceXX": source,
    }


def x__vanilla_stack__mutmut_19(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "SOURCE": source,
    }

mutants_x__vanilla_stack__mutmut['_mutmut_orig'] = x__vanilla_stack__mutmut_orig # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_1'] = x__vanilla_stack__mutmut_1 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_2'] = x__vanilla_stack__mutmut_2 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_3'] = x__vanilla_stack__mutmut_3 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_4'] = x__vanilla_stack__mutmut_4 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_5'] = x__vanilla_stack__mutmut_5 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_6'] = x__vanilla_stack__mutmut_6 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_7'] = x__vanilla_stack__mutmut_7 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_8'] = x__vanilla_stack__mutmut_8 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_9'] = x__vanilla_stack__mutmut_9 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_10'] = x__vanilla_stack__mutmut_10 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_11'] = x__vanilla_stack__mutmut_11 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_12'] = x__vanilla_stack__mutmut_12 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_13'] = x__vanilla_stack__mutmut_13 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_14'] = x__vanilla_stack__mutmut_14 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_15'] = x__vanilla_stack__mutmut_15 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_16'] = x__vanilla_stack__mutmut_16 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_17'] = x__vanilla_stack__mutmut_17 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_18'] = x__vanilla_stack__mutmut_18 # type: ignore # mutmut generated
mutants_x__vanilla_stack__mutmut['x__vanilla_stack__mutmut_19'] = x__vanilla_stack__mutmut_19 # type: ignore # mutmut generated
