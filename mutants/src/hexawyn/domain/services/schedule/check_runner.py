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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCheckRunnerUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CheckRunnerUseCase:
    """Exécute un CronCheck, détecte les changements d'état, notifie.

    Agnostique du use case : ne connaît que des noms de use case en string,
    résolus via un registre injecté.
    """

    @_mutmut_mutated(mutants_xǁCheckRunnerUseCaseǁ__init____mutmut)
    def __init__(
        self,
        store: ScheduleStorePort,
        alert_port: AlertNotificationPort,
        use_case_registry: UseCaseRegistry,
    ) -> None:
        self._store = store
        self._alert_port = alert_port
        self._registry = use_case_registry

    def xǁCheckRunnerUseCaseǁ__init____mutmut_orig(
        self,
        store: ScheduleStorePort,
        alert_port: AlertNotificationPort,
        use_case_registry: UseCaseRegistry,
    ) -> None:
        self._store = store
        self._alert_port = alert_port
        self._registry = use_case_registry

    def xǁCheckRunnerUseCaseǁ__init____mutmut_1(
        self,
        store: ScheduleStorePort,
        alert_port: AlertNotificationPort,
        use_case_registry: UseCaseRegistry,
    ) -> None:
        self._store = None
        self._alert_port = alert_port
        self._registry = use_case_registry

    def xǁCheckRunnerUseCaseǁ__init____mutmut_2(
        self,
        store: ScheduleStorePort,
        alert_port: AlertNotificationPort,
        use_case_registry: UseCaseRegistry,
    ) -> None:
        self._store = store
        self._alert_port = None
        self._registry = use_case_registry

    def xǁCheckRunnerUseCaseǁ__init____mutmut_3(
        self,
        store: ScheduleStorePort,
        alert_port: AlertNotificationPort,
        use_case_registry: UseCaseRegistry,
    ) -> None:
        self._store = store
        self._alert_port = alert_port
        self._registry = None

    @_mutmut_mutated(mutants_xǁCheckRunnerUseCaseǁexecute__mutmut)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_orig(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_1(self, check: CronCheck) -> CheckResult:
        started = None
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_2(self, check: CronCheck) -> CheckResult:
        started = datetime.now(None)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_3(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = None

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_4(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(None)

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_5(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is not None:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_6(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_7(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_8(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_9(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
                finished_at=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_10(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
                finished_at=datetime.now(UTC),
                duration_ms=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_11(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
                finished_at=datetime.now(UTC),
                duration_ms=0,
                payload_digest=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_12(self, check: CronCheck) -> CheckResult:
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
                error_message=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_13(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_14(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_15(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_16(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_17(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
                finished_at=datetime.now(UTC),
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_18(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
                finished_at=datetime.now(UTC),
                duration_ms=0,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_19(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_20(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
                finished_at=datetime.now(None),
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_21(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
                finished_at=datetime.now(UTC),
                duration_ms=1,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_22(self, check: CronCheck) -> CheckResult:
        started = datetime.now(UTC)
        use_case_fn = self._registry.get(check.use_case)

        if use_case_fn is None:
            return CheckResult(
                check_name=check.name,
                phase=CheckPhase.FAILED.value,
                started_at=started,
                finished_at=datetime.now(UTC),
                duration_ms=0,
                payload_digest="XXXX",
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_23(self, check: CronCheck) -> CheckResult:
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
            output = None
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_24(self, check: CronCheck) -> CheckResult:
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
            output = use_case_fn(None)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_25(self, check: CronCheck) -> CheckResult:
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
                check_name=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_26(self, check: CronCheck) -> CheckResult:
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
                phase=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_27(self, check: CronCheck) -> CheckResult:
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
                started_at=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_28(self, check: CronCheck) -> CheckResult:
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
                finished_at=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_29(self, check: CronCheck) -> CheckResult:
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
                duration_ms=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_30(self, check: CronCheck) -> CheckResult:
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
                payload_digest=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_31(self, check: CronCheck) -> CheckResult:
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
                error_message=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_32(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_33(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_34(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_35(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_36(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_37(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_38(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_39(self, check: CronCheck) -> CheckResult:
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
                finished_at=datetime.now(None),
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_40(self, check: CronCheck) -> CheckResult:
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
                duration_ms=1,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_41(self, check: CronCheck) -> CheckResult:
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
                payload_digest="XXXX",
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_42(self, check: CronCheck) -> CheckResult:
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
                error_message=str(None),
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_43(self, check: CronCheck) -> CheckResult:
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

        finished = None
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_44(self, check: CronCheck) -> CheckResult:
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

        finished = datetime.now(None)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_45(self, check: CronCheck) -> CheckResult:
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
        payload_json = None
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_46(self, check: CronCheck) -> CheckResult:
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
        payload_json = json.dumps(None, sort_keys=True, default=str)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_47(self, check: CronCheck) -> CheckResult:
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
        payload_json = json.dumps(output, sort_keys=None, default=str)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_48(self, check: CronCheck) -> CheckResult:
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
        payload_json = json.dumps(output, sort_keys=True, default=None)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_49(self, check: CronCheck) -> CheckResult:
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
        payload_json = json.dumps(sort_keys=True, default=str)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_50(self, check: CronCheck) -> CheckResult:
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
        payload_json = json.dumps(output, default=str)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_51(self, check: CronCheck) -> CheckResult:
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
        payload_json = json.dumps(output, sort_keys=True, )
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_52(self, check: CronCheck) -> CheckResult:
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
        payload_json = json.dumps(output, sort_keys=False, default=str)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_53(self, check: CronCheck) -> CheckResult:
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
        digest = None

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_54(self, check: CronCheck) -> CheckResult:
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
        digest = hashlib.sha256(None).hexdigest()

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_55(self, check: CronCheck) -> CheckResult:
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

        previous = None
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_56(self, check: CronCheck) -> CheckResult:
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

        previous = self._store.last_result(None)
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_57(self, check: CronCheck) -> CheckResult:
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
        changed = None

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_58(self, check: CronCheck) -> CheckResult:
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
        changed = previous is None and previous.payload_digest != digest

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_59(self, check: CronCheck) -> CheckResult:
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
        changed = previous is not None or previous.payload_digest != digest

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_60(self, check: CronCheck) -> CheckResult:
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
        changed = previous is None or previous.payload_digest == digest

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_61(self, check: CronCheck) -> CheckResult:
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

        should_notify = None

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_62(self, check: CronCheck) -> CheckResult:
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

        should_notify = check.notify_policy == "always" and (
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_63(self, check: CronCheck) -> CheckResult:
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

        should_notify = check.notify_policy != "always" or (
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_64(self, check: CronCheck) -> CheckResult:
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

        should_notify = check.notify_policy == "XXalwaysXX" or (
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_65(self, check: CronCheck) -> CheckResult:
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

        should_notify = check.notify_policy == "ALWAYS" or (
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_66(self, check: CronCheck) -> CheckResult:
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
            check.notify_policy == "on_change" or changed
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_67(self, check: CronCheck) -> CheckResult:
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
            check.notify_policy != "on_change" and changed
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_68(self, check: CronCheck) -> CheckResult:
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
            check.notify_policy == "XXon_changeXX" and changed
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_69(self, check: CronCheck) -> CheckResult:
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
            check.notify_policy == "ON_CHANGE" and changed
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_70(self, check: CronCheck) -> CheckResult:
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

        notified = None
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_71(self, check: CronCheck) -> CheckResult:
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

        notified = True
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_72(self, check: CronCheck) -> CheckResult:
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
            notified = None

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_73(self, check: CronCheck) -> CheckResult:
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
                None
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_74(self, check: CronCheck) -> CheckResult:
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
                    text=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_75(self, check: CronCheck) -> CheckResult:
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
                    title=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_76(self, check: CronCheck) -> CheckResult:
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
                    severity=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_77(self, check: CronCheck) -> CheckResult:
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
                    cluster_name=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_78(self, check: CronCheck) -> CheckResult:
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
                    score=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_79(self, check: CronCheck) -> CheckResult:
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
                    is_pro=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_80(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_81(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_82(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_83(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_84(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_85(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_86(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_87(self, check: CronCheck) -> CheckResult:
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
                    text=f"[{check.name}] {check.use_case}: {_summarize(None)}",
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_88(self, check: CronCheck) -> CheckResult:
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
                    severity="XXwarningXX" if changed else "info",
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_89(self, check: CronCheck) -> CheckResult:
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
                    severity="WARNING" if changed else "info",
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_90(self, check: CronCheck) -> CheckResult:
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
                    severity="warning" if changed else "XXinfoXX",
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_91(self, check: CronCheck) -> CheckResult:
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
                    severity="warning" if changed else "INFO",
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_92(self, check: CronCheck) -> CheckResult:
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
                    cluster_name="XXdefaultXX",
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_93(self, check: CronCheck) -> CheckResult:
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
                    cluster_name="DEFAULT",
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_94(self, check: CronCheck) -> CheckResult:
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
                    score=1,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_95(self, check: CronCheck) -> CheckResult:
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
                    is_pro=True,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_96(self, check: CronCheck) -> CheckResult:
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

        phase = None

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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_97(self, check: CronCheck) -> CheckResult:
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

        result = None
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_98(self, check: CronCheck) -> CheckResult:
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
            check_name=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_99(self, check: CronCheck) -> CheckResult:
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
            phase=None,
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_100(self, check: CronCheck) -> CheckResult:
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
            started_at=None,
            finished_at=finished,
            duration_ms=int((finished - started).total_seconds() * 1000),
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_101(self, check: CronCheck) -> CheckResult:
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
            finished_at=None,
            duration_ms=int((finished - started).total_seconds() * 1000),
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_102(self, check: CronCheck) -> CheckResult:
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
            duration_ms=None,
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_103(self, check: CronCheck) -> CheckResult:
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
            summary=None,
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_104(self, check: CronCheck) -> CheckResult:
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
            payload_digest=None,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_105(self, check: CronCheck) -> CheckResult:
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
            changed=None,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_106(self, check: CronCheck) -> CheckResult:
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
            notified=None,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_107(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_108(self, check: CronCheck) -> CheckResult:
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

    def xǁCheckRunnerUseCaseǁexecute__mutmut_109(self, check: CronCheck) -> CheckResult:
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
            finished_at=finished,
            duration_ms=int((finished - started).total_seconds() * 1000),
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_110(self, check: CronCheck) -> CheckResult:
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
            duration_ms=int((finished - started).total_seconds() * 1000),
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_111(self, check: CronCheck) -> CheckResult:
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
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_112(self, check: CronCheck) -> CheckResult:
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
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_113(self, check: CronCheck) -> CheckResult:
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
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_114(self, check: CronCheck) -> CheckResult:
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
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_115(self, check: CronCheck) -> CheckResult:
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
            )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_116(self, check: CronCheck) -> CheckResult:
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
            duration_ms=int(None),
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_117(self, check: CronCheck) -> CheckResult:
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
            duration_ms=int((finished - started).total_seconds() / 1000),
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_118(self, check: CronCheck) -> CheckResult:
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
            duration_ms=int((finished + started).total_seconds() * 1000),
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_119(self, check: CronCheck) -> CheckResult:
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
            duration_ms=int((finished - started).total_seconds() * 1001),
            summary=_summarize(output),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_120(self, check: CronCheck) -> CheckResult:
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
            summary=_summarize(None),
            payload_digest=digest,
            changed=changed,
            notified=notified,
        )
        self._store.save_result(result)
        return result

    def xǁCheckRunnerUseCaseǁexecute__mutmut_121(self, check: CronCheck) -> CheckResult:
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
        self._store.save_result(None)
        return result

mutants_xǁCheckRunnerUseCaseǁ__init____mutmut['_mutmut_orig'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁ__init____mutmut['xǁCheckRunnerUseCaseǁ__init____mutmut_1'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁ__init____mutmut['xǁCheckRunnerUseCaseǁ__init____mutmut_2'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁ__init____mutmut['xǁCheckRunnerUseCaseǁ__init____mutmut_3'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['_mutmut_orig'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_1'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_2'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_3'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_4'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_5'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_6'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_7'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_8'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_9'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_10'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_11'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_12'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_13'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_14'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_15'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_16'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_17'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_18'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_19'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_20'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_21'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_22'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_23'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_24'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_25'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_26'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_27'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_28'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_29'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_30'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_31'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_32'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_33'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_34'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_35'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_36'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_37'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_38'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_39'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_40'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_41'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_42'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_43'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_44'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_45'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_46'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_47'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_48'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_49'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_50'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_51'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_52'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_53'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_54'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_55'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_56'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_57'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_58'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_59'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_60'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_61'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_62'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_63'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_64'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_65'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_66'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_67'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_68'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_68 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_69'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_69 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_70'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_70 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_71'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_71 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_72'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_72 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_73'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_73 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_74'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_74 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_75'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_75 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_76'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_76 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_77'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_77 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_78'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_78 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_79'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_79 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_80'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_80 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_81'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_81 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_82'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_82 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_83'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_83 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_84'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_84 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_85'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_85 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_86'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_86 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_87'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_87 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_88'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_88 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_89'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_89 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_90'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_90 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_91'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_91 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_92'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_92 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_93'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_93 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_94'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_94 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_95'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_95 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_96'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_96 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_97'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_97 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_98'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_98 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_99'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_99 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_100'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_100 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_101'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_101 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_102'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_102 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_103'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_103 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_104'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_104 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_105'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_105 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_106'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_106 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_107'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_107 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_108'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_108 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_109'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_109 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_110'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_110 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_111'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_111 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_112'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_112 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_113'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_113 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_114'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_114 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_115'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_115 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_116'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_116 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_117'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_117 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_118'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_118 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_119'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_119 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_120'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_120 # type: ignore # mutmut generated
mutants_xǁCheckRunnerUseCaseǁexecute__mutmut['xǁCheckRunnerUseCaseǁexecute__mutmut_121'] = CheckRunnerUseCase.xǁCheckRunnerUseCaseǁexecute__mutmut_121 # type: ignore # mutmut generated
mutants_x__summarize__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summarize__mutmut)
def _summarize(output: dict[str, object]) -> str:
    if not output:
        return "empty response"
    keys = list(output.keys())[:3]
    return ", ".join(keys)  # pragma: no cover — trivial string join


def x__summarize__mutmut_orig(output: dict[str, object]) -> str:
    if not output:
        return "empty response"
    keys = list(output.keys())[:3]
    return ", ".join(keys)  # pragma: no cover — trivial string join


def x__summarize__mutmut_1(output: dict[str, object]) -> str:
    if output:
        return "empty response"
    keys = list(output.keys())[:3]
    return ", ".join(keys)  # pragma: no cover — trivial string join


def x__summarize__mutmut_2(output: dict[str, object]) -> str:
    if not output:
        return "XXempty responseXX"
    keys = list(output.keys())[:3]
    return ", ".join(keys)  # pragma: no cover — trivial string join


def x__summarize__mutmut_3(output: dict[str, object]) -> str:
    if not output:
        return "EMPTY RESPONSE"
    keys = list(output.keys())[:3]
    return ", ".join(keys)  # pragma: no cover — trivial string join


def x__summarize__mutmut_4(output: dict[str, object]) -> str:
    if not output:
        return "empty response"
    keys = None
    return ", ".join(keys)  # pragma: no cover — trivial string join


def x__summarize__mutmut_5(output: dict[str, object]) -> str:
    if not output:
        return "empty response"
    keys = list(None)[:3]
    return ", ".join(keys)  # pragma: no cover — trivial string join


def x__summarize__mutmut_6(output: dict[str, object]) -> str:
    if not output:
        return "empty response"
    keys = list(output.keys())[:4]
    return ", ".join(keys)  # pragma: no cover — trivial string join


def x__summarize__mutmut_7(output: dict[str, object]) -> str:
    if not output:
        return "empty response"
    keys = list(output.keys())[:3]
    return ", ".join(None)  # pragma: no cover — trivial string join


def x__summarize__mutmut_8(output: dict[str, object]) -> str:
    if not output:
        return "empty response"
    keys = list(output.keys())[:3]
    return "XX, XX".join(keys)  # pragma: no cover — trivial string join

mutants_x__summarize__mutmut['_mutmut_orig'] = x__summarize__mutmut_orig # type: ignore # mutmut generated
mutants_x__summarize__mutmut['x__summarize__mutmut_1'] = x__summarize__mutmut_1 # type: ignore # mutmut generated
mutants_x__summarize__mutmut['x__summarize__mutmut_2'] = x__summarize__mutmut_2 # type: ignore # mutmut generated
mutants_x__summarize__mutmut['x__summarize__mutmut_3'] = x__summarize__mutmut_3 # type: ignore # mutmut generated
mutants_x__summarize__mutmut['x__summarize__mutmut_4'] = x__summarize__mutmut_4 # type: ignore # mutmut generated
mutants_x__summarize__mutmut['x__summarize__mutmut_5'] = x__summarize__mutmut_5 # type: ignore # mutmut generated
mutants_x__summarize__mutmut['x__summarize__mutmut_6'] = x__summarize__mutmut_6 # type: ignore # mutmut generated
mutants_x__summarize__mutmut['x__summarize__mutmut_7'] = x__summarize__mutmut_7 # type: ignore # mutmut generated
mutants_x__summarize__mutmut['x__summarize__mutmut_8'] = x__summarize__mutmut_8 # type: ignore # mutmut generated
