from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.governance.policy_list.command import (
    PolicyListCommand,
)
from hexawyn.application.use_case.governance.policy_list.response import (
    PolicyListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPolicyListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class PolicyListUseCase:
    @_mutmut_mutated(mutants_xǁPolicyListUseCaseǁ__init____mutmut)
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyListUseCaseǁ__init____mutmut_orig(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyListUseCaseǁ__init____mutmut_1(self, policy_port: PolicyPort) -> None:
        self._policy = None

    @_mutmut_mutated(mutants_xǁPolicyListUseCaseǁexecute__mutmut)
    def execute(self, command: PolicyListCommand) -> PolicyListResponse:
        policies = self._policy.list_policies(namespace=command.namespace)
        return PolicyListResponse(policies=[asdict(p) for p in policies])

    def xǁPolicyListUseCaseǁexecute__mutmut_orig(self, command: PolicyListCommand) -> PolicyListResponse:
        policies = self._policy.list_policies(namespace=command.namespace)
        return PolicyListResponse(policies=[asdict(p) for p in policies])

    def xǁPolicyListUseCaseǁexecute__mutmut_1(self, command: PolicyListCommand) -> PolicyListResponse:
        policies = None
        return PolicyListResponse(policies=[asdict(p) for p in policies])

    def xǁPolicyListUseCaseǁexecute__mutmut_2(self, command: PolicyListCommand) -> PolicyListResponse:
        policies = self._policy.list_policies(namespace=None)
        return PolicyListResponse(policies=[asdict(p) for p in policies])

    def xǁPolicyListUseCaseǁexecute__mutmut_3(self, command: PolicyListCommand) -> PolicyListResponse:
        policies = self._policy.list_policies(namespace=command.namespace)
        return PolicyListResponse(policies=None)

    def xǁPolicyListUseCaseǁexecute__mutmut_4(self, command: PolicyListCommand) -> PolicyListResponse:
        policies = self._policy.list_policies(namespace=command.namespace)
        return PolicyListResponse(policies=[asdict(None) for p in policies])

mutants_xǁPolicyListUseCaseǁ__init____mutmut['_mutmut_orig'] = PolicyListUseCase.xǁPolicyListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyListUseCaseǁ__init____mutmut['xǁPolicyListUseCaseǁ__init____mutmut_1'] = PolicyListUseCase.xǁPolicyListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPolicyListUseCaseǁexecute__mutmut['_mutmut_orig'] = PolicyListUseCase.xǁPolicyListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyListUseCaseǁexecute__mutmut['xǁPolicyListUseCaseǁexecute__mutmut_1'] = PolicyListUseCase.xǁPolicyListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyListUseCaseǁexecute__mutmut['xǁPolicyListUseCaseǁexecute__mutmut_2'] = PolicyListUseCase.xǁPolicyListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyListUseCaseǁexecute__mutmut['xǁPolicyListUseCaseǁexecute__mutmut_3'] = PolicyListUseCase.xǁPolicyListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyListUseCaseǁexecute__mutmut['xǁPolicyListUseCaseǁexecute__mutmut_4'] = PolicyListUseCase.xǁPolicyListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
