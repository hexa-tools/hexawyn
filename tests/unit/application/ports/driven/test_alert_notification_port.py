from abc import ABC

import pytest
from hexawyn.application.ports.driven.alert_notification_port import (
    AlertMessage,
    AlertNotificationPort,
)


class TestAlertNotificationPort:
    def test_is_abstract(self) -> None:
        assert issubclass(AlertNotificationPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            AlertNotificationPort()  # type: ignore[abstract]

    def test_send_alert_is_abstract(self) -> None:
        assert getattr(AlertNotificationPort.send_alert, "__isabstractmethod__", False)

    def test_format_finding_alert_is_abstract(self) -> None:
        assert getattr(AlertNotificationPort.format_finding_alert, "__isabstractmethod__", False)


class TestAlertMessage:
    def test_has_required_fields(self) -> None:
        msg = AlertMessage(
            text="OOM detected",
            title="hexawyn Alert — prod-eu",
            severity="critical",
            remediation="increase memory",
            cluster_name="prod-eu",
            score=76,
            is_pro=False,
        )
        assert msg["text"] == "OOM detected"
        assert msg["severity"] == "critical"
        assert msg["is_pro"] is False

    def test_title_and_remediation_can_be_none(self) -> None:
        msg = AlertMessage(
            text="alert",
            title=None,
            severity="info",
            remediation=None,
            cluster_name="staging",
            score=95,
            is_pro=False,
        )
        assert msg["title"] is None
        assert msg["remediation"] is None
