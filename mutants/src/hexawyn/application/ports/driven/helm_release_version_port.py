from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class HelmReleaseRawData(TypedDict):
    release_name: str
    namespace: str
    chart_name: str
    chart_version: str
    is_pinned: bool


class ChartLatestRawData(TypedDict):
    chart_name: str
    latest_version: str
    breaking_changes: str
    repo_error: str


class HelmReleaseVersionPort(ABC):
    @abstractmethod
    def list_releases(self, namespace: str | None) -> list[HelmReleaseRawData]: ...

    @abstractmethod
    def fetch_latest_version(self, chart_name: str) -> ChartLatestRawData: ...
