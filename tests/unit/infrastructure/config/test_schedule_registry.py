"""Tests for schedule_registry.py — build_registry and helper functions."""

from __future__ import annotations

from unittest.mock import patch

from hexawyn.infrastructure.config.schedule_registry import (
    _certs_list,
    _global_health,
    build_registry,
)


class TestBuildRegistry:
    """Cover build_registry and helper functions (lines 5-7, 11-13)."""

    def test_registry_has_two_keys(self) -> None:
        registry = build_registry()
        assert set(registry.keys()) == {"certs_list", "global_health_check"}

    def test_registry_values_are_callable(self) -> None:
        registry = build_registry()
        for key, func in registry.items():
            assert callable(func)

    def test_certs_list_calls_check_certificate_health(self) -> None:
        with patch(
            "hexawyn.mcp.tools.check_cluster_certificate_health.check_cluster_certificate_health",
            return_value={"status": "ok"},
        ) as mock_func:
            result = _certs_list({})
            mock_func.assert_called_once()
            assert result == {"status": "ok"}

    def test_global_health_calls_global_health_check(self) -> None:
        with patch(
            "hexawyn.mcp.tools.global_health_check.global_health_check",
            return_value={"health": "good"},
        ) as mock_func:
            result = _global_health({})
            mock_func.assert_called_once()
            assert result == {"health": "good"}

    def test_certs_list_ignores_params(self) -> None:
        with patch(
            "hexawyn.mcp.tools.check_cluster_certificate_health.check_cluster_certificate_health",
            return_value={"status": "ok"},
        ):
            result1 = _certs_list({})
            result2 = _certs_list({"namespace": "ignored"})
            assert result1 == result2

    def test_build_registry_is_idempotent(self) -> None:
        reg1 = build_registry()
        reg2 = build_registry()
        assert reg1.keys() == reg2.keys()
        assert reg1["certs_list"] is reg2["certs_list"]
        assert reg1["global_health_check"] is reg2["global_health_check"]
