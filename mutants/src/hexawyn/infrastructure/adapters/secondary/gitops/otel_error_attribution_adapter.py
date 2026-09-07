from __future__ import annotations

from hexawyn.application.ports.driven.error_attribution_port import (
    ErrorAttributionPort,
)
from hexawyn.domain.models.error_attribution import ErrorAttributionRequest
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import search_jaeger_traces


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut: MutantDict = {}  # type: ignore


class OTelErrorAttributionAdapter(ErrorAttributionPort):
    @_mutmut_mutated(mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut)
    def fetch_error_attribution(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_orig(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_1(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_2(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = None
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_3(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=None,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_4(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=None,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_5(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=None,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_6(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_7(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_8(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_9(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=False,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_10(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=21,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_11(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = None
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_12(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                None
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_13(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "XXtrace_idXX": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_14(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "TRACE_ID": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_15(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["XXtraceIDXX"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_16(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceid"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_17(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["TRACEID"],
                    "error": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_18(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "XXerrorXX": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_19(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "ERROR": bool(trace.get("hasErrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_20(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(None),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_21(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get(None)),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_22(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("XXhasErrorsXX")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_23(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("haserrors")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_24(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("HASERRORS")),
                    "service": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_25(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "XXserviceXX": request.gateway,
                }
            )
        return result
    def xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_26(self, request: ErrorAttributionRequest) -> list[dict[str, object]]:
        if not request.gateway:
            return []

        traces = search_jaeger_traces(
            service=request.gateway,
            with_errors=True,
            limit=20,
        )
        result: list[dict[str, object]] = []
        for trace in traces:
            result.append(
                {
                    "trace_id": trace["traceID"],
                    "error": bool(trace.get("hasErrors")),
                    "SERVICE": request.gateway,
                }
            )
        return result

mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['_mutmut_orig'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_1'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_2'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_3'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_4'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_5'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_6'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_7'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_8'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_9'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_10'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_11'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_12'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_13'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_14'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_15'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_16'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_17'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_18'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_19'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_20'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_21'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_22'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_23'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_24'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_25'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut['xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_26'] = OTelErrorAttributionAdapter.xǁOTelErrorAttributionAdapterǁfetch_error_attribution__mutmut_26 # type: ignore # mutmut generated
