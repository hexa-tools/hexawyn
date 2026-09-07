"""Unit tests for parse_label_selector — PromQL-construction-style pure logic."""

from __future__ import annotations

import pytest
from hexawyn.domain.errors import LabelSelectorError
from hexawyn.domain.services.label_search.label_parser import parse_label_selector


class TestParseLabelSelector:
    def test_single_pair(self) -> None:
        assert parse_label_selector("app=payment") == [("app", "payment")]

    def test_multiple_pairs(self) -> None:
        pairs = parse_label_selector("app=payment,env=production")
        assert pairs == [("app", "payment"), ("env", "production")]

    def test_special_characters_in_value(self) -> None:
        """Edge case: version=1.2.3"""
        assert parse_label_selector("version=1.2.3") == [("version", "1.2.3")]

    def test_kubernetes_io_domain_prefixed_key(self) -> None:
        """Edge case: app.kubernetes.io/name=payment"""
        assert parse_label_selector("app.kubernetes.io/name=payment") == [
            ("app.kubernetes.io/name", "payment")
        ]

    def test_whitespace_around_pairs_is_trimmed(self) -> None:
        assert parse_label_selector("app=payment, env=production") == [
            ("app", "payment"),
            ("env", "production"),
        ]

    def test_missing_equals_sign_raises(self) -> None:
        with pytest.raises(LabelSelectorError):
            parse_label_selector("app")

    def test_empty_key_raises(self) -> None:
        with pytest.raises(LabelSelectorError):
            parse_label_selector("=payment")

    def test_empty_value_raises(self) -> None:
        with pytest.raises(LabelSelectorError):
            parse_label_selector("app=")

    def test_empty_selector_raises(self) -> None:
        with pytest.raises(LabelSelectorError):
            parse_label_selector("")
