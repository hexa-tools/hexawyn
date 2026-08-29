"""Unit tests for the session clipboard/export helpers."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.cli.screens.session.clipboard import (
    copy_to_clipboard,
    open_in_editor,
    write_export_file,
)


class TestCopyToClipboard:
    def test_darwin_uses_pbcopy(self) -> None:
        with (
            patch("platform.system", return_value="Darwin"),
            patch("subprocess.run") as mock_run,
        ):
            assert copy_to_clipboard("hello") == "✓ Copied to clipboard"
        mock_run.assert_called_once_with(["pbcopy"], input=b"hello", check=True)

    def test_linux_wl_copy_first(self) -> None:
        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.run") as mock_run,
        ):
            assert copy_to_clipboard("hello") == "✓ Copied to clipboard"
        mock_run.assert_called_once_with(["wl-copy"], input=b"hello", check=True)

    def test_linux_falls_back_to_xclip(self) -> None:
        def fake_run(cmd, **kwargs):  # type: ignore[no-untyped-def]
            if cmd == ["wl-copy"]:
                raise FileNotFoundError("wl-copy missing")
            return MagicMock()

        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.run", side_effect=fake_run),
        ):
            assert copy_to_clipboard("hello") == "✓ Copied to clipboard"

    def test_linux_no_tool_hints_install(self) -> None:
        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.run", side_effect=FileNotFoundError("missing")),
        ):
            assert "xclip or wl-clipboard" in copy_to_clipboard("hello")

    def test_unsupported_system(self) -> None:
        with patch("platform.system", return_value="Windows"):
            assert "not supported" in copy_to_clipboard("hello")

    def test_failure_returns_failed_message(self) -> None:
        with (
            patch("platform.system", return_value="Darwin"),
            patch("subprocess.run", side_effect=OSError("denied")),
        ):
            assert "Copy failed" in copy_to_clipboard("hello")


class TestWriteExportFile:
    def test_writes_text_and_returns_path(self) -> None:
        mock_file = MagicMock()
        mock_file.name = "/tmp/out.txt"
        with patch("tempfile.NamedTemporaryFile") as mock_tmp:
            mock_tmp.return_value.__enter__.return_value = mock_file
            assert write_export_file("the answer") == "/tmp/out.txt"
        mock_file.write.assert_called_once_with("the answer")


class TestOpenInEditor:
    def test_darwin_open(self) -> None:
        with (
            patch("platform.system", return_value="Darwin"),
            patch("subprocess.Popen") as mock_popen,
        ):
            open_in_editor("/tmp/out.txt")
        mock_popen.assert_called_once_with(["open", "/tmp/out.txt"])

    def test_linux_xdg_open(self) -> None:
        with (
            patch("platform.system", return_value="Linux"),
            patch("subprocess.Popen") as mock_popen,
        ):
            open_in_editor("/tmp/out.txt")
        mock_popen.assert_called_once_with(["xdg-open", "/tmp/out.txt"])

    def test_other_system_noop(self) -> None:
        with (
            patch("platform.system", return_value="Windows"),
            patch("subprocess.Popen") as mock_popen,
        ):
            open_in_editor("/tmp/out.txt")
        mock_popen.assert_not_called()
