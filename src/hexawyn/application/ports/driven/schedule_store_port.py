from abc import ABC, abstractmethod

from hexawyn.domain.models.schedule import CheckResult, CronCheck


class ScheduleStorePort(ABC):
    """Persistance des définitions de checks + historique des résultats."""

    @abstractmethod
    def list_checks(self) -> list[CronCheck]: ...

    @abstractmethod
    def get_check(self, name: str) -> CronCheck | None: ...

    @abstractmethod
    def save_check(self, check: CronCheck) -> None: ...

    @abstractmethod
    def delete_check(self, name: str) -> None: ...

    @abstractmethod
    def save_result(self, result: CheckResult) -> None: ...

    @abstractmethod
    def last_result(self, name: str) -> CheckResult | None: ...

    @abstractmethod
    def history(self, name: str, limit: int = 10) -> list[CheckResult]: ...
