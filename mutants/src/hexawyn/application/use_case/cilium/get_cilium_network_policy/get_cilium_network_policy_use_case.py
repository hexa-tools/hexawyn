from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.get_cilium_network_policy.command import (
    GetCiliumNetworkPolicyCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_network_policy.response import (
    CiliumRuleOutput,
    GetCiliumNetworkPolicyResponse,
)
from hexawyn.domain.models.cilium import CiliumRuleSummary


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut: MutantDict = {}  # type: ignore


class GetCiliumNetworkPolicyUseCase:
    @_mutmut_mutated(mutants_xǁGetCiliumNetworkPolicyUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumPort) -> None:
        self._port = port
    def xǁGetCiliumNetworkPolicyUseCaseǁ__init____mutmut_orig(self, port: CiliumPort) -> None:
        self._port = port
    def xǁGetCiliumNetworkPolicyUseCaseǁ__init____mutmut_1(self, port: CiliumPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut)
    def execute(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_orig(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_1(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = None
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_2(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(None, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_3(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, None)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_4(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_5(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, )
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_6(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=None,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_7(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=None,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_8(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=None,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_9(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=None,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_10(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=None,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_11(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=None,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_12(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=None,
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_13(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=None,
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_14(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=None,
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_15(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=None,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_16(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=None,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_17(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_18(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_19(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_20(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_21(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_22(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_23(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_24(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_25(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_26(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_27(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_28(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(None) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_29(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(None) for rule in detail.egress_rules],
            l7_protocols=list(detail.l7_protocols),
            spec=detail.spec,
            note=detail.note,
        )

    def xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_30(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse:
        detail = self._port.get_network_policy(command.name, command.namespace)
        return GetCiliumNetworkPolicyResponse(
            installed=detail.installed,
            status=detail.status,
            kind=detail.kind,
            name=detail.name,
            namespace=detail.namespace,
            endpoint_selector=detail.endpoint_selector,
            ingress_rules=[self._to_rule(rule) for rule in detail.ingress_rules],
            egress_rules=[self._to_rule(rule) for rule in detail.egress_rules],
            l7_protocols=list(None),
            spec=detail.spec,
            note=detail.note,
        )

    @staticmethod
    @_mutmut_mutated(mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut)
    def _to_rule(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_orig(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_1(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "XXdirectionXX": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_2(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "DIRECTION": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_3(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "XXendpointsXX": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_4(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "ENDPOINTS": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_5(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(None),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_6(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "XXportsXX": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_7(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "PORTS": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_8(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(None),
            "l7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_9(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "XXl7XX": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_10(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "L7": [{"protocol": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_11(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"XXprotocolXX": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_12(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"PROTOCOL": l7.protocol, "match": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_13(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "XXmatchXX": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_14(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "MATCH": list(l7.match)} for l7 in rule.l7],
        }

    @staticmethod
    def xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_15(rule: CiliumRuleSummary) -> CiliumRuleOutput:
        return {
            "direction": rule.direction,
            "endpoints": list(rule.endpoints),
            "ports": list(rule.ports),
            "l7": [{"protocol": l7.protocol, "match": list(None)} for l7 in rule.l7],
        }

mutants_xǁGetCiliumNetworkPolicyUseCaseǁ__init____mutmut['_mutmut_orig'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ__init____mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ__init____mutmut_1'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['_mutmut_orig'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_1'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_2'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_3'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_4'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_5'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_6'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_7'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_8'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_9'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_10'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_11'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_12'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_13'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_14'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_15'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_16'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_17'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_18'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_19'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_20'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_21'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_22'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_23'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_24'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_25'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_26'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_27'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_28'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_29'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_30'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated

mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['_mutmut_orig'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_1'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_2'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_3'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_4'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_5'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_6'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_7'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_8'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_9'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_10'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_11'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_12'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_13'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_14'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut['xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_15'] = GetCiliumNetworkPolicyUseCase.xǁGetCiliumNetworkPolicyUseCaseǁ_to_rule__mutmut_15 # type: ignore # mutmut generated
