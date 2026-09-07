from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.cluster_certificate_health_port import IngressRef
from hexawyn.domain.models.certificate import CertificateInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_ingress_map__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_ingress_map__mutmut)
def build_ingress_map(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["ingress_name"])
    return mapping


def x_build_ingress_map__mutmut_orig(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["ingress_name"])
    return mapping


def x_build_ingress_map__mutmut_1(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = None
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["ingress_name"])
    return mapping


def x_build_ingress_map__mutmut_2(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(None)
    return mapping


def x_build_ingress_map__mutmut_3(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(None, []).append(ref["ingress_name"])
    return mapping


def x_build_ingress_map__mutmut_4(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], None).append(ref["ingress_name"])
    return mapping


def x_build_ingress_map__mutmut_5(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault([]).append(ref["ingress_name"])
    return mapping


def x_build_ingress_map__mutmut_6(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], ).append(ref["ingress_name"])
    return mapping


def x_build_ingress_map__mutmut_7(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["XXsecret_nameXX"], []).append(ref["ingress_name"])
    return mapping


def x_build_ingress_map__mutmut_8(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["SECRET_NAME"], []).append(ref["ingress_name"])
    return mapping


def x_build_ingress_map__mutmut_9(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["XXingress_nameXX"])
    return mapping


def x_build_ingress_map__mutmut_10(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["INGRESS_NAME"])
    return mapping

mutants_x_build_ingress_map__mutmut['_mutmut_orig'] = x_build_ingress_map__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_ingress_map__mutmut['x_build_ingress_map__mutmut_1'] = x_build_ingress_map__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_ingress_map__mutmut['x_build_ingress_map__mutmut_2'] = x_build_ingress_map__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_ingress_map__mutmut['x_build_ingress_map__mutmut_3'] = x_build_ingress_map__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_ingress_map__mutmut['x_build_ingress_map__mutmut_4'] = x_build_ingress_map__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_ingress_map__mutmut['x_build_ingress_map__mutmut_5'] = x_build_ingress_map__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_ingress_map__mutmut['x_build_ingress_map__mutmut_6'] = x_build_ingress_map__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_ingress_map__mutmut['x_build_ingress_map__mutmut_7'] = x_build_ingress_map__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_ingress_map__mutmut['x_build_ingress_map__mutmut_8'] = x_build_ingress_map__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_ingress_map__mutmut['x_build_ingress_map__mutmut_9'] = x_build_ingress_map__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_ingress_map__mutmut['x_build_ingress_map__mutmut_10'] = x_build_ingress_map__mutmut_10 # type: ignore # mutmut generated
mutants_x_is_wildcard__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_wildcard__mutmut)
def is_wildcard(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(name.startswith("*.") for name in san_list)


def x_is_wildcard__mutmut_orig(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(name.startswith("*.") for name in san_list)


def x_is_wildcard__mutmut_1(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith(None):
        return True
    return any(name.startswith("*.") for name in san_list)


def x_is_wildcard__mutmut_2(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("XX*.XX"):
        return True
    return any(name.startswith("*.") for name in san_list)


def x_is_wildcard__mutmut_3(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return False
    return any(name.startswith("*.") for name in san_list)


def x_is_wildcard__mutmut_4(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(None)


def x_is_wildcard__mutmut_5(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(name.startswith(None) for name in san_list)


def x_is_wildcard__mutmut_6(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(name.startswith("XX*.XX") for name in san_list)

mutants_x_is_wildcard__mutmut['_mutmut_orig'] = x_is_wildcard__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_wildcard__mutmut['x_is_wildcard__mutmut_1'] = x_is_wildcard__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_wildcard__mutmut['x_is_wildcard__mutmut_2'] = x_is_wildcard__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_wildcard__mutmut['x_is_wildcard__mutmut_3'] = x_is_wildcard__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_wildcard__mutmut['x_is_wildcard__mutmut_4'] = x_is_wildcard__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_wildcard__mutmut['x_is_wildcard__mutmut_5'] = x_is_wildcard__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_wildcard__mutmut['x_is_wildcard__mutmut_6'] = x_is_wildcard__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_pem_to_cert_info__mutmut)
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


def x_parse_pem_to_cert_info__mutmut_orig(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_1(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_2(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_3(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_4(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_5(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_6(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_7(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_8(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_9(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_10(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_11(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_12(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_13(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_14(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_15(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_16(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_17(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_18(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_19(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_20(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_21(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_22(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_23(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_24(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_25(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_26(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_27(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_28(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_29(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_30(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_31(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_32(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_33(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_34(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_35(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_36(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_37(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_38(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_39(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_40(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_41(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_42(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_43(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_44(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_45(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_46(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_47(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_48(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_49(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_50(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_51(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_52(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_53(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_54(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_55(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_56(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_57(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_58(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_59(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_60(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_61(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_62(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_63(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_64(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_65(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_66(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_67(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_68(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_69(cert_pem: str) -> CertificateInfo:
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


def x_parse_pem_to_cert_info__mutmut_70(cert_pem: str) -> CertificateInfo:
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

mutants_x_parse_pem_to_cert_info__mutmut['_mutmut_orig'] = x_parse_pem_to_cert_info__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_1'] = x_parse_pem_to_cert_info__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_2'] = x_parse_pem_to_cert_info__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_3'] = x_parse_pem_to_cert_info__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_4'] = x_parse_pem_to_cert_info__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_5'] = x_parse_pem_to_cert_info__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_6'] = x_parse_pem_to_cert_info__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_7'] = x_parse_pem_to_cert_info__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_8'] = x_parse_pem_to_cert_info__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_9'] = x_parse_pem_to_cert_info__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_10'] = x_parse_pem_to_cert_info__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_11'] = x_parse_pem_to_cert_info__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_12'] = x_parse_pem_to_cert_info__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_13'] = x_parse_pem_to_cert_info__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_14'] = x_parse_pem_to_cert_info__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_15'] = x_parse_pem_to_cert_info__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_16'] = x_parse_pem_to_cert_info__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_17'] = x_parse_pem_to_cert_info__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_18'] = x_parse_pem_to_cert_info__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_19'] = x_parse_pem_to_cert_info__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_20'] = x_parse_pem_to_cert_info__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_21'] = x_parse_pem_to_cert_info__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_22'] = x_parse_pem_to_cert_info__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_23'] = x_parse_pem_to_cert_info__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_24'] = x_parse_pem_to_cert_info__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_25'] = x_parse_pem_to_cert_info__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_26'] = x_parse_pem_to_cert_info__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_27'] = x_parse_pem_to_cert_info__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_28'] = x_parse_pem_to_cert_info__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_29'] = x_parse_pem_to_cert_info__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_30'] = x_parse_pem_to_cert_info__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_31'] = x_parse_pem_to_cert_info__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_32'] = x_parse_pem_to_cert_info__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_33'] = x_parse_pem_to_cert_info__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_34'] = x_parse_pem_to_cert_info__mutmut_34 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_35'] = x_parse_pem_to_cert_info__mutmut_35 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_36'] = x_parse_pem_to_cert_info__mutmut_36 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_37'] = x_parse_pem_to_cert_info__mutmut_37 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_38'] = x_parse_pem_to_cert_info__mutmut_38 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_39'] = x_parse_pem_to_cert_info__mutmut_39 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_40'] = x_parse_pem_to_cert_info__mutmut_40 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_41'] = x_parse_pem_to_cert_info__mutmut_41 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_42'] = x_parse_pem_to_cert_info__mutmut_42 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_43'] = x_parse_pem_to_cert_info__mutmut_43 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_44'] = x_parse_pem_to_cert_info__mutmut_44 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_45'] = x_parse_pem_to_cert_info__mutmut_45 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_46'] = x_parse_pem_to_cert_info__mutmut_46 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_47'] = x_parse_pem_to_cert_info__mutmut_47 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_48'] = x_parse_pem_to_cert_info__mutmut_48 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_49'] = x_parse_pem_to_cert_info__mutmut_49 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_50'] = x_parse_pem_to_cert_info__mutmut_50 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_51'] = x_parse_pem_to_cert_info__mutmut_51 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_52'] = x_parse_pem_to_cert_info__mutmut_52 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_53'] = x_parse_pem_to_cert_info__mutmut_53 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_54'] = x_parse_pem_to_cert_info__mutmut_54 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_55'] = x_parse_pem_to_cert_info__mutmut_55 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_56'] = x_parse_pem_to_cert_info__mutmut_56 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_57'] = x_parse_pem_to_cert_info__mutmut_57 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_58'] = x_parse_pem_to_cert_info__mutmut_58 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_59'] = x_parse_pem_to_cert_info__mutmut_59 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_60'] = x_parse_pem_to_cert_info__mutmut_60 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_61'] = x_parse_pem_to_cert_info__mutmut_61 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_62'] = x_parse_pem_to_cert_info__mutmut_62 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_63'] = x_parse_pem_to_cert_info__mutmut_63 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_64'] = x_parse_pem_to_cert_info__mutmut_64 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_65'] = x_parse_pem_to_cert_info__mutmut_65 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_66'] = x_parse_pem_to_cert_info__mutmut_66 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_67'] = x_parse_pem_to_cert_info__mutmut_67 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_68'] = x_parse_pem_to_cert_info__mutmut_68 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_69'] = x_parse_pem_to_cert_info__mutmut_69 # type: ignore # mutmut generated
mutants_x_parse_pem_to_cert_info__mutmut['x_parse_pem_to_cert_info__mutmut_70'] = x_parse_pem_to_cert_info__mutmut_70 # type: ignore # mutmut generated
