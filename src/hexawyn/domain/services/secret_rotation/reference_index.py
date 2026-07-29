from __future__ import annotations

from hexawyn.application.ports.driven.secret_rotation_audit_port import SecretRaw
from hexawyn.domain.models.constants import SecretRotationConstants
from hexawyn.domain.models.secret_rotation import ExcludedSecretKey

_cfg = SecretRotationConstants()


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


def index_references(
    references_raw: list[dict[str, str]],
) -> dict[ExcludedSecretKey, list[str]]:
    index: dict[ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key: tuple[str, str] = (reference["namespace"], reference["secret_name"])
        index.setdefault(key, []).append(reference["workload_name"])
    return index
