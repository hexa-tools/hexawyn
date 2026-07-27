"""Tests for machine_id.py — hardware fingerprint generation."""

import platform
import tempfile
from pathlib import Path
from unittest.mock import patch

from hexawyn.infrastructure.config import machine_id as machine_id_mod
from hexawyn.infrastructure.config.machine_id import (
    _hardware_fingerprint,
    _linux_machine_id,
    _macos_platform_uuid,
    _read_stored,
    _validate_or_repair,
    _windows_machine_guid,
    get_machine_id,
    get_machine_id_short,
)


class TestLinuxMachineId:
    def test_returns_content_of_etc_machine_id(self) -> None:
        with tempfile.NamedTemporaryFile(suffix=".machine_id") as f:
            f.write(b"abc123def456\n")
            f.flush()
            with patch("hexawyn.infrastructure.config.machine_id.Path") as mock_path:
                mock_path.side_effect = (
                    lambda p: Path(p) if str(p) != "/etc/machine-id" else Path(f.name)
                )
                result = _linux_machine_id()
            assert result is not None

    def test_returns_none_when_no_file(self) -> None:
        with patch("pathlib.Path.exists", return_value=False):
            result = _linux_machine_id()
            assert result is None


class TestWindowsMachineGuid:
    def test_handles_exception_gracefully(self) -> None:
        with patch("builtins.__import__", side_effect=ImportError):
            result = _windows_machine_guid()
            assert result is None


class TestMacosPlatformUuid:
    def test_handles_exception_gracefully(self) -> None:
        with patch("subprocess.run", side_effect=FileNotFoundError):
            result = _macos_platform_uuid()
            assert result is None

    def test_returns_none_when_ioreg_fails(self) -> None:
        import subprocess

        with patch.object(subprocess, "run", side_effect=subprocess.TimeoutExpired("ioreg", 5)):
            result = _macos_platform_uuid()
            assert result is None


class TestHardwareFingerprint:
    def test_returns_24_char_hex_string(self) -> None:
        fp = _hardware_fingerprint()
        assert len(fp) == 24  # noqa: PLR2004

    def test_same_machine_same_fingerprint(self) -> None:
        fp1 = _hardware_fingerprint()
        fp2 = _hardware_fingerprint()
        assert fp1 == fp2

    def test_uses_windows_guid_when_on_windows(self) -> None:
        with patch.object(platform, "system", return_value="Windows"):
            with patch.object(
                machine_id_mod,
                "_windows_machine_guid",
                return_value="win-guid-123",
            ):
                fp = _hardware_fingerprint()
                assert len(fp) == 24  # noqa: PLR2004


class TestReadStored:
    def test_returns_none_when_file_missing(self) -> None:
        with patch.object(Path, "exists", return_value=False):
            assert _read_stored() is None

    def test_returns_none_for_short_content(self) -> None:
        valid = "short"
        with tempfile.NamedTemporaryFile(suffix=".id", delete=False) as f:
            f.write(valid.encode())
            f.flush()
        try:
            with patch.object(machine_id_mod, "MACHINE_ID_PATH", Path(f.name)):
                result = _read_stored()
                assert result is None
        finally:
            Path(f.name).unlink()

    def test_returns_content_when_valid(self) -> None:
        valid = "a" * 24
        with tempfile.NamedTemporaryFile(suffix=".id", delete=False) as f:
            f.write(valid.encode())
            f.flush()
        try:
            with patch.object(machine_id_mod, "MACHINE_ID_PATH", Path(f.name)):
                result = _read_stored()
                assert result == valid
        finally:
            Path(f.name).unlink()


class TestValidateOrRepair:
    def test_keeps_stored_when_matches_hardware(self) -> None:
        fp = _hardware_fingerprint()
        assert _validate_or_repair(fp) == fp

    def test_replaces_when_mismatch(self) -> None:
        with patch.object(
            machine_id_mod,
            "_hardware_fingerprint",
            return_value="new-fp-new-fp-new-fp-aa",
        ):
            result = _validate_or_repair("old-fp-old-fp-old-fp-zz")
            assert result == "new-fp-new-fp-new-fp-aa"


class TestGetMachineId:
    def test_returns_fingerprint_on_first_call(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fake_path = Path(tmp) / ".machine_id"
            with patch.object(machine_id_mod, "MACHINE_ID_PATH", fake_path):
                fp = get_machine_id()
                assert len(fp) == 24  # noqa: PLR2004
                assert fake_path.exists()

    def test_returns_stored_on_second_call(self) -> None:
        stored = "stored-fp-stored-fp-ok"
        with tempfile.TemporaryDirectory() as tmp:
            fake_path = Path(tmp) / ".machine_id"
            fake_path.write_text(stored)
            with patch.object(machine_id_mod, "MACHINE_ID_PATH", fake_path):
                with patch.object(
                    machine_id_mod,
                    "_hardware_fingerprint",
                    return_value=stored,
                ):
                    fp = get_machine_id()
                    assert fp == stored


class TestGetMachineIdShort:
    def test_returns_12_chars(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fake_path = Path(tmp) / ".machine_id"
            fake_path.write_text("a" * 24)
            with patch.object(machine_id_mod, "MACHINE_ID_PATH", fake_path):
                sid = get_machine_id_short()
                assert len(sid) == 12  # noqa: PLR2004
