"""RED → GREEN — AlertHistoryDecorator (persistance des alertes)."""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock, call

from hexawyn.application.ports.driven.alert_notification_port import AlertMessage
from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

_CREATE_TABLE_SQL = """
            CREATE TABLE IF NOT EXISTS alerts (
                id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                timestamp TIMESTAMPTZ DEFAULT now(),
                cluster_name VARCHAR NOT NULL DEFAULT 'default',
                check_name VARCHAR,
                severity VARCHAR NOT NULL DEFAULT 'info',
                title VARCHAR,
                text TEXT NOT NULL,
                source VARCHAR NOT NULL DEFAULT 'scheduler',
                notified BOOLEAN DEFAULT FALSE,
                delivery_status VARCHAR DEFAULT 'sent'
            )
        """
_INDEX_TIMESTAMP_SQL = "CREATE INDEX IF NOT EXISTS idx_alerts_timestamp ON alerts(timestamp)"
_INDEX_CHECK_NAME_SQL = "CREATE INDEX IF NOT EXISTS idx_alerts_check_name ON alerts(check_name)"
_INSERT_SQL = (
    "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
)


def _full_message() -> AlertMessage:
    return {
        "text": "Certificate expiring in 5 days",
        "title": "certs_detect",
        "severity": "critical",
        "remediation": None,
        "cluster_name": "prod-eu",
        "score": 42,
        "is_pro": True,
    }


class TestEnsureSchema:
    def test_creates_table_and_indexes_on_init(self) -> None:
        connection = MagicMock()
        real_port = MagicMock()

        AlertHistoryDecorator(real_port=real_port, connection=connection)

        assert connection.execute.call_args_list == [
            call(_CREATE_TABLE_SQL),
            call(_INDEX_TIMESTAMP_SQL),
            call(_INDEX_CHECK_NAME_SQL),
        ]


class TestSendAlert:
    def test_success_records_sent_with_full_message(self) -> None:
        connection = MagicMock()
        real_port = MagicMock()
        real_port.send_alert.return_value = True
        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        message = _full_message()

        success = decorator.send_alert(message)

        assert success is True
        real_port.send_alert.assert_called_once_with(message)
        sql, params = connection.execute.call_args.args
        assert sql == _INSERT_SQL
        assert params[:8] == [
            "prod-eu",
            "certs_detect",
            "critical",
            "certs_detect",
            "Certificate expiring in 5 days",
            "scheduler",
            True,
            "sent",
        ]
        assert isinstance(params[8], datetime)
        assert params[8].tzinfo is UTC

    def test_failure_records_failed_status(self) -> None:
        connection = MagicMock()
        real_port = MagicMock()
        real_port.send_alert.return_value = False
        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        message = _full_message()

        success = decorator.send_alert(message)

        assert success is False
        sql, params = connection.execute.call_args.args
        assert sql == _INSERT_SQL
        assert params[:8] == [
            "prod-eu",
            "certs_detect",
            "critical",
            "certs_detect",
            "Certificate expiring in 5 days",
            "scheduler",
            False,
            "failed",
        ]

    def test_missing_keys_use_defaults(self) -> None:
        connection = MagicMock()
        real_port = MagicMock()
        real_port.send_alert.return_value = True
        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)

        decorator.send_alert({"text": "something happened"})

        sql, params = connection.execute.call_args.args
        assert sql == _INSERT_SQL
        assert params[:8] == [
            "default",
            "",
            "info",
            None,
            "something happened",
            "scheduler",
            True,
            "sent",
        ]


class TestFormatFindingAlert:
    def test_delegates_with_explicit_pro_flag(self) -> None:
        connection = MagicMock()
        real_port = MagicMock()
        real_port.format_finding_alert.return_value = _full_message()
        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        finding = {"cluster": "prod-eu"}

        result = decorator.format_finding_alert(finding, "prod-eu", 42, is_pro=True)

        assert result == _full_message()
        real_port.format_finding_alert.assert_called_once_with(finding, "prod-eu", 42, True)

    def test_delegates_with_default_pro_flag_false(self) -> None:
        connection = MagicMock()
        real_port = MagicMock()
        real_port.format_finding_alert.return_value = _full_message()
        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        finding = {"cluster": "prod-eu"}

        decorator.format_finding_alert(finding, "prod-eu", 42)

        real_port.format_finding_alert.assert_called_once_with(finding, "prod-eu", 42, False)
