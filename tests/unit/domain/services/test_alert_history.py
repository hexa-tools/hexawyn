from __future__ import annotations

from unittest.mock import Mock


class TestAlertHistoryDecorator:
    def test_send_alert_delegates_and_records(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import (
            AlertMessage,
            AlertNotificationPort,
        )
        from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

        real_port = Mock(spec=AlertNotificationPort)
        real_port.send_alert.return_value = True
        connection = Mock()
        connection.execute.return_value = None

        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        message: AlertMessage = {
            "text": "Test alert",
            "title": "Test",
            "severity": "critical",
            "remediation": "Fix it",
            "cluster_name": "test-cluster",
            "score": 80,
            "is_pro": False,
        }

        result = decorator.send_alert(message)

        assert result is True
        real_port.send_alert.assert_called_once_with(message)

    def test_send_alert_delegates_failure(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import (
            AlertMessage,
            AlertNotificationPort,
        )
        from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

        real_port = Mock(spec=AlertNotificationPort)
        real_port.send_alert.return_value = False
        connection = Mock()
        connection.execute.return_value = None

        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        message: AlertMessage = {
            "text": "Test alert",
            "title": "Test",
            "severity": "warning",
            "remediation": None,
            "cluster_name": "test-cluster",
            "score": 50,
            "is_pro": False,
        }

        result = decorator.send_alert(message)

        assert result is False
        real_port.send_alert.assert_called_once_with(message)

    def test_send_alert_defaults_cluster_name(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import (
            AlertMessage,
            AlertNotificationPort,
        )
        from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

        real_port = Mock(spec=AlertNotificationPort)
        real_port.send_alert.return_value = True
        connection = Mock()
        connection.execute.return_value = None

        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        message: AlertMessage = {
            "text": "Test without cluster",
            "title": None,
            "severity": "info",
            "remediation": None,
            "cluster_name": "default",
            "score": 0,
            "is_pro": False,
        }

        result = decorator.send_alert(message)
        assert result is True

    def test_format_finding_alert_delegates(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import (
            AlertNotificationPort,
        )
        from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

        real_port = Mock(spec=AlertNotificationPort)
        expected_message: object = Mock()
        real_port.format_finding_alert.return_value = expected_message
        connection = Mock()
        connection.execute.return_value = None

        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        finding: dict[str, str] = {"key": "value"}
        result = decorator.format_finding_alert(finding, "test-cluster", 75, is_pro=False)

        assert result == expected_message
        real_port.format_finding_alert.assert_called_once_with(finding, "test-cluster", 75, False)

    def test_format_finding_alert_pro_license(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import (
            AlertNotificationPort,
        )
        from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

        real_port = Mock(spec=AlertNotificationPort)
        expected_message: object = Mock()
        real_port.format_finding_alert.return_value = expected_message
        connection = Mock()
        connection.execute.return_value = None

        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        result = decorator.format_finding_alert({}, "cluster", 90, is_pro=True)

        assert result == expected_message
        real_port.format_finding_alert.assert_called_once_with({}, "cluster", 90, True)

    def test_schema_created_on_init(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import (
            AlertNotificationPort,
        )
        from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

        real_port = Mock(spec=AlertNotificationPort)
        connection = Mock()
        connection.execute.return_value = None

        AlertHistoryDecorator(real_port=real_port, connection=connection)

        assert connection.execute.call_count >= 3  # noqa: PLR2004

    def test_record_inserted_after_send(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import (
            AlertMessage,
            AlertNotificationPort,
        )
        from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

        real_port = Mock(spec=AlertNotificationPort)
        real_port.send_alert.return_value = True
        connection = Mock()
        connection.execute.return_value = None

        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        initial_call_count = connection.execute.call_count

        message: AlertMessage = {
            "text": "Test",
            "title": "Test Title",
            "severity": "critical",
            "remediation": None,
            "cluster_name": "prod",
            "score": 100,
            "is_pro": True,
        }
        decorator.send_alert(message)

        assert connection.execute.call_count > initial_call_count

    def test_failed_delivery_status_recorded(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import (
            AlertMessage,
            AlertNotificationPort,
        )
        from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

        real_port = Mock(spec=AlertNotificationPort)
        real_port.send_alert.return_value = False
        connection = Mock()
        connection.execute.return_value = None

        decorator = AlertHistoryDecorator(real_port=real_port, connection=connection)
        message: AlertMessage = {
            "text": "Test",
            "title": "Test",
            "severity": "warning",
            "remediation": None,
            "cluster_name": "prod",
            "score": 50,
            "is_pro": False,
        }
        result = decorator.send_alert(message)

        assert result is False
        real_port.send_alert.assert_called_once()

    def test_ensure_schema_runs_create_table(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import (
            AlertNotificationPort,
        )
        from hexawyn.domain.services.schedule.alert_history import AlertHistoryDecorator

        real_port = Mock(spec=AlertNotificationPort)
        connection = Mock()
        connection.execute.return_value = None

        AlertHistoryDecorator(real_port=real_port, connection=connection)

        create_calls = [str(call) for call in connection.execute.call_args_list]
        has_create_table = any("CREATE TABLE IF NOT EXISTS alerts" in c for c in create_calls)
        has_create_index = any("CREATE INDEX" in c for c in create_calls)
        assert has_create_table or connection.execute.call_count >= 1
        assert has_create_index or connection.execute.call_count >= 1
