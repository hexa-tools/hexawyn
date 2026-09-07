from unittest.mock import patch


class TestFindings:
    def test_crashloop_detected(self) -> None:
        from hexawyn.cli.presentation.findings import format_finding_warnings

        findings = [
            {"type": "CrashLoopBackOff", "severity": "high"},
            {"type": "Other", "severity": "low"},
        ]
        with (
            patch("hexawyn.cli.presentation.findings.crashloop_finding_count", return_value=2),
            patch("hexawyn.cli.presentation.findings.restarting_finding_count", return_value=0),
        ):
            lines = format_finding_warnings(findings)
        assert any("2 CrashLoopBackOff detected" in line for line in lines)
        assert any("\u26a0" in line for line in lines)

    def test_restarting_frequently(self) -> None:
        from hexawyn.cli.presentation.findings import format_finding_warnings

        findings = [{"type": "anything"}]
        with (
            patch("hexawyn.cli.presentation.findings.crashloop_finding_count", return_value=0),
            patch("hexawyn.cli.presentation.findings.restarting_finding_count", return_value=3),
        ):
            lines = format_finding_warnings(findings)
        assert any("3 pods with high restart count" in line for line in lines)

    def test_no_warnings_shows_green(self) -> None:
        from hexawyn.cli.presentation.findings import format_finding_warnings

        findings: list[dict[str, object]] = []
        with (
            patch("hexawyn.cli.presentation.findings.crashloop_finding_count", return_value=0),
            patch("hexawyn.cli.presentation.findings.restarting_finding_count", return_value=0),
        ):
            lines = format_finding_warnings(findings)
        assert any("No active warnings" in line for line in lines)
        assert any("green" in line for line in lines)
