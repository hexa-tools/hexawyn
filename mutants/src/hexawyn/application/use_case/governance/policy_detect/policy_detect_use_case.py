from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.governance.policy_detect.command import (
    PolicyDetectCommand,
)
from hexawyn.application.use_case.governance.policy_detect.response import (
    PolicyDetectResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPolicyDetectUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class PolicyDetectUseCase:
    @_mutmut_mutated(mutants_xǁPolicyDetectUseCaseǁ__init____mutmut)
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyDetectUseCaseǁ__init____mutmut_orig(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port
    def xǁPolicyDetectUseCaseǁ__init____mutmut_1(self, policy_port: PolicyPort) -> None:
        self._policy = None

    @_mutmut_mutated(mutants_xǁPolicyDetectUseCaseǁexecute__mutmut)
    def execute(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_orig(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_1(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = None
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_2(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=None,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_3(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=None,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_4(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=None,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_5(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=None,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_6(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=None,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_7(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=None,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_8(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=None,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_9(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=None,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_10(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_11(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_12(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_13(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_14(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_15(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            total_violations=r.total_violations,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_16(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            high_severity=r.high_severity,
        )

    def xǁPolicyDetectUseCaseǁexecute__mutmut_17(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        r = self._policy.detect_engine()
        return PolicyDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            total_policies=r.total_policies,
            enforce_policies=r.enforce_policies,
            audit_policies=r.audit_policies,
            total_violations=r.total_violations,
            )

mutants_xǁPolicyDetectUseCaseǁ__init____mutmut['_mutmut_orig'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁ__init____mutmut['xǁPolicyDetectUseCaseǁ__init____mutmut_1'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['_mutmut_orig'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_1'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_2'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_3'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_4'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_5'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_6'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_7'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_8'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_9'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_10'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_11'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_12'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_13'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_14'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_15'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_16'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPolicyDetectUseCaseǁexecute__mutmut['xǁPolicyDetectUseCaseǁexecute__mutmut_17'] = PolicyDetectUseCase.xǁPolicyDetectUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
