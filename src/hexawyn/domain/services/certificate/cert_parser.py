from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.cluster_certificate_health_port import IngressRef
from hexawyn.domain.models.certificate import CertificateInfo


def build_ingress_map(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["ingress_name"])
    return mapping


def is_wildcard(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(name.startswith("*.") for name in san_list)


def parse_pem_to_cert_info(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = (not_after - now).days

    subject_attrs = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    subject_cn = str(subject_attrs[0].value) if subject_attrs else ""

    issuer_attrs = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
    issuer_cn = str(issuer_attrs[0].value) if issuer_attrs else ""

    san_list: list[str] = []
    try:
        from cryptography.x509 import SubjectAlternativeName
        from cryptography.x509.oid import ExtensionOID

        san_ext = cert.extensions.get_extension_for_oid(ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
        san_value = san_ext.value
        if isinstance(san_value, SubjectAlternativeName):
            san_list = [str(name.value) for name in san_value]
    except Exception:
        pass

    key_size: int = getattr(cert.public_key(), "key_size", 0)

    is_ca: bool = False
    try:
        from cryptography.x509 import BasicConstraints
        from cryptography.x509.oid import ExtensionOID

        bc_ext = cert.extensions.get_extension_for_oid(ExtensionOID.BASIC_CONSTRAINTS)
        bc_value = bc_ext.value
        if isinstance(bc_value, BasicConstraints):
            is_ca = bc_value.ca
    except Exception:
        pass

    return CertificateInfo(
        subject_cn=subject_cn,
        issuer_cn=issuer_cn,
        not_before=cert.not_valid_before_utc,
        not_after=not_after,
        days_remaining=days_remaining,
        san_list=san_list,
        is_ca=is_ca,
        key_size=key_size,
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )
