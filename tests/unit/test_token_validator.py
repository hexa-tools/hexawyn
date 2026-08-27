"""Unit tests for the HTTP token validator."""

from __future__ import annotations

from collections.abc import Callable

import httpx
from hexawyn.adapters.secondary.auth.token_validator import HttpTokenValidator
from hexawyn.domain.models.auth import TokenValidationState

BASE_URL = "http://cloud.test"
VALIDATE_PATH = "/api/v1/quota/check"


def _client(handler: Callable[[httpx.Request], httpx.Response]) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler))


class TestTokenValidator:
    def test_2xx_is_valid(self) -> None:
        client = _client(lambda _r: httpx.Response(200, json={"allowed": True}))
        result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.VALID
        assert result.is_valid is True

    def test_401_is_invalid(self) -> None:
        client = _client(lambda _r: httpx.Response(401, json={}))
        result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.INVALID

    def test_403_is_invalid(self) -> None:
        client = _client(lambda _r: httpx.Response(403, json={}))
        result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.INVALID

    def test_5xx_is_unavailable(self) -> None:
        client = _client(lambda _r: httpx.Response(500, json={}))
        result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.UNAVAILABLE

    def test_404_is_unavailable_not_invalid(self) -> None:
        client = _client(lambda _r: httpx.Response(404, json={}))
        result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.UNAVAILABLE

    def test_204_is_valid(self) -> None:
        client = _client(lambda _r: httpx.Response(204))
        result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.VALID

    def test_timeout_is_unavailable(self) -> None:
        def _raise(_request: httpx.Request) -> httpx.Response:
            raise httpx.TimeoutException("timed out")

        result = HttpTokenValidator(_client(_raise), BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.UNAVAILABLE

    def test_connection_error_is_unavailable(self) -> None:
        def _raise(_request: httpx.Request) -> httpx.Response:
            raise httpx.ConnectError("connection refused")

        result = HttpTokenValidator(_client(_raise), BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.UNAVAILABLE

    def test_bearer_header_is_correct(self) -> None:
        captured: dict[str, str] = {}

        def _handler(request: httpx.Request) -> httpx.Response:
            captured["auth"] = request.headers.get("Authorization", "")
            captured["url"] = str(request.url)
            return httpx.Response(200)

        HttpTokenValidator(_client(_handler), BASE_URL).validate_token("hxw_secret")
        assert captured["auth"] == "Bearer hxw_secret"
        assert captured["url"] == f"{BASE_URL}{VALIDATE_PATH}"

    def test_token_not_in_url(self) -> None:
        captured: dict[str, str] = {}

        def _handler(request: httpx.Request) -> httpx.Response:
            captured["url"] = str(request.url)
            return httpx.Response(200)

        HttpTokenValidator(_client(_handler), BASE_URL).validate_token("hxw_supersecret")
        assert "hxw_supersecret" not in captured["url"]
