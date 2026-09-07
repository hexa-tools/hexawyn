from __future__ import annotations

from typing import Protocol, cast

from hexawyn.application.ports.driven.cost_estimation_port import (
    CostEstimationPort,
    CostReportRaw,
    NamespaceCostRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CloudBillingClient(Protocol):
    """Minimal contract for the GCP Cloud Billing client used here."""

    def query_billing_data(self, request: dict[str, object]) -> dict[str, object]: ...
mutants_xǁGCPCostAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCostAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class GCPCostAdapter(CostEstimationPort):
    """CostEstimationPort backed by GCP Cloud Billing.

    Queries the Cloud Billing API filtering by the *k8s-namespace* label.
    Read-only — requires ``roles/billing.viewer`` only.
    """

    @_mutmut_mutated(mutants_xǁGCPCostAdapterǁ__init____mutmut)
    def __init__(
        self,
        project_id: str,
        billing_client: CloudBillingClient | None = None,
    ) -> None:
        self._project_id = project_id
        self._billing_client = billing_client

    def xǁGCPCostAdapterǁ__init____mutmut_orig(
        self,
        project_id: str,
        billing_client: CloudBillingClient | None = None,
    ) -> None:
        self._project_id = project_id
        self._billing_client = billing_client

    def xǁGCPCostAdapterǁ__init____mutmut_1(
        self,
        project_id: str,
        billing_client: CloudBillingClient | None = None,
    ) -> None:
        self._project_id = None
        self._billing_client = billing_client

    def xǁGCPCostAdapterǁ__init____mutmut_2(
        self,
        project_id: str,
        billing_client: CloudBillingClient | None = None,
    ) -> None:
        self._project_id = project_id
        self._billing_client = None

    @_mutmut_mutated(mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut)
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_orig(self, cluster_name: str) -> CostReportRaw:
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_1(self, cluster_name: str) -> CostReportRaw:
        client = None
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_2(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = None
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_3(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_billing_data(
                None
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_4(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_billing_data(
                {
                    "XXprojectXX": self._project_id,
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_5(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_billing_data(
                {
                    "PROJECT": self._project_id,
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_6(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_billing_data(
                {
                    "project": self._project_id,
                    "XXfilterXX": f"labels.k8s-cluster={cluster_name}",
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_7(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_billing_data(
                {
                    "project": self._project_id,
                    "FILTER": f"labels.k8s-cluster={cluster_name}",
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_8(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_billing_data(
                {
                    "project": self._project_id,
                    "filter": f"labels.k8s-cluster={cluster_name}",
                    "XXgroup_byXX": "k8s-namespace",
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_9(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_billing_data(
                {
                    "project": self._project_id,
                    "filter": f"labels.k8s-cluster={cluster_name}",
                    "GROUP_BY": "k8s-namespace",
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_10(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_billing_data(
                {
                    "project": self._project_id,
                    "filter": f"labels.k8s-cluster={cluster_name}",
                    "group_by": "XXk8s-namespaceXX",
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_11(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_billing_data(
                {
                    "project": self._project_id,
                    "filter": f"labels.k8s-cluster={cluster_name}",
                    "group_by": "K8S-NAMESPACE",
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_12(self, cluster_name: str) -> CostReportRaw:
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
            raise _translate_error(None) from exc

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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_13(self, cluster_name: str) -> CostReportRaw:
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

        namespace_costs = None
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_14(self, cluster_name: str) -> CostReportRaw:
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

        namespace_costs = _parse_gcp_rows(None)
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

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_15(self, cluster_name: str) -> CostReportRaw:
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
        namespace_costs_ns: list[NamespaceCostRaw] = None
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_16(self, cluster_name: str) -> CostReportRaw:
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
            cast(None, ns) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_17(self, cluster_name: str) -> CostReportRaw:
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
            cast(NamespaceCostRaw, None) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_18(self, cluster_name: str) -> CostReportRaw:
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
            cast(ns) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_19(self, cluster_name: str) -> CostReportRaw:
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
            cast(NamespaceCostRaw, ) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_20(self, cluster_name: str) -> CostReportRaw:
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
            cluster_name=None,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_21(self, cluster_name: str) -> CostReportRaw:
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
            namespace_costs=None,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_22(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=None,
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_23(self, cluster_name: str) -> CostReportRaw:
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
            data_source=None,
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_24(self, cluster_name: str) -> CostReportRaw:
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
            currency=None,
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_25(self, cluster_name: str) -> CostReportRaw:
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
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_26(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_27(self, cluster_name: str) -> CostReportRaw:
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
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_28(self, cluster_name: str) -> CostReportRaw:
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
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_29(self, cluster_name: str) -> CostReportRaw:
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
            )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_30(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(None),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_31(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(ns["XXmonthly_cost_usdXX"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_32(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(ns["MONTHLY_COST_USD"] for ns in namespace_costs_ns),
            data_source="gcp",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_33(self, cluster_name: str) -> CostReportRaw:
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
            data_source="XXgcpXX",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_34(self, cluster_name: str) -> CostReportRaw:
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
            data_source="GCP",
            currency="USD",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_35(self, cluster_name: str) -> CostReportRaw:
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
            currency="XXUSDXX",
        )

    def xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_36(self, cluster_name: str) -> CostReportRaw:
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
            currency="usd",
        )

    @_mutmut_mutated(mutants_xǁGCPCostAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> CloudBillingClient:  # pragma: no cover — requires GCP SDK
        if self._billing_client is None:
            from google.cloud import billing_v1

            raw_client = billing_v1.CloudBillingClient()
            self._billing_client = _GCPClientWrapper(raw_client)
        return self._billing_client

    def xǁGCPCostAdapterǁ_client_or_create__mutmut_orig(self) -> CloudBillingClient:  # pragma: no cover — requires GCP SDK
        if self._billing_client is None:
            from google.cloud import billing_v1

            raw_client = billing_v1.CloudBillingClient()
            self._billing_client = _GCPClientWrapper(raw_client)
        return self._billing_client

    def xǁGCPCostAdapterǁ_client_or_create__mutmut_1(self) -> CloudBillingClient:  # pragma: no cover — requires GCP SDK
        if self._billing_client is not None:
            from google.cloud import billing_v1

            raw_client = billing_v1.CloudBillingClient()
            self._billing_client = _GCPClientWrapper(raw_client)
        return self._billing_client

    def xǁGCPCostAdapterǁ_client_or_create__mutmut_2(self) -> CloudBillingClient:  # pragma: no cover — requires GCP SDK
        if self._billing_client is None:
            from google.cloud import billing_v1

            raw_client = None
            self._billing_client = _GCPClientWrapper(raw_client)
        return self._billing_client

    def xǁGCPCostAdapterǁ_client_or_create__mutmut_3(self) -> CloudBillingClient:  # pragma: no cover — requires GCP SDK
        if self._billing_client is None:
            from google.cloud import billing_v1

            raw_client = billing_v1.CloudBillingClient()
            self._billing_client = None
        return self._billing_client

    def xǁGCPCostAdapterǁ_client_or_create__mutmut_4(self) -> CloudBillingClient:  # pragma: no cover — requires GCP SDK
        if self._billing_client is None:
            from google.cloud import billing_v1

            raw_client = billing_v1.CloudBillingClient()
            self._billing_client = _GCPClientWrapper(None)
        return self._billing_client

mutants_xǁGCPCostAdapterǁ__init____mutmut['_mutmut_orig'] = GCPCostAdapter.xǁGCPCostAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁ__init____mutmut['xǁGCPCostAdapterǁ__init____mutmut_1'] = GCPCostAdapter.xǁGCPCostAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁ__init____mutmut['xǁGCPCostAdapterǁ__init____mutmut_2'] = GCPCostAdapter.xǁGCPCostAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['_mutmut_orig'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_1'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_2'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_3'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_4'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_5'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_6'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_7'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_8'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_9'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_10'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_11'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_12'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_13'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_14'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_15'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_16'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_17'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_18'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_19'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_20'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_21'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_22'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_23'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_24'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_25'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_26'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_27'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_28'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_29'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_30'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_31'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_32'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_33'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_34'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_35'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁestimate_cluster_cost__mutmut['xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_36'] = GCPCostAdapter.xǁGCPCostAdapterǁestimate_cluster_cost__mutmut_36 # type: ignore # mutmut generated

mutants_xǁGCPCostAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = GCPCostAdapter.xǁGCPCostAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁ_client_or_create__mutmut['xǁGCPCostAdapterǁ_client_or_create__mutmut_1'] = GCPCostAdapter.xǁGCPCostAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁ_client_or_create__mutmut['xǁGCPCostAdapterǁ_client_or_create__mutmut_2'] = GCPCostAdapter.xǁGCPCostAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁ_client_or_create__mutmut['xǁGCPCostAdapterǁ_client_or_create__mutmut_3'] = GCPCostAdapter.xǁGCPCostAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPCostAdapterǁ_client_or_create__mutmut['xǁGCPCostAdapterǁ_client_or_create__mutmut_4'] = GCPCostAdapter.xǁGCPCostAdapterǁ_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁ_GCPClientWrapperǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁ_GCPClientWrapperǁquery_billing_data__mutmut: MutantDict = {}  # type: ignore


class _GCPClientWrapper:  # pragma: no cover — requires GCP SDK
    """Wraps the real GCP Billing client to match the CloudBillingClient protocol."""

    @_mutmut_mutated(mutants_xǁ_GCPClientWrapperǁ__init____mutmut)
    def __init__(self, raw_client: object) -> None:
        self._raw = raw_client

    def xǁ_GCPClientWrapperǁ__init____mutmut_orig(self, raw_client: object) -> None:
        self._raw = raw_client

    def xǁ_GCPClientWrapperǁ__init____mutmut_1(self, raw_client: object) -> None:
        self._raw = None

    @_mutmut_mutated(mutants_xǁ_GCPClientWrapperǁquery_billing_data__mutmut)
    def query_billing_data(self, request: dict[str, object]) -> dict[str, object]:
        return {"rows": []}

    def xǁ_GCPClientWrapperǁquery_billing_data__mutmut_orig(self, request: dict[str, object]) -> dict[str, object]:
        return {"rows": []}

    def xǁ_GCPClientWrapperǁquery_billing_data__mutmut_1(self, request: dict[str, object]) -> dict[str, object]:
        return {"XXrowsXX": []}

    def xǁ_GCPClientWrapperǁquery_billing_data__mutmut_2(self, request: dict[str, object]) -> dict[str, object]:
        return {"ROWS": []}

mutants_xǁ_GCPClientWrapperǁ__init____mutmut['_mutmut_orig'] = _GCPClientWrapper.xǁ_GCPClientWrapperǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁ_GCPClientWrapperǁ__init____mutmut['xǁ_GCPClientWrapperǁ__init____mutmut_1'] = _GCPClientWrapper.xǁ_GCPClientWrapperǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁ_GCPClientWrapperǁquery_billing_data__mutmut['_mutmut_orig'] = _GCPClientWrapper.xǁ_GCPClientWrapperǁquery_billing_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁ_GCPClientWrapperǁquery_billing_data__mutmut['xǁ_GCPClientWrapperǁquery_billing_data__mutmut_1'] = _GCPClientWrapper.xǁ_GCPClientWrapperǁquery_billing_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁ_GCPClientWrapperǁquery_billing_data__mutmut['xǁ_GCPClientWrapperǁquery_billing_data__mutmut_2'] = _GCPClientWrapper.xǁ_GCPClientWrapperǁquery_billing_data__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_gcp_rows__mutmut)
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


def x__parse_gcp_rows__mutmut_orig(response: dict[str, object]) -> list[dict[str, object]]:
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


def x__parse_gcp_rows__mutmut_1(response: dict[str, object]) -> list[dict[str, object]]:
    rows = None
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


def x__parse_gcp_rows__mutmut_2(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get(None)
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


def x__parse_gcp_rows__mutmut_3(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("XXrowsXX")
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


def x__parse_gcp_rows__mutmut_4(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("ROWS")
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


def x__parse_gcp_rows__mutmut_5(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if isinstance(rows, list):
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


def x__parse_gcp_rows__mutmut_6(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if not isinstance(rows, list):
        return []
    results: list[dict[str, object]] = None
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


def x__parse_gcp_rows__mutmut_7(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if not isinstance(rows, list):
        return []
    results: list[dict[str, object]] = []
    for row in rows:
        if isinstance(row, dict):
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


def x__parse_gcp_rows__mutmut_8(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if not isinstance(rows, list):
        return []
    results: list[dict[str, object]] = []
    for row in rows:
        if not isinstance(row, dict):
            break
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


def x__parse_gcp_rows__mutmut_9(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if not isinstance(rows, list):
        return []
    results: list[dict[str, object]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        labels = None
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


def x__parse_gcp_rows__mutmut_10(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if not isinstance(rows, list):
        return []
    results: list[dict[str, object]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        labels = row.get(None)
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


def x__parse_gcp_rows__mutmut_11(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if not isinstance(rows, list):
        return []
    results: list[dict[str, object]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        labels = row.get("XXlabelsXX")
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


def x__parse_gcp_rows__mutmut_12(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if not isinstance(rows, list):
        return []
    results: list[dict[str, object]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        labels = row.get("LABELS")
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


def x__parse_gcp_rows__mutmut_13(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if not isinstance(rows, list):
        return []
    results: list[dict[str, object]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        labels = row.get("labels")
        ns = None
        if isinstance(labels, list):
            for label in labels:
                if isinstance(label, dict) and label.get("key") == "k8s-namespace":
                    ns = str(label.get("value", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_14(response: dict[str, object]) -> list[dict[str, object]]:
    rows = response.get("rows")
    if not isinstance(rows, list):
        return []
    results: list[dict[str, object]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        labels = row.get("labels")
        ns = "XXXX"
        if isinstance(labels, list):
            for label in labels:
                if isinstance(label, dict) and label.get("key") == "k8s-namespace":
                    ns = str(label.get("value", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_15(response: dict[str, object]) -> list[dict[str, object]]:
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
                if isinstance(label, dict) or label.get("key") == "k8s-namespace":
                    ns = str(label.get("value", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_16(response: dict[str, object]) -> list[dict[str, object]]:
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
                if isinstance(label, dict) and label.get(None) == "k8s-namespace":
                    ns = str(label.get("value", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_17(response: dict[str, object]) -> list[dict[str, object]]:
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
                if isinstance(label, dict) and label.get("XXkeyXX") == "k8s-namespace":
                    ns = str(label.get("value", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_18(response: dict[str, object]) -> list[dict[str, object]]:
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
                if isinstance(label, dict) and label.get("KEY") == "k8s-namespace":
                    ns = str(label.get("value", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_19(response: dict[str, object]) -> list[dict[str, object]]:
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
                if isinstance(label, dict) and label.get("key") != "k8s-namespace":
                    ns = str(label.get("value", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_20(response: dict[str, object]) -> list[dict[str, object]]:
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
                if isinstance(label, dict) and label.get("key") == "XXk8s-namespaceXX":
                    ns = str(label.get("value", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_21(response: dict[str, object]) -> list[dict[str, object]]:
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
                if isinstance(label, dict) and label.get("key") == "K8S-NAMESPACE":
                    ns = str(label.get("value", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_22(response: dict[str, object]) -> list[dict[str, object]]:
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
                    ns = None
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_23(response: dict[str, object]) -> list[dict[str, object]]:
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
                    ns = str(None)
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_24(response: dict[str, object]) -> list[dict[str, object]]:
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
                    ns = str(label.get(None, ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_25(response: dict[str, object]) -> list[dict[str, object]]:
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
                    ns = str(label.get("value", None))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_26(response: dict[str, object]) -> list[dict[str, object]]:
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
                    ns = str(label.get(""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_27(response: dict[str, object]) -> list[dict[str, object]]:
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
                    ns = str(label.get("value", ))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_28(response: dict[str, object]) -> list[dict[str, object]]:
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
                    ns = str(label.get("XXvalueXX", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_29(response: dict[str, object]) -> list[dict[str, object]]:
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
                    ns = str(label.get("VALUE", ""))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_30(response: dict[str, object]) -> list[dict[str, object]]:
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
                    ns = str(label.get("value", "XXXX"))
        cost_raw = row.get("cost")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_31(response: dict[str, object]) -> list[dict[str, object]]:
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
        cost_raw = None
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_32(response: dict[str, object]) -> list[dict[str, object]]:
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
        cost_raw = row.get(None)
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_33(response: dict[str, object]) -> list[dict[str, object]]:
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
        cost_raw = row.get("XXcostXX")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_34(response: dict[str, object]) -> list[dict[str, object]]:
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
        cost_raw = row.get("COST")
        cost = float(str(cost_raw)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_35(response: dict[str, object]) -> list[dict[str, object]]:
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
        cost = None
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_36(response: dict[str, object]) -> list[dict[str, object]]:
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
        cost = float(None) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_37(response: dict[str, object]) -> list[dict[str, object]]:
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
        cost = float(str(None)) if cost_raw is not None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_38(response: dict[str, object]) -> list[dict[str, object]]:
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
        cost = float(str(cost_raw)) if cost_raw is None else 0.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_39(response: dict[str, object]) -> list[dict[str, object]]:
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
        cost = float(str(cost_raw)) if cost_raw is not None else 1.0
        if ns:
            results.append({"namespace": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_40(response: dict[str, object]) -> list[dict[str, object]]:
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
            results.append(None)
    return results


def x__parse_gcp_rows__mutmut_41(response: dict[str, object]) -> list[dict[str, object]]:
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
            results.append({"XXnamespaceXX": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_42(response: dict[str, object]) -> list[dict[str, object]]:
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
            results.append({"NAMESPACE": ns, "monthly_cost_usd": cost})
    return results


def x__parse_gcp_rows__mutmut_43(response: dict[str, object]) -> list[dict[str, object]]:
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
            results.append({"namespace": ns, "XXmonthly_cost_usdXX": cost})
    return results


def x__parse_gcp_rows__mutmut_44(response: dict[str, object]) -> list[dict[str, object]]:
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
            results.append({"namespace": ns, "MONTHLY_COST_USD": cost})
    return results

mutants_x__parse_gcp_rows__mutmut['_mutmut_orig'] = x__parse_gcp_rows__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_1'] = x__parse_gcp_rows__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_2'] = x__parse_gcp_rows__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_3'] = x__parse_gcp_rows__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_4'] = x__parse_gcp_rows__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_5'] = x__parse_gcp_rows__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_6'] = x__parse_gcp_rows__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_7'] = x__parse_gcp_rows__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_8'] = x__parse_gcp_rows__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_9'] = x__parse_gcp_rows__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_10'] = x__parse_gcp_rows__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_11'] = x__parse_gcp_rows__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_12'] = x__parse_gcp_rows__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_13'] = x__parse_gcp_rows__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_14'] = x__parse_gcp_rows__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_15'] = x__parse_gcp_rows__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_16'] = x__parse_gcp_rows__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_17'] = x__parse_gcp_rows__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_18'] = x__parse_gcp_rows__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_19'] = x__parse_gcp_rows__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_20'] = x__parse_gcp_rows__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_21'] = x__parse_gcp_rows__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_22'] = x__parse_gcp_rows__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_23'] = x__parse_gcp_rows__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_24'] = x__parse_gcp_rows__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_25'] = x__parse_gcp_rows__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_26'] = x__parse_gcp_rows__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_27'] = x__parse_gcp_rows__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_28'] = x__parse_gcp_rows__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_29'] = x__parse_gcp_rows__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_30'] = x__parse_gcp_rows__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_31'] = x__parse_gcp_rows__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_32'] = x__parse_gcp_rows__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_33'] = x__parse_gcp_rows__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_34'] = x__parse_gcp_rows__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_35'] = x__parse_gcp_rows__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_36'] = x__parse_gcp_rows__mutmut_36 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_37'] = x__parse_gcp_rows__mutmut_37 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_38'] = x__parse_gcp_rows__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_39'] = x__parse_gcp_rows__mutmut_39 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_40'] = x__parse_gcp_rows__mutmut_40 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_41'] = x__parse_gcp_rows__mutmut_41 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_42'] = x__parse_gcp_rows__mutmut_42 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_43'] = x__parse_gcp_rows__mutmut_43 # type: ignore # mutmut generated
mutants_x__parse_gcp_rows__mutmut['x__parse_gcp_rows__mutmut_44'] = x__parse_gcp_rows__mutmut_44 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
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


def x__translate_error__mutmut_orig(
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


def x__translate_error__mutmut_1(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            None,
            context={"hint": "gcloud auth"},
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_2(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            "GCP credentials not found. Run 'gcloud auth application-default login'.",
            context=None,
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_3(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            context={"hint": "gcloud auth"},
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_4(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            "GCP credentials not found. Run 'gcloud auth application-default login'.",
            )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_5(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            "XXGCP credentials not found. Run 'gcloud auth application-default login'.XX",
            context={"hint": "gcloud auth"},
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_6(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            "gcp credentials not found. run 'gcloud auth application-default login'.",
            context={"hint": "gcloud auth"},
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_7(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            "GCP CREDENTIALS NOT FOUND. RUN 'GCLOUD AUTH APPLICATION-DEFAULT LOGIN'.",
            context={"hint": "gcloud auth"},
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_8(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            "GCP credentials not found. Run 'gcloud auth application-default login'.",
            context={"XXhintXX": "gcloud auth"},
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_9(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            "GCP credentials not found. Run 'gcloud auth application-default login'.",
            context={"HINT": "gcloud auth"},
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_10(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            "GCP credentials not found. Run 'gcloud auth application-default login'.",
            context={"hint": "XXgcloud authXX"},
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_11(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with GCP SDK installed
    from google.api_core.exceptions import PermissionDenied
    from google.auth.exceptions import DefaultCredentialsError

    if isinstance(exc, DefaultCredentialsError):
        return InsufficientPermissionsError(
            "GCP credentials not found. Run 'gcloud auth application-default login'.",
            context={"hint": "GCLOUD AUTH"},
        )
    if isinstance(exc, PermissionDenied):
        return ClusterUnreachableError(f"GCP Cloud Billing access denied: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_12(
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
        return ClusterUnreachableError(None)
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_13(
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
    return ClusterUnreachableError(None)

mutants_x__translate_error__mutmut['_mutmut_orig'] = x__translate_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_1'] = x__translate_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_2'] = x__translate_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_3'] = x__translate_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_4'] = x__translate_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_5'] = x__translate_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_6'] = x__translate_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_7'] = x__translate_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_8'] = x__translate_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_9'] = x__translate_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_10'] = x__translate_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_11'] = x__translate_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_12'] = x__translate_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_13'] = x__translate_error__mutmut_13 # type: ignore # mutmut generated
