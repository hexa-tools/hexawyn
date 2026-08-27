"""HTTP token validator against the Control Plane.

Sends ``Authorization: Bearer <token>`` to the Cloud quota-check endpoint and
maps the response to a TokenValidationResult:

- 2xx            -> VALID
- 401/403        -> INVALID
- timeout/5xx/err -> UNAVAILABLE

The token is never placed in the URL and never logged.
"""

from __future__ import annotations

import httpx
from hexawyn.domain.models.auth import TokenValidationResult, TokenValidationState

VALIDATE_PATH = "/api/v1/quota/check"
_HTTP_2XX_RANGE = (200, 300)
_HTTP_INVALID_STATUSES = frozenset({401, 403})


class HttpTokenValidator:
    """Validates a cloud token using the Control Plane quota-check endpoint."""

    def __init__(self, client: httpx.Client, base_url: str, timeout: float = 10.0) -> None:
        self._client = client
        self._validate_url = f"{base_url.rstrip('/')}{VALIDATE_PATH}"
        self._timeout = timeout

    def validate_token(self, token: str) -> TokenValidationResult:
        headers = {"Authorization": f"Bearer {token}"}
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")
