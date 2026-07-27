# mypy: ignore-errors
"""CertManagerAdapter — queries real cert-manager CRDs via VanillaAdapter."""

from __future__ import annotations

from typing import cast

from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.domain.models.certificates import (
    AcmeChallenge,
    Certificate,
    CertificateIssuer,
    CertificateStatus,
    CertManagerDetectionResult,
    IssuerType,
)
from kubernetes import client

_CERT_MANAGER_GROUP = "cert-manager.io"
_CERT_MANAGER_VERSION = "v1"
_ACME_GROUP = "acme.cert-manager.io"
_ACME_VERSION = "v1"


class CertManagerAdapter(CertManagerPort):
    """Real cert-manager adapter using VanillaAdapter's CustomObjectsApi."""

    def __init__(self, vanilla: VanillaAdapter) -> None:
        self._vanilla = vanilla

    def _crd(self) -> client.CustomObjectsApi:
        return self._vanilla._crd_api_client()  # type: ignore[return-value]

    def detect(self) -> CertManagerDetectionResult:
        try:
            certs_raw = self._crd().list_namespaced_custom_object(
                group=_CERT_MANAGER_GROUP,
                version=_CERT_MANAGER_VERSION,
                namespace="",
                plural="certificates",
            )
        except Exception:
            return CertManagerDetectionResult(
                installed=False,
                version=None,
                namespace=None,
                total_certs=0,
                ready_certs=0,
                expiring_soon=0,
                failed_certs=0,
                active_challenges=0,
            )

        items = cast(dict, certs_raw).get("items", [])  # type: ignore
        certs = [self._parse_certificate(c) for c in items if isinstance(c, dict)]
        ready = sum(1 for c in certs if c.status == CertificateStatus.READY)
        return CertManagerDetectionResult(
            installed=True,
            version=None,
            namespace="cert-manager",
            total_certs=len(certs),
            ready_certs=ready,
            expiring_soon=0,
            failed_certs=len(certs) - ready,
            active_challenges=0,
        )

    def list_certificates(self, namespace: str | None = None) -> list[Certificate]:
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(
                    group=_CERT_MANAGER_GROUP,
                    version=_CERT_MANAGER_VERSION,
                    namespace=namespace,
                    plural="certificates",
                )
            else:
                raw = self._crd().list_cluster_custom_object(
                    group=_CERT_MANAGER_GROUP,
                    version=_CERT_MANAGER_VERSION,
                    plural="certificates",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [self._parse_certificate(c) for c in items if isinstance(c, dict)]

    def get_certificate(self, name: str, namespace: str) -> Certificate:
        raw = self._crd().get_namespaced_custom_object(
            group=_CERT_MANAGER_GROUP,
            version=_CERT_MANAGER_VERSION,
            namespace=namespace,
            plural="certificates",
            name=name,
        )
        result = self._parse_certificate(cast(dict, raw))  # type: ignore
        if result.name != name:
            raise ValueError(f"Certificate {name} not found in {namespace}")
        return result

    def list_issuers(self, namespace: str | None = None) -> list[CertificateIssuer]:
        issuers: list[CertificateIssuer] = []
        try:
            raw = self._crd().list_cluster_custom_object(
                group=_CERT_MANAGER_GROUP,
                version=_CERT_MANAGER_VERSION,
                plural="clusterissuers",
            )
            items = cast(dict, raw).get("items", [])  # type: ignore
            issuers.extend(
                self._parse_issuer(c, "ClusterIssuer") for c in items if isinstance(c, dict)
            )
        except Exception:
            pass
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(
                    group=_CERT_MANAGER_GROUP,
                    version=_CERT_MANAGER_VERSION,
                    namespace=namespace,
                    plural="issuers",
                )
            else:
                raw = self._crd().list_cluster_custom_object(
                    group=_CERT_MANAGER_GROUP,
                    version=_CERT_MANAGER_VERSION,
                    plural="issuers",
                )
            items = cast(dict, raw).get("items", [])  # type: ignore
            issuers.extend(self._parse_issuer(c, "Issuer") for c in items if isinstance(c, dict))
        except Exception:
            pass
        return issuers

    def get_issuer(self, name: str, namespace: str | None = None) -> CertificateIssuer:
        try:
            raw = self._crd().get_cluster_custom_object(
                group=_CERT_MANAGER_GROUP,
                version=_CERT_MANAGER_VERSION,
                plural="clusterissuers",
                name=name,
            )
            return self._parse_issuer(cast(dict, raw), "ClusterIssuer")  # type: ignore
        except Exception:
            pass
        ns = namespace or "default"
        raw = self._crd().get_namespaced_custom_object(
            group=_CERT_MANAGER_GROUP,
            version=_CERT_MANAGER_VERSION,
            namespace=ns,
            plural="issuers",
            name=name,
        )
        return self._parse_issuer(cast(dict, raw), "Issuer")  # type: ignore

    def list_challenges(self, namespace: str | None = None) -> list[AcmeChallenge]:
        challenges: list[AcmeChallenge] = []
        try:
            raw = self._crd().list_cluster_custom_object(
                group=_ACME_GROUP,
                version=_ACME_VERSION,
                plural="challenges",
            )
            items = cast(dict, raw).get("items", [])  # type: ignore
            for c in items:
                if not isinstance(c, dict):
                    continue
                meta = c.get("metadata", {}) if isinstance(c.get("metadata"), dict) else {}
                spec = c.get("spec", {}) if isinstance(c.get("spec"), dict) else {}
                status = c.get("status", {}) if isinstance(c.get("status"), dict) else {}
                if namespace and meta.get("namespace") != namespace:
                    continue
                challenges.append(
                    AcmeChallenge(
                        name=str(meta.get("name", "")),
                        namespace=str(meta.get("namespace", "default")),
                        type=str(spec.get("type", "")),
                        domain=str(spec.get("dnsName", "")),
                        state=str(status.get("state", "unknown")),
                        reason=status.get("reason"),
                        age_seconds=0,
                    )
                )
        except Exception:
            pass
        return challenges

    def list_requests(self, namespace: str | None = None) -> list[Certificate]:
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(
                    group=_CERT_MANAGER_GROUP,
                    version=_CERT_MANAGER_VERSION,
                    namespace=namespace,
                    plural="certificaterequests",
                )
            else:
                raw = self._crd().list_cluster_custom_object(
                    group=_CERT_MANAGER_GROUP,
                    version=_CERT_MANAGER_VERSION,
                    plural="certificaterequests",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [self._parse_certificate(c) for c in items if isinstance(c, dict)]

    def _parse_certificate(self, obj: dict) -> Certificate:  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}
        conditions = status.get("conditions", [])
        if not isinstance(conditions, list):
            conditions = []

        ready_cond = None
        for cond in conditions:
            if isinstance(cond, dict) and cond.get("type") == "Ready":
                ready_cond = cond
                break

        cert_status = CertificateStatus.UNKNOWN
        if ready_cond:
            if ready_cond.get("status") == "True":
                cert_status = CertificateStatus.READY
            elif "issuing" in str(ready_cond.get("reason", "")).lower():
                cert_status = CertificateStatus.ISSUING
            else:
                cert_status = CertificateStatus.NOT_READY

        issuer_ref = spec.get("issuerRef", {}) if isinstance(spec.get("issuerRef"), dict) else {}
        issuer_type = self._parse_issuer_type(str(issuer_ref.get("name", "")))

        not_before = str(status.get("notBefore", "")) or None
        not_after = str(status.get("notAfter", "")) or None
        renewal_time = str(status.get("renewalTime", "")) or None
        renew_before = str(spec.get("renewBefore", ""))

        days = None
        if not_after:
            try:
                from datetime import UTC, datetime

                not_after_dt = datetime.fromisoformat(not_after.replace("Z", "+00:00"))
                days = (not_after_dt - datetime.now(UTC)).days
            except (ValueError, TypeError):
                pass

        auto_renew = bool(renew_before and renew_before != "")

        return Certificate(
            name=str(meta.get("name", "")),
            namespace=str(meta.get("namespace", "default")),
            status=cert_status,
            issuer_name=str(issuer_ref.get("name", "")),
            issuer_type=issuer_type,
            dns_names=self._str_list(spec.get("dnsNames", [])),
            not_before=not_before,
            not_after=not_after,
            days_until_expiry=days,
            renewal_time=renewal_time,
            auto_renew=auto_renew,
            message=str(ready_cond.get("message", "")) if ready_cond else None,
        )

    def _parse_issuer(self, obj: dict, kind: str) -> CertificateIssuer:  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}
        conditions = status.get("conditions", [])
        if not isinstance(conditions, list):
            conditions = []

        ready = False
        message = None
        for cond in conditions:
            if isinstance(cond, dict) and cond.get("type") == "Ready":
                ready = cond.get("status") == "True"
                message = str(cond.get("message", ""))

        acme = spec.get("acme", {}) if isinstance(spec.get("acme"), dict) else {}
        server = str(acme.get("server", "")) or None

        return CertificateIssuer(
            name=str(meta.get("name", "")),
            namespace=meta.get("namespace") or None,
            kind=kind,
            issuer_type=self._parse_issuer_type(str(meta.get("name", ""))),
            ready=ready,
            server=server,
            message=message,
        )

    @staticmethod
    def _parse_issuer_type(issuer_name: str) -> IssuerType:
        name = issuer_name.lower()
        if "letsencrypt" in name or "lets-encrypt" in name or "acme" in name:
            return IssuerType.LETS_ENCRYPT
        if "vault" in name:
            return IssuerType.VAULT
        if "self" in name and "signed" in name:
            return IssuerType.SELF_SIGNED
        if "ca" == name or name.endswith("-ca"):
            return IssuerType.CA
        if "venafi" in name:
            return IssuerType.VENAFI
        return IssuerType.UNKNOWN

    @staticmethod
    def _str_list(value: object) -> list[str]:
        if isinstance(value, list):
            return [str(v) for v in value]
        return []
