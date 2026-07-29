from __future__ import annotations

from hexawyn.application.use_case.cert_manager.cluster_certificate_health.command import (
    ClusterCertificateHealthCommand,
)


class TestClusterCertificateHealthCommand:
    def test_default_construction(self) -> None:
        command = ClusterCertificateHealthCommand()
        assert command.warning_days == 30  # noqa: PLR2004
        assert command.critical_days == 7  # noqa: PLR2004
        assert command.timeout_seconds == 10.0  # noqa: PLR2004
        assert command.namespace == ""

    def test_custom_values(self) -> None:
        command = ClusterCertificateHealthCommand(
            warning_days=60,
            critical_days=14,
            timeout_seconds=5.0,
            namespace="default",
        )
        assert command.warning_days == 60  # noqa: PLR2004
        assert command.critical_days == 14  # noqa: PLR2004
        assert command.timeout_seconds == 5.0  # noqa: PLR2004
        assert command.namespace == "default"

    def test_is_frozen(self) -> None:
        command = ClusterCertificateHealthCommand()
        try:
            command.warning_days = 99  # type: ignore[misc]
            assert False, "Expected FrozenInstanceError"
        except Exception:
            pass
