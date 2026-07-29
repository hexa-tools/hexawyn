from __future__ import annotations

from unittest.mock import patch

from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import (
    TrivyCVEScanAdapter,
    _detect_base_image,
    _parse_trivy_payload,
    _to_cve_raw,
    _unscanned_result,
)


class TestTrivyCVEScanAdapter:
    def test_scan_image_trivy_not_found_returns_unscanned(self) -> None:
        with patch("subprocess.run", side_effect=FileNotFoundError):
            adapter = TrivyCVEScanAdapter()
            result = adapter.scan_image("nginx:latest")
            assert result["scan_status"] == "unscanned"

    def test_scan_image_nonzero_return_returns_unscanned(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value.returncode = 1
            adapter = TrivyCVEScanAdapter()
            result = adapter.scan_image("nginx:latest")
            assert result["scan_status"] == "unscanned"

    def test_scan_image_invalid_json_returns_unscanned(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value.returncode = 0
            mock_run.return_value.stdout = "not json"
            adapter = TrivyCVEScanAdapter()
            result = adapter.scan_image("nginx:latest")
            assert result["scan_status"] == "unscanned"

    def test_scan_image_success(self) -> None:
        payload = {
            "Results": [
                {
                    "Target": "nginx:latest (debian 11.6)",
                    "Vulnerabilities": [
                        {
                            "VulnerabilityID": "CVE-2023-1234",
                            "Severity": "HIGH",
                            "PkgName": "libssl1.1",
                            "FixedVersion": "1.1.1n-0+deb11u5",
                        }
                    ],
                }
            ],
            "Metadata": {"OS": {"Family": "debian", "Name": "11.6"}},
        }
        import json

        with patch("subprocess.run") as mock_run:
            mock_run.return_value.returncode = 0
            mock_run.return_value.stdout = json.dumps(payload)
            adapter = TrivyCVEScanAdapter()
            result = adapter.scan_image("nginx:latest")
            assert result["scan_status"] == "scanned"
            assert len(result["cves"]) == 1
            assert result["cves"][0]["cve_id"] == "CVE-2023-1234"
            assert result["cves"][0]["severity"] == "high"
            assert result["detected_base_image"] == "debian:11.6"


class TestParseTrivyPayload:
    def test_non_dict_returns_unscanned(self) -> None:
        result = _parse_trivy_payload([])
        assert result["scan_status"] == "unscanned"

    def test_empty_results(self) -> None:
        result = _parse_trivy_payload({"Results": []})
        assert result["scan_status"] == "scanned"
        assert result["cves"] == []


class TestToCveRaw:
    def test_valid_vulnerability(self) -> None:
        result = _to_cve_raw(
            {
                "VulnerabilityID": "CVE-2023-0001",
                "Severity": "CRITICAL",
                "PkgName": "openssl",
                "FixedVersion": "3.0.7",
            }
        )
        assert result is not None
        assert result["cve_id"] == "CVE-2023-0001"
        assert result["severity"] == "critical"
        assert result["fix_version"] == "3.0.7"

    def test_missing_fields_returns_none(self) -> None:
        assert _to_cve_raw({}) is None

    def test_unknown_severity_returns_none(self) -> None:
        result = _to_cve_raw(
            {
                "VulnerabilityID": "CVE-2023-0001",
                "Severity": "UNKNOWN",
                "PkgName": "openssl",
            }
        )
        assert result is None


class TestDetectBaseImage:
    def test_detects_base_image(self) -> None:
        result = _detect_base_image({"Metadata": {"OS": {"Family": "alpine", "Name": "3.18"}}})
        assert result == "alpine:3.18"

    def test_missing_os_returns_none(self) -> None:
        assert _detect_base_image({}) is None


class TestUnscannedResult:
    def test_returns_unscanned_status(self) -> None:
        result = _unscanned_result()
        assert result["scan_status"] == "unscanned"
        assert result["cves"] == []
        assert result["detected_base_image"] is None
