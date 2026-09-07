"""CiliumHubbleAdapter — queries Cilium flow logs via a Hubble Relay HTTP client."""

from __future__ import annotations

from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.domain.errors import AdapterTimeoutError, ClusterUnreachableError
from hexawyn.domain.models.cilium import (
    CiliumDenialsQuery,
    CiliumDenialsResult,
    CiliumFlowQuery,
    CiliumFlowsResult,
)
from hexawyn.domain.services.cilium.denial_builder import (
    build_denials,
    not_installed_denials_result,
)
from hexawyn.domain.services.cilium.flow_builder import (
    build_flows,
    not_installed_flows_result,
)
from hexawyn.infrastructure.adapters.secondary.cilium.hubble_client import (
    fetch_hubble_flows,
    hubble_available,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut: MutantDict = {}  # type: ignore


class CiliumHubbleAdapter(CiliumHubblePort):
    """Real Hubble adapter using the HTTP flow client."""

    @_mutmut_mutated(mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut)
    def get_flows(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_orig(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_1(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_2(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = None
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_3(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=None,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_4(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=None,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_5(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=None,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_6(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=None,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_7(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=None,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_8(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=None,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_9(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_10(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_11(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_12(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_13(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_14(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_15(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(None) from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_16(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(None) from exc
        return build_flows(raw, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_17(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(None, query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_18(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, None)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_19(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(query)

    def xǁCiliumHubbleAdapterǁget_flows__mutmut_20(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, )

    @_mutmut_mutated(mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut)
    def detect_denials(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_orig(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_1(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = None
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_2(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=None,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_3(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=None,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_4(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=None,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_5(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict=None,
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_6(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_7(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_8(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_9(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_10(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="XXDROPPEDXX",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_11(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="dropped",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_12(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = None
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_13(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(None)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_14(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_15(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(None, query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_16(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, None)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_17(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(query)

    def xǁCiliumHubbleAdapterǁdetect_denials__mutmut_18(self, query: CiliumDenialsQuery) -> CiliumDenialsResult:
        flow_query = CiliumFlowQuery(
            namespace=query.namespace,
            window_minutes=query.window_minutes,
            limit=query.limit,
            verdict="DROPPED",
        )
        flows = self.get_flows(flow_query)
        if not flows.installed:
            return not_installed_denials_result()
        return build_denials(flows.flows, )

mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['_mutmut_orig'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_1'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_2'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_3'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_4'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_5'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_6'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_7'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_8'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_9'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_10'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_11'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_12'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_13'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_14'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_15'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_16'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_17'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_18'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_19'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁget_flows__mutmut['xǁCiliumHubbleAdapterǁget_flows__mutmut_20'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁget_flows__mutmut_20 # type: ignore # mutmut generated

mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['_mutmut_orig'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_1'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_2'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_3'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_4'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_5'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_6'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_7'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_8'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_9'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_10'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_11'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_12'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_13'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_14'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_15'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_16'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_17'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCiliumHubbleAdapterǁdetect_denials__mutmut['xǁCiliumHubbleAdapterǁdetect_denials__mutmut_18'] = CiliumHubbleAdapter.xǁCiliumHubbleAdapterǁdetect_denials__mutmut_18 # type: ignore # mutmut generated
