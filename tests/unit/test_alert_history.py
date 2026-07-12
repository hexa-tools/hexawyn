from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.alert_notification_port import (
    AlertMessage,
    AlertNotificationPort,
)


class TestAlertHistoryDecorator:
    def test_delegates_send_alert(self) -> None:
        real = MagicMock(spec=AlertNotificationPort)
        real.send_alert.return_value = True
        conn = MagicMock()

        with patch("duckdb.connect"):
            from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

            decorator = AlertHistoryDecorator(real_port=real, connection=conn)
            msg: AlertMessage = {
                "text": "test alert",
                "title": "check-name",
                "severity": "warning",
                "remediation": None,
                "cluster_name": "prod",
                "score": 0,
                "is_pro": False,
            }
            result = decorator.send_alert(msg)

        assert result is True
        real.send_alert.assert_called_once_with(msg)
        conn.execute.assert_called()

    def test_records_failure(self) -> None:
        real = MagicMock(spec=AlertNotificationPort)
        real.send_alert.return_value = False
        conn = MagicMock()

        with patch("duckdb.connect"):
            from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

            decorator = AlertHistoryDecorator(real_port=real, connection=conn)
            result = decorator.send_alert(
                {
                    "text": "fail",
                    "title": None,
                    "severity": "critical",
                    "remediation": None,
                    "cluster_name": "default",
                    "score": 0,
                    "is_pro": False,
                }
            )

        assert result is False

    def test_delegates_format_finding(self) -> None:
        real = MagicMock(spec=AlertNotificationPort)
        real.format_finding_alert.return_value = {
            "text": "fmt",
            "title": None,
            "severity": "info",
            "remediation": None,
            "cluster_name": "default",
            "score": 0,
            "is_pro": False,
        }
        conn = MagicMock()

        with patch("duckdb.connect"):
            from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

            decorator = AlertHistoryDecorator(real_port=real, connection=conn)
            result = decorator.format_finding_alert({"key": "val"}, "prod", 10)

        assert result["text"] == "fmt"
        real.format_finding_alert.assert_called_once_with({"key": "val"}, "prod", 10, False)
