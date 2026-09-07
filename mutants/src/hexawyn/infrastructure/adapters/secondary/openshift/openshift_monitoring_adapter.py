from __future__ import annotations

from hexawyn.application.ports.driven.metrics_query_port import (
    MetricsQueryPort,
    PrometheusInstantSample,
    PrometheusRangeSample,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOpenShiftMonitoringAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut: MutantDict = {}  # type: ignore


class OpenShiftMonitoringAdapter(MetricsQueryPort):
    """MetricsQueryPort backed by the built-in OpenShift Monitoring stack.

    OpenShift ships a Thanos Querier exposing a Prometheus-compatible API, so
    this adapter is thin: it targets the in-cluster monitoring endpoint and
    reuses the vanilla Prometheus HTTP adapter for query execution and parsing.
    """

    @_mutmut_mutated(mutants_xǁOpenShiftMonitoringAdapterǁ__init____mutmut)
    def __init__(
        self,
        endpoint: str,
        token: str | None = None,
        delegate: MetricsQueryPort | None = None,
    ) -> None:
        self._endpoint = endpoint
        self._token = token
        self._delegate = delegate

    def xǁOpenShiftMonitoringAdapterǁ__init____mutmut_orig(
        self,
        endpoint: str,
        token: str | None = None,
        delegate: MetricsQueryPort | None = None,
    ) -> None:
        self._endpoint = endpoint
        self._token = token
        self._delegate = delegate

    def xǁOpenShiftMonitoringAdapterǁ__init____mutmut_1(
        self,
        endpoint: str,
        token: str | None = None,
        delegate: MetricsQueryPort | None = None,
    ) -> None:
        self._endpoint = None
        self._token = token
        self._delegate = delegate

    def xǁOpenShiftMonitoringAdapterǁ__init____mutmut_2(
        self,
        endpoint: str,
        token: str | None = None,
        delegate: MetricsQueryPort | None = None,
    ) -> None:
        self._endpoint = endpoint
        self._token = None
        self._delegate = delegate

    def xǁOpenShiftMonitoringAdapterǁ__init____mutmut_3(
        self,
        endpoint: str,
        token: str | None = None,
        delegate: MetricsQueryPort | None = None,
    ) -> None:
        self._endpoint = endpoint
        self._token = token
        self._delegate = None

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @_mutmut_mutated(mutants_xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut)
    def instant_query(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        return self._prometheus().instant_query(promql, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_orig(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        return self._prometheus().instant_query(promql, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_1(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        return self._prometheus().instant_query(None, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_2(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        return self._prometheus().instant_query(promql, None)

    def xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_3(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        return self._prometheus().instant_query(timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_4(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        return self._prometheus().instant_query(promql, )

    @_mutmut_mutated(mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut)
    def range_query(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, start, end, step, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_orig(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, start, end, step, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_1(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(None, start, end, step, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_2(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, None, end, step, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_3(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, start, None, step, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_4(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, start, end, None, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_5(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, start, end, step, None)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_6(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(start, end, step, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_7(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, end, step, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_8(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, start, step, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_9(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, start, end, timeout_seconds)

    def xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_10(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, start, end, step, )

    @_mutmut_mutated(mutants_xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut)
    def _prometheus(self) -> MetricsQueryPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
                PrometheusHTTPAdapter,
            )

            self._delegate = PrometheusHTTPAdapter(self._endpoint, token=self._token)
        return self._delegate

    def xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_orig(self) -> MetricsQueryPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
                PrometheusHTTPAdapter,
            )

            self._delegate = PrometheusHTTPAdapter(self._endpoint, token=self._token)
        return self._delegate

    def xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_1(self) -> MetricsQueryPort:
        if self._delegate is not None:
            from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
                PrometheusHTTPAdapter,
            )

            self._delegate = PrometheusHTTPAdapter(self._endpoint, token=self._token)
        return self._delegate

    def xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_2(self) -> MetricsQueryPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
                PrometheusHTTPAdapter,
            )

            self._delegate = None
        return self._delegate

    def xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_3(self) -> MetricsQueryPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
                PrometheusHTTPAdapter,
            )

            self._delegate = PrometheusHTTPAdapter(None, token=self._token)
        return self._delegate

    def xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_4(self) -> MetricsQueryPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
                PrometheusHTTPAdapter,
            )

            self._delegate = PrometheusHTTPAdapter(self._endpoint, token=None)
        return self._delegate

    def xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_5(self) -> MetricsQueryPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
                PrometheusHTTPAdapter,
            )

            self._delegate = PrometheusHTTPAdapter(token=self._token)
        return self._delegate

    def xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_6(self) -> MetricsQueryPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
                PrometheusHTTPAdapter,
            )

            self._delegate = PrometheusHTTPAdapter(self._endpoint, )
        return self._delegate

mutants_xǁOpenShiftMonitoringAdapterǁ__init____mutmut['_mutmut_orig'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁ__init____mutmut['xǁOpenShiftMonitoringAdapterǁ__init____mutmut_1'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁ__init____mutmut['xǁOpenShiftMonitoringAdapterǁ__init____mutmut_2'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁ__init____mutmut['xǁOpenShiftMonitoringAdapterǁ__init____mutmut_3'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut['_mutmut_orig'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut['xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_1'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut['xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_2'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut['xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_3'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut['xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_4'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁinstant_query__mutmut_4 # type: ignore # mutmut generated

mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['_mutmut_orig'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_1'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_2'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_3'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_4'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_5'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_6'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_7'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_8'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_9'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁrange_query__mutmut['xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_10'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁrange_query__mutmut_10 # type: ignore # mutmut generated

mutants_xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut['_mutmut_orig'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut['xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_1'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut['xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_2'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut['xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_3'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut['xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_4'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut['xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_5'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut['xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_6'] = OpenShiftMonitoringAdapter.xǁOpenShiftMonitoringAdapterǁ_prometheus__mutmut_6 # type: ignore # mutmut generated
