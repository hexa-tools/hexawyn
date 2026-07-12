from __future__ import annotations

import hashlib
import json
from collections.abc import Callable
from datetime import UTC, datetime

from hexawyn.application.ports.driven.alert_notification_port import (
    AlertMessage,
    AlertNotificationPort,
)
from hexawyn.application.ports.driven.schedule_store_port import ScheduleStorePort
from hexawyn.domain.models.schedule import CheckPhase, CheckResult, CronCheck

UseCaseRegistry = dict[str, Callable[[dict[str, str]], dict[str, object]]]


class CheckRunnerUseCase:
    """Exécute un CronCheck, détecte les changements d'état, notifie.

    Agnostique du use case : ne connaît que des noms de use case en string,
    résolus via un registre injecté.
    """

    def __init__(
        self,
        store: ScheduleStorePort,
        alert_port: AlertNotificationPort,
        use_case_registry: UseCaseRegistry,
    ) -> None:
        self._store = store
        self._alert_port = alert_port
        self._registry = use_case_registry

    def execute(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
                finished_at=datetime.now(UTC),
                duration_ms=0,
                payload_digest="",
                error_message=f"Use case '{check.use_case}' not found in registry.",
            )

        try:
            output = use_case_fn(check.params)
        except Exception as exc:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
                finished_at=datetime.now(UTC),
                duration_ms=0,
                payload_digest="",
                error_message=str(exc),
            )

        finished = datetime.now(UTC)
        payload_json = json.dumps(output, sort_keys=True, default=str)
        digest = hashlib.sha256(payload_json.encode()).hexdigest()

        previous = self._store.last_result(check.name)
        changed = previous is None or previous.payload_digest != digest

        should_notify = check.notify_policy == "always" or (
            check.notify_policy == "on_change" and changed
        )

        notified = False
        if should_notify:
            notified = self._alert_port.send_alert(
                AlertMessage(
                    text=f"[{check.name}] {check.use_case}: {_summarize(output)}",
                    title=f"Schedule: {check.name}",
                    severity="warning" if changed else "info",
                    remediation=None,
                    cluster_name="default",
                    score=0,
                    is_pro=False,
                )
            )

        phase = CheckPhase.ALERTING.value if changed else CheckPhase.SUCCESS.value

        result = CheckResult(
            check_name=check.name,
            phase=phase,
            started_at=started,
            finished_at=finished,
            duration_ms=int((finished - started).total_seconds() * 1000),
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result


def _summarize(output: dict[str, object]) -> str:
    if not output:
        return "empty response"
    keys = list(output.keys())[:3]
    return ", ".join(keys)  # pragma: no cover — trivial string join
