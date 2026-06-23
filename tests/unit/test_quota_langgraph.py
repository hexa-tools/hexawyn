from unittest.mock import patch

import pytest
from hexawyn.domain.errors import QuotaExceededError
from hexawyn.domain.models.cluster import ClusterContext
from hexawyn.domain.models.investigation import InvestigationStatus
from hexawyn.domain.models.quota import (
    UNLIMITED,
    LicenseTier,
    UsageQuota,
    get_investigation_limit,
)
from hexawyn.lang_graph.typing.agent_state import AgentState


def _make_state() -> AgentState:
    return AgentState(
        query="why is payments-api crashing?",
        cluster_context=ClusterContext(name="prod-eu"),
        intent="",
        tool_name="",
        tool_args={},
        cache_hit=False,
        cached_result=None,
        tool_output={},
        llm_response="",
        retry_count=0,
        checker_result=None,
        judge_result=None,
        final_result=None,
        suggestions=[],
        status=InvestigationStatus.PENDING,
        error=None,
    )


class TestParseIntentQuota:
    def test_raises_quota_exceeded_when_limit_reached(self) -> None:
        with patch("os.environ", {"HEXAWYN_DEMO_MODE": "false"}):
            with patch(
                "hexawyn.lang_graph.nodes.parse_intent.check_quota",
                side_effect=QuotaExceededError(used=50, limit=50),
            ):
                import hexawyn.lang_graph.nodes.parse_intent as pi

                with pytest.raises(QuotaExceededError):
                    pi.run(_make_state())

    def test_does_not_check_quota_in_demo_mode(self) -> None:
        with patch("os.environ", {"HEXAWYN_DEMO_MODE": "true"}):
            with patch("hexawyn.lang_graph.nodes.parse_intent.check_quota") as mock_check:
                import hexawyn.lang_graph.nodes.parse_intent as pi

                pi.run(_make_state())
                mock_check.assert_not_called()

    def test_checks_quota_in_normal_mode(self) -> None:
        with patch("os.environ", {"HEXAWYN_DEMO_MODE": "false"}):
            with patch("hexawyn.lang_graph.nodes.parse_intent.check_quota") as mock_check:
                import hexawyn.lang_graph.nodes.parse_intent as pi

                pi.run(_make_state())
                mock_check.assert_called_once()


class TestQuotaInLangGraph:
    """Full chain: parse_intent → check_quota → _get_current_investigation_quota."""

    def test_free_tier_raises_at_50(self) -> None:
        limit = get_investigation_limit(LicenseTier.FREE)
        quota = UsageQuota(month="2026-06", count=limit, limit=limit)
        with patch("os.environ", {"HEXAWYN_DEMO_MODE": "false"}):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
                return_value=quota,
            ):
                import hexawyn.lang_graph.nodes.parse_intent as pi

                with pytest.raises(QuotaExceededError) as exc_info:
                    pi.run(_make_state())
                assert exc_info.value.used == limit

    def test_dev_tier_raises_at_200(self) -> None:
        limit = get_investigation_limit(LicenseTier.DEV)
        quota = UsageQuota(month="2026-06", count=limit, limit=limit)
        with patch("os.environ", {"HEXAWYN_DEMO_MODE": "false"}):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
                return_value=quota,
            ):
                import hexawyn.lang_graph.nodes.parse_intent as pi

                with pytest.raises(QuotaExceededError) as exc_info:
                    pi.run(_make_state())
                assert exc_info.value.limit == limit

    def test_startup_tier_raises_at_500(self) -> None:
        limit = get_investigation_limit(LicenseTier.STARTUP)
        quota = UsageQuota(month="2026-06", count=limit, limit=limit)
        with patch("os.environ", {"HEXAWYN_DEMO_MODE": "false"}):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
                return_value=quota,
            ):
                import hexawyn.lang_graph.nodes.parse_intent as pi

                with pytest.raises(QuotaExceededError) as exc_info:
                    pi.run(_make_state())
                assert exc_info.value.limit == limit

    def test_scale_up_never_raises(self) -> None:
        quota = UsageQuota(month="2026-06", count=99999, limit=UNLIMITED)
        with patch("os.environ", {"HEXAWYN_DEMO_MODE": "false"}):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
                return_value=quota,
            ):
                import hexawyn.lang_graph.nodes.parse_intent as pi

                pi.run(_make_state())

    def test_enterprise_never_raises(self) -> None:
        quota = UsageQuota(month="2026-06", count=99999, limit=UNLIMITED)
        with patch("os.environ", {"HEXAWYN_DEMO_MODE": "false"}):
            with patch(
                "hexawyn.infrastructure.config.quota_manager._get_current_investigation_quota",
                return_value=quota,
            ):
                import hexawyn.lang_graph.nodes.parse_intent as pi

                pi.run(_make_state())


class TestStoreMemoryQuota:
    def test_increments_quota_after_successful_investigation(self) -> None:
        with patch("os.environ", {"HEXAWYN_DEMO_MODE": "false"}):
            with patch("hexawyn.lang_graph.nodes.store_memory.increment_quota") as mock_inc:
                import hexawyn.lang_graph.nodes.store_memory as sm

                sm.run(_make_state())
                mock_inc.assert_called_once()

    def test_does_not_increment_quota_in_demo_mode(self) -> None:
        with patch("os.environ", {"HEXAWYN_DEMO_MODE": "true"}):
            with patch("hexawyn.lang_graph.nodes.store_memory.increment_quota") as mock_inc:
                import hexawyn.lang_graph.nodes.store_memory as sm

                sm.run(_make_state())
                mock_inc.assert_not_called()
