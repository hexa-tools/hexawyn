from dataclasses import dataclass, field


@dataclass
class HelmReleaseEntry:
    release_name: str = ""
    namespace: str = ""
    chart_version: str = ""
    latest_version: str = ""
    outdated: bool = False


@dataclass
class OutdatedHelmResult:
    total_releases: int = 0
    outdated_count: int = 0
    releases: list[HelmReleaseEntry] = field(default_factory=list)


@dataclass
class DetectOutdatedHelmReleasesResponse:
    result: OutdatedHelmResult
    error: str | None = None
