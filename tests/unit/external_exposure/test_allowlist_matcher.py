"""Unit tests for is_allowlisted — Checker case 1: an allowlisted service
must never be flagged, so this check must be exact and reliable."""

from __future__ import annotations


class TestIsAllowlisted:
    def test_tc2_allowlisted_service_matches(self) -> None:
        from hexawyn.domain.services.external_exposure.allowlist_matcher import is_allowlisted

        assert is_allowlisted("api-gateway", ("api-gateway", "ingress-nginx-controller")) is True

    def test_service_not_in_allowlist_does_not_match(self) -> None:
        from hexawyn.domain.services.external_exposure.allowlist_matcher import is_allowlisted

        assert is_allowlisted("postgres-svc", ("api-gateway", "ingress-nginx-controller")) is False

    def test_empty_allowlist_never_matches(self) -> None:
        from hexawyn.domain.services.external_exposure.allowlist_matcher import is_allowlisted

        assert is_allowlisted("api-gateway", ()) is False
