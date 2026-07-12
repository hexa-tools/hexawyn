from __future__ import annotations

from typing import Protocol, cast

from hexawyn.application.ports.driven.cost_estimation_port import (
    CostEstimationPort,
    CostReportRaw,
    NamespaceCostRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


class CloudBillingClient(Protocol):
    """Minimal contract for the GCP Cloud Billing client used here."""

    def query_billing_data(self, request: dict[str, object]) -> dict[str, object]: ...


class GCPCostAdapter(CostEstimationPort):
    """CostEstimationPort backed by GCP Cloud Billing.

    Queries the Cloud Billing API filtering by the *k8s-namespace* label.
    Read-only — requires ``roles/billing.viewer`` only.
    """

    def __init__(
        self,
        project_id: str,
        billing_client: CloudBillingClient | None = None,
    ) -> None:
        self._project_id = project_id
        self._billing_client = billing_client

    def estimate_cluster_cost(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_billing_data(
                {
                    "project": self._project_id,
                    "filter": f"labels.k8s-cluster={cluster_name}",
                    "group_by": "k8s-namespace",
                }
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

        namespace_costs = _parse_gcp_rows(response)
        namespace_costs_ns: list[NamespaceCostRaw] = [
            cast(NamespaceCostRaw, ns) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def _client_or_create(self) -> CloudBillingClient:  # pragma: no cover — requires GCP SDK
        if self._billing_client is None:
            from google.cloud import billing_v1

            raw_client = billing_v1.CloudBillingClient()
            self._billing_client = _GCPClientWrapper(raw_client)
        return self._billing_client


class _GCPClientWrapper:  # pragma: no cover — requires GCP SDK
    """Wraps the real GCP Billing client to match the CloudBillingClient protocol."""

    def __init__(self, raw_client: object) -> None:
        self._raw = raw_client

    def query_billing_data(self, request: dict[str, object]) -> dict[str, object]:
        raise NotImplementedError("Real GCP billing query not implemented yet — use mock in tests.")


def _parse_gcp_rows(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if not isinstance(rows, list):
        return []
    results: list[dict[str, object]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        labels = row.get("labels")
        ns = ""
        if isinstance(labels, list):
            for label in labels:
                if isinstance(label, dict) and label.get("key") == "k8s-namespace":
                    ns = str(label.get("value", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def _translate_error(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            "GCP credentials not found. Run 'gcloud auth application-default login'.",
            context={"hint": "gcloud auth"},
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")
