"""HTTP token validator against the Control Plane.

Sends ``X-API-Key`` (and ``X-Machine-ID``) to the Control Plane /auth/validate
endpoint and maps the response to a TokenValidationResult:

- 2xx            -> VALID
- 401/403        -> INVALID
- timeout/5xx/err -> UNAVAILABLE

The token is never placed in the URL and never logged.
"""

from __future__ import annotations

import httpx
from hexawyn.domain.models.auth import TokenValidationResult, TokenValidationState

VALIDATE_PATH = "/api/v1/auth/validate"
_HTTP_2XX_RANGE = (200, 300)
_HTTP_INVALID_STATUSES = frozenset({401, 403})


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁHttpTokenValidatorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut: MutantDict = {}  # type: ignore


class HttpTokenValidator:
    """Validates a cloud token via the Control Plane (Gateway) endpoint."""

    @_mutmut_mutated(mutants_xǁHttpTokenValidatorǁ__init____mutmut)
    def __init__(self, client: httpx.Client, base_url: str, timeout: float = 10.0) -> None:
        self._client = client
        self._validate_url = f"{base_url.rstrip('/')}{VALIDATE_PATH}"
        self._timeout = timeout

    def xǁHttpTokenValidatorǁ__init____mutmut_orig(self, client: httpx.Client, base_url: str, timeout: float = 10.0) -> None:
        self._client = client
        self._validate_url = f"{base_url.rstrip('/')}{VALIDATE_PATH}"
        self._timeout = timeout

    def xǁHttpTokenValidatorǁ__init____mutmut_1(self, client: httpx.Client, base_url: str, timeout: float = 11.0) -> None:
        self._client = client
        self._validate_url = f"{base_url.rstrip('/')}{VALIDATE_PATH}"
        self._timeout = timeout

    def xǁHttpTokenValidatorǁ__init____mutmut_2(self, client: httpx.Client, base_url: str, timeout: float = 10.0) -> None:
        self._client = None
        self._validate_url = f"{base_url.rstrip('/')}{VALIDATE_PATH}"
        self._timeout = timeout

    def xǁHttpTokenValidatorǁ__init____mutmut_3(self, client: httpx.Client, base_url: str, timeout: float = 10.0) -> None:
        self._client = client
        self._validate_url = None
        self._timeout = timeout

    def xǁHttpTokenValidatorǁ__init____mutmut_4(self, client: httpx.Client, base_url: str, timeout: float = 10.0) -> None:
        self._client = client
        self._validate_url = f"{base_url.rstrip(None)}{VALIDATE_PATH}"
        self._timeout = timeout

    def xǁHttpTokenValidatorǁ__init____mutmut_5(self, client: httpx.Client, base_url: str, timeout: float = 10.0) -> None:
        self._client = client
        self._validate_url = f"{base_url.lstrip('/')}{VALIDATE_PATH}"
        self._timeout = timeout

    def xǁHttpTokenValidatorǁ__init____mutmut_6(self, client: httpx.Client, base_url: str, timeout: float = 10.0) -> None:
        self._client = client
        self._validate_url = f"{base_url.rstrip('XX/XX')}{VALIDATE_PATH}"
        self._timeout = timeout

    def xǁHttpTokenValidatorǁ__init____mutmut_7(self, client: httpx.Client, base_url: str, timeout: float = 10.0) -> None:
        self._client = client
        self._validate_url = f"{base_url.rstrip('/')}{VALIDATE_PATH}"
        self._timeout = None

    @_mutmut_mutated(mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut)
    def validate_token(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
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

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_orig(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
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

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_1(self, token: str) -> TokenValidationResult:
        headers = None
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

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_2(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(None)
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

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_3(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = None
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_4(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(None, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_5(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=None, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_6(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=None)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_7(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_8(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_9(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, )
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_10(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(None, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_11(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, None)
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_12(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult("timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_13(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, )
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_14(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "XXtimeoutXX")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_15(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "TIMEOUT")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_16(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(None, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_17(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, None)

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_18(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult("connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_19(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, )

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_20(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "XXconnection_errorXX")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_21(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "CONNECTION_ERROR")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_22(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[1] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_23(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] < response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_24(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code <= _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_25(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[2]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_26(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(None)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_27(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code not in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(TokenValidationState.INVALID)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_28(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
        try:
            response = self._client.get(self._validate_url, headers=headers, timeout=self._timeout)
        except httpx.TimeoutException:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "timeout")
        except httpx.HTTPError:
            return TokenValidationResult(TokenValidationState.UNAVAILABLE, "connection_error")

        if _HTTP_2XX_RANGE[0] <= response.status_code < _HTTP_2XX_RANGE[1]:
            return TokenValidationResult(TokenValidationState.VALID)
        if response.status_code in _HTTP_INVALID_STATUSES:
            return TokenValidationResult(None)
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_29(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
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
        return TokenValidationResult(None, "server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_30(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
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
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, None)

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_31(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
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
        return TokenValidationResult("server_error")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_32(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
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
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, )

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_33(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
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
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "XXserver_errorXX")

    def xǁHttpTokenValidatorǁvalidate_token__mutmut_34(self, token: str) -> TokenValidationResult:
        headers = self._build_headers(token)
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
        return TokenValidationResult(TokenValidationState.UNAVAILABLE, "SERVER_ERROR")

    @_mutmut_mutated(mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut)
    def _build_headers(self, token: str) -> dict[str, str]:
        headers = {"X-API-Key": token}
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        return headers

    def xǁHttpTokenValidatorǁ_build_headers__mutmut_orig(self, token: str) -> dict[str, str]:
        headers = {"X-API-Key": token}
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        return headers

    def xǁHttpTokenValidatorǁ_build_headers__mutmut_1(self, token: str) -> dict[str, str]:
        headers = None
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        return headers

    def xǁHttpTokenValidatorǁ_build_headers__mutmut_2(self, token: str) -> dict[str, str]:
        headers = {"XXX-API-KeyXX": token}
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        return headers

    def xǁHttpTokenValidatorǁ_build_headers__mutmut_3(self, token: str) -> dict[str, str]:
        headers = {"x-api-key": token}
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        return headers

    def xǁHttpTokenValidatorǁ_build_headers__mutmut_4(self, token: str) -> dict[str, str]:
        headers = {"X-API-KEY": token}
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        return headers

    def xǁHttpTokenValidatorǁ_build_headers__mutmut_5(self, token: str) -> dict[str, str]:
        headers = {"X-API-Key": token}
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            headers["X-Machine-ID"] = None
        except Exception:
            pass
        return headers

    def xǁHttpTokenValidatorǁ_build_headers__mutmut_6(self, token: str) -> dict[str, str]:
        headers = {"X-API-Key": token}
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            headers["XXX-Machine-IDXX"] = get_machine_id()
        except Exception:
            pass
        return headers

    def xǁHttpTokenValidatorǁ_build_headers__mutmut_7(self, token: str) -> dict[str, str]:
        headers = {"X-API-Key": token}
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            headers["x-machine-id"] = get_machine_id()
        except Exception:
            pass
        return headers

    def xǁHttpTokenValidatorǁ_build_headers__mutmut_8(self, token: str) -> dict[str, str]:
        headers = {"X-API-Key": token}
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            headers["X-MACHINE-ID"] = get_machine_id()
        except Exception:
            pass
        return headers

mutants_xǁHttpTokenValidatorǁ__init____mutmut['_mutmut_orig'] = HttpTokenValidator.xǁHttpTokenValidatorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ__init____mutmut['xǁHttpTokenValidatorǁ__init____mutmut_1'] = HttpTokenValidator.xǁHttpTokenValidatorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ__init____mutmut['xǁHttpTokenValidatorǁ__init____mutmut_2'] = HttpTokenValidator.xǁHttpTokenValidatorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ__init____mutmut['xǁHttpTokenValidatorǁ__init____mutmut_3'] = HttpTokenValidator.xǁHttpTokenValidatorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ__init____mutmut['xǁHttpTokenValidatorǁ__init____mutmut_4'] = HttpTokenValidator.xǁHttpTokenValidatorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ__init____mutmut['xǁHttpTokenValidatorǁ__init____mutmut_5'] = HttpTokenValidator.xǁHttpTokenValidatorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ__init____mutmut['xǁHttpTokenValidatorǁ__init____mutmut_6'] = HttpTokenValidator.xǁHttpTokenValidatorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ__init____mutmut['xǁHttpTokenValidatorǁ__init____mutmut_7'] = HttpTokenValidator.xǁHttpTokenValidatorǁ__init____mutmut_7 # type: ignore # mutmut generated

mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['_mutmut_orig'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_1'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_2'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_3'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_4'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_5'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_6'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_7'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_8'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_9'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_10'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_11'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_12'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_13'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_14'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_15'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_16'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_17'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_18'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_19'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_20'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_21'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_22'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_23'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_24'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_25'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_26'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_27'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_28'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_29'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_30'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_31'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_31 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_32'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_32 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_33'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_33 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁvalidate_token__mutmut['xǁHttpTokenValidatorǁvalidate_token__mutmut_34'] = HttpTokenValidator.xǁHttpTokenValidatorǁvalidate_token__mutmut_34 # type: ignore # mutmut generated

mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut['_mutmut_orig'] = HttpTokenValidator.xǁHttpTokenValidatorǁ_build_headers__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut['xǁHttpTokenValidatorǁ_build_headers__mutmut_1'] = HttpTokenValidator.xǁHttpTokenValidatorǁ_build_headers__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut['xǁHttpTokenValidatorǁ_build_headers__mutmut_2'] = HttpTokenValidator.xǁHttpTokenValidatorǁ_build_headers__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut['xǁHttpTokenValidatorǁ_build_headers__mutmut_3'] = HttpTokenValidator.xǁHttpTokenValidatorǁ_build_headers__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut['xǁHttpTokenValidatorǁ_build_headers__mutmut_4'] = HttpTokenValidator.xǁHttpTokenValidatorǁ_build_headers__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut['xǁHttpTokenValidatorǁ_build_headers__mutmut_5'] = HttpTokenValidator.xǁHttpTokenValidatorǁ_build_headers__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut['xǁHttpTokenValidatorǁ_build_headers__mutmut_6'] = HttpTokenValidator.xǁHttpTokenValidatorǁ_build_headers__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut['xǁHttpTokenValidatorǁ_build_headers__mutmut_7'] = HttpTokenValidator.xǁHttpTokenValidatorǁ_build_headers__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHttpTokenValidatorǁ_build_headers__mutmut['xǁHttpTokenValidatorǁ_build_headers__mutmut_8'] = HttpTokenValidator.xǁHttpTokenValidatorǁ_build_headers__mutmut_8 # type: ignore # mutmut generated
