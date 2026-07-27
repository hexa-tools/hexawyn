from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.alert_notification_port import (
    AlertMessage,
    AlertNotificationPort,
)

if TYPE_CHECKING:
    from duckdb import DuckDBPyConnection


class AlertHistoryDecorator(AlertNotificationPort):
    def __init__(
        self,
        real_port: AlertNotificationPort,
        connection: DuckDBPyConnection,
    ) -> None:
        self._real = real_port
        self._conn = connection
        self._ensure_schema()

    def _ensure_schema(self) -> None:
        self._conn.execute("""
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
        """)
        self._conn.execute("CREATE INDEX IF NOT EXISTS idx_alerts_timestamp ON alerts(timestamp)")
        self._conn.execute("CREATE INDEX IF NOT EXISTS idx_alerts_check_name ON alerts(check_name)")

    def send_alert(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", "info"),
                message.get("title"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def format_finding_alert(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(finding, cluster_name, score, is_pro)
