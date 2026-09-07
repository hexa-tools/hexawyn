"""GetCalicoNetworkPolicyUseCase — full detail of a Calico policy."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.get_calico_network_policy.command import (
    GetCalicoNetworkPolicyCommand,
)
from hexawyn.application.use_case.calico.get_calico_network_policy.response import (
    GetCalicoNetworkPolicyResponse,
)
from hexawyn.domain.errors import InsufficientDataError, ResourceNotFoundError
from hexawyn.domain.models.calico import CalicoNetworkPolicy

_KIND_GLOBAL = "GlobalNetworkPolicy"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut: MutantDict = {}  # type: ignore


class GetCalicoNetworkPolicyUseCase:
    """Orchestrates fetching one Calico policy — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁGetCalicoNetworkPolicyUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁGetCalicoNetworkPolicyUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁGetCalicoNetworkPolicyUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut)
    def execute(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_orig(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_1(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_2(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError(None)

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_3(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("XXCalico network policy name is requiredXX")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_4(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_5(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("CALICO NETWORK POLICY NAME IS REQUIRED")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_6(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = None
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_7(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_8(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=None,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_9(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=None,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_10(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=None,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_11(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=None,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_12(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_13(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_14(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_15(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_16(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=True,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_17(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=True,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_18(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = None
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_19(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(None, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_20(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, None)
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_21(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_22(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, )
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_23(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace and "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_24(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "XXXX")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_25(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is not None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_26(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(None)
        return self._to_response(policy)

    def xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_27(self, command: GetCalicoNetworkPolicyCommand) -> GetCalicoNetworkPolicyResponse:
        if not command.name:
            raise InsufficientDataError("Calico network policy name is required")

        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoNetworkPolicyResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                found=False,
                error=detection.error,
            )

        policy = self._port.get_network_policy(command.name, command.namespace or "")
        if policy is None:
            raise ResourceNotFoundError(f"Calico network policy '{command.name}' not found")
        return self._to_response(None)

    @staticmethod
    @_mutmut_mutated(mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut)
    def _to_response(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_orig(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_1(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = None
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_2(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "XXcluster-wideXX" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_3(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "CLUSTER-WIDE" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_4(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind != _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_5(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "XXnamespacedXX"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_6(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "NAMESPACED"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_7(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=None,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_8(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=None,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_9(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=None,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_10(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=None,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_11(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=None,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_12(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=None,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_13(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=None,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_14(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=None,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_15(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=None,
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_16(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=None,
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_17(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=None,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_18(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=None,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_19(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=None,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_20(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=None,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_21(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_22(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_23(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_24(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_25(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_26(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_27(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_28(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_29(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_30(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_31(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_32(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_33(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_34(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_35(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_36(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_37(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=False,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_38(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=False,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_39(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(None),
            egress_rules=list(policy.egress_rules),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

    @staticmethod
    def xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_40(policy: CalicoNetworkPolicy) -> GetCalicoNetworkPolicyResponse:
        scope = "cluster-wide" if policy.kind == _KIND_GLOBAL else "namespaced"
        return GetCalicoNetworkPolicyResponse(
            installed=True,
            not_installed_marker=None,
            found=True,
            name=policy.name,
            namespace=policy.namespace,
            scope=scope,
            kind=policy.kind,
            selector=policy.selector,
            action=policy.action,
            ingress_rules=list(policy.ingress_rules),
            egress_rules=list(None),
            ingress_rule_count=policy.ingress_rule_count,
            egress_rule_count=policy.egress_rule_count,
            order=policy.order,
            apply_on_forward=policy.apply_on_forward,
            error=None,
        )

mutants_xǁGetCalicoNetworkPolicyUseCaseǁ__init____mutmut['_mutmut_orig'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ__init____mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ__init____mutmut_1'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['_mutmut_orig'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_1'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_2'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_3'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_4'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_5'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_6'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_7'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_8'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_9'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_10'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_11'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_12'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_13'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_14'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_15'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_16'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_17'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_18'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_19'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_20'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_21'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_22'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_23'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_24'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_25'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_26'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_27'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated

mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['_mutmut_orig'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_1'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_2'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_3'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_4'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_5'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_6'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_7'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_8'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_9'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_10'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_11'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_12'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_13'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_14'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_15'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_16'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_17'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_18'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_19'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_20'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_21'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_22'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_23'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_24'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_25'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_26'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_27'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_28'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_29'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_30'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_31'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_32'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_33'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_34'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_35'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_36'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_37'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_38'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_39'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut['xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_40'] = GetCalicoNetworkPolicyUseCase.xǁGetCalicoNetworkPolicyUseCaseǁ_to_response__mutmut_40 # type: ignore # mutmut generated
