"""Regex-based anonymizer adapter — masks secrets, tokens, IPs in text."""

from __future__ import annotations

import re

from hexawyn.application.ports.driven.anonymizer_port import AnonymizerPort
from hexawyn.domain.models.anonymization import (
    AnonymizationMap,
    Destination,
    RedactionPolicy,
    SensitiveKind,
    SensitiveMatch,
)

_IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
_TOKEN_RE = re.compile(r"\beyJ[A-Za-z0-9_-]{5,}\.[A-Za-z0-9_-]{5,}\S*\b")
_SECRET_RE = re.compile(r"(?i)(?:secretRef|secret-key-ref|secret)\W+(\S+)")
_EMAIL_RE = re.compile(r"\b[\w.-]+@[\w.-]+\.\w{2,}\b")
_HOST_RE = re.compile(r"\b(?:host|Host)\s*[:=]\s*(\S+)")
_NAME_RE = re.compile(
    r"\b([a-z][a-z0-9-]*-(?:deployment|service|pod|configmap|secret|statefulset|daemonset|ingress))\b"
)


class RegexAnonymizerAdapter(AnonymizerPort):
    def mask(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = f"<SECRET_REF_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(1), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(1), placeholder, 1)

        if policy.mask_tokens:
            for m in _TOKEN_RE.finditer(result):
                counter += 1
                placeholder = f"<TOKEN_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.TOKEN, original=m.group(0), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        if policy.mask_ips:
            for m in _IP_RE.finditer(result):
                counter += 1
                placeholder = f"<IP_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.IP, original=m.group(0), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        if policy.mask_resource_names:
            for m in _NAME_RE.finditer(result):
                counter += 1
                placeholder = f"<K8S_NAME_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(0), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap

    def unmask(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str:
        if destination != Destination.LOCAL:
            return text

        result = text
        for match in mapping.matches:
            result = result.replace(match.placeholder, match.original)
        return result
