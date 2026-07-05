from __future__ import annotations

import json
import subprocess
from datetime import UTC, datetime
from typing import Any

from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
    CVERaw,
    ImageScanResultRaw,
    ImageVulnerabilityScanPort,
)

_TRIVY_COMMAND_TIMEOUT_SECONDS = 60.0
_KNOWN_SEVERITIES = frozenset({"critical", "high", "medium", "low"})


class TrivyCVEScanAdapter(ImageVulnerabilityScanPort):
    """Secondary adapter — shells out to the `trivy` CLI. Any scan failure
    (missing binary, timeout, non-zero exit, unparsable output) is returned
    as `scan_status="unscanned"` data, never raised — the scanner being
    unavailable or the image being unreachable (e.g. a private registry) is
    an expected, gracefully-handled state for this feature."""

    def scan_image(self, image: str) -> ImageScanResultRaw:
        try:
            result = subprocess.run(
                ["trivy", "image", "--format", "json", "--quiet", image],
                capture_output=True,
                text=True,
                timeout=_TRIVY_COMMAND_TIMEOUT_SECONDS,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return _unscanned_result()

        if result.returncode != 0:
            return _unscanned_result()

        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            return _unscanned_result()

        return _parse_trivy_payload(payload)


def _unscanned_result() -> ImageScanResultRaw:
    return ImageScanResultRaw(
        scan_status="unscanned", cves=[], detected_base_image=None, scanned_at=None
    )


def _parse_trivy_payload(payload: Any) -> ImageScanResultRaw:
    if not isinstance(payload, dict):
        return _unscanned_result()

    cves: list[CVERaw] = []
    for result_entry in payload.get("Results") or []:
        for vulnerability in result_entry.get("Vulnerabilities") or []:
            cve = _to_cve_raw(vulnerability)
            if cve is not None:
                cves.append(cve)

    return ImageScanResultRaw(
        scan_status="scanned",
        cves=cves,
        detected_base_image=_detect_base_image(payload),
        scanned_at=datetime.now(UTC).isoformat(),
    )


def _to_cve_raw(vulnerability: dict[str, Any]) -> CVERaw | None:
    cve_id = vulnerability.get("VulnerabilityID")
    severity = vulnerability.get("Severity")
    package = vulnerability.get("PkgName")
    if not isinstance(cve_id, str) or not isinstance(severity, str) or not isinstance(package, str):
        return None
    normalized_severity = severity.lower()
    if normalized_severity not in _KNOWN_SEVERITIES:
        return None
    fix_version = vulnerability.get("FixedVersion") or None
    return CVERaw(
        cve_id=cve_id, severity=normalized_severity, package=package, fix_version=fix_version
    )


def _detect_base_image(payload: dict[str, Any]) -> str | None:
    metadata = payload.get("Metadata") or {}
    os_info = metadata.get("OS") or {}
    family = os_info.get("Family")
    name = os_info.get("Name")
    if isinstance(family, str) and isinstance(name, str):
        return f"{family}:{name}"
    return None
