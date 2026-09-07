from __future__ import annotations

from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.use_case.observability.analyze_pod_logs.command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.use_case.observability.analyze_pod_logs.response import (
    AnalyzePodLogsResponse,
    ConnectionIssueDict,
    LogPatternDict,
    PodRunSummaryDict,
    RankedEventDict,
)
from hexawyn.domain.models.analyze_pod_logs import (
    AnalyzePodLogsRequest,
    AnalyzePodLogsResult,
    ConnectionIssue,
)
from hexawyn.domain.services.log_analysis.pod_log_analyzer import analyze_pod_logs


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAnalyzePodLogsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class AnalyzePodLogsUseCase:
    @_mutmut_mutated(mutants_xǁAnalyzePodLogsUseCaseǁ__init____mutmut)
    def __init__(self, port: PodLogsPort) -> None:
        self._port = port
    def xǁAnalyzePodLogsUseCaseǁ__init____mutmut_orig(self, port: PodLogsPort) -> None:
        self._port = port
    def xǁAnalyzePodLogsUseCaseǁ__init____mutmut_1(self, port: PodLogsPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut)
    def execute(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_orig(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_1(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = None
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_2(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=None,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_3(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=None,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_4(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=None,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_5(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_6(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_7(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_8(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = None
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_9(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(None)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_10(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = None
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_11(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(None, log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_12(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, None)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_13(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(log_lines)
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_14(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, )
        return _to_response(result)

    def xǁAnalyzePodLogsUseCaseǁexecute__mutmut_15(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        request = AnalyzePodLogsRequest(
            pod_name=command.pod_name,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        log_lines = self._port.fetch_logs(request)
        result = analyze_pod_logs(request, log_lines)
        return _to_response(None)

mutants_xǁAnalyzePodLogsUseCaseǁ__init____mutmut['_mutmut_orig'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁ__init____mutmut['xǁAnalyzePodLogsUseCaseǁ__init____mutmut_1'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['_mutmut_orig'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_1'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_2'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_3'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_4'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_5'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_6'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_7'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_8'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_9'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_10'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_11'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_12'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_13'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_14'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAnalyzePodLogsUseCaseǁexecute__mutmut['xǁAnalyzePodLogsUseCaseǁexecute__mutmut_15'] = AnalyzePodLogsUseCase.xǁAnalyzePodLogsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_orig(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_1(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=None,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_2(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=None,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_3(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=None,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_4(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=None,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_5(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=None,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_6(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=None,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_7(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=None,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_8(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=None,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_9(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=None,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_10(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=None,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_11(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=None,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_12(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=None,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_13(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=None,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_14(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=None,
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_15(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=None,  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_16(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=None,  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_17(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=None,
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_18(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=None,
    )


def x__to_response__mutmut_19(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_20(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_21(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_22(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_23(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_24(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_25(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_26(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_27(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_28(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_29(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_30(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_31(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_32(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_33(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_34(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_35(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_36(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        )


def x__to_response__mutmut_37(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=None, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_38(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=None, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_39(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=None)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_40(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_41(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_42(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, )  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_43(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(None) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_44(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(None) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_45(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=None,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_46(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=None,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_47(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=None,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_48(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=None,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_49(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_50(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_51(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_52(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_53(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=None, count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_54(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=None, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_55(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, severity=None)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_56(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(count=e.count, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_57(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, severity=e.severity)  # type: ignore
            for e in result.ranked_events
        ],
    )


def x__to_response__mutmut_58(result: AnalyzePodLogsResult) -> AnalyzePodLogsResponse:
    return AnalyzePodLogsResponse(
        pod_name=result.pod_name,
        namespace=result.namespace,
        time_window_minutes=result.time_window_minutes,
        strategy_used=result.strategy_used,
        total_lines=result.total_lines,
        error_count=result.error_count,
        warning_count=result.warning_count,
        confidence=result.confidence,  # type: ignore
        summary=result.summary,
        restarts_detected=result.restarts_detected,
        sanitized_binary=result.sanitized_binary,  # type: ignore
        token_reduction_percentage=result.token_reduction_percentage,  # type: ignore
        degraded=result.degraded,  # type: ignore
        patterns=[  # type: ignore
            LogPatternDict(pattern=p.pattern, count=p.count, confidence=p.confidence)  # type: ignore
            for p in result.patterns
        ],
        connection_timeouts=[_to_connection_issue_dict(c) for c in result.connection_timeouts],  # type: ignore
        connection_refused=[_to_connection_issue_dict(c) for c in result.connection_refused],  # type: ignore
        runs=[  # type: ignore
            PodRunSummaryDict(  # type: ignore
                run_index=r.run_index,
                line_count=r.line_count,
                error_count=r.error_count,
                warning_count=r.warning_count,
            )
            for r in result.runs
        ],
        ranked_events=[  # type: ignore
            RankedEventDict(line=e.line, count=e.count, )  # type: ignore
            for e in result.ranked_events
        ],
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_13'] = x__to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_14'] = x__to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_15'] = x__to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_16'] = x__to_response__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_17'] = x__to_response__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_18'] = x__to_response__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_19'] = x__to_response__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_20'] = x__to_response__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_21'] = x__to_response__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_22'] = x__to_response__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_23'] = x__to_response__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_24'] = x__to_response__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_25'] = x__to_response__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_26'] = x__to_response__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_27'] = x__to_response__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_28'] = x__to_response__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_29'] = x__to_response__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_30'] = x__to_response__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_31'] = x__to_response__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_32'] = x__to_response__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_33'] = x__to_response__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_34'] = x__to_response__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_35'] = x__to_response__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_36'] = x__to_response__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_37'] = x__to_response__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_38'] = x__to_response__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_39'] = x__to_response__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_40'] = x__to_response__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_41'] = x__to_response__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_42'] = x__to_response__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_43'] = x__to_response__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_44'] = x__to_response__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_45'] = x__to_response__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_46'] = x__to_response__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_47'] = x__to_response__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_48'] = x__to_response__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_49'] = x__to_response__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_50'] = x__to_response__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_51'] = x__to_response__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_52'] = x__to_response__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_53'] = x__to_response__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_54'] = x__to_response__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_55'] = x__to_response__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_56'] = x__to_response__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_57'] = x__to_response__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_58'] = x__to_response__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_connection_issue_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_connection_issue_dict__mutmut)
def _to_connection_issue_dict(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        category=issue.category,
        message_sample=issue.message_sample,
        count=issue.count,
        confidence=issue.confidence,
    )


def x__to_connection_issue_dict__mutmut_orig(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        category=issue.category,
        message_sample=issue.message_sample,
        count=issue.count,
        confidence=issue.confidence,
    )


def x__to_connection_issue_dict__mutmut_1(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        category=None,
        message_sample=issue.message_sample,
        count=issue.count,
        confidence=issue.confidence,
    )


def x__to_connection_issue_dict__mutmut_2(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        category=issue.category,
        message_sample=None,
        count=issue.count,
        confidence=issue.confidence,
    )


def x__to_connection_issue_dict__mutmut_3(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        category=issue.category,
        message_sample=issue.message_sample,
        count=None,
        confidence=issue.confidence,
    )


def x__to_connection_issue_dict__mutmut_4(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        category=issue.category,
        message_sample=issue.message_sample,
        count=issue.count,
        confidence=None,
    )


def x__to_connection_issue_dict__mutmut_5(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        message_sample=issue.message_sample,
        count=issue.count,
        confidence=issue.confidence,
    )


def x__to_connection_issue_dict__mutmut_6(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        category=issue.category,
        count=issue.count,
        confidence=issue.confidence,
    )


def x__to_connection_issue_dict__mutmut_7(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        category=issue.category,
        message_sample=issue.message_sample,
        confidence=issue.confidence,
    )


def x__to_connection_issue_dict__mutmut_8(issue: ConnectionIssue) -> ConnectionIssueDict:
    return ConnectionIssueDict(  # type: ignore
        category=issue.category,
        message_sample=issue.message_sample,
        count=issue.count,
        )

mutants_x__to_connection_issue_dict__mutmut['_mutmut_orig'] = x__to_connection_issue_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_connection_issue_dict__mutmut['x__to_connection_issue_dict__mutmut_1'] = x__to_connection_issue_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_connection_issue_dict__mutmut['x__to_connection_issue_dict__mutmut_2'] = x__to_connection_issue_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_connection_issue_dict__mutmut['x__to_connection_issue_dict__mutmut_3'] = x__to_connection_issue_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_connection_issue_dict__mutmut['x__to_connection_issue_dict__mutmut_4'] = x__to_connection_issue_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_connection_issue_dict__mutmut['x__to_connection_issue_dict__mutmut_5'] = x__to_connection_issue_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_connection_issue_dict__mutmut['x__to_connection_issue_dict__mutmut_6'] = x__to_connection_issue_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_connection_issue_dict__mutmut['x__to_connection_issue_dict__mutmut_7'] = x__to_connection_issue_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_connection_issue_dict__mutmut['x__to_connection_issue_dict__mutmut_8'] = x__to_connection_issue_dict__mutmut_8 # type: ignore # mutmut generated
