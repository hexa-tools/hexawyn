"""Unit tests for is_noise — health-check/informational noise classifier."""

from __future__ import annotations

from hexawyn.domain.services.log_analysis.noise_filter import is_noise


class TestIsNoiseHealthCheckEndpoints:
    def test_health_endpoint_is_noise(self) -> None:
        assert is_noise("GET /health HTTP/1.1 200") is True

    def test_healthz_endpoint_is_noise(self) -> None:
        assert is_noise("GET /healthz HTTP/1.1 200") is True

    def test_readyz_endpoint_is_noise(self) -> None:
        assert is_noise("GET /readyz HTTP/1.1 200") is True

    def test_livez_endpoint_is_noise(self) -> None:
        assert is_noise("GET /livez HTTP/1.1 200") is True

    def test_probe_messages_are_noise(self) -> None:
        assert is_noise("readiness probe succeeded") is True
        assert is_noise("liveness probe succeeded") is True

    def test_case_insensitive(self) -> None:
        assert is_noise("get /health http/1.1 200") is True


class TestIsNoiseMeaningfulLines:
    def test_error_line_is_not_noise(self) -> None:
        assert is_noise("Error: connection refused") is False

    def test_oom_line_is_not_noise(self) -> None:
        assert is_noise("OOMKilled: memory limit exceeded") is False

    def test_business_request_is_not_noise(self) -> None:
        assert is_noise("POST /api/orders HTTP/1.1 201") is False
