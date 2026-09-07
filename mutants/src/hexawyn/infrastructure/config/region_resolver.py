import re
from collections.abc import Mapping

_ARN_REGION_PATTERN = re.compile(r"arn:aws:eks:([a-z0-9-]+):")
_REGION_IN_NAME_PATTERN = re.compile(r"\b([a-z]{2}-[a-z]+-\d)\b")
_ENV_KEYS = ("AWS_REGION", "AWS_DEFAULT_REGION")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_resolve_region__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resolve_region__mutmut)
def resolve_region(context_name: str, env: Mapping[str, str]) -> str | None:
    """Resolve the AWS region with standard precedence.

    1. AWS_REGION / AWS_DEFAULT_REGION environment variables
    2. Region embedded in the kubeconfig context (ARN or name pattern)
    3. None — let boto3 resolve from the active profile (~/.aws/config)

    No hardcoded default: returning None lets boto3 use the caller's profile
    instead of silently querying the wrong region.
    """
    for key in _ENV_KEYS:
        value = env.get(key)
        if value:
            return value
    return _region_from_context(context_name)


def x_resolve_region__mutmut_orig(context_name: str, env: Mapping[str, str]) -> str | None:
    """Resolve the AWS region with standard precedence.

    1. AWS_REGION / AWS_DEFAULT_REGION environment variables
    2. Region embedded in the kubeconfig context (ARN or name pattern)
    3. None — let boto3 resolve from the active profile (~/.aws/config)

    No hardcoded default: returning None lets boto3 use the caller's profile
    instead of silently querying the wrong region.
    """
    for key in _ENV_KEYS:
        value = env.get(key)
        if value:
            return value
    return _region_from_context(context_name)


def x_resolve_region__mutmut_1(context_name: str, env: Mapping[str, str]) -> str | None:
    """Resolve the AWS region with standard precedence.

    1. AWS_REGION / AWS_DEFAULT_REGION environment variables
    2. Region embedded in the kubeconfig context (ARN or name pattern)
    3. None — let boto3 resolve from the active profile (~/.aws/config)

    No hardcoded default: returning None lets boto3 use the caller's profile
    instead of silently querying the wrong region.
    """
    for key in _ENV_KEYS:
        value = None
        if value:
            return value
    return _region_from_context(context_name)


def x_resolve_region__mutmut_2(context_name: str, env: Mapping[str, str]) -> str | None:
    """Resolve the AWS region with standard precedence.

    1. AWS_REGION / AWS_DEFAULT_REGION environment variables
    2. Region embedded in the kubeconfig context (ARN or name pattern)
    3. None — let boto3 resolve from the active profile (~/.aws/config)

    No hardcoded default: returning None lets boto3 use the caller's profile
    instead of silently querying the wrong region.
    """
    for key in _ENV_KEYS:
        value = env.get(None)
        if value:
            return value
    return _region_from_context(context_name)


def x_resolve_region__mutmut_3(context_name: str, env: Mapping[str, str]) -> str | None:
    """Resolve the AWS region with standard precedence.

    1. AWS_REGION / AWS_DEFAULT_REGION environment variables
    2. Region embedded in the kubeconfig context (ARN or name pattern)
    3. None — let boto3 resolve from the active profile (~/.aws/config)

    No hardcoded default: returning None lets boto3 use the caller's profile
    instead of silently querying the wrong region.
    """
    for key in _ENV_KEYS:
        value = env.get(key)
        if value:
            return value
    return _region_from_context(None)

mutants_x_resolve_region__mutmut['_mutmut_orig'] = x_resolve_region__mutmut_orig # type: ignore # mutmut generated
mutants_x_resolve_region__mutmut['x_resolve_region__mutmut_1'] = x_resolve_region__mutmut_1 # type: ignore # mutmut generated
mutants_x_resolve_region__mutmut['x_resolve_region__mutmut_2'] = x_resolve_region__mutmut_2 # type: ignore # mutmut generated
mutants_x_resolve_region__mutmut['x_resolve_region__mutmut_3'] = x_resolve_region__mutmut_3 # type: ignore # mutmut generated
mutants_x__region_from_context__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__region_from_context__mutmut)
def _region_from_context(context_name: str) -> str | None:
    arn_match = _ARN_REGION_PATTERN.search(context_name)
    if arn_match:
        return arn_match.group(1)
    name_match = _REGION_IN_NAME_PATTERN.search(context_name)
    if name_match:
        return name_match.group(1)
    return None


