from __future__ import annotations

from hexawyn.application.ports.driven.canary_comparison_port import CanaryComparisonPort
from hexawyn.domain.models.canary_comparison import CanaryComparisonRequest, VersionMetrics


class OTelCanaryComparisonAdapter(CanaryComparisonPort):
    def fetch_canary_metrics(self, request: CanaryComparisonRequest) -> VersionMetrics:
        return VersionMetrics(
            version="unknown",
            request_count=0,
            p50_ms=0.0,
            p95_ms=0.0,
            p99_ms=0.0,
            error_rate_pct=0.0,
        )

    def fetch_stable_metrics(self, request: CanaryComparisonRequest) -> VersionMetrics:
        return VersionMetrics(
            version="unknown",
            request_count=0,
            p50_ms=0.0,
            p95_ms=0.0,
            p99_ms=0.0,
            error_rate_pct=0.0,
        )
