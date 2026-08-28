from __future__ import annotations

from hexawyn.domain.services.cilium.encryption_status_builder import (
    build_encryption_status,
    deduce_encryption_mode,
    not_installed_encryption_status,
    unknown_encryption_status,
)


class TestDeduceEncryptionMode:
    def test_wireguard(self) -> None:
        assert deduce_encryption_mode("wireguard", "true") == "wireguard"

    def test_ipsec(self) -> None:
        assert deduce_encryption_mode("ipsec", "true") == "ipsec"

    def test_none_when_disabled(self) -> None:
        assert deduce_encryption_mode("", "false") == "none"

    def test_unknown_when_unreadable(self) -> None:
        assert deduce_encryption_mode(None, None) == "UNKNOWN"

    def test_unknown_when_enabled_with_unknown_type(self) -> None:
        assert deduce_encryption_mode("mystery", "true") == "UNKNOWN"


class TestBuildEncryptionStatus:
    def test_wireguard_enabled_with_coverage(self) -> None:
        result = build_encryption_status("wireguard", 3, 4)
        assert result.status == "enabled"
        assert result.coverage == "3/4"
        assert result.encrypted_nodes == 3  # noqa: PLR2004

    def test_none_disabled_zero_coverage(self) -> None:
        result = build_encryption_status("none", 4, 4)
        assert result.status == "disabled"
        assert result.encrypted_nodes == 0
        assert result.coverage == "0/4"

    def test_unknown_mode(self) -> None:
        result = build_encryption_status("UNKNOWN", 0, 4)
        assert result.status == "unknown"
        assert result.coverage == "0/4"

    def test_no_coverage_when_no_nodes(self) -> None:
        result = build_encryption_status("wireguard", 0, 0)
        assert result.coverage is None


class TestNotInstalledEncryptionStatus:
    def test_returns_marker(self) -> None:
        result = not_installed_encryption_status()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.mode == "UNKNOWN"
        assert result.note is not None


class TestUnknownEncryptionStatus:
    def test_returns_unknown(self) -> None:
        result = unknown_encryption_status()
        assert result.installed is True
        assert result.status == "unknown"
        assert result.mode == "UNKNOWN"
        assert result.note is not None