def x__region_from_context__mutmut_orig(context_name: str) -> str | None:
    arn_match = _ARN_REGION_PATTERN.search(context_name)
    if arn_match:
        return arn_match.group(1)
    name_match = _REGION_IN_NAME_PATTERN.search(context_name)
    if name_match:
        return name_match.group(1)
    return None


def x__region_from_context__mutmut_1(context_name: str) -> str | None:
    arn_match = None
    if arn_match:
        return arn_match.group(1)
    name_match = _REGION_IN_NAME_PATTERN.search(context_name)
    if name_match:
        return name_match.group(1)
    return None


def x__region_from_context__mutmut_2(context_name: str) -> str | None:
    arn_match = _ARN_REGION_PATTERN.search(None)
    if arn_match:
        return arn_match.group(1)
    name_match = _REGION_IN_NAME_PATTERN.search(context_name)
    if name_match:
        return name_match.group(1)
    return None


def x__region_from_context__mutmut_3(context_name: str) -> str | None:
    arn_match = _ARN_REGION_PATTERN.search(context_name)
    if arn_match:
        return arn_match.group(None)
    name_match = _REGION_IN_NAME_PATTERN.search(context_name)
    if name_match:
        return name_match.group(1)
    return None


def x__region_from_context__mutmut_4(context_name: str) -> str | None:
    arn_match = _ARN_REGION_PATTERN.search(context_name)
    if arn_match:
        return arn_match.group(2)
    name_match = _REGION_IN_NAME_PATTERN.search(context_name)
    if name_match:
        return name_match.group(1)
    return None


def x__region_from_context__mutmut_5(context_name: str) -> str | None:
    arn_match = _ARN_REGION_PATTERN.search(context_name)
    if arn_match:
        return arn_match.group(1)
    name_match = None
    if name_match:
        return name_match.group(1)
    return None


def x__region_from_context__mutmut_6(context_name: str) -> str | None:
    arn_match = _ARN_REGION_PATTERN.search(context_name)
    if arn_match:
        return arn_match.group(1)
    name_match = _REGION_IN_NAME_PATTERN.search(None)
    if name_match:
        return name_match.group(1)
    return None


def x__region_from_context__mutmut_7(context_name: str) -> str | None:
    arn_match = _ARN_REGION_PATTERN.search(context_name)
    if arn_match:
        return arn_match.group(1)
    name_match = _REGION_IN_NAME_PATTERN.search(context_name)
    if name_match:
        return name_match.group(None)
    return None


def x__region_from_context__mutmut_8(context_name: str) -> str | None:
    arn_match = _ARN_REGION_PATTERN.search(context_name)
    if arn_match:
        return arn_match.group(1)
    name_match = _REGION_IN_NAME_PATTERN.search(context_name)
    if name_match:
        return name_match.group(2)
    return None

mutants_x__region_from_context__mutmut['_mutmut_orig'] = x__region_from_context__mutmut_orig # type: ignore # mutmut generated
mutants_x__region_from_context__mutmut['x__region_from_context__mutmut_1'] = x__region_from_context__mutmut_1 # type: ignore # mutmut generated
mutants_x__region_from_context__mutmut['x__region_from_context__mutmut_2'] = x__region_from_context__mutmut_2 # type: ignore # mutmut generated
mutants_x__region_from_context__mutmut['x__region_from_context__mutmut_3'] = x__region_from_context__mutmut_3 # type: ignore # mutmut generated
mutants_x__region_from_context__mutmut['x__region_from_context__mutmut_4'] = x__region_from_context__mutmut_4 # type: ignore # mutmut generated
mutants_x__region_from_context__mutmut['x__region_from_context__mutmut_5'] = x__region_from_context__mutmut_5 # type: ignore # mutmut generated
mutants_x__region_from_context__mutmut['x__region_from_context__mutmut_6'] = x__region_from_context__mutmut_6 # type: ignore # mutmut generated
mutants_x__region_from_context__mutmut['x__region_from_context__mutmut_7'] = x__region_from_context__mutmut_7 # type: ignore # mutmut generated
mutants_x__region_from_context__mutmut['x__region_from_context__mutmut_8'] = x__region_from_context__mutmut_8 # type: ignore # mutmut generated
