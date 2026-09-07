import json
import os
from unittest.mock import patch

import pytest
from hexawyn.application.ports.driven.runtime_port import QuotaCheckResult
from hexawyn.infrastructure.config import quota_cache


@pytest.fixture
def cache_path(tmp_path):
    path = tmp_path / "quota.cache"
    with (
        patch.object(quota_cache, "QUOTA_CACHE_PATH", path),
        patch.dict(os.environ, {"HEXAWYN_DISABLE_ENCRYPTION": "true"}, clear=True),
    ):
        yield path


class TestQuotaCache:
    def test_load_returns_none_when_no_cache(self, cache_path):
        assert quota_cache.load_quota() is None

    def test_save_then_load_roundtrips(self, cache_path):
        quota_cache.save_quota(QuotaCheckResult(allowed=True, used=12, limit=50, remaining=38))
        result = quota_cache.load_quota()
        assert result == QuotaCheckResult(allowed=True, used=12, limit=50, remaining=38)

    def test_save_creates_file_with_restrictive_permissions(self, cache_path):
        quota_cache.save_quota(QuotaCheckResult(allowed=True, used=0, limit=50, remaining=50))
        assert cache_path.exists()
        assert cache_path.stat().st_mode & 0o777 == 0o600  # noqa: PLR2004

    def test_load_returns_none_on_corrupted_cache(self, cache_path):
        cache_path.write_text("not a valid cache", encoding="utf-8")
        assert quota_cache.load_quota() is None

    def test_load_returns_none_on_encrypted_cache_too_short(self, tmp_path):
        # Category: encrypted-corrupt error propagation. A ciphertext shorter
        # than nonce+ciphertext must not fabricate a quota — it degrades to None.
        path = tmp_path / "quota.cache"
        path.write_bytes(b"too-")  # < 13 bytes: nonce + ciphertext minimum
        with (
            patch.object(quota_cache, "QUOTA_CACHE_PATH", path),
            patch(
                "hexawyn.infrastructure.config.quota_cache.is_encryption_disabled",
                return_value=False,
            ),
            patch(
                "hexawyn.infrastructure.config.quota_cache.derive_key",
                return_value=b"k" * 32,
            ),
        ):
            assert quota_cache.load_quota() is None

    def test_load_ignores_missing_fields(self, cache_path):
        cache_path.write_text(
            json.dumps({"allowed": True, "used": 5}),
            encoding="utf-8",
        )
        assert quota_cache.load_quota() is None

    def test_clear_removes_cache(self, cache_path):
        quota_cache.save_quota(QuotaCheckResult(allowed=True, used=1, limit=50, remaining=49))
        quota_cache.clear_quota()
        assert quota_cache.load_quota() is None
