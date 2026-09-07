from __future__ import annotations

import math

from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.domain.models.span_bottleneck import BottleneckRequest, SpanBreakdown
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import (
    query_prometheus_instant,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut: MutantDict = {}  # type: ignore


class OTelSpanBreakdownAdapter(SpanBottleneckPort):
    @_mutmut_mutated(mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut)
    def fetch_db_spans(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, category="db", label_filter='db_system!="redis"'
        )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_orig(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, category="db", label_filter='db_system!="redis"'
        )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_1(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = None
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_2(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            None, category="db", label_filter='db_system!="redis"'
        )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_3(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, category=None, label_filter='db_system!="redis"'
        )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_4(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, category="db", label_filter=None
        )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_5(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            category="db", label_filter='db_system!="redis"'
        )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_6(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, label_filter='db_system!="redis"'
        )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_7(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, category="db", )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_8(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, category="XXdbXX", label_filter='db_system!="redis"'
        )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_9(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, category="DB", label_filter='db_system!="redis"'
        )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_10(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, category="db", label_filter='XXdb_system!="redis"XX'
        )
        return breakdown
    def xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_11(self, request: BottleneckRequest) -> SpanBreakdown:
        breakdown, _ = self._fetch_breakdown(
            request, category="db", label_filter='DB_SYSTEM!="REDIS"'
        )
        return breakdown

    @_mutmut_mutated(mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut)
    def fetch_redis_spans(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="redis", label_filter='db_system="redis"'
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_orig(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="redis", label_filter='db_system="redis"'
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_1(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = None
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_2(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            None, category="redis", label_filter='db_system="redis"'
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_3(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category=None, label_filter='db_system="redis"'
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_4(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="redis", label_filter=None
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_5(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            category="redis", label_filter='db_system="redis"'
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_6(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, label_filter='db_system="redis"'
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_7(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="redis", )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_8(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="XXredisXX", label_filter='db_system="redis"'
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_9(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="REDIS", label_filter='db_system="redis"'
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_10(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="redis", label_filter='XXdb_system="redis"XX'
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_11(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="redis", label_filter='DB_SYSTEM="REDIS"'
        )
        return breakdown if sample_count > 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_12(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="redis", label_filter='db_system="redis"'
        )
        return breakdown if sample_count >= 0 else None

    def xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_13(self, request: BottleneckRequest) -> SpanBreakdown | None:
        breakdown, sample_count = self._fetch_breakdown(
            request, category="redis", label_filter='db_system="redis"'
        )
        return breakdown if sample_count > 1 else None

    @_mutmut_mutated(mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut)
    def _fetch_breakdown(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_orig(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_1(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = None
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_2(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = None
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_3(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = None
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_4(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = None
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_5(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = None
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_6(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = None

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_7(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = None
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_8(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(None)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_9(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = None
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_10(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(None)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_11(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = None
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_12(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(None)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_13(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = None
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_14(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(None)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_15(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = None

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_16(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(None)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_17(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = None
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_18(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] / 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_19(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[1]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_20(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["XXvalueXX"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_21(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["VALUE"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_22(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1001.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_23(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 1.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_24(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = None
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_25(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] / 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_26(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[1]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_27(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["XXvalueXX"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_28(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["VALUE"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_29(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1001.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_30(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 1.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_31(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = None
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_32(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] / 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_33(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[1]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_34(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["XXvalueXX"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_35(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["VALUE"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_36(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1001.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_37(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 1.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_38(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = None
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_39(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(None) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_40(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = None
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_41(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(None) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_42(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[1]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_43(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["XXvalueXX"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_44(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["VALUE"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_45(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 1
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_46(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = None

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_47(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get(None) if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_48(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[1]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_49(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["XXlabelsXX"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_50(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["LABELS"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_51(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("XXdb_operationXX") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_52(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("DB_OPERATION") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_53(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=None,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_54(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=None,
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_55(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=None,
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_56(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=None,
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_57(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=None,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_58(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_59(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_60(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_61(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_62(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_63(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(None, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_64(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, None),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_65(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_66(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, ),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_67(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 3),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_68(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(None, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_69(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, None),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_70(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_71(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, ),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_72(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 3),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_73(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(None, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_74(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, None),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_75(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_76(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, ),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_77(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 3),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_78(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=None, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_79(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=None, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_80(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=None, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_81(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=None, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_82(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_83(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_84(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_85(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_86(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_87(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=1.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_88(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=1.0, max_ms=0.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_89(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=1.0, slowest_operation=None
                ),
                0,
            )

    def xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_90(
        self, request: BottleneckRequest, category: str, label_filter: str
    ) -> tuple[SpanBreakdown, int]:
        window = f"{request.time_window_minutes}m"
        avg_query = (
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        )
        p95_query = (
            f"histogram_quantile(0.95, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        max_query = (
            f"histogram_quantile(1.0, "
            f"rate(db_client_duration_seconds_bucket{{{label_filter}}}[{window}]))"
        )
        count_query = f"rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])"
        slowest_query = (
            f"topk(1, avg by (db_operation) ("
            f"rate(db_client_duration_seconds_sum{{{label_filter}}}[{window}]) "
            f"/ rate(db_client_duration_seconds_count{{{label_filter}}}[{window}])))"
        )

        try:
            avg_metrics = query_prometheus_instant(avg_query)
            p95_metrics = query_prometheus_instant(p95_query)
            max_metrics = query_prometheus_instant(max_query)
            count_metrics = query_prometheus_instant(count_query)
            slowest_metrics = query_prometheus_instant(slowest_query)

            avg_ms = (avg_metrics[0]["value"] * 1000.0) if avg_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            max_ms_raw = (max_metrics[0]["value"] * 1000.0) if max_metrics else 0.0
            max_ms = max_ms_raw if math.isfinite(max_ms_raw) else p95_ms
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0
            slowest_operation = (
                slowest_metrics[0]["labels"].get("db_operation") if slowest_metrics else None
            )

            return (
                SpanBreakdown(
                    category=category,
                    avg_ms=round(avg_ms, 2),
                    p95_ms=round(p95_ms, 2),
                    max_ms=round(max_ms, 2),
                    slowest_operation=slowest_operation,
                ),
                sample_count,
            )
        except Exception:
            return (
                SpanBreakdown(
                    category=category, avg_ms=0.0, p95_ms=0.0, max_ms=0.0, slowest_operation=None
                ),
                1,
            )

mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['_mutmut_orig'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_1'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_2'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_3'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_4'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_5'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_6'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_7'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_8'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_9'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_10'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_11'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_db_spans__mutmut_11 # type: ignore # mutmut generated

mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['_mutmut_orig'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_1'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_2'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_3'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_4'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_5'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_6'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_7'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_8'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_9'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_10'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_11'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_12'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut['xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_13'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁfetch_redis_spans__mutmut_13 # type: ignore # mutmut generated

mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['_mutmut_orig'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_1'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_2'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_3'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_4'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_5'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_6'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_7'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_8'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_9'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_10'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_11'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_12'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_13'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_14'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_15'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_16'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_17'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_18'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_19'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_20'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_21'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_22'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_23'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_24'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_25'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_26'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_27'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_28'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_29'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_30'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_31'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_32'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_33'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_34'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_35'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_36'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_37'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_38'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_39'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_40'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_41'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_42'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_43'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_43 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_44'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_44 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_45'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_45 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_46'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_46 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_47'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_47 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_48'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_48 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_49'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_49 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_50'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_50 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_51'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_51 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_52'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_52 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_53'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_53 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_54'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_54 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_55'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_55 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_56'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_56 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_57'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_57 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_58'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_58 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_59'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_59 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_60'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_60 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_61'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_61 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_62'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_62 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_63'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_63 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_64'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_64 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_65'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_65 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_66'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_66 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_67'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_67 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_68'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_68 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_69'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_69 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_70'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_70 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_71'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_71 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_72'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_72 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_73'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_73 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_74'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_74 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_75'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_75 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_76'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_76 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_77'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_77 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_78'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_78 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_79'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_79 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_80'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_80 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_81'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_81 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_82'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_82 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_83'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_83 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_84'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_84 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_85'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_85 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_86'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_86 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_87'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_87 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_88'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_88 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_89'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_89 # type: ignore # mutmut generated
mutants_xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut['xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_90'] = OTelSpanBreakdownAdapter.xǁOTelSpanBreakdownAdapterǁ_fetch_breakdown__mutmut_90 # type: ignore # mutmut generated
