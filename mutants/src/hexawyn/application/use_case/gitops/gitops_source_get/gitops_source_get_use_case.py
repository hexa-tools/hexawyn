from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_source_get.command import GitopsSourceGetCommand
from hexawyn.application.use_case.gitops.gitops_source_get.response import GitopsSourceGetResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGitopsSourceGetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GitopsSourceGetUseCase:
    @_mutmut_mutated(mutants_xǁGitopsSourceGetUseCaseǁ__init____mutmut)
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsSourceGetUseCaseǁ__init____mutmut_orig(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsSourceGetUseCaseǁ__init____mutmut_1(self, gitops_port: GitOpsPort) -> None:
        self._gitops = None

    @_mutmut_mutated(mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut)
    def execute(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_orig(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_1(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = None
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_2(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=None, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_3(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=None)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_4(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_5(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, )
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_6(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=None,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_7(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=None,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_8(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=None,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_9(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=None,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_10(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=None,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_11(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=None,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_12(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=None,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_13(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_14(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_15(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_16(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_17(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_18(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            message=source.message,  # type: ignore
        )

    def xǁGitopsSourceGetUseCaseǁexecute__mutmut_19(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            )

mutants_xǁGitopsSourceGetUseCaseǁ__init____mutmut['_mutmut_orig'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁ__init____mutmut['xǁGitopsSourceGetUseCaseǁ__init____mutmut_1'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['_mutmut_orig'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_1'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_2'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_3'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_4'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_5'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_6'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_7'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_8'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_9'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_10'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_11'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_12'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_13'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_14'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_15'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_16'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_17'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_18'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitopsSourceGetUseCaseǁexecute__mutmut['xǁGitopsSourceGetUseCaseǁexecute__mutmut_19'] = GitopsSourceGetUseCase.xǁGitopsSourceGetUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
