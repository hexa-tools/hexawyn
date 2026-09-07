from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_app_sync.command import GitopsAppSyncCommand
from hexawyn.application.use_case.gitops.gitops_app_sync.response import GitopsAppSyncResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGitopsAppSyncUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GitopsAppSyncUseCase:
    @_mutmut_mutated(mutants_xǁGitopsAppSyncUseCaseǁ__init____mutmut)
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsAppSyncUseCaseǁ__init____mutmut_orig(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsAppSyncUseCaseǁ__init____mutmut_1(self, gitops_port: GitOpsPort) -> None:
        self._gitops = None

    @_mutmut_mutated(mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut)
    def execute(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_orig(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_1(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = None
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_2(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=None, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_3(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=None)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_4(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_5(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, )
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_6(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=None,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_7(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=None,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_8(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=None,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_9(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=None,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_10(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=None,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_11(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=None,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_12(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_13(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_14(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_15(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_16(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppSyncUseCaseǁexecute__mutmut_17(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            )

mutants_xǁGitopsAppSyncUseCaseǁ__init____mutmut['_mutmut_orig'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁ__init____mutmut['xǁGitopsAppSyncUseCaseǁ__init____mutmut_1'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['_mutmut_orig'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_1'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_2'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_3'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_4'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_5'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_6'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_7'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_8'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_9'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_10'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_11'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_12'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_13'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_14'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_15'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_16'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitopsAppSyncUseCaseǁexecute__mutmut['xǁGitopsAppSyncUseCaseǁexecute__mutmut_17'] = GitopsAppSyncUseCase.xǁGitopsAppSyncUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
