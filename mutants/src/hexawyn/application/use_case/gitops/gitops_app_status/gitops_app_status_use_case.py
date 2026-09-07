from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_app_status.command import GitopsAppStatusCommand
from hexawyn.application.use_case.gitops.gitops_app_status.response import GitopsAppStatusResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGitopsAppStatusUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GitopsAppStatusUseCase:
    @_mutmut_mutated(mutants_xǁGitopsAppStatusUseCaseǁ__init____mutmut)
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsAppStatusUseCaseǁ__init____mutmut_orig(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsAppStatusUseCaseǁ__init____mutmut_1(self, gitops_port: GitOpsPort) -> None:
        self._gitops = None

    @_mutmut_mutated(mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut)
    def execute(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_orig(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_1(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = None
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_2(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=None, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_3(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=None)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_4(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_5(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, )
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_6(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=None,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_7(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=None,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_8(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=None,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_9(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=None,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_10(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=None,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_11(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=None,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_12(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=None,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_13(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=None,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_14(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_15(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_16(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_17(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_18(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_19(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_20(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            message=app.message,  # type: ignore
        )

    def xǁGitopsAppStatusUseCaseǁexecute__mutmut_21(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            )

mutants_xǁGitopsAppStatusUseCaseǁ__init____mutmut['_mutmut_orig'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁ__init____mutmut['xǁGitopsAppStatusUseCaseǁ__init____mutmut_1'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['_mutmut_orig'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_1'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_2'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_3'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_4'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_5'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_6'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_7'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_8'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_9'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_10'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_11'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_12'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_13'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_14'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_15'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_16'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_17'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_18'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_19'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_20'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitopsAppStatusUseCaseǁexecute__mutmut['xǁGitopsAppStatusUseCaseǁexecute__mutmut_21'] = GitopsAppStatusUseCase.xǁGitopsAppStatusUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
