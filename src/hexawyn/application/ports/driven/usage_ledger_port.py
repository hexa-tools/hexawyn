from abc import ABC, abstractmethod

from hexawyn.domain.models.usage import (
    InvestigationUsage,
    MonthlyReport,
    UsageStats,
)


class UsageLedgerPort(ABC):
    @abstractmethod
    def record(self, usage: InvestigationUsage) -> None: ...

    @abstractmethod
    def read_all(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]: ...

    @abstractmethod
    def stats(self, days: int = 30) -> UsageStats: ...

    @abstractmethod
    def monthly_report(self, year: int, month: int) -> MonthlyReport: ...
