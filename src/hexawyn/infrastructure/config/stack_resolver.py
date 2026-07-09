from typing import TypedDict

_AWS_PROVIDER = "aws-eks"
_VANILLA_PROVIDER = "vanilla"
_SOURCE_OVERRIDE = "override"
_SOURCE_AUTO = "auto"


class StackDescription(TypedDict):
    provider: str
    metrics: str
    traces: str
    logs: str
    source: str


def resolve_stack(override: str | None, aws_supported: bool) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    return _aws_stack(_SOURCE_AUTO) if aws_supported else _vanilla_stack(_SOURCE_AUTO)


def _aws_stack(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def _vanilla_stack(source: str) -> StackDescription:
    return {
        "provider": _VANILLA_PROVIDER,
        "metrics": "Prometheus",
        "traces": "OpenTelemetry",
        "logs": "Kubernetes",
        "source": source,
    }
