import pytest
from hexawyn.domain.errors import HexawynError, QuotaExceededError, SlackQuotaExceededError


class TestQuotaExceededError:
    def test_inherits_from_hexawyn_error(self):
        assert issubclass(QuotaExceededError, HexawynError)

    def test_includes_usage_info(self):
        err = QuotaExceededError(used=50, limit=50)
        assert "50" in str(err)

    def test_includes_upgrade_url(self):
        err = QuotaExceededError(used=50, limit=50)
        assert "hexawyn.com/pricing" in str(err)

    def test_includes_reset_info(self):
        err = QuotaExceededError(used=50, limit=50)
        assert "reset" in str(err).lower()

    def test_stores_used_and_limit(self):
        err = QuotaExceededError(used=23, limit=50)
        assert err.used == 23  # noqa: PLR2004
        assert err.limit == 50  # noqa: PLR2004

    def test_can_be_caught_as_hexawyn_error(self):
        with pytest.raises(HexawynError):
            raise QuotaExceededError(used=50, limit=50)


class TestSlackQuotaExceededError:
    def test_inherits_from_hexawyn_error(self):
        assert issubclass(SlackQuotaExceededError, HexawynError)

    def test_stores_used_and_limit(self):
        err = SlackQuotaExceededError(used=3, limit=5)
        assert err.used == 3  # noqa: PLR2004
        assert err.limit == 5  # noqa: PLR2004

    def test_includes_slack_context(self):
        err = SlackQuotaExceededError(used=5, limit=5)
        assert "5" in str(err)
        assert "hexawyn.com" in str(err)

    def test_can_be_caught_as_hexawyn_error(self):
        with pytest.raises(HexawynError):
            raise SlackQuotaExceededError(used=5, limit=5)
