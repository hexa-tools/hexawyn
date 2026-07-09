import re
from collections.abc import Mapping

_ARN_REGION_PATTERN = re.compile(r"arn:aws:eks:([a-z0-9-]+):")
_REGION_IN_NAME_PATTERN = re.compile(r"\b([a-z]{2}-[a-z]+-\d)\b")
_ENV_KEYS = ("AWS_REGION", "AWS_DEFAULT_REGION")


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


def _region_from_context(context_name: str) -> str | None:
    arn_match = _ARN_REGION_PATTERN.search(context_name)
    if arn_match:
        return arn_match.group(1)
    name_match = _REGION_IN_NAME_PATTERN.search(context_name)
    if name_match:
        return name_match.group(1)
    return None
