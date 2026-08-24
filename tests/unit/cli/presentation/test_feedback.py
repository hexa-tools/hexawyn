"""Unit tests for cli/presentation/feedback.py — emoji step rendering."""

from __future__ import annotations

from hexawyn.cli.presentation.feedback import fail, header, ok, step, success


class TestFeedbackRenderers:
    def test_step_prints_spinner_label(self, capsys) -> None:
        step("Checking PyPI")

        assert "Checking PyPI" in capsys.readouterr().err

    def test_ok_prints_check_emoji(self, capsys) -> None:
        ok("Detected")

        assert "Detected" in capsys.readouterr().out

    def test_success_prints_celebration(self, capsys) -> None:
        success("Up to date")

        assert "Up to date" in capsys.readouterr().out

    def test_fail_prints_cross_and_goes_to_stderr(self, capsys) -> None:
        fail("boom")

        captured = capsys.readouterr()
        assert "boom" in captured.err
        assert "boom" not in captured.out


class TestHeader:
    def test_header_renders_logo_and_version(self, capsys) -> None:
        header()

        out = capsys.readouterr().out
        assert "█" in out
        assert "v0.1.0b7" in out
