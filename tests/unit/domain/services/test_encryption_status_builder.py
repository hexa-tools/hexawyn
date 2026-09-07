from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumEncryptionStatusResult
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

    def test_type_present_enabled_absent_not_unknown(self) -> None:
        # only one of the two is None -> not the both-None early return
        assert deduce_encryption_mode("wireguard", None) == "wireguard"

    def test_type_absent_enabled_present_not_unknown(self) -> None:
        assert deduce_encryption_mode(None, "false") == "none"

    def test_mode_case_insensitive(self) -> None:
        assert deduce_encryption_mode("WireGuard", "true") == "wireguard"

    def test_mode_whitespace_stripped(self) -> None:
        assert deduce_encryption_mode("  ipsec  ", "true") == "ipsec"

    def test_enabled_value_one(self) -> None:
        assert deduce_encryption_mode("mystery", "1") == "UNKNOWN"

    def test_enabled_value_yes(self) -> None:
        assert deduce_encryption_mode("mystery", "yes") == "UNKNOWN"

    def test_enabled_value_enabled(self) -> None:
        assert deduce_encryption_mode("mystery", "enabled") == "UNKNOWN"

    def test_enabled_value_uppercase_true(self) -> None:
        assert deduce_encryption_mode("mystery", "TRUE") == "UNKNOWN"

    def test_disabled_uppercase_false_is_none(self) -> None:
        assert deduce_encryption_mode("", "FALSE") == "none"


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

    def test_enabled_exact_result(self) -> None:
        result = build_encryption_status("ipsec", 2, 5)  # noqa: PLR2004

        assert result == CiliumEncryptionStatusResult(
            installed=True,
            status="enabled",
            mode="ipsec",
            encrypted_nodes=2,  # noqa: PLR2004
            total_nodes=5,  # noqa: PLR2004
            coverage="2/5",
            note=None,
        )

    def test_single_node_still_has_coverage(self) -> None:
        result = build_encryption_status("wireguard", 1, 1)

        assert result.coverage == "1/1"

    def test_unknown_exact_result(self) -> None:
        result = build_encryption_status("UNKNOWN", 0, 0)

        assert result == CiliumEncryptionStatusResult(
            installed=True,
            status="unknown",
            mode="UNKNOWN",
            encrypted_nodes=0,
            total_nodes=0,
            coverage=None,
            note=None,
        )


class TestNotInstalledEncryptionStatus:
    def test_returns_marker(self) -> None:
        result = not_installed_encryption_status()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.mode == "UNKNOWN"
        assert result.note is not None

    def test_exact_dataclass(self) -> None:
        result = not_installed_encryption_status()

        assert result == CiliumEncryptionStatusResult(
            installed=False,
            status="not_installed",
            mode="UNKNOWN",
            encrypted_nodes=0,
            total_nodes=0,
            coverage=None,
            note="Cilium is not installed in this cluster",
        )


class TestUnknownEncryptionStatus:
    def test_returns_unknown(self) -> None:
        result = unknown_encryption_status()
        assert result.installed is True
        assert result.status == "unknown"
        assert result.mode == "UNKNOWN"
        assert result.note is not None

    def test_exact_dataclass(self) -> None:
        result = unknown_encryption_status()

        assert result == CiliumEncryptionStatusResult(
            installed=True,
            status="unknown",
            mode="UNKNOWN",
            encrypted_nodes=0,
            total_nodes=0,
            coverage=None,
            note="Cilium encryption configuration could not be established",
        )
