from __future__ import annotations

from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import (
    get_jaeger_dependencies,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut: MutantDict = {}  # type: ignore


class OTelDependencyGraphAdapter(ServiceDependencyGraphPort):
    @_mutmut_mutated(mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut)
    def fetch_edges(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_orig(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_1(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = None
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_2(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(None)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_3(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() / 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_4(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1000001)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_5(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = None

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_6(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 / 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_7(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes / 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_8(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 61 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_9(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1000001

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_10(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = None
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_11(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=None, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_12(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=None)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_13(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_14(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, )
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_15(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = None
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_16(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                None
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_17(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "XXsourceXX": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_18(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "SOURCE": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_19(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["XXparentXX"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_20(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["PARENT"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_21(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "XXtargetXX": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_22(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "TARGET": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_23(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["XXchildXX"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_24(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["CHILD"],
                    "call_count": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_25(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "XXcall_countXX": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_26(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "CALL_COUNT": dep["callCount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_27(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["XXcallCountXX"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_28(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callcount"],
                }
            )
        return result
    def xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_29(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["CALLCOUNT"],
                }
            )
        return result

mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['_mutmut_orig'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_1'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_2'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_3'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_4'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_5'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_6'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_7'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_8'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_9'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_10'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_11'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_12'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_13'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_14'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_15'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_16'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_17'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_18'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_19'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_20'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_21'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_22'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_23'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_24'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_25'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_26'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_27'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_28'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut['xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_29'] = OTelDependencyGraphAdapter.xǁOTelDependencyGraphAdapterǁfetch_edges__mutmut_29 # type: ignore # mutmut generated
