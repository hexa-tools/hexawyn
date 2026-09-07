from __future__ import annotations

from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
    CrossNamespaceFlowDict,
    CrossNamespaceTrafficPort,
)
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import list_jaeger_services


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut: MutantDict = {}  # type: ignore


class OTelCrossNamespaceTrafficAdapter(CrossNamespaceTrafficPort):
    @_mutmut_mutated(mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut)
    def list_cross_namespace_flows(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_orig(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_1(self) -> list[CrossNamespaceFlowDict]:
        services = None
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_2(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = None
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_3(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                None
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_4(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace=None,
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_5(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace=None,
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_6(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=None,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_7(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    target_service=None,
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_8(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=None,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_9(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_10(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_11(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_12(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_13(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_14(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="XXunknownXX",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_15(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="UNKNOWN",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_16(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="XXunknownXX",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_17(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="UNKNOWN",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_18(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="XXXX",
                    call_count=0,
                )
            )
        return result
    def xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_19(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=1,
                )
            )
        return result

mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['_mutmut_orig'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_1'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_2'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_3'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_4'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_5'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_6'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_7'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_8'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_9'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_10'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_11'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_12'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_13'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_14'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_15'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_16'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_17'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_18'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut['xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_19'] = OTelCrossNamespaceTrafficAdapter.xǁOTelCrossNamespaceTrafficAdapterǁlist_cross_namespace_flows__mutmut_19 # type: ignore # mutmut generated
