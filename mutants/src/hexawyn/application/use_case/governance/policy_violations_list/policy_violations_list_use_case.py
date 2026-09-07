from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.governance.policy_violations_list.command import (
    PolicyViolationsListCommand,
)
from hexawyn.application.use_case.governance.policy_violations_list.response import (
    PolicyViolationsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPolicyViolationsListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyViolationsListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class PolicyViolationsListUseCase:
    @_mutmut_mutated(mutants_xǁPolicyViolationsListUseCaseǁ__init____mutmut)
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyViolationsListUseCaseǁ__init____mutmut_orig(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyViolationsListUseCaseǁ__init____mutmut_1(self, policy_port: PolicyPort) -> None:
        self._policy = None

    @_mutmut_mutated(mutants_xǁPolicyViolationsListUseCaseǁexecute__mutmut)
    def execute(self, command: PolicyViolationsListCommand) -> PolicyViolationsListResponse:
        violations = self._policy.list_violations(namespace=command.namespace)
        return PolicyViolationsListResponse(violations=[asdict(v) for v in violations])

    def xǁPolicyViolationsListUseCaseǁexecute__mutmut_orig(self, command: PolicyViolationsListCommand) -> PolicyViolationsListResponse:
        violations = self._policy.list_violations(namespace=command.namespace)
        return PolicyViolationsListResponse(violations=[asdict(v) for v in violations])

    def xǁPolicyViolationsListUseCaseǁexecute__mutmut_1(self, command: PolicyViolationsListCommand) -> PolicyViolationsListResponse:
        violations = None
        return PolicyViolationsListResponse(violations=[asdict(v) for v in violations])

    def xǁPolicyViolationsListUseCaseǁexecute__mutmut_2(self, command: PolicyViolationsListCommand) -> PolicyViolationsListResponse:
        violations = self._policy.list_violations(namespace=None)
        return PolicyViolationsListResponse(violations=[asdict(v) for v in violations])

    def xǁPolicyViolationsListUseCaseǁexecute__mutmut_3(self, command: PolicyViolationsListCommand) -> PolicyViolationsListResponse:
        violations = self._policy.list_violations(namespace=command.namespace)
        return PolicyViolationsListResponse(violations=None)

    def xǁPolicyViolationsListUseCaseǁexecute__mutmut_4(self, command: PolicyViolationsListCommand) -> PolicyViolationsListResponse:
        violations = self._policy.list_violations(namespace=command.namespace)
        return PolicyViolationsListResponse(violations=[asdict(None) for v in violations])

mutants_xǁPolicyViolationsListUseCaseǁ__init____mutmut['_mutmut_orig'] = PolicyViolationsListUseCase.xǁPolicyViolationsListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyViolationsListUseCaseǁ__init____mutmut['xǁPolicyViolationsListUseCaseǁ__init____mutmut_1'] = PolicyViolationsListUseCase.xǁPolicyViolationsListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPolicyViolationsListUseCaseǁexecute__mutmut['_mutmut_orig'] = PolicyViolationsListUseCase.xǁPolicyViolationsListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyViolationsListUseCaseǁexecute__mutmut['xǁPolicyViolationsListUseCaseǁexecute__mutmut_1'] = PolicyViolationsListUseCase.xǁPolicyViolationsListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyViolationsListUseCaseǁexecute__mutmut['xǁPolicyViolationsListUseCaseǁexecute__mutmut_2'] = PolicyViolationsListUseCase.xǁPolicyViolationsListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyViolationsListUseCaseǁexecute__mutmut['xǁPolicyViolationsListUseCaseǁexecute__mutmut_3'] = PolicyViolationsListUseCase.xǁPolicyViolationsListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyViolationsListUseCaseǁexecute__mutmut['xǁPolicyViolationsListUseCaseǁexecute__mutmut_4'] = PolicyViolationsListUseCase.xǁPolicyViolationsListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
