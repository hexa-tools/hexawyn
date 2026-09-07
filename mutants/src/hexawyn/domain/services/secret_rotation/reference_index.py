from __future__ import annotations

from hexawyn.application.ports.driven.secret_rotation_audit_port import SecretRaw
from hexawyn.domain.models.constants import SecretRotationConstants
from hexawyn.domain.models.secret_rotation import ExcludedSecretKey

_cfg = SecretRotationConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_exclusion_reason__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_exclusion_reason__mutmut)
def exclusion_reason(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_orig(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_1(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_2(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_3(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_4(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_5(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_6(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_7(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_8(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_9(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_10(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_11(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_12(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_13(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_14(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_15(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_16(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_17(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_18(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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


def x_exclusion_reason__mutmut_19(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
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
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault(key, []).append(reference["workload_name"])
    return index


def x_index_references__mutmut_orig(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault(key, []).append(reference["workload_name"])
    return index


def x_index_references__mutmut_1(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = None
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault(key, []).append(reference["workload_name"])
    return index


def x_index_references__mutmut_2(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = None
        index.setdefault(key, []).append(reference["workload_name"])
    return index


def x_index_references__mutmut_3(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["XXnamespaceXX"], reference["secret_name"])
        index.setdefault(key, []).append(reference["workload_name"])
    return index


def x_index_references__mutmut_4(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["NAMESPACE"], reference["secret_name"])
        index.setdefault(key, []).append(reference["workload_name"])
    return index


def x_index_references__mutmut_5(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["XXsecret_nameXX"])
        index.setdefault(key, []).append(reference["workload_name"])
    return index


def x_index_references__mutmut_6(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["SECRET_NAME"])
        index.setdefault(key, []).append(reference["workload_name"])
    return index


def x_index_references__mutmut_7(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault(key, []).append(None)
    return index


def x_index_references__mutmut_8(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault(None, []).append(reference["workload_name"])
    return index


def x_index_references__mutmut_9(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault(key, None).append(reference["workload_name"])
    return index


def x_index_references__mutmut_10(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault([]).append(reference["workload_name"])
    return index


def x_index_references__mutmut_11(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault(key, ).append(reference["workload_name"])
    return index


def x_index_references__mutmut_12(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault(key, []).append(reference["XXworkload_nameXX"])
    return index


def x_index_references__mutmut_13(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault(key, []).append(reference["WORKLOAD_NAME"])
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
