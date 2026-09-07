from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.governance.policy_get.command import (
    PolicyGetCommand,
)
from hexawyn.application.use_case.governance.policy_get.response import (
    PolicyGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPolicyGetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyGetUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class PolicyGetUseCase:
    @_mutmut_mutated(mutants_xǁPolicyGetUseCaseǁ__init____mutmut)
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyGetUseCaseǁ__init____mutmut_orig(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyGetUseCaseǁ__init____mutmut_1(self, policy_port: PolicyPort) -> None:
        self._policy = None

    @_mutmut_mutated(mutants_xǁPolicyGetUseCaseǁexecute__mutmut)
    def execute(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_orig(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_1(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = None
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_2(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=None, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_3(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=None)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_4(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_5(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, )
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_6(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=None,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_7(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=None,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_8(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=None,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_9(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=None,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_10(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=None,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_11(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=None,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_12(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=None,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_13(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=None,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_14(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=None,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_15(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_16(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_17(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_18(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_19(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_20(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_21(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            violations_count=p.violations_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_22(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            ready=p.ready,
        )

    def xǁPolicyGetUseCaseǁexecute__mutmut_23(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            )

mutants_xǁPolicyGetUseCaseǁ__init____mutmut['_mutmut_orig'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁ__init____mutmut['xǁPolicyGetUseCaseǁ__init____mutmut_1'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPolicyGetUseCaseǁexecute__mutmut['_mutmut_orig'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_1'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_2'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_3'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_4'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_5'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_6'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_7'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_8'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_9'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_10'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_11'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_12'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_13'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_14'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_15'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_16'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_17'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_18'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_19'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_20'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_21'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_22'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPolicyGetUseCaseǁexecute__mutmut['xǁPolicyGetUseCaseǁexecute__mutmut_23'] = PolicyGetUseCase.xǁPolicyGetUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
