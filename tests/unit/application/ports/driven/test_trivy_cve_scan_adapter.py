"""Unit tests for TrivyCVEScanAdapter — mocks subprocess.run (HelmDriftAdapter's
exact pattern). Every failure mode (missing binary, timeout, non-zero exit,
bad JSON) must become scan_status="unscanned" data, never a raised
exception — the scanner being unavailable is this ticket's own explicit
graceful-degradation requirement, not an exceptional case."""

from __future__ import annotations

import json
import subprocess
from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
    ImageVulnerabilityScanPort,
)


def _completed(returncode: int = 0, stdout: str = "", stderr: str = "") -> MagicMock:
    result = MagicMock()
    result.returncode = returncode
    result.stdout = stdout
    result.stderr = stderr
    return result


def _trivy_payload(
    vulnerabilities: list[dict] | None = None,
    os_family: str | None = None,
    os_name: str | None = None,
) -> str:
    payload: dict = {"Results": [{"Vulnerabilities": vulnerabilities or []}]}
    if os_family is not None:
        payload["Metadata"] = {"OS": {"Family": os_family, "Name": os_name}}
    return json.dumps(payload)


class TestTrivyCVEScanAdapterIsPort:
    def test_is_image_vulnerability_scan_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        assert isinstance(TrivyCVEScanAdapter(), ImageVulnerabilityScanPort)


class TestScanImageSuccess:
    def test_parses_vulnerabilities_into_cve_raw(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        payload = _trivy_payload(
            vulnerabilities=[
                {
                    "VulnerabilityID": "CVE-2024-5535",
                    "Severity": "CRITICAL",
                    "PkgName": "openssl",
                    "FixedVersion": "3.0.14",
                },
                {
                    "VulnerabilityID": "CVE-2024-4603",
                    "Severity": "HIGH",
                    "PkgName": "openssl",
                },
            ]
        )

        with patch("subprocess.run", return_value=_completed(stdout=payload)):
            result = TrivyCVEScanAdapter().scan_image("payment:v1.2")

        assert result["scan_status"] == "scanned"
        cve_ids = {cve["cve_id"] for cve in result["cves"]}
        assert cve_ids == {"CVE-2024-5535", "CVE-2024-4603"}
        critical = next(cve for cve in result["cves"] if cve["cve_id"] == "CVE-2024-5535")
        assert critical["severity"] == "critical"
        assert critical["fix_version"] == "3.0.14"
        high = next(cve for cve in result["cves"] if cve["cve_id"] == "CVE-2024-4603")
        assert high["fix_version"] is None

    def test_no_vulnerabilities_is_a_clean_scan(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        with patch("subprocess.run", return_value=_completed(stdout=_trivy_payload())):
            result = TrivyCVEScanAdapter().scan_image("alpine:3.18")

        assert result["scan_status"] == "scanned"
        assert result["cves"] == []

    def test_unknown_severity_is_dropped(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        payload = _trivy_payload(
            vulnerabilities=[
                {"VulnerabilityID": "CVE-X", "Severity": "UNKNOWN", "PkgName": "p"},
            ]
        )

        with patch("subprocess.run", return_value=_completed(stdout=payload)):
            result = TrivyCVEScanAdapter().scan_image("app:v1")

        assert result["cves"] == []

    def test_vulnerability_missing_required_fields_is_skipped(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        payload = _trivy_payload(
            vulnerabilities=[{"VulnerabilityID": "CVE-X", "Severity": "critical"}]
        )

        with patch("subprocess.run", return_value=_completed(stdout=payload)):
            result = TrivyCVEScanAdapter().scan_image("app:v1")

        assert result["cves"] == []

    def test_non_dict_json_payload_is_unscanned_not_raised(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        with patch(
            "subprocess.run", return_value=_completed(stdout=json.dumps(["not", "a", "dict"]))
        ):
            result = TrivyCVEScanAdapter().scan_image("app:v1")

        assert result["scan_status"] == "unscanned"

    def test_detects_base_image_from_os_metadata(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        payload = _trivy_payload(os_family="ubuntu", os_name="18.04")

        with patch("subprocess.run", return_value=_completed(stdout=payload)):
            result = TrivyCVEScanAdapter().scan_image("legacy-tool:v1")

        assert result["detected_base_image"] == "ubuntu:18.04"

    def test_no_os_metadata_is_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        with patch("subprocess.run", return_value=_completed(stdout=_trivy_payload())):
            result = TrivyCVEScanAdapter().scan_image("app:v1")

        assert result["detected_base_image"] is None

    def test_scanned_at_is_populated_on_success(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        with patch("subprocess.run", return_value=_completed(stdout=_trivy_payload())):
            result = TrivyCVEScanAdapter().scan_image("app:v1")

        assert result["scanned_at"] is not None


class TestScanImageGracefulFailure:
    def test_missing_trivy_binary_is_unscanned_not_raised(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        with patch("subprocess.run", side_effect=FileNotFoundError()):
            result = TrivyCVEScanAdapter().scan_image("app:v1")

        assert result["scan_status"] == "unscanned"
        assert result["cves"] == []
        assert result["scanned_at"] is None

    def test_timeout_is_unscanned_not_raised(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        with patch(
            "subprocess.run", side_effect=subprocess.TimeoutExpired(cmd="trivy", timeout=60.0)
        ):
            result = TrivyCVEScanAdapter().scan_image("app:v1")

        assert result["scan_status"] == "unscanned"

    def test_non_zero_exit_code_is_unscanned_not_raised(self) -> None:
        """Edge Case 1: private registry, auth required -> scan skipped,
        image listed as unscanned (trivy exits non-zero on pull failure)."""
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        with patch("subprocess.run", return_value=_completed(returncode=1, stderr="unauthorized")):
            result = TrivyCVEScanAdapter().scan_image("private-registry.example.com/app:v1")

        assert result["scan_status"] == "unscanned"

    def test_invalid_json_output_is_unscanned_not_raised(self) -> None:
        from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

        with patch("subprocess.run", return_value=_completed(stdout="not json")):
            result = TrivyCVEScanAdapter().scan_image("app:v1")

        assert result["scan_status"] == "unscanned"
