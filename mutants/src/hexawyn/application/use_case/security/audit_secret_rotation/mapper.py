from __future__ import annotations

from datetime import UTC, date, datetime

from hexawyn.application.ports.driven.secret_rotation_audit_port import (
    ManagedFieldsEntryRaw,
    SecretRaw,
    SecretReferenceRaw,
)
from hexawyn.application.use_case.security.audit_secret_rotation.response import (
    AuditSecretRotationResponse,
    ExcludedSecretDict,
    StaleSecretFindingDict,
)
from hexawyn.domain.models.constants import SecretRotationConstants
from hexawyn.domain.models.secret_rotation import (
    ExcludedSecret,
    ManagedFieldsEntry,
    SecretRotationReport,
    StaleSecretFinding,
)

_cfg = SecretRotationConstants()
_ExcludedSecretKey = tuple[str, str]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_exclusion_reason__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_exclusion_reason__mutmut)
def exclusion_reason(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_orig(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_1(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["XXnamespaceXX"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_2(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["NAMESPACE"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_3(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] not in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_4(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "XXnamespace exempt from rotation policyXX"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_5(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "NAMESPACE EXEMPT FROM ROTATION POLICY"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_6(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = None
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_7(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["XXannotationsXX"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_8(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["ANNOTATIONS"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_9(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key not in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_10(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "XXexternally managed (External Secrets Operator)XX"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_11(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (external secrets operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_12(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "EXTERNALLY MANAGED (EXTERNAL SECRETS OPERATOR)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_13(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types or _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_14(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["XXsecret_typeXX"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_15(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["SECRET_TYPE"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_16(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] not in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_17(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key not in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def x_exclusion_reason__mutmut_18(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "XXauto-rotated (cert-manager)XX"
    return None


def x_exclusion_reason__mutmut_19(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "AUTO-ROTATED (CERT-MANAGER)"
    return None

mutants_x_exclusion_reason__mutmut['_mutmut_orig'] = x_exclusion_reason__mutmut_orig # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_1'] = x_exclusion_reason__mutmut_1 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_2'] = x_exclusion_reason__mutmut_2 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_3'] = x_exclusion_reason__mutmut_3 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_4'] = x_exclusion_reason__mutmut_4 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_5'] = x_exclusion_reason__mutmut_5 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_6'] = x_exclusion_reason__mutmut_6 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_7'] = x_exclusion_reason__mutmut_7 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_8'] = x_exclusion_reason__mutmut_8 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_9'] = x_exclusion_reason__mutmut_9 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_10'] = x_exclusion_reason__mutmut_10 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_11'] = x_exclusion_reason__mutmut_11 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_12'] = x_exclusion_reason__mutmut_12 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_13'] = x_exclusion_reason__mutmut_13 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_14'] = x_exclusion_reason__mutmut_14 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_15'] = x_exclusion_reason__mutmut_15 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_16'] = x_exclusion_reason__mutmut_16 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_17'] = x_exclusion_reason__mutmut_17 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_18'] = x_exclusion_reason__mutmut_18 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_19'] = x_exclusion_reason__mutmut_19 # type: ignore # mutmut generated
mutants_x_index_references__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_index_references__mutmut)
def index_references(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault(key, []).append(ref["workload_name"])
    return index


def x_index_references__mutmut_orig(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault(key, []).append(ref["workload_name"])
    return index


def x_index_references__mutmut_1(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = None
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault(key, []).append(ref["workload_name"])
    return index


def x_index_references__mutmut_2(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = None
        index.setdefault(key, []).append(ref["workload_name"])
    return index


def x_index_references__mutmut_3(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["XXnamespaceXX"], ref["secret_name"])
        index.setdefault(key, []).append(ref["workload_name"])
    return index


def x_index_references__mutmut_4(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["NAMESPACE"], ref["secret_name"])
        index.setdefault(key, []).append(ref["workload_name"])
    return index


def x_index_references__mutmut_5(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["XXsecret_nameXX"])
        index.setdefault(key, []).append(ref["workload_name"])
    return index


def x_index_references__mutmut_6(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["SECRET_NAME"])
        index.setdefault(key, []).append(ref["workload_name"])
    return index


def x_index_references__mutmut_7(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault(key, []).append(None)
    return index


def x_index_references__mutmut_8(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault(None, []).append(ref["workload_name"])
    return index


def x_index_references__mutmut_9(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault(key, None).append(ref["workload_name"])
    return index


def x_index_references__mutmut_10(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault([]).append(ref["workload_name"])
    return index


def x_index_references__mutmut_11(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault(key, ).append(ref["workload_name"])
    return index


def x_index_references__mutmut_12(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault(key, []).append(ref["XXworkload_nameXX"])
    return index


def x_index_references__mutmut_13(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault(key, []).append(ref["WORKLOAD_NAME"])
    return index

mutants_x_index_references__mutmut['_mutmut_orig'] = x_index_references__mutmut_orig # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_1'] = x_index_references__mutmut_1 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_2'] = x_index_references__mutmut_2 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_3'] = x_index_references__mutmut_3 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_4'] = x_index_references__mutmut_4 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_5'] = x_index_references__mutmut_5 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_6'] = x_index_references__mutmut_6 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_7'] = x_index_references__mutmut_7 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_8'] = x_index_references__mutmut_8 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_9'] = x_index_references__mutmut_9 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_10'] = x_index_references__mutmut_10 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_11'] = x_index_references__mutmut_11 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_12'] = x_index_references__mutmut_12 # type: ignore # mutmut generated
mutants_x_index_references__mutmut['x_index_references__mutmut_13'] = x_index_references__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_domain_entry__mutmut)
def to_domain_entry(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_orig(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_1(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=None,
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_2(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=None,
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_3(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=None,
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_4(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=None,
    )


def x_to_domain_entry__mutmut_5(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_6(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_7(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_8(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=raw["time"],
        )


def x_to_domain_entry__mutmut_9(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["XXmanagerXX"],
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_10(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["MANAGER"],
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_11(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["XXoperationXX"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_12(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["OPERATION"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_13(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=raw["XXtimeXX"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_14(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=raw["TIME"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def x_to_domain_entry__mutmut_15(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=raw["XXfields_v1_rawXX"],
    )


def x_to_domain_entry__mutmut_16(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=raw["FIELDS_V1_RAW"],
    )

mutants_x_to_domain_entry__mutmut['_mutmut_orig'] = x_to_domain_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_1'] = x_to_domain_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_2'] = x_to_domain_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_3'] = x_to_domain_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_4'] = x_to_domain_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_5'] = x_to_domain_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_6'] = x_to_domain_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_7'] = x_to_domain_entry__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_8'] = x_to_domain_entry__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_9'] = x_to_domain_entry__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_10'] = x_to_domain_entry__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_11'] = x_to_domain_entry__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_12'] = x_to_domain_entry__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_13'] = x_to_domain_entry__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_14'] = x_to_domain_entry__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_15'] = x_to_domain_entry__mutmut_15 # type: ignore # mutmut generated
mutants_x_to_domain_entry__mutmut['x_to_domain_entry__mutmut_16'] = x_to_domain_entry__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_date__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_date__mutmut)
def parse_date(value: str) -> date:
    return datetime.fromisoformat(value).astimezone(UTC).date()


def x_parse_date__mutmut_orig(value: str) -> date:
    return datetime.fromisoformat(value).astimezone(UTC).date()


def x_parse_date__mutmut_1(value: str) -> date:
    return datetime.fromisoformat(value).astimezone(None).date()


def x_parse_date__mutmut_2(value: str) -> date:
    return datetime.fromisoformat(None).astimezone(UTC).date()

mutants_x_parse_date__mutmut['_mutmut_orig'] = x_parse_date__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_date__mutmut['x_parse_date__mutmut_1'] = x_parse_date__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_date__mutmut['x_parse_date__mutmut_2'] = x_parse_date__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_response__mutmut)
def to_response(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_orig(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_1(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=None,
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_2(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=None,
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_3(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=None,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_4(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=None,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_5(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=None,
        error=None,
    )


def x_to_response__mutmut_6(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_7(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_8(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_9(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_10(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        error=None,
    )


def x_to_response__mutmut_11(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        )


def x_to_response__mutmut_12(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(None) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )


def x_to_response__mutmut_13(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(None) for e in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )

mutants_x_to_response__mutmut['_mutmut_orig'] = x_to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_1'] = x_to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_2'] = x_to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_3'] = x_to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_4'] = x_to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_5'] = x_to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_6'] = x_to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_7'] = x_to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_8'] = x_to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_9'] = x_to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_10'] = x_to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_11'] = x_to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_12'] = x_to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_13'] = x_to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_finding_dict__mutmut)
def _to_finding_dict(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_orig(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_1(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=None,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_2(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=None,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_3(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=None,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_4(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=None,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_5(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=None,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_6(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=None,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_7(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=None,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_8(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=None,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_9(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=None,
    )


def x__to_finding_dict__mutmut_10(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_11(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_12(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_13(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_14(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_15(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_16(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_17(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        note=finding.note,
    )


def x__to_finding_dict__mutmut_18(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        )

mutants_x__to_finding_dict__mutmut['_mutmut_orig'] = x__to_finding_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_1'] = x__to_finding_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_2'] = x__to_finding_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_3'] = x__to_finding_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_4'] = x__to_finding_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_5'] = x__to_finding_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_6'] = x__to_finding_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_7'] = x__to_finding_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_8'] = x__to_finding_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_9'] = x__to_finding_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_10'] = x__to_finding_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_11'] = x__to_finding_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_12'] = x__to_finding_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_13'] = x__to_finding_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_14'] = x__to_finding_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_15'] = x__to_finding_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_16'] = x__to_finding_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_17'] = x__to_finding_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_18'] = x__to_finding_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_excluded_dict__mutmut)
def _to_excluded_dict(excluded: ExcludedSecret) -> ExcludedSecretDict:
    return ExcludedSecretDict(
        name=excluded.name,
        namespace=excluded.namespace,
        reason=excluded.reason,
    )


def x__to_excluded_dict__mutmut_orig(excluded: ExcludedSecret) -> ExcludedSecretDict:
    return ExcludedSecretDict(
        name=excluded.name,
        namespace=excluded.namespace,
        reason=excluded.reason,
    )


def x__to_excluded_dict__mutmut_1(excluded: ExcludedSecret) -> ExcludedSecretDict:
    return ExcludedSecretDict(
        name=None,
        namespace=excluded.namespace,
        reason=excluded.reason,
    )


def x__to_excluded_dict__mutmut_2(excluded: ExcludedSecret) -> ExcludedSecretDict:
    return ExcludedSecretDict(
        name=excluded.name,
        namespace=None,
        reason=excluded.reason,
    )


def x__to_excluded_dict__mutmut_3(excluded: ExcludedSecret) -> ExcludedSecretDict:
    return ExcludedSecretDict(
        name=excluded.name,
        namespace=excluded.namespace,
        reason=None,
    )


def x__to_excluded_dict__mutmut_4(excluded: ExcludedSecret) -> ExcludedSecretDict:
    return ExcludedSecretDict(
        namespace=excluded.namespace,
        reason=excluded.reason,
    )


def x__to_excluded_dict__mutmut_5(excluded: ExcludedSecret) -> ExcludedSecretDict:
    return ExcludedSecretDict(
        name=excluded.name,
        reason=excluded.reason,
    )


def x__to_excluded_dict__mutmut_6(excluded: ExcludedSecret) -> ExcludedSecretDict:
    return ExcludedSecretDict(
        name=excluded.name,
        namespace=excluded.namespace,
        )

mutants_x__to_excluded_dict__mutmut['_mutmut_orig'] = x__to_excluded_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_1'] = x__to_excluded_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_2'] = x__to_excluded_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_3'] = x__to_excluded_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_4'] = x__to_excluded_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_5'] = x__to_excluded_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_excluded_dict__mutmut['x__to_excluded_dict__mutmut_6'] = x__to_excluded_dict__mutmut_6 # type: ignore # mutmut generated
