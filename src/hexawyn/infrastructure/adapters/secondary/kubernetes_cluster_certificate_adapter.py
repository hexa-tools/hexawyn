"""KubernetesClusterCertificateAdapter — reads TLS secrets and ingresses from K8s."""

from __future__ import annotations

import base64

from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
    IngressRef,
    TlsSecretData,
)
from hexawyn.domain.errors import AdapterTimeoutError, InsufficientPermissionsError

_CERT_MANAGER_ANNOTATION = "cert-manager.io/certificate-name"
_TLS_SECRET_TYPE = "kubernetes.io/tls"
_K8S_FORBIDDEN = 403


class KubernetesClusterCertificateAdapter(ClusterCertificateHealthPort):
    def __init__(self, api: object, timeout_seconds: float = 10.0) -> None:
        self._api = api
        self._timeout = int(timeout_seconds)

    def list_namespaces(self) -> list[str]:
        try:
            ns_list = getattr(self._api, "list_namespace")(timeout_seconds=self._timeout)
            return [
                str(getattr(getattr(ns, "metadata", None), "name", ""))
                for ns in (getattr(ns_list, "items", None) or [])
            ]
        except Exception as exc:
            raise AdapterTimeoutError(
                f"Failed to list namespaces: {exc}", context={"error": str(exc)}
            ) from exc

    def list_tls_secrets(self, namespace: str) -> list[TlsSecretData]:
        try:
            secret_list = getattr(self._api, "list_namespaced_secret")(
                namespace=namespace, timeout_seconds=self._timeout
            )
        except Exception as exc:
            _raise_on_rbac(namespace, exc)
            raise

        result: list[TlsSecretData] = []
        for secret in getattr(secret_list, "items", None) or []:
            if str(getattr(secret, "type", "")) != _TLS_SECRET_TYPE:
                continue
            cert_pem = _extract_cert_pem(secret)
            if not cert_pem:
                continue
            annotations = _get_annotations(secret)
            cert_manager_managed = _CERT_MANAGER_ANNOTATION in annotations
            cert_manager_auto_renewing = cert_manager_managed and _is_auto_renewing(
                secret, namespace
            )
            result.append(
                TlsSecretData(
                    secret_name=str(getattr(getattr(secret, "metadata", None), "name", "")),
                    namespace=namespace,
                    cert_pem=cert_pem,
                    cert_manager_managed=cert_manager_managed,
                    cert_manager_auto_renewing=cert_manager_auto_renewing,
                )
            )
        return result

    def list_ingresses(self, namespace: str) -> list[IngressRef]:
        try:
            from kubernetes import client as k8s

            networking_api = k8s.NetworkingV1Api()
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=self._timeout
            )
        except Exception as exc:
            _raise_on_rbac(namespace, exc)
            raise

        result: list[IngressRef] = []
        for ingress in getattr(ingress_list, "items", None) or []:
            ingress_name = str(getattr(getattr(ingress, "metadata", None), "name", ""))
            spec = getattr(ingress, "spec", None)
            for tls_entry in getattr(spec, "tls", None) or []:
                secret_name = str(getattr(tls_entry, "secret_name", "") or "")
                hosts = getattr(tls_entry, "hosts", None) or [""]
                host = str(hosts[0]) if hosts else ""
                if secret_name:
                    result.append(
                        IngressRef(
                            ingress_name=ingress_name,
                            namespace=namespace,
                            secret_name=secret_name,
                            host=host,
                        )
                    )
        return result


# ── Helpers ────────────────────────────────────────────────────────────────


def _extract_cert_pem(secret: object) -> str:
    data = getattr(secret, "data", None) or {}
    cert_b64 = data.get("tls.crt") if isinstance(data, dict) else None
    if not cert_b64:
        return ""
    try:
        return base64.b64decode(cert_b64).decode("utf-8")
    except Exception:
        return ""


def _get_annotations(secret: object) -> dict[str, str]:
    metadata = getattr(secret, "metadata", None)
    annotations = getattr(metadata, "annotations", None) or {}
    return dict(annotations) if isinstance(annotations, dict) else {}


def _is_auto_renewing(secret: object, namespace: str) -> bool:
    """Returns True when cert-manager has a renewal in progress (ready=False)."""
    try:
        from kubernetes import client as k8s

        custom_api = k8s.CustomObjectsApi()
        annotations = _get_annotations(secret)
        cert_name = annotations.get(_CERT_MANAGER_ANNOTATION, "")
        if not cert_name:
            return False
        cert_obj = custom_api.get_namespaced_custom_object(
            group="cert-manager.io",
            version="v1",
            namespace=namespace,
            plural="certificates",
            name=cert_name,
        )
        conditions = (
            (cert_obj.get("status") or {}).get("conditions") or []
            if isinstance(cert_obj, dict)
            else []
        )
        for cond in conditions:
            if isinstance(cond, dict) and cond.get("type") == "Ready":
                return str(cond.get("status", "True")) == "False"
    except Exception:
        pass
    return False


def _raise_on_rbac(namespace: str, exc: Exception) -> None:
    status_code = getattr(exc, "status", None)
    if status_code == _K8S_FORBIDDEN:
        raise InsufficientPermissionsError(
            f"RBAC denied access to namespace {namespace!r}",
            context={"namespace": namespace},
        ) from exc
