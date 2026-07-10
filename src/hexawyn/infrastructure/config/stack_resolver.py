from typing import TypedDict

_AWS_PROVIDER = "aws-eks"
_GCP_PROVIDER = "gcp-gke"
_AZURE_PROVIDER = "azure-aks"
_VANILLA_PROVIDER = "vanilla"
_SOURCE_OVERRIDE = "override"
_SOURCE_AUTO = "auto"


class StackDescription(TypedDict):
    provider: str
    metrics: str
    traces: str
    logs: str
    source: str


def resolve_stack(
    override: str | None,
    aws_supported: bool,
    gcp_supported: bool,
    azure_supported: bool,
) -> StackDescription:
    """Resolve the effective observability stack for a context.

    An explicit override always wins over auto-detection.
    """
    if override == "aws":
        return _aws_stack(_SOURCE_OVERRIDE)
    if override == "gcp":
        return _gcp_stack(_SOURCE_OVERRIDE)
    if override == "azure":
        return _azure_stack(_SOURCE_OVERRIDE)
    if override == "vanilla":
        return _vanilla_stack(_SOURCE_OVERRIDE)
    if azure_supported:
        return _azure_stack(_SOURCE_AUTO)
    if gcp_supported:
        return _gcp_stack(_SOURCE_AUTO)
    if aws_supported:
        return _aws_stack(_SOURCE_AUTO)
    return _vanilla_stack(_SOURCE_AUTO)


def _aws_stack(source: str) -> StackDescription:
    return {
        "provider": _AWS_PROVIDER,
        "metrics": "CloudWatch Container Insights",
        "traces": "AWS X-Ray",
        "logs": "CloudWatch Logs",
        "source": source,
    }


def _gcp_stack(source: str) -> StackDescription:
    return {
        "provider": _GCP_PROVIDER,
        "metrics": "GCP Managed Prometheus",
        "traces": "Google Cloud Trace",
        "logs": "Google Cloud Logging",
        "source": source,
    }


def _azure_stack(source: str) -> StackDescription:
    return {
        "provider": _AZURE_PROVIDER,
        "metrics": "Azure Monitor Prometheus",
        "traces": "Azure Monitor Traces",
        "logs": "Azure Log Analytics",
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
