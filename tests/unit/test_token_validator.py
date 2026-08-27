"""Unit tests for the HTTP token validator (Control Plane gateway)."""

from __future__ import annotations

from collections.abc import Callable
from unittest.mock import patch

import httpx
from hexawyn.adapters.secondary.auth.token_validator import HttpTokenValidator
from hexawyn.domain.models.auth import TokenValidationState

BASE_URL = "http://control-plane.test"
VALIDATE_PATH = "/api/v1/auth/validate"
MACHINE_ID = "machine-abc-123"


def _client(handler: Callable[[httpx.Request], httpx.Response]) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler))


def _patch_machine_id() -> object:
    return patch("hexawyn.infrastructure.config.machine_id.get_machine_id", return_value=MACHINE_ID)


class TestTokenValidator:
    def test_2xx_is_valid(self) -> None:
        with _patch_machine_id():
            client = _client(lambda _r: httpx.Response(200, json={"valid": True}))
            result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.VALID
        assert result.is_valid is True

    def test_401_is_invalid(self) -> None:
        with _patch_machine_id():
            client = _client(lambda _r: httpx.Response(401, json={}))
            result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.INVALID

    def test_403_is_invalid(self) -> None:
        with _patch_machine_id():
            client = _client(lambda _r: httpx.Response(403, json={}))
            result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.INVALID

    def test_5xx_is_unavailable(self) -> None:
        with _patch_machine_id():
            client = _client(lambda _r: httpx.Response(500, json={}))
            result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.UNAVAILABLE

    def test_404_is_unavailable_not_invalid(self) -> None:
        with _patch_machine_id():
            client = _client(lambda _r: httpx.Response(404, json={}))
            result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.UNAVAILABLE

    def test_204_is_valid(self) -> None:
        with _patch_machine_id():
            client = _client(lambda _r: httpx.Response(204))
            result = HttpTokenValidator(client, BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.VALID

    def test_timeout_is_unavailable(self) -> None:
        def _raise(_request: httpx.Request) -> httpx.Response:
            raise httpx.TimeoutException("timed out")

        with _patch_machine_id():
            result = HttpTokenValidator(_client(_raise), BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.UNAVAILABLE

    def test_connection_error_is_unavailable(self) -> None:
        def _raise(_request: httpx.Request) -> httpx.Response:
            raise httpx.ConnectError("connection refused")

        with _patch_machine_id():
            result = HttpTokenValidator(_client(_raise), BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.UNAVAILABLE

    def test_xapi_key_and_machine_id_headers(self) -> None:
        captured: dict[str, str] = {}

        def _handler(request: httpx.Request) -> httpx.Response:
            captured["x_api_key"] = request.headers.get("X-API-Key", "")
            captured["x_machine_id"] = request.headers.get("X-Machine-ID", "")
            captured["url"] = str(request.url)
            return httpx.Response(200)

        with _patch_machine_id():
            HttpTokenValidator(_client(_handler), BASE_URL).validate_token("hxw_secret")

        assert captured["x_api_key"] == "hxw_secret"
        assert captured["x_machine_id"] == MACHINE_ID
        assert captured["url"] == f"{BASE_URL}{VALIDATE_PATH}"

    def test_token_not_in_url(self) -> None:
        captured: dict[str, str] = {}

        def _handler(request: httpx.Request) -> httpx.Response:
            captured["url"] = str(request.url)
            return httpx.Response(200)

        with _patch_machine_id():
            HttpTokenValidator(_client(_handler), BASE_URL).validate_token("hxw_supersecret")

        assert "hxw_supersecret" not in captured["url"]

    def test_machine_id_failure_still_validates(self) -> None:
        def _handler(request: httpx.Request) -> httpx.Response:
            assert request.headers.get("X-Machine-ID") is None
            assert request.headers.get("X-API-Key") == "hxw_x"
            return httpx.Response(200)

        with patch(
            "hexawyn.infrastructure.config.machine_id.get_machine_id",
            side_effect=OSError("no machine id"),
        ):
            result = HttpTokenValidator(_client(_handler), BASE_URL).validate_token("hxw_x")
        assert result.state == TokenValidationState.VALID
