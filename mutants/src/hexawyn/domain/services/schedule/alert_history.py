from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.alert_notification_port import (
    AlertMessage,
    AlertNotificationPort,
)

if TYPE_CHECKING:
    from duckdb import DuckDBPyConnection


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAlertHistoryDecoratorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut: MutantDict = {}  # type: ignore


class AlertHistoryDecorator(AlertNotificationPort):
    @_mutmut_mutated(mutants_xǁAlertHistoryDecoratorǁ__init____mutmut)
    def __init__(
        self,
        real_port: AlertNotificationPort,
        connection: DuckDBPyConnection,
    ) -> None:
        self._real = real_port
        self._conn = connection
        self._ensure_schema()
    def xǁAlertHistoryDecoratorǁ__init____mutmut_orig(
        self,
        real_port: AlertNotificationPort,
        connection: DuckDBPyConnection,
    ) -> None:
        self._real = real_port
        self._conn = connection
        self._ensure_schema()
    def xǁAlertHistoryDecoratorǁ__init____mutmut_1(
        self,
        real_port: AlertNotificationPort,
        connection: DuckDBPyConnection,
    ) -> None:
        self._real = None
        self._conn = connection
        self._ensure_schema()
    def xǁAlertHistoryDecoratorǁ__init____mutmut_2(
        self,
        real_port: AlertNotificationPort,
        connection: DuckDBPyConnection,
    ) -> None:
        self._real = real_port
        self._conn = None
        self._ensure_schema()

    @_mutmut_mutated(mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut)
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

    def xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_orig(self) -> None:
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

    def xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_1(self) -> None:
        self._conn.execute(None)
        self._conn.execute("CREATE INDEX IF NOT EXISTS idx_alerts_timestamp ON alerts(timestamp)")
        self._conn.execute("CREATE INDEX IF NOT EXISTS idx_alerts_check_name ON alerts(check_name)")

    def xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_2(self) -> None:
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
        self._conn.execute(None)
        self._conn.execute("CREATE INDEX IF NOT EXISTS idx_alerts_check_name ON alerts(check_name)")

    def xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_3(self) -> None:
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
        self._conn.execute("XXCREATE INDEX IF NOT EXISTS idx_alerts_timestamp ON alerts(timestamp)XX")
        self._conn.execute("CREATE INDEX IF NOT EXISTS idx_alerts_check_name ON alerts(check_name)")

    def xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_4(self) -> None:
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
        self._conn.execute("create index if not exists idx_alerts_timestamp on alerts(timestamp)")
        self._conn.execute("CREATE INDEX IF NOT EXISTS idx_alerts_check_name ON alerts(check_name)")

    def xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_5(self) -> None:
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
        self._conn.execute("CREATE INDEX IF NOT EXISTS IDX_ALERTS_TIMESTAMP ON ALERTS(TIMESTAMP)")
        self._conn.execute("CREATE INDEX IF NOT EXISTS idx_alerts_check_name ON alerts(check_name)")

    def xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_6(self) -> None:
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
        self._conn.execute(None)

    def xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_7(self) -> None:
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
        self._conn.execute("XXCREATE INDEX IF NOT EXISTS idx_alerts_check_name ON alerts(check_name)XX")

    def xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_8(self) -> None:
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
        self._conn.execute("create index if not exists idx_alerts_check_name on alerts(check_name)")

    def xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_9(self) -> None:
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
        self._conn.execute("CREATE INDEX IF NOT EXISTS IDX_ALERTS_CHECK_NAME ON ALERTS(CHECK_NAME)")

    @_mutmut_mutated(mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut)
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_orig(self, message: AlertMessage) -> bool:
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_1(self, message: AlertMessage) -> bool:
        success = None
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_2(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(None)
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_3(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            None,
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_4(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            None,
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_5(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_6(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_7(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "XXINSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) XX"  # noqa: E501
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_8(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "insert into alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_9(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO ALERTS (CLUSTER_NAME, CHECK_NAME, SEVERITY, TITLE, TEXT, SOURCE, NOTIFIED, DELIVERY_STATUS, TIMESTAMP) "  # noqa: E501
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_10(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "XXVALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)XX",
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_11(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "values (?, ?, ?, ?, ?, ?, ?, ?, ?)",
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_12(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get(None, "default"),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_13(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", None),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_14(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("default"),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_15(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", ),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_16(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("XXcluster_nameXX", "default"),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_17(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("CLUSTER_NAME", "default"),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_18(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "XXdefaultXX"),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_19(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "DEFAULT"),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_20(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get(None, ""),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_21(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", None),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_22(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get(""),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_23(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_24(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("XXtitleXX", ""),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_25(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("TITLE", ""),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_26(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", "XXXX"),
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

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_27(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get(None, "info"),
                message.get("title"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_28(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", None),
                message.get("title"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_29(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("info"),
                message.get("title"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_30(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", ),
                message.get("title"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_31(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("XXseverityXX", "info"),
                message.get("title"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_32(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("SEVERITY", "info"),
                message.get("title"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_33(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", "XXinfoXX"),
                message.get("title"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_34(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", "INFO"),
                message.get("title"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_35(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", "info"),
                message.get(None),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_36(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", "info"),
                message.get("XXtitleXX"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_37(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", "info"),
                message.get("TITLE"),
                message.get("text"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_38(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", "info"),
                message.get("title"),
                message.get(None),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_39(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", "info"),
                message.get("title"),
                message.get("XXtextXX"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_40(self, message: AlertMessage) -> bool:
        success = self._real.send_alert(message)
        self._conn.execute(
            "INSERT INTO alerts (cluster_name, check_name, severity, title, text, source, notified, delivery_status, timestamp) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                message.get("cluster_name", "default"),
                message.get("title", ""),
                message.get("severity", "info"),
                message.get("title"),
                message.get("TEXT"),
                "scheduler",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_41(self, message: AlertMessage) -> bool:
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
                "XXschedulerXX",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_42(self, message: AlertMessage) -> bool:
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
                "SCHEDULER",
                success,
                "sent" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_43(self, message: AlertMessage) -> bool:
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
                "XXsentXX" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_44(self, message: AlertMessage) -> bool:
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
                "SENT" if success else "failed",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_45(self, message: AlertMessage) -> bool:
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
                "sent" if success else "XXfailedXX",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_46(self, message: AlertMessage) -> bool:
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
                "sent" if success else "FAILED",
                datetime.now(UTC),
            ],
        )
        return success

    def xǁAlertHistoryDecoratorǁsend_alert__mutmut_47(self, message: AlertMessage) -> bool:
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
                datetime.now(None),
            ],
        )
        return success

    @_mutmut_mutated(mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut)
    def format_finding_alert(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(finding, cluster_name, score, is_pro)

    def xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_orig(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(finding, cluster_name, score, is_pro)

    def xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_1(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = True,
    ) -> AlertMessage:
        return self._real.format_finding_alert(finding, cluster_name, score, is_pro)

    def xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_2(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(None, cluster_name, score, is_pro)

    def xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_3(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(finding, None, score, is_pro)

    def xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_4(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(finding, cluster_name, None, is_pro)

    def xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_5(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(finding, cluster_name, score, None)

    def xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_6(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(cluster_name, score, is_pro)

    def xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_7(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(finding, score, is_pro)

    def xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_8(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(finding, cluster_name, is_pro)

    def xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_9(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        return self._real.format_finding_alert(finding, cluster_name, score, )

mutants_xǁAlertHistoryDecoratorǁ__init____mutmut['_mutmut_orig'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ__init____mutmut['xǁAlertHistoryDecoratorǁ__init____mutmut_1'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ__init____mutmut['xǁAlertHistoryDecoratorǁ__init____mutmut_2'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut['_mutmut_orig'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut['xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_1'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut['xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_2'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut['xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_3'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut['xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_4'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut['xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_5'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut['xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_6'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut['xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_7'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut['xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_8'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut['xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_9'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁ_ensure_schema__mutmut_9 # type: ignore # mutmut generated

mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['_mutmut_orig'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_1'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_2'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_3'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_4'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_5'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_6'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_7'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_8'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_9'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_10'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_11'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_12'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_13'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_14'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_15'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_16'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_17'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_18'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_19'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_20'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_21'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_22'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_23'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_24'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_25'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_26'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_27'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_28'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_29'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_30'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_31'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_32'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_33'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_34'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_35'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_36'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_37'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_38'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_39'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_40'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_41'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_42'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_43'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_44'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_45'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_46'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁsend_alert__mutmut['xǁAlertHistoryDecoratorǁsend_alert__mutmut_47'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁsend_alert__mutmut_47 # type: ignore # mutmut generated

mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut['_mutmut_orig'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut['xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_1'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut['xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_2'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut['xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_3'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut['xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_4'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut['xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_5'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut['xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_6'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut['xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_7'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut['xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_8'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut['xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_9'] = AlertHistoryDecorator.xǁAlertHistoryDecoratorǁformat_finding_alert__mutmut_9 # type: ignore # mutmut generated
