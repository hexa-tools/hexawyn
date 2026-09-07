"""Unit tests for is_unused / deduplicate_references — the ticket's
explicitly-named "usage mapping" domain logic. Test Scenario 4: a secret
referenced by nothing is stale AND unused, safe to delete."""

from __future__ import annotations


class TestIsUnused:
    def test_tc4_empty_references_is_unused(self) -> None:
        from hexawyn.domain.services.secret_rotation.usage_mapper import is_unused

        assert is_unused([]) is True

    def test_referenced_secret_is_not_unused(self) -> None:
        from hexawyn.domain.services.secret_rotation.usage_mapper import is_unused

        assert is_unused(["payment-deploy"]) is False


class TestDeduplicateReferences:
    def test_removes_duplicate_workload_names(self) -> None:
        from hexawyn.domain.services.secret_rotation.usage_mapper import deduplicate_references

        result = deduplicate_references(["payment-deploy", "payment-deploy", "checkout-deploy"])

        assert result == ["checkout-deploy", "payment-deploy"]

    def test_empty_list_returns_empty(self) -> None:
        from hexawyn.domain.services.secret_rotation.usage_mapper import deduplicate_references

        assert deduplicate_references([]) == []
