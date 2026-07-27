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


def _build_ingress_map(ingresses: list[IngressRef]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for ref in ingresses:
        mapping.setdefault(ref["secret_name"], []).append(ref["ingress_name"])
    return mapping


def _is_wildcard(subject_cn: str, san_list: list[str]) -> bool:
    if subject_cn.startswith("*."):
        return True
    return any(name.startswith("*.") for name in san_list)


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


class ClusterCertificateHealthUseCase:
    def __init__(
        self,
        port: ClusterCertificateHealthPort,
        cluster_name: str = "default",
    ) -> None:
        self._port = port
        self._cluster_name = cluster_name

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
