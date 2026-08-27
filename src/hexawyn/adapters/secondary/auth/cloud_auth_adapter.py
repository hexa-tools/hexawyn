"""Composite CloudAuthPort adapter.

Wires the HTTP token validator and the config-backed token store into a
single CloudAuthPort implementation.
"""

from __future__ import annotations

from hexawyn.adapters.secondary.auth.config_token_store import ConfigTokenStore
from hexawyn.adapters.secondary.auth.token_validator import HttpTokenValidator
from hexawyn.application.ports.driven.cloud_auth_port import CloudAuthPort
from hexawyn.domain.models.auth import TokenValidationResult


class CloudAuthAdapter(CloudAuthPort):
    """Satisfies CloudAuthPort by delegating to validator + store."""

    def __init__(self, validator: HttpTokenValidator, store: ConfigTokenStore) -> None:
        self._validator = validator
        self._store = store

    def validate_token(self, token: str) -> TokenValidationResult:
        return self._validator.validate_token(token)

    def get_token(self) -> str | None:
        return self._store.get_token()

    def save_token(self, token: str) -> None:
        self._store.save_token(token)
