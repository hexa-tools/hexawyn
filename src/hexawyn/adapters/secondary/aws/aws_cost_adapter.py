from __future__ import annotations

from typing import Protocol, cast

from hexawyn.application.ports.driven.cost_estimation_port import (
    CostEstimationPort,
    CostReportRaw,
    NamespaceCostRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_COST_EXPLORER_GRANULARITY = "MONTHLY"
_COST_EXPLORER_METRICS = ["UnblendedCost"]


class CostExplorerClient(Protocol):
    """Minimal contract for the boto3 Cost Explorer client used here."""

    def get_cost_and_usage(
        self,
        time_period: dict[str, str],
        granularity: str,
        filter_obj: dict[str, object],
        group_by: list[dict[str, str]],
        metrics: list[str],
    ) -> dict[str, object]: ...


class AWSCostAdapter(CostEstimationPort):
    """CostEstimationPort backed by AWS Cost Explorer.

    Queries the Cost Explorer API for the *kubernetes.io/cluster* tag,
    grouping results by *kubernetes.io/namespace*.
    Read-only — requires ``ce:GetCostAndUsage`` only.
    """

    def __init__(self, region: str, ce_client: CostExplorerClient | None = None) -> None:
        self._region = region
        self._ce_client = ce_client

    def estimate_cluster_cost(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "Tags": {
                        "Key": f"kubernetes.io/cluster/{cluster_name}",
                        "Values": ["owned"],
                    }
                },
                group_by=[{"Type": "TAG", "Key": "kubernetes.io/namespace"}],
                metrics=list(_COST_EXPLORER_METRICS),
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        namespace_costs = _parse_namespace_costs(response)
        namespace_costs_ns: list[NamespaceCostRaw] = [
            cast(NamespaceCostRaw, ns) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def _client_or_create(self) -> CostExplorerClient:
        if self._ce_client is None:
            import boto3

            self._ce_client = boto3.client("ce", region_name=self._region)
        return self._ce_client


def _parse_namespace_costs(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if not isinstance(results_by_time, list):
        return results
    for time_block in results_by_time:
        if not isinstance(time_block, dict):
            continue
        groups = time_block.get("Groups")
        if not isinstance(groups, list):
            continue
        for group in groups:
            if not isinstance(group, dict):
                continue
            keys = group.get("Keys")
            if not isinstance(keys, list) or not keys:
                continue
            metrics = group.get("Metrics")
            if not isinstance(metrics, dict):
                continue
            cost = metrics.get("UnblendedCost")
            if not isinstance(cost, dict):
                continue
            amount = cost.get("Amount")
            results.append(
                {
                    "namespace": str(keys[0]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def _translate_error(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
            context={"hint": "aws configure"},
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")
