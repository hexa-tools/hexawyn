from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_detect.command import GitopsDetectCommand
from hexawyn.application.use_case.gitops.gitops_detect.response import GitopsDetectResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGitopsDetectUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GitopsDetectUseCase:
    @_mutmut_mutated(mutants_xǁGitopsDetectUseCaseǁ__init____mutmut)
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsDetectUseCaseǁ__init____mutmut_orig(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsDetectUseCaseǁ__init____mutmut_1(self, gitops_port: GitOpsPort) -> None:
        self._gitops = None

    @_mutmut_mutated(mutants_xǁGitopsDetectUseCaseǁexecute__mutmut)
    def execute(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_orig(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_1(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = None
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_2(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=None,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_3(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=None,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_4(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=None,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_5(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=None,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_6(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=None,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_7(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=None,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_8(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_9(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_10(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_11(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_12(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            failed_count=result.failed_count,
        )

    def xǁGitopsDetectUseCaseǁexecute__mutmut_13(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            )

mutants_xǁGitopsDetectUseCaseǁ__init____mutmut['_mutmut_orig'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁ__init____mutmut['xǁGitopsDetectUseCaseǁ__init____mutmut_1'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['_mutmut_orig'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_1'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_2'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_3'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_4'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_5'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_6'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_7'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_8'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_9'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_10'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_11'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_12'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitopsDetectUseCaseǁexecute__mutmut['xǁGitopsDetectUseCaseǁexecute__mutmut_13'] = GitopsDetectUseCase.xǁGitopsDetectUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
