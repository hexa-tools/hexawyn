from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.governance.policy_explain_denial.command import (
    PolicyExplainDenialCommand,
)
from hexawyn.application.use_case.governance.policy_explain_denial.response import (
    PolicyExplainDenialResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPolicyExplainDenialUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class PolicyExplainDenialUseCase:
    @_mutmut_mutated(mutants_xǁPolicyExplainDenialUseCaseǁ__init____mutmut)
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyExplainDenialUseCaseǁ__init____mutmut_orig(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyExplainDenialUseCaseǁ__init____mutmut_1(self, policy_port: PolicyPort) -> None:
        self._policy = None

    @_mutmut_mutated(mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut)
    def execute(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_orig(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_1(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = None
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_2(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=None,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_3(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=None,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_4(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=None,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_5(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_6(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_7(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_8(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=None,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_9(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=None,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_10(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=None,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_11(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=None,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_12(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=None,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_13(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_14(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_15(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_16(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            fix_suggestion=e.fix_suggestion,
        )

    def xǁPolicyExplainDenialUseCaseǁexecute__mutmut_17(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            )

mutants_xǁPolicyExplainDenialUseCaseǁ__init____mutmut['_mutmut_orig'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁ__init____mutmut['xǁPolicyExplainDenialUseCaseǁ__init____mutmut_1'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['_mutmut_orig'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_1'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_2'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_3'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_4'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_5'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_6'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_7'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_8'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_9'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_10'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_11'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_12'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_13'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_14'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_15'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_16'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPolicyExplainDenialUseCaseǁexecute__mutmut['xǁPolicyExplainDenialUseCaseǁexecute__mutmut_17'] = PolicyExplainDenialUseCase.xǁPolicyExplainDenialUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
