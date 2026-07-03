"""Unit tests for should_keep_line — bounds memory for high-volume watch sessions."""

from __future__ import annotations

from hexawyn.domain.services.log_analysis.line_sampler import should_keep_line


class TestShouldKeepLine:
    def test_first_line_always_kept(self) -> None:
        assert should_keep_line(0, sample_rate=100) is True

    def test_line_at_sample_boundary_kept(self) -> None:
        assert should_keep_line(100, sample_rate=100) is True

    def test_line_between_boundaries_dropped(self) -> None:
        assert should_keep_line(1, sample_rate=100) is False
        assert should_keep_line(99, sample_rate=100) is False

    def test_sample_rate_one_keeps_everything(self) -> None:
        assert all(should_keep_line(i, sample_rate=1) for i in range(50))

    def test_high_volume_bounds_kept_count(self) -> None:
        """Edge case: 10000 lines/second -> sampling bounds what's retained."""
        kept = sum(should_keep_line(i, sample_rate=100) for i in range(50000))
        assert kept == 500
