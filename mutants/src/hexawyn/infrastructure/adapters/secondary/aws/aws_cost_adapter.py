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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CostExplorerClient(Protocol):
    """Minimal contract for the boto3 Cost Explorer client used here."""

    def get_cost_and_usage(  # noqa: PLR0913
        self,
        time_period: dict[str, str],
        granularity: str,
        filter_obj: dict[str, object],
        group_by: list[dict[str, str]],
        metrics: list[str],
    ) -> dict[str, object]: ...
mutants_xǁAWSCostAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class AWSCostAdapter(CostEstimationPort):
    """CostEstimationPort backed by AWS Cost Explorer.

    Queries the Cost Explorer API for the *kubernetes.io/cluster* tag,
    grouping results by *kubernetes.io/namespace*.
    Read-only — requires ``ce:GetCostAndUsage`` only.
    """

    @_mutmut_mutated(mutants_xǁAWSCostAdapterǁ__init____mutmut)
    def __init__(self, region: str, ce_client: CostExplorerClient | None = None) -> None:
        self._region = region
        self._ce_client = ce_client

    def xǁAWSCostAdapterǁ__init____mutmut_orig(self, region: str, ce_client: CostExplorerClient | None = None) -> None:
        self._region = region
        self._ce_client = ce_client

    def xǁAWSCostAdapterǁ__init____mutmut_1(self, region: str, ce_client: CostExplorerClient | None = None) -> None:
        self._region = None
        self._ce_client = ce_client

    def xǁAWSCostAdapterǁ__init____mutmut_2(self, region: str, ce_client: CostExplorerClient | None = None) -> None:
        self._region = region
        self._ce_client = None

    @_mutmut_mutated(mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut)
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_orig(self, cluster_name: str) -> CostReportRaw:
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_1(self, cluster_name: str) -> CostReportRaw:
        client = None
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_2(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = None
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_3(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period=None,
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_4(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=None,
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_5(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj=None,
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_6(self, cluster_name: str) -> CostReportRaw:
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
                group_by=None,
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_7(self, cluster_name: str) -> CostReportRaw:
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
                metrics=None,
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_8(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_9(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_10(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_11(self, cluster_name: str) -> CostReportRaw:
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_12(self, cluster_name: str) -> CostReportRaw:
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_13(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"XXStartXX": "2026-01-01", "End": "2026-02-01"},
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_14(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"start": "2026-01-01", "End": "2026-02-01"},
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_15(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"START": "2026-01-01", "End": "2026-02-01"},
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_16(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "XX2026-01-01XX", "End": "2026-02-01"},
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_17(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "XXEndXX": "2026-02-01"},
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_18(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "end": "2026-02-01"},
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_19(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "END": "2026-02-01"},
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_20(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "XX2026-02-01XX"},
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_21(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "XXTagsXX": {
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_22(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "tags": {
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_23(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "TAGS": {
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_24(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "Tags": {
                        "XXKeyXX": f"kubernetes.io/cluster/{cluster_name}",
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_25(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "Tags": {
                        "key": f"kubernetes.io/cluster/{cluster_name}",
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_26(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "Tags": {
                        "KEY": f"kubernetes.io/cluster/{cluster_name}",
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_27(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "Tags": {
                        "Key": f"kubernetes.io/cluster/{cluster_name}",
                        "XXValuesXX": ["owned"],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_28(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "Tags": {
                        "Key": f"kubernetes.io/cluster/{cluster_name}",
                        "values": ["owned"],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_29(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "Tags": {
                        "Key": f"kubernetes.io/cluster/{cluster_name}",
                        "VALUES": ["owned"],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_30(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "Tags": {
                        "Key": f"kubernetes.io/cluster/{cluster_name}",
                        "Values": ["XXownedXX"],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_31(self, cluster_name: str) -> CostReportRaw:
        client = self._client_or_create()
        try:
            response = client.get_cost_and_usage(
                time_period={"Start": "2026-01-01", "End": "2026-02-01"},
                granularity=_COST_EXPLORER_GRANULARITY,
                filter_obj={
                    "Tags": {
                        "Key": f"kubernetes.io/cluster/{cluster_name}",
                        "Values": ["OWNED"],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_32(self, cluster_name: str) -> CostReportRaw:
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
                group_by=[{"XXTypeXX": "TAG", "Key": "kubernetes.io/namespace"}],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_33(self, cluster_name: str) -> CostReportRaw:
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
                group_by=[{"type": "TAG", "Key": "kubernetes.io/namespace"}],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_34(self, cluster_name: str) -> CostReportRaw:
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
                group_by=[{"TYPE": "TAG", "Key": "kubernetes.io/namespace"}],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_35(self, cluster_name: str) -> CostReportRaw:
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
                group_by=[{"Type": "XXTAGXX", "Key": "kubernetes.io/namespace"}],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_36(self, cluster_name: str) -> CostReportRaw:
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
                group_by=[{"Type": "tag", "Key": "kubernetes.io/namespace"}],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_37(self, cluster_name: str) -> CostReportRaw:
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
                group_by=[{"Type": "TAG", "XXKeyXX": "kubernetes.io/namespace"}],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_38(self, cluster_name: str) -> CostReportRaw:
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
                group_by=[{"Type": "TAG", "key": "kubernetes.io/namespace"}],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_39(self, cluster_name: str) -> CostReportRaw:
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
                group_by=[{"Type": "TAG", "KEY": "kubernetes.io/namespace"}],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_40(self, cluster_name: str) -> CostReportRaw:
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
                group_by=[{"Type": "TAG", "Key": "XXkubernetes.io/namespaceXX"}],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_41(self, cluster_name: str) -> CostReportRaw:
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
                group_by=[{"Type": "TAG", "Key": "KUBERNETES.IO/NAMESPACE"}],
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_42(self, cluster_name: str) -> CostReportRaw:
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
                metrics=list(None),
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_43(self, cluster_name: str) -> CostReportRaw:
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
            raise _translate_error(None) from exc

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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_44(self, cluster_name: str) -> CostReportRaw:
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

        namespace_costs = None
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_45(self, cluster_name: str) -> CostReportRaw:
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

        namespace_costs = _parse_namespace_costs(None)
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

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_46(self, cluster_name: str) -> CostReportRaw:
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
        namespace_costs_ns: list[NamespaceCostRaw] = None
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_47(self, cluster_name: str) -> CostReportRaw:
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
            cast(None, ns) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_48(self, cluster_name: str) -> CostReportRaw:
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
            cast(NamespaceCostRaw, None) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_49(self, cluster_name: str) -> CostReportRaw:
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
            cast(ns) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_50(self, cluster_name: str) -> CostReportRaw:
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
            cast(NamespaceCostRaw, ) for ns in namespace_costs
        ]
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_51(self, cluster_name: str) -> CostReportRaw:
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
            cluster_name=None,
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_52(self, cluster_name: str) -> CostReportRaw:
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
            namespace_costs=None,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_53(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=None,
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_54(self, cluster_name: str) -> CostReportRaw:
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
            data_source=None,
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_55(self, cluster_name: str) -> CostReportRaw:
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
            currency=None,
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_56(self, cluster_name: str) -> CostReportRaw:
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
            namespace_costs=namespace_costs_ns,
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_57(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(ns["monthly_cost_usd"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_58(self, cluster_name: str) -> CostReportRaw:
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
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_59(self, cluster_name: str) -> CostReportRaw:
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
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_60(self, cluster_name: str) -> CostReportRaw:
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
            )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_61(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(None),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_62(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(ns["XXmonthly_cost_usdXX"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_63(self, cluster_name: str) -> CostReportRaw:
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
            total_monthly_cost_usd=sum(ns["MONTHLY_COST_USD"] for ns in namespace_costs_ns),
            data_source="aws",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_64(self, cluster_name: str) -> CostReportRaw:
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
            data_source="XXawsXX",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_65(self, cluster_name: str) -> CostReportRaw:
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
            data_source="AWS",
            currency="USD",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_66(self, cluster_name: str) -> CostReportRaw:
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
            currency="XXUSDXX",
        )

    def xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_67(self, cluster_name: str) -> CostReportRaw:
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
            currency="usd",
        )

    @_mutmut_mutated(mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> CostExplorerClient:
        if self._ce_client is None:
            import boto3

            self._ce_client = boto3.client("ce", region_name=self._region)
        return self._ce_client

    def xǁAWSCostAdapterǁ_client_or_create__mutmut_orig(self) -> CostExplorerClient:
        if self._ce_client is None:
            import boto3

            self._ce_client = boto3.client("ce", region_name=self._region)
        return self._ce_client

    def xǁAWSCostAdapterǁ_client_or_create__mutmut_1(self) -> CostExplorerClient:
        if self._ce_client is not None:
            import boto3

            self._ce_client = boto3.client("ce", region_name=self._region)
        return self._ce_client

    def xǁAWSCostAdapterǁ_client_or_create__mutmut_2(self) -> CostExplorerClient:
        if self._ce_client is None:
            import boto3

            self._ce_client = None
        return self._ce_client

    def xǁAWSCostAdapterǁ_client_or_create__mutmut_3(self) -> CostExplorerClient:
        if self._ce_client is None:
            import boto3

            self._ce_client = boto3.client(None, region_name=self._region)
        return self._ce_client

    def xǁAWSCostAdapterǁ_client_or_create__mutmut_4(self) -> CostExplorerClient:
        if self._ce_client is None:
            import boto3

            self._ce_client = boto3.client("ce", region_name=None)
        return self._ce_client

    def xǁAWSCostAdapterǁ_client_or_create__mutmut_5(self) -> CostExplorerClient:
        if self._ce_client is None:
            import boto3

            self._ce_client = boto3.client(region_name=self._region)
        return self._ce_client

    def xǁAWSCostAdapterǁ_client_or_create__mutmut_6(self) -> CostExplorerClient:
        if self._ce_client is None:
            import boto3

            self._ce_client = boto3.client("ce", )
        return self._ce_client

    def xǁAWSCostAdapterǁ_client_or_create__mutmut_7(self) -> CostExplorerClient:
        if self._ce_client is None:
            import boto3

            self._ce_client = boto3.client("XXceXX", region_name=self._region)
        return self._ce_client

    def xǁAWSCostAdapterǁ_client_or_create__mutmut_8(self) -> CostExplorerClient:
        if self._ce_client is None:
            import boto3

            self._ce_client = boto3.client("CE", region_name=self._region)
        return self._ce_client

mutants_xǁAWSCostAdapterǁ__init____mutmut['_mutmut_orig'] = AWSCostAdapter.xǁAWSCostAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁ__init____mutmut['xǁAWSCostAdapterǁ__init____mutmut_1'] = AWSCostAdapter.xǁAWSCostAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁ__init____mutmut['xǁAWSCostAdapterǁ__init____mutmut_2'] = AWSCostAdapter.xǁAWSCostAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['_mutmut_orig'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_1'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_2'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_3'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_4'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_5'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_6'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_7'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_8'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_9'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_10'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_11'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_12'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_13'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_14'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_15'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_16'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_17'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_18'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_19'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_20'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_21'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_22'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_23'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_24'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_25'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_26'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_27'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_28'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_29'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_30'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_31'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_32'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_33'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_34'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_35'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_36'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_37'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_38'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_39'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_40'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_41'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_42'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_43'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_44'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_45'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_46'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_47'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_48'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_49'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_50'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_51'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_52'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_53'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_54'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_55'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_55 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_56'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_56 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_57'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_57 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_58'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_58 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_59'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_59 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_60'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_60 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_61'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_61 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_62'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_62 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_63'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_63 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_64'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_64 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_65'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_65 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_66'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_66 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁestimate_cluster_cost__mutmut['xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_67'] = AWSCostAdapter.xǁAWSCostAdapterǁestimate_cluster_cost__mutmut_67 # type: ignore # mutmut generated

mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = AWSCostAdapter.xǁAWSCostAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut['xǁAWSCostAdapterǁ_client_or_create__mutmut_1'] = AWSCostAdapter.xǁAWSCostAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut['xǁAWSCostAdapterǁ_client_or_create__mutmut_2'] = AWSCostAdapter.xǁAWSCostAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut['xǁAWSCostAdapterǁ_client_or_create__mutmut_3'] = AWSCostAdapter.xǁAWSCostAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut['xǁAWSCostAdapterǁ_client_or_create__mutmut_4'] = AWSCostAdapter.xǁAWSCostAdapterǁ_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut['xǁAWSCostAdapterǁ_client_or_create__mutmut_5'] = AWSCostAdapter.xǁAWSCostAdapterǁ_client_or_create__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut['xǁAWSCostAdapterǁ_client_or_create__mutmut_6'] = AWSCostAdapter.xǁAWSCostAdapterǁ_client_or_create__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut['xǁAWSCostAdapterǁ_client_or_create__mutmut_7'] = AWSCostAdapter.xǁAWSCostAdapterǁ_client_or_create__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSCostAdapterǁ_client_or_create__mutmut['xǁAWSCostAdapterǁ_client_or_create__mutmut_8'] = AWSCostAdapter.xǁAWSCostAdapterǁ_client_or_create__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_namespace_costs__mutmut)
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


def x__parse_namespace_costs__mutmut_orig(response: dict[str, object]) -> list[dict[str, object]]:
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


def x__parse_namespace_costs__mutmut_1(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = None
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


def x__parse_namespace_costs__mutmut_2(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = None
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


def x__parse_namespace_costs__mutmut_3(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get(None)
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


def x__parse_namespace_costs__mutmut_4(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("XXResultsByTimeXX")
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


def x__parse_namespace_costs__mutmut_5(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("resultsbytime")
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


def x__parse_namespace_costs__mutmut_6(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("RESULTSBYTIME")
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


def x__parse_namespace_costs__mutmut_7(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if isinstance(results_by_time, list):
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


def x__parse_namespace_costs__mutmut_8(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if not isinstance(results_by_time, list):
        return results
    for time_block in results_by_time:
        if isinstance(time_block, dict):
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


def x__parse_namespace_costs__mutmut_9(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if not isinstance(results_by_time, list):
        return results
    for time_block in results_by_time:
        if not isinstance(time_block, dict):
            break
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


def x__parse_namespace_costs__mutmut_10(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if not isinstance(results_by_time, list):
        return results
    for time_block in results_by_time:
        if not isinstance(time_block, dict):
            continue
        groups = None
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


def x__parse_namespace_costs__mutmut_11(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if not isinstance(results_by_time, list):
        return results
    for time_block in results_by_time:
        if not isinstance(time_block, dict):
            continue
        groups = time_block.get(None)
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


def x__parse_namespace_costs__mutmut_12(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if not isinstance(results_by_time, list):
        return results
    for time_block in results_by_time:
        if not isinstance(time_block, dict):
            continue
        groups = time_block.get("XXGroupsXX")
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


def x__parse_namespace_costs__mutmut_13(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if not isinstance(results_by_time, list):
        return results
    for time_block in results_by_time:
        if not isinstance(time_block, dict):
            continue
        groups = time_block.get("groups")
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


def x__parse_namespace_costs__mutmut_14(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if not isinstance(results_by_time, list):
        return results
    for time_block in results_by_time:
        if not isinstance(time_block, dict):
            continue
        groups = time_block.get("GROUPS")
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


def x__parse_namespace_costs__mutmut_15(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if not isinstance(results_by_time, list):
        return results
    for time_block in results_by_time:
        if not isinstance(time_block, dict):
            continue
        groups = time_block.get("Groups")
        if isinstance(groups, list):
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


def x__parse_namespace_costs__mutmut_16(response: dict[str, object]) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    results_by_time = response.get("ResultsByTime")
    if not isinstance(results_by_time, list):
        return results
    for time_block in results_by_time:
        if not isinstance(time_block, dict):
            continue
        groups = time_block.get("Groups")
        if not isinstance(groups, list):
            break
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


def x__parse_namespace_costs__mutmut_17(response: dict[str, object]) -> list[dict[str, object]]:
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
            if isinstance(group, dict):
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


def x__parse_namespace_costs__mutmut_18(response: dict[str, object]) -> list[dict[str, object]]:
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
                break
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


def x__parse_namespace_costs__mutmut_19(response: dict[str, object]) -> list[dict[str, object]]:
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
            keys = None
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


def x__parse_namespace_costs__mutmut_20(response: dict[str, object]) -> list[dict[str, object]]:
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
            keys = group.get(None)
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


def x__parse_namespace_costs__mutmut_21(response: dict[str, object]) -> list[dict[str, object]]:
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
            keys = group.get("XXKeysXX")
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


def x__parse_namespace_costs__mutmut_22(response: dict[str, object]) -> list[dict[str, object]]:
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
            keys = group.get("keys")
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


def x__parse_namespace_costs__mutmut_23(response: dict[str, object]) -> list[dict[str, object]]:
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
            keys = group.get("KEYS")
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


def x__parse_namespace_costs__mutmut_24(response: dict[str, object]) -> list[dict[str, object]]:
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
            if not isinstance(keys, list) and not keys:
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


def x__parse_namespace_costs__mutmut_25(response: dict[str, object]) -> list[dict[str, object]]:
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
            if isinstance(keys, list) or not keys:
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


def x__parse_namespace_costs__mutmut_26(response: dict[str, object]) -> list[dict[str, object]]:
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
            if not isinstance(keys, list) or keys:
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


def x__parse_namespace_costs__mutmut_27(response: dict[str, object]) -> list[dict[str, object]]:
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
                break
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


def x__parse_namespace_costs__mutmut_28(response: dict[str, object]) -> list[dict[str, object]]:
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
            metrics = None
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


def x__parse_namespace_costs__mutmut_29(response: dict[str, object]) -> list[dict[str, object]]:
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
            metrics = group.get(None)
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


def x__parse_namespace_costs__mutmut_30(response: dict[str, object]) -> list[dict[str, object]]:
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
            metrics = group.get("XXMetricsXX")
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


def x__parse_namespace_costs__mutmut_31(response: dict[str, object]) -> list[dict[str, object]]:
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
            metrics = group.get("metrics")
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


def x__parse_namespace_costs__mutmut_32(response: dict[str, object]) -> list[dict[str, object]]:
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
            metrics = group.get("METRICS")
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


def x__parse_namespace_costs__mutmut_33(response: dict[str, object]) -> list[dict[str, object]]:
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
            if isinstance(metrics, dict):
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


def x__parse_namespace_costs__mutmut_34(response: dict[str, object]) -> list[dict[str, object]]:
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
                break
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


def x__parse_namespace_costs__mutmut_35(response: dict[str, object]) -> list[dict[str, object]]:
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
            cost = None
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


def x__parse_namespace_costs__mutmut_36(response: dict[str, object]) -> list[dict[str, object]]:
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
            cost = metrics.get(None)
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


def x__parse_namespace_costs__mutmut_37(response: dict[str, object]) -> list[dict[str, object]]:
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
            cost = metrics.get("XXUnblendedCostXX")
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


def x__parse_namespace_costs__mutmut_38(response: dict[str, object]) -> list[dict[str, object]]:
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
            cost = metrics.get("unblendedcost")
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


def x__parse_namespace_costs__mutmut_39(response: dict[str, object]) -> list[dict[str, object]]:
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
            cost = metrics.get("UNBLENDEDCOST")
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


def x__parse_namespace_costs__mutmut_40(response: dict[str, object]) -> list[dict[str, object]]:
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
            if isinstance(cost, dict):
                continue
            amount = cost.get("Amount")
            results.append(
                {
                    "namespace": str(keys[0]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_41(response: dict[str, object]) -> list[dict[str, object]]:
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
                break
            amount = cost.get("Amount")
            results.append(
                {
                    "namespace": str(keys[0]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_42(response: dict[str, object]) -> list[dict[str, object]]:
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
            amount = None
            results.append(
                {
                    "namespace": str(keys[0]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_43(response: dict[str, object]) -> list[dict[str, object]]:
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
            amount = cost.get(None)
            results.append(
                {
                    "namespace": str(keys[0]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_44(response: dict[str, object]) -> list[dict[str, object]]:
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
            amount = cost.get("XXAmountXX")
            results.append(
                {
                    "namespace": str(keys[0]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_45(response: dict[str, object]) -> list[dict[str, object]]:
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
            amount = cost.get("amount")
            results.append(
                {
                    "namespace": str(keys[0]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_46(response: dict[str, object]) -> list[dict[str, object]]:
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
            amount = cost.get("AMOUNT")
            results.append(
                {
                    "namespace": str(keys[0]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_47(response: dict[str, object]) -> list[dict[str, object]]:
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
                None
            )
    return results


def x__parse_namespace_costs__mutmut_48(response: dict[str, object]) -> list[dict[str, object]]:
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
                    "XXnamespaceXX": str(keys[0]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_49(response: dict[str, object]) -> list[dict[str, object]]:
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
                    "NAMESPACE": str(keys[0]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_50(response: dict[str, object]) -> list[dict[str, object]]:
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
                    "namespace": str(None),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_51(response: dict[str, object]) -> list[dict[str, object]]:
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
                    "namespace": str(keys[1]),
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_52(response: dict[str, object]) -> list[dict[str, object]]:
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
                    "XXmonthly_cost_usdXX": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_53(response: dict[str, object]) -> list[dict[str, object]]:
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
                    "MONTHLY_COST_USD": float(str(amount)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_54(response: dict[str, object]) -> list[dict[str, object]]:
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
                    "monthly_cost_usd": float(None) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_55(response: dict[str, object]) -> list[dict[str, object]]:
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
                    "monthly_cost_usd": float(str(None)) if amount is not None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_56(response: dict[str, object]) -> list[dict[str, object]]:
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
                    "monthly_cost_usd": float(str(amount)) if amount is None else 0.0,
                }
            )
    return results


def x__parse_namespace_costs__mutmut_57(response: dict[str, object]) -> list[dict[str, object]]:
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
                    "monthly_cost_usd": float(str(amount)) if amount is not None else 1.0,
                }
            )
    return results

mutants_x__parse_namespace_costs__mutmut['_mutmut_orig'] = x__parse_namespace_costs__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_1'] = x__parse_namespace_costs__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_2'] = x__parse_namespace_costs__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_3'] = x__parse_namespace_costs__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_4'] = x__parse_namespace_costs__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_5'] = x__parse_namespace_costs__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_6'] = x__parse_namespace_costs__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_7'] = x__parse_namespace_costs__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_8'] = x__parse_namespace_costs__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_9'] = x__parse_namespace_costs__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_10'] = x__parse_namespace_costs__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_11'] = x__parse_namespace_costs__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_12'] = x__parse_namespace_costs__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_13'] = x__parse_namespace_costs__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_14'] = x__parse_namespace_costs__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_15'] = x__parse_namespace_costs__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_16'] = x__parse_namespace_costs__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_17'] = x__parse_namespace_costs__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_18'] = x__parse_namespace_costs__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_19'] = x__parse_namespace_costs__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_20'] = x__parse_namespace_costs__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_21'] = x__parse_namespace_costs__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_22'] = x__parse_namespace_costs__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_23'] = x__parse_namespace_costs__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_24'] = x__parse_namespace_costs__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_25'] = x__parse_namespace_costs__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_26'] = x__parse_namespace_costs__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_27'] = x__parse_namespace_costs__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_28'] = x__parse_namespace_costs__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_29'] = x__parse_namespace_costs__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_30'] = x__parse_namespace_costs__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_31'] = x__parse_namespace_costs__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_32'] = x__parse_namespace_costs__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_33'] = x__parse_namespace_costs__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_34'] = x__parse_namespace_costs__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_35'] = x__parse_namespace_costs__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_36'] = x__parse_namespace_costs__mutmut_36 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_37'] = x__parse_namespace_costs__mutmut_37 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_38'] = x__parse_namespace_costs__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_39'] = x__parse_namespace_costs__mutmut_39 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_40'] = x__parse_namespace_costs__mutmut_40 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_41'] = x__parse_namespace_costs__mutmut_41 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_42'] = x__parse_namespace_costs__mutmut_42 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_43'] = x__parse_namespace_costs__mutmut_43 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_44'] = x__parse_namespace_costs__mutmut_44 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_45'] = x__parse_namespace_costs__mutmut_45 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_46'] = x__parse_namespace_costs__mutmut_46 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_47'] = x__parse_namespace_costs__mutmut_47 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_48'] = x__parse_namespace_costs__mutmut_48 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_49'] = x__parse_namespace_costs__mutmut_49 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_50'] = x__parse_namespace_costs__mutmut_50 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_51'] = x__parse_namespace_costs__mutmut_51 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_52'] = x__parse_namespace_costs__mutmut_52 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_53'] = x__parse_namespace_costs__mutmut_53 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_54'] = x__parse_namespace_costs__mutmut_54 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_55'] = x__parse_namespace_costs__mutmut_55 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_56'] = x__parse_namespace_costs__mutmut_56 # type: ignore # mutmut generated
mutants_x__parse_namespace_costs__mutmut['x__parse_namespace_costs__mutmut_57'] = x__parse_namespace_costs__mutmut_57 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
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


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
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


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            None,
            context={"hint": "aws configure"},
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
            context=None,
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            context={"hint": "aws configure"},
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
            )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            "XXAWS credentials not found. Run 'aws configure' or attach an IAM role.XX",
            context={"hint": "aws configure"},
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            "aws credentials not found. run 'aws configure' or attach an iam role.",
            context={"hint": "aws configure"},
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            "AWS CREDENTIALS NOT FOUND. RUN 'AWS CONFIGURE' OR ATTACH AN IAM ROLE.",
            context={"hint": "aws configure"},
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
            context={"XXhintXX": "aws configure"},
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
            context={"HINT": "aws configure"},
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
            context={"hint": "XXaws configureXX"},
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    from botocore.exceptions import (
        BotoCoreError,
        ClientError,
        NoCredentialsError,
    )

    if isinstance(exc, NoCredentialsError):
        return InsufficientPermissionsError(
            "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
            context={"hint": "AWS CONFIGURE"},
        )
    if isinstance(exc, ClientError | BotoCoreError):
        return ClusterUnreachableError(f"AWS Cost Explorer unreachable: {exc}")
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
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
        return ClusterUnreachableError(None)
    return ClusterUnreachableError(f"Unexpected billing API error: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
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
