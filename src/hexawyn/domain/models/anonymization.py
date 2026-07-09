"""Anonymization domain models — SensitiveMatch, AnonymizationMap, policies."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class SensitiveKind(Enum):
    SECRET_REF = "secret_ref"
    TOKEN = "token"
    IP = "ip"
    EMAIL = "email"
    INTERNAL_HOST = "internal_host"


class Destination(Enum):
    LOCAL = "local"
    SLACK = "slack"
    EXPORT = "export"
    LOG = "log"


@dataclass(frozen=True)
class SensitiveMatch:
    kind: SensitiveKind
    original: str
    placeholder: str


@dataclass
class AnonymizationMap:
    matches: list[SensitiveMatch] = field(default_factory=list)


@dataclass
class RedactionPolicy:
    mask_secrets: bool = True
    mask_tokens: bool = True
    mask_ips: bool = True
    mask_resource_names: bool = False
