"""Unit tests for the AdaptiveLogProcessor."""

from hexawyn.domain.services.log_analysis.analyzer import AdaptiveLogProcessor


class TestAdaptiveLogProcessorConstruction:
    def test_default_budget(self) -> None:
        processor = AdaptiveLogProcessor()
        assert processor.max_token_budget == 150000  # noqa: PLR2004
        assert processor.get_remaining_budget() > 0

    def test_custom_budget(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=50000)
        assert processor.max_token_budget == 50000  # noqa: PLR2004


class TestAdaptiveLogProcessorBudget:
    def test_initial_usage_is_zero(self) -> None:
        processor = AdaptiveLogProcessor()
        assert processor.used_tokens == 0

    def test_effective_budget_is_80_percent_of_max(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        assert processor.get_remaining_budget() == 80000  # noqa: PLR2004

    def test_can_process_more_within_budget(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        assert processor.can_process_more(50000) is True

    def test_cannot_process_more_exceeding_budget(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        assert processor.can_process_more(90000) is False

    def test_can_process_more_at_boundary(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        assert processor.can_process_more(80000) is True
        assert processor.can_process_more(80001) is False


class TestAdaptiveLogProcessorUsage:
    def test_record_usage_updates_count(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        processor.record_usage(30000)
        assert processor.used_tokens == 30000  # noqa: PLR2004

    def test_record_usage_exceeding_budget_raises(self) -> None:
        import pytest

        processor = AdaptiveLogProcessor(max_token_budget=100000)
        with pytest.raises(ValueError, match="Token budget exceeded"):
            processor.record_usage(90000)

    def test_multiple_records_accumulate(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        processor.record_usage(10000)
        processor.record_usage(20000)
        assert processor.used_tokens == 30000  # noqa: PLR2004
        assert processor.get_remaining_budget() == 50000  # noqa: PLR2004


class TestAdaptiveLogProcessorReporting:
    def test_get_remaining_budget_decreases(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        initial = processor.get_remaining_budget()
        processor.record_usage(20000)
        after = processor.get_remaining_budget()
        assert after == initial - 20000

    def test_remaining_budget_never_negative(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        processor.record_usage(80000)
        assert processor.get_remaining_budget() == 0

    def test_usage_percentage_starts_zero(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        assert processor.get_usage_percentage() == 0.0

    def test_usage_percentage_after_recording(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        processor.record_usage(40000)
        assert processor.get_usage_percentage() == 50.0  # noqa: PLR2004

    def test_usage_percentage_capped_at_100(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        processor.record_usage(80000)
        assert processor.get_usage_percentage() == 100.0  # noqa: PLR2004

    def test_usage_ratio(self) -> None:
        processor = AdaptiveLogProcessor(max_token_budget=100000)
        processor.record_usage(40000)
        assert processor.get_usage_ratio() == 0.5  # noqa: PLR2004


class TestAdaptiveLogProcessorHelpers:
    def test_estimate_tokens_from_lines(self) -> None:
        processor = AdaptiveLogProcessor()
        lines = ["short line", "a slightly longer log line", "x"]
        estimated = processor.estimate_tokens_from_lines(lines)
        assert estimated > 0

    def test_estimate_tokens_empty_lines(self) -> None:
        processor = AdaptiveLogProcessor()
        assert processor.estimate_tokens_from_lines([]) == 0

    def test_prioritize_pods_returns_sorted(self) -> None:
        processor = AdaptiveLogProcessor()
        pods = [
            {"name": "healthy", "restart_count": 0, "status": "Running"},
            {"name": "failing", "restart_count": 5, "status": "CrashLoopBackOff"},
            {"name": "warning", "restart_count": 1, "status": "Running"},
        ]
        prioritized = processor.prioritize_pods(pods)
        assert len(prioritized) == 3  # noqa: PLR2004
        assert prioritized[0]["name"] == "failing"

    def test_prioritize_pods_failed_first(self) -> None:
        processor = AdaptiveLogProcessor()
        pods = [
            {"name": "ok", "restart_count": 0, "status": "Running"},
            {"name": "broken", "restart_count": 0, "status": "Error"},
        ]
        prioritized = processor.prioritize_pods(pods)
        assert prioritized[0]["name"] == "broken"
