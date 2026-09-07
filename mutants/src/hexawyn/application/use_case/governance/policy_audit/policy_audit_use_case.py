from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.governance.policy_audit.command import (
    PolicyAuditCommand,
)
from hexawyn.application.use_case.governance.policy_audit.response import (
    PolicyAuditResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPolicyAuditUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyAuditUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class PolicyAuditUseCase:
    @_mutmut_mutated(mutants_xǁPolicyAuditUseCaseǁ__init____mutmut)
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyAuditUseCaseǁ__init____mutmut_orig(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyAuditUseCaseǁ__init____mutmut_1(self, policy_port: PolicyPort) -> None:
        self._policy = None

    @_mutmut_mutated(mutants_xǁPolicyAuditUseCaseǁexecute__mutmut)
    def execute(self, command: PolicyAuditCommand) -> PolicyAuditResponse:
        results = self._policy.audit(namespace=command.namespace)
        return PolicyAuditResponse(results=results)

    def xǁPolicyAuditUseCaseǁexecute__mutmut_orig(self, command: PolicyAuditCommand) -> PolicyAuditResponse:
        results = self._policy.audit(namespace=command.namespace)
        return PolicyAuditResponse(results=results)

    def xǁPolicyAuditUseCaseǁexecute__mutmut_1(self, command: PolicyAuditCommand) -> PolicyAuditResponse:
        results = None
        return PolicyAuditResponse(results=results)

    def xǁPolicyAuditUseCaseǁexecute__mutmut_2(self, command: PolicyAuditCommand) -> PolicyAuditResponse:
        results = self._policy.audit(namespace=None)
        return PolicyAuditResponse(results=results)

    def xǁPolicyAuditUseCaseǁexecute__mutmut_3(self, command: PolicyAuditCommand) -> PolicyAuditResponse:
        results = self._policy.audit(namespace=command.namespace)
        return PolicyAuditResponse(results=None)

mutants_xǁPolicyAuditUseCaseǁ__init____mutmut['_mutmut_orig'] = PolicyAuditUseCase.xǁPolicyAuditUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyAuditUseCaseǁ__init____mutmut['xǁPolicyAuditUseCaseǁ__init____mutmut_1'] = PolicyAuditUseCase.xǁPolicyAuditUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPolicyAuditUseCaseǁexecute__mutmut['_mutmut_orig'] = PolicyAuditUseCase.xǁPolicyAuditUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyAuditUseCaseǁexecute__mutmut['xǁPolicyAuditUseCaseǁexecute__mutmut_1'] = PolicyAuditUseCase.xǁPolicyAuditUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyAuditUseCaseǁexecute__mutmut['xǁPolicyAuditUseCaseǁexecute__mutmut_2'] = PolicyAuditUseCase.xǁPolicyAuditUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyAuditUseCaseǁexecute__mutmut['xǁPolicyAuditUseCaseǁexecute__mutmut_3'] = PolicyAuditUseCase.xǁPolicyAuditUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
