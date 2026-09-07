from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_apps_list.command import GitopsAppsListCommand
from hexawyn.application.use_case.gitops.gitops_apps_list.response import GitopsAppsListResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGitopsAppsListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitopsAppsListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GitopsAppsListUseCase:
    @_mutmut_mutated(mutants_xǁGitopsAppsListUseCaseǁ__init____mutmut)
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsAppsListUseCaseǁ__init____mutmut_orig(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsAppsListUseCaseǁ__init____mutmut_1(self, gitops_port: GitOpsPort) -> None:
        self._gitops = None

    @_mutmut_mutated(mutants_xǁGitopsAppsListUseCaseǁexecute__mutmut)
    def execute(self, command: GitopsAppsListCommand) -> GitopsAppsListResponse:
        apps = self._gitops.list_apps(namespace=command.namespace)
        return GitopsAppsListResponse(apps=[asdict(app) for app in apps])

    def xǁGitopsAppsListUseCaseǁexecute__mutmut_orig(self, command: GitopsAppsListCommand) -> GitopsAppsListResponse:
        apps = self._gitops.list_apps(namespace=command.namespace)
        return GitopsAppsListResponse(apps=[asdict(app) for app in apps])

    def xǁGitopsAppsListUseCaseǁexecute__mutmut_1(self, command: GitopsAppsListCommand) -> GitopsAppsListResponse:
        apps = None
        return GitopsAppsListResponse(apps=[asdict(app) for app in apps])

    def xǁGitopsAppsListUseCaseǁexecute__mutmut_2(self, command: GitopsAppsListCommand) -> GitopsAppsListResponse:
        apps = self._gitops.list_apps(namespace=None)
        return GitopsAppsListResponse(apps=[asdict(app) for app in apps])

    def xǁGitopsAppsListUseCaseǁexecute__mutmut_3(self, command: GitopsAppsListCommand) -> GitopsAppsListResponse:
        apps = self._gitops.list_apps(namespace=command.namespace)
        return GitopsAppsListResponse(apps=None)

    def xǁGitopsAppsListUseCaseǁexecute__mutmut_4(self, command: GitopsAppsListCommand) -> GitopsAppsListResponse:
        apps = self._gitops.list_apps(namespace=command.namespace)
        return GitopsAppsListResponse(apps=[asdict(None) for app in apps])

mutants_xǁGitopsAppsListUseCaseǁ__init____mutmut['_mutmut_orig'] = GitopsAppsListUseCase.xǁGitopsAppsListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsAppsListUseCaseǁ__init____mutmut['xǁGitopsAppsListUseCaseǁ__init____mutmut_1'] = GitopsAppsListUseCase.xǁGitopsAppsListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitopsAppsListUseCaseǁexecute__mutmut['_mutmut_orig'] = GitopsAppsListUseCase.xǁGitopsAppsListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsAppsListUseCaseǁexecute__mutmut['xǁGitopsAppsListUseCaseǁexecute__mutmut_1'] = GitopsAppsListUseCase.xǁGitopsAppsListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitopsAppsListUseCaseǁexecute__mutmut['xǁGitopsAppsListUseCaseǁexecute__mutmut_2'] = GitopsAppsListUseCase.xǁGitopsAppsListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitopsAppsListUseCaseǁexecute__mutmut['xǁGitopsAppsListUseCaseǁexecute__mutmut_3'] = GitopsAppsListUseCase.xǁGitopsAppsListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitopsAppsListUseCaseǁexecute__mutmut['xǁGitopsAppsListUseCaseǁexecute__mutmut_4'] = GitopsAppsListUseCase.xǁGitopsAppsListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
