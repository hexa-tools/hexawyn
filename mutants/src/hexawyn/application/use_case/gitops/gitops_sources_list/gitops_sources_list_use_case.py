from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_sources_list.command import GitopsSourcesListCommand
from hexawyn.application.use_case.gitops.gitops_sources_list.response import (
    GitopsSourcesListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGitopsSourcesListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitopsSourcesListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GitopsSourcesListUseCase:
    @_mutmut_mutated(mutants_xǁGitopsSourcesListUseCaseǁ__init____mutmut)
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsSourcesListUseCaseǁ__init____mutmut_orig(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsSourcesListUseCaseǁ__init____mutmut_1(self, gitops_port: GitOpsPort) -> None:
        self._gitops = None

    @_mutmut_mutated(mutants_xǁGitopsSourcesListUseCaseǁexecute__mutmut)
    def execute(self, command: GitopsSourcesListCommand) -> GitopsSourcesListResponse:
        sources = self._gitops.list_sources(namespace=command.namespace)
        return GitopsSourcesListResponse(sources=[asdict(source) for source in sources])

    def xǁGitopsSourcesListUseCaseǁexecute__mutmut_orig(self, command: GitopsSourcesListCommand) -> GitopsSourcesListResponse:
        sources = self._gitops.list_sources(namespace=command.namespace)
        return GitopsSourcesListResponse(sources=[asdict(source) for source in sources])

    def xǁGitopsSourcesListUseCaseǁexecute__mutmut_1(self, command: GitopsSourcesListCommand) -> GitopsSourcesListResponse:
        sources = None
        return GitopsSourcesListResponse(sources=[asdict(source) for source in sources])

    def xǁGitopsSourcesListUseCaseǁexecute__mutmut_2(self, command: GitopsSourcesListCommand) -> GitopsSourcesListResponse:
        sources = self._gitops.list_sources(namespace=None)
        return GitopsSourcesListResponse(sources=[asdict(source) for source in sources])

    def xǁGitopsSourcesListUseCaseǁexecute__mutmut_3(self, command: GitopsSourcesListCommand) -> GitopsSourcesListResponse:
        sources = self._gitops.list_sources(namespace=command.namespace)
        return GitopsSourcesListResponse(sources=None)

    def xǁGitopsSourcesListUseCaseǁexecute__mutmut_4(self, command: GitopsSourcesListCommand) -> GitopsSourcesListResponse:
        sources = self._gitops.list_sources(namespace=command.namespace)
        return GitopsSourcesListResponse(sources=[asdict(None) for source in sources])

mutants_xǁGitopsSourcesListUseCaseǁ__init____mutmut['_mutmut_orig'] = GitopsSourcesListUseCase.xǁGitopsSourcesListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsSourcesListUseCaseǁ__init____mutmut['xǁGitopsSourcesListUseCaseǁ__init____mutmut_1'] = GitopsSourcesListUseCase.xǁGitopsSourcesListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitopsSourcesListUseCaseǁexecute__mutmut['_mutmut_orig'] = GitopsSourcesListUseCase.xǁGitopsSourcesListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsSourcesListUseCaseǁexecute__mutmut['xǁGitopsSourcesListUseCaseǁexecute__mutmut_1'] = GitopsSourcesListUseCase.xǁGitopsSourcesListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitopsSourcesListUseCaseǁexecute__mutmut['xǁGitopsSourcesListUseCaseǁexecute__mutmut_2'] = GitopsSourcesListUseCase.xǁGitopsSourcesListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitopsSourcesListUseCaseǁexecute__mutmut['xǁGitopsSourcesListUseCaseǁexecute__mutmut_3'] = GitopsSourcesListUseCase.xǁGitopsSourcesListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitopsSourcesListUseCaseǁexecute__mutmut['xǁGitopsSourcesListUseCaseǁexecute__mutmut_4'] = GitopsSourcesListUseCase.xǁGitopsSourcesListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
