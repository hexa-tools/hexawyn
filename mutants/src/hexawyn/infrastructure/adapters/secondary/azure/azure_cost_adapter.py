from __future__ import annotations

from typing import Protocol, cast

from hexawyn.application.ports.driven.cost_estimation_port import (
    CostEstimationPort,
    CostReportRaw,
    NamespaceCostRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CostManagementClient(Protocol):
    """Minimal contract for the azure cost-management client used here."""

    def query_usage(self, scope: str, parameters: dict[str, object]) -> dict[str, object]: ...
mutants_xǁAzureCostAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureCostAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class AzureCostAdapter(CostEstimationPort):
    """CostEstimationPort backed by Azure Cost Management.

    Queries the Cost Management API filtering by the *kubernetes-namespace* tag.
    Read-only — requires Cost Management Reader role only.
    """

    @_mutmut_mutated(mutants_xǁAzureCostAdapterǁ__init____mutmut)
    def __init__(
        self,
        subscription_id: str,
        cm_client: CostManagementClient | None = None,
    ) -> None:
        self._subscription_id = subscription_id
        self._cm_client = cm_client

    def xǁAzureCostAdapterǁ__init____mutmut_orig(
        self,
        subscription_id: str,
        cm_client: CostManagementClient | None = None,
    ) -> None:
        self._subscription_id = subscription_id
        self._cm_client = cm_client

    def xǁAzureCostAdapterǁ__init____mutmut_1(
        self,
        subscription_id: str,
        cm_client: CostManagementClient | None = None,
    ) -> None:
        self._subscription_id = None
        self._cm_client = cm_client

    def xǁAzureCostAdapterǁ__init____mutmut_2(
        self,
        subscription_id: str,
        cm_client: CostManagementClient | None = None,
    ) -> None:
        self._subscription_id = subscription_id
        self._cm_client = None

    @_mutmut_mutated(mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut)
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_orig(self, cluster_name: str) -> CostReportRaw:
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_1(self, cluster_name: str) -> CostReportRaw:
        client = None
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_2(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = None
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_3(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=None,
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_4(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters=None,
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_5(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_6(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_7(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "XXtypeXX": "ActualCost",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_8(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "TYPE": "ActualCost",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_9(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "XXActualCostXX",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_10(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "actualcost",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_11(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ACTUALCOST",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_12(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "XXtimeframeXX": "MonthToDate",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_13(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "TIMEFRAME": "MonthToDate",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_14(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "XXMonthToDateXX",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_15(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "monthtodate",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_16(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MONTHTODATE",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_17(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "XXdatasetXX": {
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_18(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "DATASET": {
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_19(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "XXgranularityXX": "None",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_20(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "GRANULARITY": "None",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_21(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "XXNoneXX",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_22(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "none",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_23(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "NONE",
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_24(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "XXgroupingXX": [{"type": "TagKey", "name": "kubernetes-namespace"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_25(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "GROUPING": [{"type": "TagKey", "name": "kubernetes-namespace"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_26(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "grouping": [{"XXtypeXX": "TagKey", "name": "kubernetes-namespace"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_27(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "grouping": [{"TYPE": "TagKey", "name": "kubernetes-namespace"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_28(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "grouping": [{"type": "XXTagKeyXX", "name": "kubernetes-namespace"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_29(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "grouping": [{"type": "tagkey", "name": "kubernetes-namespace"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_30(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "grouping": [{"type": "TAGKEY", "name": "kubernetes-namespace"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_31(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "grouping": [{"type": "TagKey", "XXnameXX": "kubernetes-namespace"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_32(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "grouping": [{"type": "TagKey", "NAME": "kubernetes-namespace"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_33(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "grouping": [{"type": "TagKey", "name": "XXkubernetes-namespaceXX"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_34(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.query_usage(
                scope=f"/subscriptions/{self._subscription_id}",
                parameters={
                    "type": "ActualCost",
                    "timeframe": "MonthToDate",
                    "dataset": {
                        "granularity": "None",
                        "grouping": [{"type": "TagKey", "name": "KUBERNETES-NAMESPACE"}],
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_35(self, cluster_name: str) -> CostReportRaw:
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
            raise _translate_error(None) from exc

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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_36(self, cluster_name: str) -> CostReportRaw:
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

        namespace_costs = None
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_37(self, cluster_name: str) -> CostReportRaw:
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

        namespace_costs = _parse_azure_rows(None)
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

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_38(self, cluster_name: str) -> CostReportRaw:
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
        namespace_costs_ns: list[NamespaceCostRaw] = None
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_39(self, cluster_name: str) -> CostReportRaw:
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
            cast(None, ns) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_40(self, cluster_name: str) -> CostReportRaw:
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
            cast(NamespaceCostRaw, None) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_41(self, cluster_name: str) -> CostReportRaw:
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
            cast(ns) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_42(self, cluster_name: str) -> CostReportRaw:
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
            cast(NamespaceCostRaw, ) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_43(self, cluster_name: str) -> CostReportRaw:
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
            cluster_name=None,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_44(self, cluster_name: str) -> CostReportRaw:
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
            namespace_costs=None,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_45(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=None,
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_46(self, cluster_name: str) -> CostReportRaw:
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
            data_source=None,
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_47(self, cluster_name: str) -> CostReportRaw:
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
            currency=None,
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_48(self, cluster_name: str) -> CostReportRaw:
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
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_49(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_50(self, cluster_name: str) -> CostReportRaw:
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
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_51(self, cluster_name: str) -> CostReportRaw:
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
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_52(self, cluster_name: str) -> CostReportRaw:
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
            )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_53(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(None),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_54(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(ns["XXmonthly_cost_usdXX"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_55(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(ns["MONTHLY_COST_USD"] for ns in namespace_costs_ns),
            data_source="azure",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_56(self, cluster_name: str) -> CostReportRaw:
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
            data_source="XXazureXX",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_57(self, cluster_name: str) -> CostReportRaw:
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
            data_source="AZURE",
            currency="USD",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_58(self, cluster_name: str) -> CostReportRaw:
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
            currency="XXUSDXX",
        )

    def xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_59(self, cluster_name: str) -> CostReportRaw:
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
            currency="usd",
        )

    @_mutmut_mutated(mutants_xǁAzureCostAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> CostManagementClient:  # pragma: no cover — requires Azure SDK
        if self._cm_client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.costmanagement import (
                CostManagementClient as AzureCostManagementClient,
            )

            self._cm_client = AzureCostManagementClient(DefaultAzureCredential())
        return self._cm_client

    def xǁAzureCostAdapterǁ_client_or_create__mutmut_orig(self) -> CostManagementClient:  # pragma: no cover — requires Azure SDK
        if self._cm_client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.costmanagement import (
                CostManagementClient as AzureCostManagementClient,
            )

            self._cm_client = AzureCostManagementClient(DefaultAzureCredential())
        return self._cm_client

    def xǁAzureCostAdapterǁ_client_or_create__mutmut_1(self) -> CostManagementClient:  # pragma: no cover — requires Azure SDK
        if self._cm_client is not None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.costmanagement import (
                CostManagementClient as AzureCostManagementClient,
            )

            self._cm_client = AzureCostManagementClient(DefaultAzureCredential())
        return self._cm_client

    def xǁAzureCostAdapterǁ_client_or_create__mutmut_2(self) -> CostManagementClient:  # pragma: no cover — requires Azure SDK
        if self._cm_client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.costmanagement import (
                CostManagementClient as AzureCostManagementClient,
            )

            self._cm_client = None
        return self._cm_client

    def xǁAzureCostAdapterǁ_client_or_create__mutmut_3(self) -> CostManagementClient:  # pragma: no cover — requires Azure SDK
        if self._cm_client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.costmanagement import (
                CostManagementClient as AzureCostManagementClient,
            )

            self._cm_client = AzureCostManagementClient(None)
        return self._cm_client

mutants_xǁAzureCostAdapterǁ__init____mutmut['_mutmut_orig'] = AzureCostAdapter.xǁAzureCostAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁ__init____mutmut['xǁAzureCostAdapterǁ__init____mutmut_1'] = AzureCostAdapter.xǁAzureCostAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁ__init____mutmut['xǁAzureCostAdapterǁ__init____mutmut_2'] = AzureCostAdapter.xǁAzureCostAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['_mutmut_orig'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_1'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_2'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_3'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_4'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_5'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_6'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_7'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_8'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_9'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_10'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_11'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_12'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_13'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_14'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_15'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_16'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_17'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_18'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_19'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_20'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_21'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_22'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_23'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_24'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_25'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_26'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_27'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_28'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_29'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_30'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_31'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_32'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_33'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_34'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_35'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_36'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_37'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_38'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_39'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_40'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_41'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_42'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_43'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_44'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_45'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_46'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_47'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_48'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_49'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_50'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_51'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_52'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_53'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_54'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_55'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_55 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_56'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_56 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_57'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_57 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_58'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_58 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁestimate_cluster_cost__mutmut['xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_59'] = AzureCostAdapter.xǁAzureCostAdapterǁestimate_cluster_cost__mutmut_59 # type: ignore # mutmut generated

mutants_xǁAzureCostAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = AzureCostAdapter.xǁAzureCostAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁ_client_or_create__mutmut['xǁAzureCostAdapterǁ_client_or_create__mutmut_1'] = AzureCostAdapter.xǁAzureCostAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁ_client_or_create__mutmut['xǁAzureCostAdapterǁ_client_or_create__mutmut_2'] = AzureCostAdapter.xǁAzureCostAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureCostAdapterǁ_client_or_create__mutmut['xǁAzureCostAdapterǁ_client_or_create__mutmut_3'] = AzureCostAdapter.xǁAzureCostAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_azure_rows__mutmut)
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


def x__parse_azure_rows__mutmut_orig(response: dict[str, object]) -> list[dict[str, object]]:
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


def x__parse_azure_rows__mutmut_1(response: dict[str, object]) -> list[dict[str, object]]:
    properties = None
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


def x__parse_azure_rows__mutmut_2(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get(None)
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


def x__parse_azure_rows__mutmut_3(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("XXpropertiesXX")
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


def x__parse_azure_rows__mutmut_4(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("PROPERTIES")
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


def x__parse_azure_rows__mutmut_5(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_6(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = None
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_7(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get(None)
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_8(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("XXrowsXX")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_9(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("ROWS")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_10(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_11(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"XXnamespaceXX": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_12(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"NAMESPACE": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_13(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(None), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_14(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[1]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_15(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "XXmonthly_cost_usdXX": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_16(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "MONTHLY_COST_USD": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_17(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(None)}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_18(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(None))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_19(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[2]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_20(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) or len(row) >= 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_21(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) > 2  # noqa: PLR2004
    ]


def x__parse_azure_rows__mutmut_22(response: dict[str, object]) -> list[dict[str, object]]:
    properties = response.get("properties")
    if not isinstance(properties, dict):
        return []
    rows = properties.get("rows")
    if not isinstance(rows, list):
        return []
    return [
        {"namespace": str(row[0]), "monthly_cost_usd": float(str(row[1]))}
        for row in rows
        if isinstance(row, list) and len(row) >= 3  # noqa: PLR2004
    ]

mutants_x__parse_azure_rows__mutmut['_mutmut_orig'] = x__parse_azure_rows__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_1'] = x__parse_azure_rows__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_2'] = x__parse_azure_rows__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_3'] = x__parse_azure_rows__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_4'] = x__parse_azure_rows__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_5'] = x__parse_azure_rows__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_6'] = x__parse_azure_rows__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_7'] = x__parse_azure_rows__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_8'] = x__parse_azure_rows__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_9'] = x__parse_azure_rows__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_10'] = x__parse_azure_rows__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_11'] = x__parse_azure_rows__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_12'] = x__parse_azure_rows__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_13'] = x__parse_azure_rows__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_14'] = x__parse_azure_rows__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_15'] = x__parse_azure_rows__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_16'] = x__parse_azure_rows__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_17'] = x__parse_azure_rows__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_18'] = x__parse_azure_rows__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_19'] = x__parse_azure_rows__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_20'] = x__parse_azure_rows__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_21'] = x__parse_azure_rows__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_azure_rows__mutmut['x__parse_azure_rows__mutmut_22'] = x__parse_azure_rows__mutmut_22 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
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


def x__translate_error__mutmut_orig(
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


def x__translate_error__mutmut_1(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            None,
            context={"hint": "az login"},
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_2(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            "Azure credentials not found. Run 'az login' or attach a managed identity.",
            context=None,
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_3(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            context={"hint": "az login"},
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_4(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            "Azure credentials not found. Run 'az login' or attach a managed identity.",
            )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_5(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            "XXAzure credentials not found. Run 'az login' or attach a managed identity.XX",
            context={"hint": "az login"},
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_6(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            "azure credentials not found. run 'az login' or attach a managed identity.",
            context={"hint": "az login"},
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_7(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            "AZURE CREDENTIALS NOT FOUND. RUN 'AZ LOGIN' OR ATTACH A MANAGED IDENTITY.",
            context={"hint": "az login"},
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_8(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            "Azure credentials not found. Run 'az login' or attach a managed identity.",
            context={"XXhintXX": "az login"},
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_9(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            "Azure credentials not found. Run 'az login' or attach a managed identity.",
            context={"HINT": "az login"},
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_10(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            "Azure credentials not found. Run 'az login' or attach a managed identity.",
            context={"hint": "XXaz loginXX"},
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_11(
    exc: Exception,
) -> Exception:  # pragma: no cover — only testable with Azure SDK installed
    from azure.core.exceptions import (
        ClientAuthenticationError,
        HttpResponseError,
    )

    if isinstance(exc, ClientAuthenticationError):
        return InsufficientPermissionsError(
            "Azure credentials not found. Run 'az login' or attach a managed identity.",
            context={"hint": "AZ LOGIN"},
        )
    if isinstance(exc, HttpResponseError):
        return ClusterUnreachableError(f"Azure Cost Management unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_12(
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
        return ClusterUnreachableError(None)
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_13(
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
