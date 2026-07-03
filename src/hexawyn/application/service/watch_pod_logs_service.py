from __future__ import annotations

import time

from hexawyn.application.ports.driven.alert_notification_port import (
    AlertMessage,
    AlertNotificationPort,
)
from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_response import (
    LogPatternDict,
)
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_command import (
    WatchPodLogsCommand,
)
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_response import (
    WatchAlertDict,
    WatchPodLogsResponse,
)
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_service_port import (
    WatchPodLogsServicePort,
)
from hexawyn.domain.models.log import LogAnalysisContext
from hexawyn.domain.models.watch_pod_logs import CriticalMatch, WatchPodLogsRequest
from hexawyn.domain.services.log_analysis.alert_deduplicator import AlertDeduplicator
from hexawyn.domain.services.log_analysis.critical_pattern_matcher import match_critical_pattern
from hexawyn.domain.services.log_analysis.line_sampler import should_keep_line
from hexawyn.domain.services.log_analysis.strategy import RealtimeLogWatchStrategy


class WatchPodLogsService(WatchPodLogsServicePort):
    def __init__(self, watch_port: PodLogWatchPort, alert_port: AlertNotificationPort) -> None:
        self._watch_port = watch_port
        self._alert_port = alert_port

    def watch(self, command: WatchPodLogsCommand) -> WatchPodLogsResponse:
        request = WatchPodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            timeout_seconds=command.timeout_seconds,
            max_reconnect_attempts=command.max_reconnect_attempts,
            sample_rate=command.sample_rate,
        )
        dedup = AlertDeduplicator()
        alerts: list[CriticalMatch] = []
        sampled_lines: list[str] = []
        lines_observed = 0
        start = time.monotonic()
        stop_reason = "timeout"

        for line_index, line in enumerate(self._watch_port.watch(request)):
            lines_observed += 1
            match = match_critical_pattern(
                line.message, pod_name=request.pod_name, timestamp=line.timestamp
            )
            if match is not None:
                sampled_lines.append(line.message)
                if dedup.should_alert(match.category, now=time.monotonic()):
                    alerts.append(match)
                    self._alert_port.send_alert(_to_alert_message(match))
            elif should_keep_line(line_index, request.sample_rate):
                sampled_lines.append(line.message)

            if time.monotonic() - start >= request.timeout_seconds:
                stop_reason = "timeout"
                break
        else:
            stop_reason = (
                "session_ended"
                if self._watch_port.pod_exists(request.pod_name, request.namespace)
                else "pod_deleted"
            )

        context = LogAnalysisContext(
            request_type="realtime_watch",
            pod_name=request.pod_name,
            namespace=request.namespace,
        )
        analysis = RealtimeLogWatchStrategy().analyze(sampled_lines, context)

        return WatchPodLogsResponse(
            pod_name=request.pod_name,
            namespace=request.namespace,
            stop_reason=stop_reason,
            lines_observed=lines_observed,
            lines_sampled=len(sampled_lines),
            reconnect_count=0,
            confidence=analysis.confidence,
            summary=analysis.summary,
            alerts=[_to_alert_dict(match) for match in alerts],
            patterns=[
                LogPatternDict(
                    pattern=pattern,
                    count=_count_occurrences(pattern, sampled_lines),
                    confidence=analysis.confidence,
                )
                for pattern in analysis.patterns
            ],
        )


def _to_alert_message(match: CriticalMatch) -> AlertMessage:
    return AlertMessage(
        text=f"🚨 Critical pattern detected in pod {match.pod_name}: {match.log_line}",
        title=f"hexawyn Alert — {match.pod_name}",
        severity="critical",
        remediation=None,
        cluster_name=match.pod_name,
        score=0,
        is_pro=False,
    )


def _to_alert_dict(match: CriticalMatch) -> WatchAlertDict:
    return WatchAlertDict(
        category=match.category,
        pattern=match.pattern,
        log_line=match.log_line,
        timestamp=match.timestamp,
        pod_name=match.pod_name,
    )


def _count_occurrences(pattern: str, messages: list[str]) -> int:
    return sum(1 for message in messages if pattern in message.lower())
