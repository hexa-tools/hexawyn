"""Unit tests for estimate_tokens / format_overview_summary / enforce_token_budget."""

from __future__ import annotations

from hexawyn.domain.models.namespace_overview import (
    NamespaceCounts,
    NamespaceHealthStatus,
    UnhealthyResource,
)
from hexawyn.domain.services.namespace_overview.token_budget import (
    enforce_token_budget,
    estimate_tokens,
    format_overview_summary,
)

_COUNTS = NamespaceCounts(
    pods_total=12,
    pods_running=9,
    pods_failed=3,
    deployments_total=4,
    deployments_ready=3,
    services_total=5,
)


class TestEstimateTokens:
    def test_longer_text_estimates_more_tokens(self) -> None:
        short = estimate_tokens("short text")
        long = estimate_tokens("this is a much longer piece of text than the short one")
        assert long > short

    def test_empty_text_estimates_at_least_one(self) -> None:
        assert estimate_tokens("") >= 1


class TestFormatOverviewSummary:
    def test_includes_core_fields(self) -> None:
        summary = format_overview_summary(
            namespace="staging",
            namespace_status="Active",
            counts=_COUNTS,
            health_status=NamespaceHealthStatus.DEGRADED,
            root_cause="checkout-pod-abc: CrashLoopBackOff",
            unhealthy_resources=[
                UnhealthyResource(name="checkout-pod-abc", kind="Pod", reason="CrashLoopBackOff")
            ],
            warnings=[],
        )

        assert "staging" in summary
        assert "Degraded" in summary
        assert "checkout-pod-abc" in summary


class TestEnforceTokenBudget:
    def test_small_list_fits_without_truncation(self) -> None:
        resources = [UnhealthyResource(name="pod-a", kind="Pod", reason="CrashLoopBackOff")]

        trimmed, has_more, remaining, tokens = enforce_token_budget(
            namespace="staging",
            namespace_status="Active",
            counts=_COUNTS,
            health_status=NamespaceHealthStatus.DEGRADED,
            root_cause="pod-a: CrashLoopBackOff",
            unhealthy_resources=resources,
            warnings=[],
            max_tokens=2000,
        )

        assert trimmed == resources
        assert has_more is False
        assert remaining == 0
        assert tokens <= 2000  # noqa: PLR2004

    def test_large_list_truncated_under_tight_budget(self) -> None:
        """TC4: namespace with 200 resources → output stays under token budget."""
        resources = [
            UnhealthyResource(name=f"pod-{i}", kind="Pod", reason="CrashLoopBackOff")
            for i in range(200)
        ]

        trimmed, has_more, remaining, tokens = enforce_token_budget(
            namespace="staging",
            namespace_status="Active",
            counts=_COUNTS,
            health_status=NamespaceHealthStatus.DEGRADED,
            root_cause="pod-0: CrashLoopBackOff (+199 more issue(s))",
            unhealthy_resources=resources,
            warnings=[],
            max_tokens=200,
        )

        assert tokens <= 200  # noqa: PLR2004
        assert has_more is True
        assert remaining == 200 - len(trimmed)
        assert len(trimmed) < 200  # noqa: PLR2004
