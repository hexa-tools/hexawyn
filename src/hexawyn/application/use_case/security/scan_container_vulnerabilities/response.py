from dataclasses import dataclass, field
from typing import TypedDict


class CVEDict(TypedDict):
    cve_id: str
    severity: str
    package: str
    fix_version: str | None


class ImageVulnerabilityFindingDict(TypedDict):
    image: str
    namespaces: list[str]
    pods_using: list[str]
    cves: list[CVEDict]
    eol_base: bool
    is_mutable_tag: bool
    scan_status: str
    scanned_at: str | None
    priority_score: int


@dataclass
class ScanContainerVulnerabilitiesResponse:
    findings: list[ImageVulnerabilityFindingDict] = field(default_factory=list)
    total_images_scanned: int = 0
    images_with_critical_cves: int = 0
    eol_image_count: int = 0
    summary: str = ""
    error: str | None = None
