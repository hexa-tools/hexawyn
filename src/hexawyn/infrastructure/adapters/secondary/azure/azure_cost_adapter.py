from __future__ import annotations

from typing import Protocol, cast

from hexawyn.application.ports.driven.cost_estimation_port import (
    CostEstimationPort,
    CostReportRaw,
    NamespaceCostRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


class CostManagementClient(Protocol):
    """Minimal contract for the azure cost-management client used here."""

    def query_usage(self, scope: str, parameters: dict[str, object]) -> dict[str, object]: ...


class AzureCostAdapter(CostEstimationPort):
    """CostEstimationPort backed by Azure Cost Management.

    Queries the Cost Management API filtering by the *kubernetes-namespace* tag.
    Read-only — requires Cost Management Reader role only.
    """

    def __init__(
        self,
        subscription_id: str,
        cm_client: CostManagementClient | None = None,
    ) -> None:
        self._subscription_id = subscription_id
        self._cm_client = cm_client

    def estimate_cluster_cost(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "grouping": [{"type": "TagKey", "name": "kubernetes-namespace"}],
                    },
                },
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        namespace_costs = _parse_azure_rows(response)
        namespace_costs_ns: list[NamespaceCostRaw] = [
            cast(NamespaceCostRaw, ns) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def _client_or_create(self) -> CostManagementClient:  # pragma: no cover — requires Azure SDK
        if self._cm_client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.costmanagement import (
                CostManagementClient as AzureCostManagementClient,
            )

            self._cm_client = AzureCostManagementClient(DefaultAzureCredential())
        return self._cm_client


def _parse_azure_rows(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def _translate_error(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            "Azure credentials not found. Run 'az login' or attach a managed identity.",
            context={"hint": "az login"},
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")
