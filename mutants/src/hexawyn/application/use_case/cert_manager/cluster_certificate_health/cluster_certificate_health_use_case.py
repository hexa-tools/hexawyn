from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
    IngressRef,
    TlsSecretData,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.command import (
    ClusterCertificateHealthCommand,
)
from hexawyn.application.use_case.cert_manager.cluster_certificate_health.response import (
    ClusterCertificateHealthResponse,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.certificate import (
    CertificateEntry,
    CertificateInfo,
    CertificateStatus,
    ClusterCertificateReport,
)
from hexawyn.domain.services.certificate.checker import CertificateChecker


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__build_ingress_map__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_ingress_map__mutmut)
def _build_ingress_map(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["ingress_name"])
    return mapping


def x__build_ingress_map__mutmut_orig(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["ingress_name"])
    return mapping


def x__build_ingress_map__mutmut_1(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = None
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["ingress_name"])
    return mapping


def x__build_ingress_map__mutmut_2(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(None)
    return mapping


def x__build_ingress_map__mutmut_3(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(None, []).append(ref["ingress_name"])
    return mapping


def x__build_ingress_map__mutmut_4(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], None).append(ref["ingress_name"])
    return mapping


def x__build_ingress_map__mutmut_5(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault([]).append(ref["ingress_name"])
    return mapping


def x__build_ingress_map__mutmut_6(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], ).append(ref["ingress_name"])
    return mapping


def x__build_ingress_map__mutmut_7(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["XXsecret_nameXX"], []).append(ref["ingress_name"])
    return mapping


def x__build_ingress_map__mutmut_8(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["SECRET_NAME"], []).append(ref["ingress_name"])
    return mapping


def x__build_ingress_map__mutmut_9(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["XXingress_nameXX"])
    return mapping


def x__build_ingress_map__mutmut_10(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["INGRESS_NAME"])
    return mapping

mutants_x__build_ingress_map__mutmut['_mutmut_orig'] = x__build_ingress_map__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_ingress_map__mutmut['x__build_ingress_map__mutmut_1'] = x__build_ingress_map__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_ingress_map__mutmut['x__build_ingress_map__mutmut_2'] = x__build_ingress_map__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_ingress_map__mutmut['x__build_ingress_map__mutmut_3'] = x__build_ingress_map__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_ingress_map__mutmut['x__build_ingress_map__mutmut_4'] = x__build_ingress_map__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_ingress_map__mutmut['x__build_ingress_map__mutmut_5'] = x__build_ingress_map__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_ingress_map__mutmut['x__build_ingress_map__mutmut_6'] = x__build_ingress_map__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_ingress_map__mutmut['x__build_ingress_map__mutmut_7'] = x__build_ingress_map__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_ingress_map__mutmut['x__build_ingress_map__mutmut_8'] = x__build_ingress_map__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_ingress_map__mutmut['x__build_ingress_map__mutmut_9'] = x__build_ingress_map__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_ingress_map__mutmut['x__build_ingress_map__mutmut_10'] = x__build_ingress_map__mutmut_10 # type: ignore # mutmut generated
mutants_x__is_wildcard__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_wildcard__mutmut)
def _is_wildcard(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(name.startswith("*.") for name in san_list)


def x__is_wildcard__mutmut_orig(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(name.startswith("*.") for name in san_list)


def x__is_wildcard__mutmut_1(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith(None):
        return True
    return any(name.startswith("*.") for name in san_list)


def x__is_wildcard__mutmut_2(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("XX*.XX"):
        return True
    return any(name.startswith("*.") for name in san_list)


def x__is_wildcard__mutmut_3(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return False
    return any(name.startswith("*.") for name in san_list)


def x__is_wildcard__mutmut_4(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(None)


def x__is_wildcard__mutmut_5(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(name.startswith(None) for name in san_list)


def x__is_wildcard__mutmut_6(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(name.startswith("XX*.XX") for name in san_list)

mutants_x__is_wildcard__mutmut['_mutmut_orig'] = x__is_wildcard__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_wildcard__mutmut['x__is_wildcard__mutmut_1'] = x__is_wildcard__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_wildcard__mutmut['x__is_wildcard__mutmut_2'] = x__is_wildcard__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_wildcard__mutmut['x__is_wildcard__mutmut_3'] = x__is_wildcard__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_wildcard__mutmut['x__is_wildcard__mutmut_4'] = x__is_wildcard__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_wildcard__mutmut['x__is_wildcard__mutmut_5'] = x__is_wildcard__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_wildcard__mutmut['x__is_wildcard__mutmut_6'] = x__is_wildcard__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_pem_to_cert_info__mutmut)
def _parse_pem_to_cert_info(cert_pem: str) -> CertificateInfo:
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


def x__parse_pem_to_cert_info__mutmut_orig(cert_pem: str) -> CertificateInfo:
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


def x__parse_pem_to_cert_info__mutmut_1(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = None
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


def x__parse_pem_to_cert_info__mutmut_2(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode(None) if isinstance(cert_pem, str) else cert_pem
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


def x__parse_pem_to_cert_info__mutmut_3(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("XXutf-8XX") if isinstance(cert_pem, str) else cert_pem
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


def x__parse_pem_to_cert_info__mutmut_4(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("UTF-8") if isinstance(cert_pem, str) else cert_pem
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


def x__parse_pem_to_cert_info__mutmut_5(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = None
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


def x__parse_pem_to_cert_info__mutmut_6(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(None)
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


def x__parse_pem_to_cert_info__mutmut_7(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = None
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


def x__parse_pem_to_cert_info__mutmut_8(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(None)
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


def x__parse_pem_to_cert_info__mutmut_9(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = None
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


def x__parse_pem_to_cert_info__mutmut_10(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = None

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


def x__parse_pem_to_cert_info__mutmut_11(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = (not_after + now).days

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


def x__parse_pem_to_cert_info__mutmut_12(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = (not_after - now).days

    subject_attrs = None
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


def x__parse_pem_to_cert_info__mutmut_13(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = (not_after - now).days

    subject_attrs = cert.subject.get_attributes_for_oid(None)
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


def x__parse_pem_to_cert_info__mutmut_14(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = (not_after - now).days

    subject_attrs = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    subject_cn = None

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


def x__parse_pem_to_cert_info__mutmut_15(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = (not_after - now).days

    subject_attrs = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    subject_cn = str(None) if subject_attrs else ""

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


def x__parse_pem_to_cert_info__mutmut_16(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = (not_after - now).days

    subject_attrs = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    subject_cn = str(subject_attrs[1].value) if subject_attrs else ""

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


def x__parse_pem_to_cert_info__mutmut_17(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = (not_after - now).days

    subject_attrs = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    subject_cn = str(subject_attrs[0].value) if subject_attrs else "XXXX"

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


def x__parse_pem_to_cert_info__mutmut_18(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = (not_after - now).days

    subject_attrs = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    subject_cn = str(subject_attrs[0].value) if subject_attrs else ""

    issuer_attrs = None
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


def x__parse_pem_to_cert_info__mutmut_19(cert_pem: str) -> CertificateInfo:
    from cryptography import x509
    from cryptography.x509.oid import NameOID

    cert_bytes = cert_pem.encode("utf-8") if isinstance(cert_pem, str) else cert_pem
    cert = x509.load_pem_x509_certificate(cert_bytes)
    now = datetime.now(UTC)
    not_after = cert.not_valid_after_utc
    days_remaining = (not_after - now).days

    subject_attrs = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    subject_cn = str(subject_attrs[0].value) if subject_attrs else ""

    issuer_attrs = cert.issuer.get_attributes_for_oid(None)
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


def x__parse_pem_to_cert_info__mutmut_20(cert_pem: str) -> CertificateInfo:
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
    issuer_cn = None

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


def x__parse_pem_to_cert_info__mutmut_21(cert_pem: str) -> CertificateInfo:
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
    issuer_cn = str(None) if issuer_attrs else ""

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


def x__parse_pem_to_cert_info__mutmut_22(cert_pem: str) -> CertificateInfo:
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
    issuer_cn = str(issuer_attrs[1].value) if issuer_attrs else ""

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


def x__parse_pem_to_cert_info__mutmut_23(cert_pem: str) -> CertificateInfo:
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
    issuer_cn = str(issuer_attrs[0].value) if issuer_attrs else "XXXX"

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


def x__parse_pem_to_cert_info__mutmut_24(cert_pem: str) -> CertificateInfo:
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

    san_list: list[str] = None
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


def x__parse_pem_to_cert_info__mutmut_25(cert_pem: str) -> CertificateInfo:
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

        san_ext = None
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


def x__parse_pem_to_cert_info__mutmut_26(cert_pem: str) -> CertificateInfo:
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

        san_ext = cert.extensions.get_extension_for_oid(None)
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


def x__parse_pem_to_cert_info__mutmut_27(cert_pem: str) -> CertificateInfo:
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
        san_value = None
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


def x__parse_pem_to_cert_info__mutmut_28(cert_pem: str) -> CertificateInfo:
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
            san_list = None
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


def x__parse_pem_to_cert_info__mutmut_29(cert_pem: str) -> CertificateInfo:
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
            san_list = [str(None) for name in san_value]
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


def x__parse_pem_to_cert_info__mutmut_30(cert_pem: str) -> CertificateInfo:
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

    key_size: int = None

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


def x__parse_pem_to_cert_info__mutmut_31(cert_pem: str) -> CertificateInfo:
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

    key_size: int = getattr(None, "key_size", 0)

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


def x__parse_pem_to_cert_info__mutmut_32(cert_pem: str) -> CertificateInfo:
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

    key_size: int = getattr(cert.public_key(), None, 0)

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


def x__parse_pem_to_cert_info__mutmut_33(cert_pem: str) -> CertificateInfo:
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

    key_size: int = getattr(cert.public_key(), "key_size", None)

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


def x__parse_pem_to_cert_info__mutmut_34(cert_pem: str) -> CertificateInfo:
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

    key_size: int = getattr("key_size", 0)

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


def x__parse_pem_to_cert_info__mutmut_35(cert_pem: str) -> CertificateInfo:
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

    key_size: int = getattr(cert.public_key(), 0)

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


def x__parse_pem_to_cert_info__mutmut_36(cert_pem: str) -> CertificateInfo:
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

    key_size: int = getattr(cert.public_key(), "key_size", )

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


def x__parse_pem_to_cert_info__mutmut_37(cert_pem: str) -> CertificateInfo:
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

    key_size: int = getattr(cert.public_key(), "XXkey_sizeXX", 0)

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


def x__parse_pem_to_cert_info__mutmut_38(cert_pem: str) -> CertificateInfo:
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

    key_size: int = getattr(cert.public_key(), "KEY_SIZE", 0)

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


def x__parse_pem_to_cert_info__mutmut_39(cert_pem: str) -> CertificateInfo:
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

    key_size: int = getattr(cert.public_key(), "key_size", 1)

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


def x__parse_pem_to_cert_info__mutmut_40(cert_pem: str) -> CertificateInfo:
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

    is_ca: bool = None
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


def x__parse_pem_to_cert_info__mutmut_41(cert_pem: str) -> CertificateInfo:
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

    is_ca: bool = True
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


def x__parse_pem_to_cert_info__mutmut_42(cert_pem: str) -> CertificateInfo:
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

        bc_ext = None
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


def x__parse_pem_to_cert_info__mutmut_43(cert_pem: str) -> CertificateInfo:
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

        bc_ext = cert.extensions.get_extension_for_oid(None)
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


def x__parse_pem_to_cert_info__mutmut_44(cert_pem: str) -> CertificateInfo:
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
        bc_value = None
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


def x__parse_pem_to_cert_info__mutmut_45(cert_pem: str) -> CertificateInfo:
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
            is_ca = None
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


def x__parse_pem_to_cert_info__mutmut_46(cert_pem: str) -> CertificateInfo:
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
        subject_cn=None,
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


def x__parse_pem_to_cert_info__mutmut_47(cert_pem: str) -> CertificateInfo:
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
        issuer_cn=None,
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


def x__parse_pem_to_cert_info__mutmut_48(cert_pem: str) -> CertificateInfo:
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
        not_before=None,
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


def x__parse_pem_to_cert_info__mutmut_49(cert_pem: str) -> CertificateInfo:
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
        not_after=None,
        days_remaining=days_remaining,
        san_list=san_list,
        is_ca=is_ca,
        key_size=key_size,
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_50(cert_pem: str) -> CertificateInfo:
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
        days_remaining=None,
        san_list=san_list,
        is_ca=is_ca,
        key_size=key_size,
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_51(cert_pem: str) -> CertificateInfo:
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
        san_list=None,
        is_ca=is_ca,
        key_size=key_size,
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_52(cert_pem: str) -> CertificateInfo:
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
        is_ca=None,
        key_size=key_size,
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_53(cert_pem: str) -> CertificateInfo:
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
        key_size=None,
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_54(cert_pem: str) -> CertificateInfo:
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
        serial_number=None,
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_55(cert_pem: str) -> CertificateInfo:
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
        signature_algorithm=None,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_56(cert_pem: str) -> CertificateInfo:
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
        subject_full=None,
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_57(cert_pem: str) -> CertificateInfo:
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
        issuer_full=None,
    )


def x__parse_pem_to_cert_info__mutmut_58(cert_pem: str) -> CertificateInfo:
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


def x__parse_pem_to_cert_info__mutmut_59(cert_pem: str) -> CertificateInfo:
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


def x__parse_pem_to_cert_info__mutmut_60(cert_pem: str) -> CertificateInfo:
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


def x__parse_pem_to_cert_info__mutmut_61(cert_pem: str) -> CertificateInfo:
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
        days_remaining=days_remaining,
        san_list=san_list,
        is_ca=is_ca,
        key_size=key_size,
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_62(cert_pem: str) -> CertificateInfo:
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
        san_list=san_list,
        is_ca=is_ca,
        key_size=key_size,
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_63(cert_pem: str) -> CertificateInfo:
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
        is_ca=is_ca,
        key_size=key_size,
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_64(cert_pem: str) -> CertificateInfo:
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
        key_size=key_size,
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_65(cert_pem: str) -> CertificateInfo:
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
        serial_number=str(cert.serial_number),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_66(cert_pem: str) -> CertificateInfo:
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
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_67(cert_pem: str) -> CertificateInfo:
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
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_68(cert_pem: str) -> CertificateInfo:
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
        issuer_full=cert.issuer.rfc4514_string(),
    )


def x__parse_pem_to_cert_info__mutmut_69(cert_pem: str) -> CertificateInfo:
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
        )


def x__parse_pem_to_cert_info__mutmut_70(cert_pem: str) -> CertificateInfo:
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
        serial_number=str(None),
        signature_algorithm=cert.signature_algorithm_oid.dotted_string,
        subject_full=cert.subject.rfc4514_string(),
        issuer_full=cert.issuer.rfc4514_string(),
    )

mutants_x__parse_pem_to_cert_info__mutmut['_mutmut_orig'] = x__parse_pem_to_cert_info__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_1'] = x__parse_pem_to_cert_info__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_2'] = x__parse_pem_to_cert_info__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_3'] = x__parse_pem_to_cert_info__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_4'] = x__parse_pem_to_cert_info__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_5'] = x__parse_pem_to_cert_info__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_6'] = x__parse_pem_to_cert_info__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_7'] = x__parse_pem_to_cert_info__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_8'] = x__parse_pem_to_cert_info__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_9'] = x__parse_pem_to_cert_info__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_10'] = x__parse_pem_to_cert_info__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_11'] = x__parse_pem_to_cert_info__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_12'] = x__parse_pem_to_cert_info__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_13'] = x__parse_pem_to_cert_info__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_14'] = x__parse_pem_to_cert_info__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_15'] = x__parse_pem_to_cert_info__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_16'] = x__parse_pem_to_cert_info__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_17'] = x__parse_pem_to_cert_info__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_18'] = x__parse_pem_to_cert_info__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_19'] = x__parse_pem_to_cert_info__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_20'] = x__parse_pem_to_cert_info__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_21'] = x__parse_pem_to_cert_info__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_22'] = x__parse_pem_to_cert_info__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_23'] = x__parse_pem_to_cert_info__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_24'] = x__parse_pem_to_cert_info__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_25'] = x__parse_pem_to_cert_info__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_26'] = x__parse_pem_to_cert_info__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_27'] = x__parse_pem_to_cert_info__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_28'] = x__parse_pem_to_cert_info__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_29'] = x__parse_pem_to_cert_info__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_30'] = x__parse_pem_to_cert_info__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_31'] = x__parse_pem_to_cert_info__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_32'] = x__parse_pem_to_cert_info__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_33'] = x__parse_pem_to_cert_info__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_34'] = x__parse_pem_to_cert_info__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_35'] = x__parse_pem_to_cert_info__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_36'] = x__parse_pem_to_cert_info__mutmut_36 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_37'] = x__parse_pem_to_cert_info__mutmut_37 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_38'] = x__parse_pem_to_cert_info__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_39'] = x__parse_pem_to_cert_info__mutmut_39 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_40'] = x__parse_pem_to_cert_info__mutmut_40 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_41'] = x__parse_pem_to_cert_info__mutmut_41 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_42'] = x__parse_pem_to_cert_info__mutmut_42 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_43'] = x__parse_pem_to_cert_info__mutmut_43 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_44'] = x__parse_pem_to_cert_info__mutmut_44 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_45'] = x__parse_pem_to_cert_info__mutmut_45 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_46'] = x__parse_pem_to_cert_info__mutmut_46 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_47'] = x__parse_pem_to_cert_info__mutmut_47 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_48'] = x__parse_pem_to_cert_info__mutmut_48 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_49'] = x__parse_pem_to_cert_info__mutmut_49 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_50'] = x__parse_pem_to_cert_info__mutmut_50 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_51'] = x__parse_pem_to_cert_info__mutmut_51 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_52'] = x__parse_pem_to_cert_info__mutmut_52 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_53'] = x__parse_pem_to_cert_info__mutmut_53 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_54'] = x__parse_pem_to_cert_info__mutmut_54 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_55'] = x__parse_pem_to_cert_info__mutmut_55 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_56'] = x__parse_pem_to_cert_info__mutmut_56 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_57'] = x__parse_pem_to_cert_info__mutmut_57 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_58'] = x__parse_pem_to_cert_info__mutmut_58 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_59'] = x__parse_pem_to_cert_info__mutmut_59 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_60'] = x__parse_pem_to_cert_info__mutmut_60 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_61'] = x__parse_pem_to_cert_info__mutmut_61 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_62'] = x__parse_pem_to_cert_info__mutmut_62 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_63'] = x__parse_pem_to_cert_info__mutmut_63 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_64'] = x__parse_pem_to_cert_info__mutmut_64 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_65'] = x__parse_pem_to_cert_info__mutmut_65 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_66'] = x__parse_pem_to_cert_info__mutmut_66 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_67'] = x__parse_pem_to_cert_info__mutmut_67 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_68'] = x__parse_pem_to_cert_info__mutmut_68 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_69'] = x__parse_pem_to_cert_info__mutmut_69 # type: ignore # mutmut generated
mutants_x__parse_pem_to_cert_info__mutmut['x__parse_pem_to_cert_info__mutmut_70'] = x__parse_pem_to_cert_info__mutmut_70 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_certificate_entry__mutmut)
def _build_certificate_entry(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_orig(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_1(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = None
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_2(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(None)
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_3(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["XXcert_pemXX"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_4(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["CERT_PEM"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_5(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = None
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_6(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(None)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_7(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = None

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_8(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(None, [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_9(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], None)

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_10(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get([])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_11(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], )

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_12(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["XXsecret_nameXX"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_13(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["SECRET_NAME"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_14(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=None,
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_15(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=None,
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_16(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=None,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_17(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=None,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_18(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=None,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_19(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=None,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_20(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=None,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_21(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=None,
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_22(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=None,
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_23(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=None,
    )


def x__build_certificate_entry__mutmut_24(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_25(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_26(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_27(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_28(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_29(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_30(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_31(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_32(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_33(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        )


def x__build_certificate_entry__mutmut_34(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["XXsecret_nameXX"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_35(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["SECRET_NAME"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_36(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["XXnamespaceXX"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_37(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["NAMESPACE"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_38(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) != 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_39(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 1,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_40(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["XXcert_manager_managedXX"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_41(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["CERT_MANAGER_MANAGED"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_42(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["XXcert_manager_auto_renewingXX"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_43(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["CERT_MANAGER_AUTO_RENEWING"],
        is_wildcard=_is_wildcard(info.subject_cn, info.san_list),
    )


def x__build_certificate_entry__mutmut_44(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(None, info.san_list),
    )


def x__build_certificate_entry__mutmut_45(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, None),
    )


def x__build_certificate_entry__mutmut_46(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.san_list),
    )


def x__build_certificate_entry__mutmut_47(
    secret: TlsSecretData,
    ingress_map: dict[str, list[str]],
    checker: CertificateChecker,
) -> CertificateEntry:
    info = _parse_pem_to_cert_info(secret["cert_pem"])
    status = checker.check(info)
    ingress_refs = ingress_map.get(secret["secret_name"], [])

    return CertificateEntry(
        secret_name=secret["secret_name"],
        namespace=secret["namespace"],
        info=info,
        status=status,
        days_remaining=info.days_remaining,
        ingress_refs=ingress_refs,
        is_orphan=len(ingress_refs) == 0,
        cert_manager_managed=secret["cert_manager_managed"],
        cert_manager_auto_renewing=secret["cert_manager_auto_renewing"],
        is_wildcard=_is_wildcard(info.subject_cn, ),
    )

mutants_x__build_certificate_entry__mutmut['_mutmut_orig'] = x__build_certificate_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_1'] = x__build_certificate_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_2'] = x__build_certificate_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_3'] = x__build_certificate_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_4'] = x__build_certificate_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_5'] = x__build_certificate_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_6'] = x__build_certificate_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_7'] = x__build_certificate_entry__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_8'] = x__build_certificate_entry__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_9'] = x__build_certificate_entry__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_10'] = x__build_certificate_entry__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_11'] = x__build_certificate_entry__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_12'] = x__build_certificate_entry__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_13'] = x__build_certificate_entry__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_14'] = x__build_certificate_entry__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_15'] = x__build_certificate_entry__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_16'] = x__build_certificate_entry__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_17'] = x__build_certificate_entry__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_18'] = x__build_certificate_entry__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_19'] = x__build_certificate_entry__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_20'] = x__build_certificate_entry__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_21'] = x__build_certificate_entry__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_22'] = x__build_certificate_entry__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_23'] = x__build_certificate_entry__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_24'] = x__build_certificate_entry__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_25'] = x__build_certificate_entry__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_26'] = x__build_certificate_entry__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_27'] = x__build_certificate_entry__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_28'] = x__build_certificate_entry__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_29'] = x__build_certificate_entry__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_30'] = x__build_certificate_entry__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_31'] = x__build_certificate_entry__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_32'] = x__build_certificate_entry__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_33'] = x__build_certificate_entry__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_34'] = x__build_certificate_entry__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_35'] = x__build_certificate_entry__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_36'] = x__build_certificate_entry__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_37'] = x__build_certificate_entry__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_38'] = x__build_certificate_entry__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_39'] = x__build_certificate_entry__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_40'] = x__build_certificate_entry__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_41'] = x__build_certificate_entry__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_42'] = x__build_certificate_entry__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_43'] = x__build_certificate_entry__mutmut_43 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_44'] = x__build_certificate_entry__mutmut_44 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_45'] = x__build_certificate_entry__mutmut_45 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_46'] = x__build_certificate_entry__mutmut_46 # type: ignore # mutmut generated
mutants_x__build_certificate_entry__mutmut['x__build_certificate_entry__mutmut_47'] = x__build_certificate_entry__mutmut_47 # type: ignore # mutmut generated
mutants_x__build_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_report__mutmut)
def _build_report(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_orig(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_1(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = None
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_2(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        None,
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_3(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=None,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_4(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_5(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_6(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status != CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_7(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: None,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_8(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = None
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_9(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        None,
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_10(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=None,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_11(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_12(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_13(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status != CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_14(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: None,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_15(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = None
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_16(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        None,
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_17(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=None,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_18(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_19(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_20(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status != CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_21(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: None,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_22(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = None

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_23(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        None,
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_24(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=None,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_25(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_26(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_27(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status != CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_28(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: None,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_29(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=None,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_30(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=None,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_31(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=None,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_32(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=None,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_33(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=None,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_34(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=None,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_35(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=None,
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_36(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=None,
    )


def x__build_report__mutmut_37(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_38(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_39(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_40(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_41(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_42(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        total_scanned=len(entries),
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_43(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        scanned_at=datetime.now(UTC),
    )


def x__build_report__mutmut_44(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        )


def x__build_report__mutmut_45(
    entries: list[CertificateEntry],
    skipped_namespaces: list[str],
    cluster_name: str,
) -> ClusterCertificateReport:
    critical = sorted(
        [e for e in entries if e.status == CertificateStatus.CRITICAL],
        key=lambda e: e.days_remaining,
    )
    warning = sorted(
        [e for e in entries if e.status == CertificateStatus.WARNING],
        key=lambda e: e.days_remaining,
    )
    healthy = sorted(
        [e for e in entries if e.status == CertificateStatus.HEALTHY],
        key=lambda e: e.days_remaining,
    )
    expired = sorted(
        [e for e in entries if e.status == CertificateStatus.EXPIRED],
        key=lambda e: e.days_remaining,
    )

    return ClusterCertificateReport(
        cluster_name=cluster_name,
        critical=critical,
        warning=warning,
        healthy=healthy,
        expired=expired,
        skipped_namespaces=skipped_namespaces,
        total_scanned=len(entries),
        scanned_at=datetime.now(None),
    )

mutants_x__build_report__mutmut['_mutmut_orig'] = x__build_report__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_1'] = x__build_report__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_2'] = x__build_report__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_3'] = x__build_report__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_4'] = x__build_report__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_5'] = x__build_report__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_6'] = x__build_report__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_7'] = x__build_report__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_8'] = x__build_report__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_9'] = x__build_report__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_10'] = x__build_report__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_11'] = x__build_report__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_12'] = x__build_report__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_13'] = x__build_report__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_14'] = x__build_report__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_15'] = x__build_report__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_16'] = x__build_report__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_17'] = x__build_report__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_18'] = x__build_report__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_19'] = x__build_report__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_20'] = x__build_report__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_21'] = x__build_report__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_22'] = x__build_report__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_23'] = x__build_report__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_24'] = x__build_report__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_25'] = x__build_report__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_26'] = x__build_report__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_27'] = x__build_report__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_28'] = x__build_report__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_29'] = x__build_report__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_30'] = x__build_report__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_31'] = x__build_report__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_32'] = x__build_report__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_33'] = x__build_report__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_34'] = x__build_report__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_35'] = x__build_report__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_36'] = x__build_report__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_37'] = x__build_report__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_38'] = x__build_report__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_39'] = x__build_report__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_40'] = x__build_report__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_41'] = x__build_report__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_42'] = x__build_report__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_43'] = x__build_report__mutmut_43 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_44'] = x__build_report__mutmut_44 # type: ignore # mutmut generated
mutants_x__build_report__mutmut['x__build_report__mutmut_45'] = x__build_report__mutmut_45 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut: MutantDict = {}  # type: ignore


class ClusterCertificateHealthUseCase:
    @_mutmut_mutated(mutants_xǁClusterCertificateHealthUseCaseǁ__init____mutmut)
    def __init__(
        self,
        port: ClusterCertificateHealthPort,
        cluster_name: str = "default",
    ) -> None:
        self._port = port
        self._cluster_name = cluster_name
    def xǁClusterCertificateHealthUseCaseǁ__init____mutmut_orig(
        self,
        port: ClusterCertificateHealthPort,
        cluster_name: str = "default",
    ) -> None:
        self._port = port
        self._cluster_name = cluster_name
    def xǁClusterCertificateHealthUseCaseǁ__init____mutmut_1(
        self,
        port: ClusterCertificateHealthPort,
        cluster_name: str = "XXdefaultXX",
    ) -> None:
        self._port = port
        self._cluster_name = cluster_name
    def xǁClusterCertificateHealthUseCaseǁ__init____mutmut_2(
        self,
        port: ClusterCertificateHealthPort,
        cluster_name: str = "DEFAULT",
    ) -> None:
        self._port = port
        self._cluster_name = cluster_name
    def xǁClusterCertificateHealthUseCaseǁ__init____mutmut_3(
        self,
        port: ClusterCertificateHealthPort,
        cluster_name: str = "default",
    ) -> None:
        self._port = None
        self._cluster_name = cluster_name
    def xǁClusterCertificateHealthUseCaseǁ__init____mutmut_4(
        self,
        port: ClusterCertificateHealthPort,
        cluster_name: str = "default",
    ) -> None:
        self._port = port
        self._cluster_name = None

    @_mutmut_mutated(mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut)
    def check_cluster_certificate_health(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_orig(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_1(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = None
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_2(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=None,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_3(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=None,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_4(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_5(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_6(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = None
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_7(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = None

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_8(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = None
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_9(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(None)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_10(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = None
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_11(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(None)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_12(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(None)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_13(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                break

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_14(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = None
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_15(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(None)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_16(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = None
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_17(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(None, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_18(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, None, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_19(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, None)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_20(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_21(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_22(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, )
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_23(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(None)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_24(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    break

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_25(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = None
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_26(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(None, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_27(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, None, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_28(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, None)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_29(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_30(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, self._cluster_name)
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_31(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, )
        return ClusterCertificateHealthResponse(report=report)

    def xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_32(
        self, command: ClusterCertificateHealthCommand
    ) -> ClusterCertificateHealthResponse:
        checker = CertificateChecker(
            warning_days=command.warning_days,
            critical_days=command.critical_days,
        )
        skipped_namespaces: list[str] = []
        all_entries: list[CertificateEntry] = []

        for namespace in self._port.list_namespaces():
            try:
                secrets = self._port.list_tls_secrets(namespace)
                ingresses = self._port.list_ingresses(namespace)
            except InsufficientPermissionsError:
                skipped_namespaces.append(namespace)
                continue

            ingress_map = _build_ingress_map(ingresses)
            for secret in secrets:
                try:
                    entry = _build_certificate_entry(secret, ingress_map, checker)
                    all_entries.append(entry)
                except Exception:
                    continue

        report = _build_report(all_entries, skipped_namespaces, self._cluster_name)
        return ClusterCertificateHealthResponse(report=None)

mutants_xǁClusterCertificateHealthUseCaseǁ__init____mutmut['_mutmut_orig'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁ__init____mutmut['xǁClusterCertificateHealthUseCaseǁ__init____mutmut_1'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁ__init____mutmut['xǁClusterCertificateHealthUseCaseǁ__init____mutmut_2'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁ__init____mutmut['xǁClusterCertificateHealthUseCaseǁ__init____mutmut_3'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁ__init____mutmut['xǁClusterCertificateHealthUseCaseǁ__init____mutmut_4'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['_mutmut_orig'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_1'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_2'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_2 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_3'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_3 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_4'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_4 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_5'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_5 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_6'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_6 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_7'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_7 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_8'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_8 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_9'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_9 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_10'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_10 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_11'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_11 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_12'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_12 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_13'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_13 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_14'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_14 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_15'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_15 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_16'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_16 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_17'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_17 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_18'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_18 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_19'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_19 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_20'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_20 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_21'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_21 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_22'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_22 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_23'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_23 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_24'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_24 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_25'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_25 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_26'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_26 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_27'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_27 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_28'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_28 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_29'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_29 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_30'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_30 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_31'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_31 # type: ignore # mutmut generated
mutants_xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut['xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_32'] = ClusterCertificateHealthUseCase.xǁClusterCertificateHealthUseCaseǁcheck_cluster_certificate_health__mutmut_32 # type: ignore # mutmut generated
