from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.list_cilium_network_policies.command import (
    ListCiliumNetworkPoliciesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_network_policies.response import (
    CiliumNetworkPolicyOutput,
    ListCiliumNetworkPoliciesResponse,
)
from hexawyn.domain.models.cilium import CiliumNetworkPolicyInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut: MutantDict = {}  # type: ignore


class ListCiliumNetworkPoliciesUseCase:
    @_mutmut_mutated(mutants_xǁListCiliumNetworkPoliciesUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumPort) -> None:
        self._port = port
    def xǁListCiliumNetworkPoliciesUseCaseǁ__init____mutmut_orig(self, port: CiliumPort) -> None:
        self._port = port
    def xǁListCiliumNetworkPoliciesUseCaseǁ__init____mutmut_1(self, port: CiliumPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut)
    def execute(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_orig(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_1(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = None
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_2(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = ""
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_3(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_4(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = None
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_5(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(None) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_6(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=None,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_7(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=None,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_8(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=None,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_9(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=None,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_10(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=None,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_11(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=None,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_12(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=None,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_13(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_14(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_15(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_16(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_17(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            policies=policies,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_18(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            note=result.note,
        )

    def xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_19(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse:
        result = self._port.list_network_policies()
        policies: list[CiliumNetworkPolicyOutput] | None = None
        if result.policies is not None:
            policies = [self._to_output(policy) for policy in result.policies]
        return ListCiliumNetworkPoliciesResponse(
            installed=result.installed,
            status=result.status,
            total_policies=result.total_policies,
            namespaced_count=result.namespaced_count,
            clusterwide_count=result.clusterwide_count,
            policies=policies,
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut)
    def _to_output(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_orig(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_1(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "XXkindXX": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_2(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "KIND": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_3(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "XXnameXX": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_4(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "NAME": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_5(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "XXnamespaceXX": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_6(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "NAMESPACE": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_7(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "XXendpoint_selectorXX": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_8(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "ENDPOINT_SELECTOR": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_9(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "XXingress_rule_countXX": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_10(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "INGRESS_RULE_COUNT": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_11(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "XXegress_rule_countXX": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_12(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "EGRESS_RULE_COUNT": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_13(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "XXl7_rule_countXX": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_14(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "L7_RULE_COUNT": policy.l7_rule_count,
            "l7_protocols": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_15(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "XXl7_protocolsXX": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_16(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "L7_PROTOCOLS": list(policy.l7_protocols),
        }

    @staticmethod
    def xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_17(policy: CiliumNetworkPolicyInfo) -> CiliumNetworkPolicyOutput:
        return {
            "kind": policy.kind,
            "name": policy.name,
            "namespace": policy.namespace,
            "endpoint_selector": policy.endpoint_selector,
            "ingress_rule_count": policy.ingress_rule_count,
            "egress_rule_count": policy.egress_rule_count,
            "l7_rule_count": policy.l7_rule_count,
            "l7_protocols": list(None),
        }

mutants_xǁListCiliumNetworkPoliciesUseCaseǁ__init____mutmut['_mutmut_orig'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ__init____mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ__init____mutmut_1'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['_mutmut_orig'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_1'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_2'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_3'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_4'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_5'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_6'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_7'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_8'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_9'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_10'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_11'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_12'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_13'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_14'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_15'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_16'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_17'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_18'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_19'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated

mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['_mutmut_orig'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_1'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_2'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_3'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_4'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_5'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_6'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_7'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_8'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_8 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_9'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_9 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_10'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_10 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_11'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_11 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_12'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_12 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_13'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_13 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_14'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_14 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_15'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_15 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_16'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_16 # type: ignore # mutmut generated
mutants_xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut['xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_17'] = ListCiliumNetworkPoliciesUseCase.xǁListCiliumNetworkPoliciesUseCaseǁ_to_output__mutmut_17 # type: ignore # mutmut generated
