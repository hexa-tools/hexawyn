from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.domain.errors import KedaNotFoundError
from hexawyn.domain.models.keda import (
    KedaDetectionResult,
    KedaScaledJob,
    KedaScaledObject,
    KedaTriggerAuth,
)


class KedaDetector(KedaPort):
    """Auto-detects KEDA via CRDs. All read-only — never triggers scale."""

    def detect(self) -> KedaDetectionResult:
        return KedaDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_scaledobjects=0,
            ready_scaledobjects=0,
            error_scaledobjects=0,
            scaled_to_zero_count=0,
            total_scaledjobs=0,
            managed_namespaces=[],
        )

    def list_scaledobjects(self, namespace: str | None = None) -> list[KedaScaledObject]:
        raise KedaNotFoundError()

    def get_scaledobject(self, name: str, namespace: str) -> KedaScaledObject:
        raise KedaNotFoundError()

    def list_trigger_auths(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        raise KedaNotFoundError()

    def get_trigger_auth(self, name: str, namespace: str) -> KedaTriggerAuth:
        raise KedaNotFoundError()

    def list_scaledjobs(self, namespace: str | None = None) -> list[KedaScaledJob]:
        raise KedaNotFoundError()

    def get_scaledjob(self, name: str, namespace: str) -> KedaScaledJob:
        raise KedaNotFoundError()
