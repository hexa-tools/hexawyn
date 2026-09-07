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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRegexAnonymizerAdapterǁunmask__mutmut: MutantDict = {}  # type: ignore


class RegexAnonymizerAdapter(AnonymizerPort):
    @_mutmut_mutated(mutants_xǁRegexAnonymizerAdapterǁmask__mutmut)
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_orig(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_1(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_2(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_3(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = None

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_4(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 1

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_5(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(None):
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_6(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter = 1
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_7(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter -= 1
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_8(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 2
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_9(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_10(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = f"<SECRET_REF_{counter}>"
                amap.matches.append(
                    None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_11(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = f"<SECRET_REF_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=None, original=m.group(1), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_12(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = f"<SECRET_REF_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=None, placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_13(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = f"<SECRET_REF_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(1), placeholder=None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_14(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = f"<SECRET_REF_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        original=m.group(1), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_15(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = f"<SECRET_REF_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_16(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = f"<SECRET_REF_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(1), )
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_17(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = f"<SECRET_REF_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(None), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_18(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
        amap = AnonymizationMap()
        result = text
        counter = 0

        if policy.mask_secrets:
            for m in _SECRET_RE.finditer(result):
                counter += 1
                placeholder = f"<SECRET_REF_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(2), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_19(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = None

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_20(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(None, placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_21(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(1), None, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_22(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(1), placeholder, None)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_23(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_24(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(1), 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_25(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(1), placeholder, )

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_26(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(None), placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_27(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(2), placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_28(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(1), placeholder, 2)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_29(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
            for m in _TOKEN_RE.finditer(None):
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_30(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                counter = 1
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_31(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                counter -= 1
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_32(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                counter += 2
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_33(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                placeholder = None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_34(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                    None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_35(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=None, original=m.group(0), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_36(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.TOKEN, original=None, placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_37(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.TOKEN, original=m.group(0), placeholder=None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_38(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        original=m.group(0), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_39(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.TOKEN, placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_40(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.TOKEN, original=m.group(0), )
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_41(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.TOKEN, original=m.group(None), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_42(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.TOKEN, original=m.group(1), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_43(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = None

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_44(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(None, placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_45(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), None, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_46(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), placeholder, None)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_47(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_48(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_49(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), placeholder, )

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_50(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(None), placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_51(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(1), placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_52(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), placeholder, 2)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_53(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
            for m in _IP_RE.finditer(None):
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_54(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                counter = 1
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_55(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                counter -= 1
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_56(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                counter += 2
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_57(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                placeholder = None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_58(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                    None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_59(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=None, original=m.group(0), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_60(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.IP, original=None, placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_61(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.IP, original=m.group(0), placeholder=None
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_62(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        original=m.group(0), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_63(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.IP, placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_64(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.IP, original=m.group(0), )
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_65(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.IP, original=m.group(None), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_66(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.IP, original=m.group(1), placeholder=placeholder
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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_67(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = None

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_68(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(None, placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_69(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), None, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_70(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), placeholder, None)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_71(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_72(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_73(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), placeholder, )

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_74(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(None), placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_75(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(1), placeholder, 1)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_76(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), placeholder, 2)

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
    def xǁRegexAnonymizerAdapterǁmask__mutmut_77(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
            for m in _NAME_RE.finditer(None):
                counter += 1
                placeholder = f"<K8S_NAME_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(0), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_78(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                counter = 1
                placeholder = f"<K8S_NAME_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(0), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_79(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                counter -= 1
                placeholder = f"<K8S_NAME_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(0), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_80(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                counter += 2
                placeholder = f"<K8S_NAME_{counter}>"
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(0), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_81(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                placeholder = None
                amap.matches.append(
                    SensitiveMatch(
                        kind=SensitiveKind.SECRET_REF, original=m.group(0), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_82(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                    None
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_83(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=None, original=m.group(0), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_84(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.SECRET_REF, original=None, placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_85(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.SECRET_REF, original=m.group(0), placeholder=None
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_86(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        original=m.group(0), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_87(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.SECRET_REF, placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_88(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.SECRET_REF, original=m.group(0), )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_89(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.SECRET_REF, original=m.group(None), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_90(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                        kind=SensitiveKind.SECRET_REF, original=m.group(1), placeholder=placeholder
                    )
                )
                result = result.replace(m.group(0), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_91(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = None

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_92(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(None, placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_93(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), None, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_94(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), placeholder, None)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_95(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_96(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_97(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), placeholder, )

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_98(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(None), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_99(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(1), placeholder, 1)

        return result, amap
    def xǁRegexAnonymizerAdapterǁmask__mutmut_100(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]:
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
                result = result.replace(m.group(0), placeholder, 2)

        return result, amap

    @_mutmut_mutated(mutants_xǁRegexAnonymizerAdapterǁunmask__mutmut)
    def unmask(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str:
        if destination != Destination.LOCAL:
            return text

        result = text
        for match in mapping.matches:
            result = result.replace(match.placeholder, match.original)
        return result

    def xǁRegexAnonymizerAdapterǁunmask__mutmut_orig(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str:
        if destination != Destination.LOCAL:
            return text

        result = text
        for match in mapping.matches:
            result = result.replace(match.placeholder, match.original)
        return result

    def xǁRegexAnonymizerAdapterǁunmask__mutmut_1(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str:
        if destination == Destination.LOCAL:
            return text

        result = text
        for match in mapping.matches:
            result = result.replace(match.placeholder, match.original)
        return result

    def xǁRegexAnonymizerAdapterǁunmask__mutmut_2(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str:
        if destination != Destination.LOCAL:
            return text

        result = None
        for match in mapping.matches:
            result = result.replace(match.placeholder, match.original)
        return result

    def xǁRegexAnonymizerAdapterǁunmask__mutmut_3(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str:
        if destination != Destination.LOCAL:
            return text

        result = text
        for match in mapping.matches:
            result = None
        return result

    def xǁRegexAnonymizerAdapterǁunmask__mutmut_4(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str:
        if destination != Destination.LOCAL:
            return text

        result = text
        for match in mapping.matches:
            result = result.replace(None, match.original)
        return result

    def xǁRegexAnonymizerAdapterǁunmask__mutmut_5(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str:
        if destination != Destination.LOCAL:
            return text

        result = text
        for match in mapping.matches:
            result = result.replace(match.placeholder, None)
        return result

    def xǁRegexAnonymizerAdapterǁunmask__mutmut_6(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str:
        if destination != Destination.LOCAL:
            return text

        result = text
        for match in mapping.matches:
            result = result.replace(match.original)
        return result

    def xǁRegexAnonymizerAdapterǁunmask__mutmut_7(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str:
        if destination != Destination.LOCAL:
            return text

        result = text
        for match in mapping.matches:
            result = result.replace(match.placeholder, )
        return result

mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['_mutmut_orig'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_1'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_2'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_3'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_4'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_5'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_6'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_7'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_8'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_9'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_10'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_11'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_12'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_13'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_14'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_15'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_16'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_17'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_18'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_19'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_20'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_21'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_22'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_23'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_24'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_25'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_26'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_27'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_28'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_29'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_30'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_31'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_32'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_33'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_34'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_35'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_36'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_37'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_38'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_39'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_40'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_41'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_42'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_43'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_44'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_45'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_46'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_47'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_47 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_48'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_48 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_49'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_49 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_50'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_50 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_51'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_51 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_52'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_52 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_53'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_53 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_54'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_54 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_55'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_55 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_56'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_56 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_57'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_57 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_58'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_58 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_59'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_59 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_60'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_60 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_61'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_61 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_62'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_62 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_63'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_63 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_64'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_64 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_65'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_65 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_66'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_66 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_67'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_67 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_68'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_68 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_69'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_69 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_70'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_70 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_71'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_71 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_72'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_72 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_73'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_73 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_74'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_74 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_75'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_75 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_76'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_76 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_77'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_77 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_78'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_78 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_79'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_79 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_80'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_80 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_81'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_81 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_82'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_82 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_83'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_83 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_84'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_84 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_85'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_85 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_86'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_86 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_87'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_87 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_88'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_88 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_89'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_89 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_90'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_90 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_91'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_91 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_92'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_92 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_93'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_93 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_94'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_94 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_95'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_95 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_96'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_96 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_97'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_97 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_98'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_98 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_99'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_99 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁmask__mutmut['xǁRegexAnonymizerAdapterǁmask__mutmut_100'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁmask__mutmut_100 # type: ignore # mutmut generated

mutants_xǁRegexAnonymizerAdapterǁunmask__mutmut['_mutmut_orig'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁunmask__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁunmask__mutmut['xǁRegexAnonymizerAdapterǁunmask__mutmut_1'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁunmask__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁunmask__mutmut['xǁRegexAnonymizerAdapterǁunmask__mutmut_2'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁunmask__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁunmask__mutmut['xǁRegexAnonymizerAdapterǁunmask__mutmut_3'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁunmask__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁunmask__mutmut['xǁRegexAnonymizerAdapterǁunmask__mutmut_4'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁunmask__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁunmask__mutmut['xǁRegexAnonymizerAdapterǁunmask__mutmut_5'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁunmask__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁunmask__mutmut['xǁRegexAnonymizerAdapterǁunmask__mutmut_6'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁunmask__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRegexAnonymizerAdapterǁunmask__mutmut['xǁRegexAnonymizerAdapterǁunmask__mutmut_7'] = RegexAnonymizerAdapter.xǁRegexAnonymizerAdapterǁunmask__mutmut_7 # type: ignore # mutmut generated
