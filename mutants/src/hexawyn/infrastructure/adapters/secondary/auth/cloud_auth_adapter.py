"""Composite CloudAuthPort adapter.

Wires the HTTP token validator and the config-backed token store into a
single CloudAuthPort implementation.
"""

from __future__ import annotations

from hexawyn.application.ports.driven.cloud_auth_port import CloudAuthPort
from hexawyn.domain.models.auth import TokenValidationResult
from hexawyn.infrastructure.adapters.secondary.auth.config_token_store import ConfigTokenStore
from hexawyn.infrastructure.adapters.secondary.auth.token_validator import HttpTokenValidator


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCloudAuthAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCloudAuthAdapterǁvalidate_token__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCloudAuthAdapterǁsave_token__mutmut: MutantDict = {}  # type: ignore


class CloudAuthAdapter(CloudAuthPort):
    """Satisfies CloudAuthPort by delegating to validator + store."""

    @_mutmut_mutated(mutants_xǁCloudAuthAdapterǁ__init____mutmut)
    def __init__(self, validator: HttpTokenValidator, store: ConfigTokenStore) -> None:
        self._validator = validator
        self._store = store

    def xǁCloudAuthAdapterǁ__init____mutmut_orig(self, validator: HttpTokenValidator, store: ConfigTokenStore) -> None:
        self._validator = validator
        self._store = store

    def xǁCloudAuthAdapterǁ__init____mutmut_1(self, validator: HttpTokenValidator, store: ConfigTokenStore) -> None:
        self._validator = None
        self._store = store

    def xǁCloudAuthAdapterǁ__init____mutmut_2(self, validator: HttpTokenValidator, store: ConfigTokenStore) -> None:
        self._validator = validator
        self._store = None

    @_mutmut_mutated(mutants_xǁCloudAuthAdapterǁvalidate_token__mutmut)
    def validate_token(self, token: str) -> TokenValidationResult:
        return self._validator.validate_token(token)

    def xǁCloudAuthAdapterǁvalidate_token__mutmut_orig(self, token: str) -> TokenValidationResult:
        return self._validator.validate_token(token)

    def xǁCloudAuthAdapterǁvalidate_token__mutmut_1(self, token: str) -> TokenValidationResult:
        return self._validator.validate_token(None)

    def get_token(self) -> str | None:
        return self._store.get_token()

    @_mutmut_mutated(mutants_xǁCloudAuthAdapterǁsave_token__mutmut)
    def save_token(self, token: str) -> None:
        self._store.save_token(token)

    def xǁCloudAuthAdapterǁsave_token__mutmut_orig(self, token: str) -> None:
        self._store.save_token(token)

    def xǁCloudAuthAdapterǁsave_token__mutmut_1(self, token: str) -> None:
        self._store.save_token(None)

mutants_xǁCloudAuthAdapterǁ__init____mutmut['_mutmut_orig'] = CloudAuthAdapter.xǁCloudAuthAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCloudAuthAdapterǁ__init____mutmut['xǁCloudAuthAdapterǁ__init____mutmut_1'] = CloudAuthAdapter.xǁCloudAuthAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCloudAuthAdapterǁ__init____mutmut['xǁCloudAuthAdapterǁ__init____mutmut_2'] = CloudAuthAdapter.xǁCloudAuthAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁCloudAuthAdapterǁvalidate_token__mutmut['_mutmut_orig'] = CloudAuthAdapter.xǁCloudAuthAdapterǁvalidate_token__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCloudAuthAdapterǁvalidate_token__mutmut['xǁCloudAuthAdapterǁvalidate_token__mutmut_1'] = CloudAuthAdapter.xǁCloudAuthAdapterǁvalidate_token__mutmut_1 # type: ignore # mutmut generated

mutants_xǁCloudAuthAdapterǁsave_token__mutmut['_mutmut_orig'] = CloudAuthAdapter.xǁCloudAuthAdapterǁsave_token__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCloudAuthAdapterǁsave_token__mutmut['xǁCloudAuthAdapterǁsave_token__mutmut_1'] = CloudAuthAdapter.xǁCloudAuthAdapterǁsave_token__mutmut_1 # type: ignore # mutmut generated
