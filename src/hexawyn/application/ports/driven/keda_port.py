from abc import ABC, abstractmethod

from hexawyn.domain.models.keda import (
    KedaDetectionResult,
    KedaScaledJob,
    KedaScaledObject,
    KedaTriggerAuth,
)


class KedaPort(ABC):
    """Port for KEDA operations — read-only. Never triggers scale."""

    @abstractmethod
    def detect(self) -> KedaDetectionResult: ...
    @abstractmethod
    def list_scaledobjects(self, namespace: str | None = None) -> list[KedaScaledObject]: ...
    @abstractmethod
    def get_scaledobject(self, name: str, namespace: str) -> KedaScaledObject: ...
    @abstractmethod
    def list_trigger_auths(self, namespace: str | None = None) -> list[KedaTriggerAuth]: ...
    @abstractmethod
    def get_trigger_auth(self, name: str, namespace: str) -> KedaTriggerAuth: ...
    @abstractmethod
    def list_scaledjobs(self, namespace: str | None = None) -> list[KedaScaledJob]: ...
    @abstractmethod
    def get_scaledjob(self, name: str, namespace: str) -> KedaScaledJob: ...
