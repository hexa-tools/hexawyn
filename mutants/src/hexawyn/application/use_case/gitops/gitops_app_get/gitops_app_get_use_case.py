from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_app_get.command import GitopsAppGetCommand
from hexawyn.application.use_case.gitops.gitops_app_get.response import GitopsAppGetResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGitopsAppGetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GitopsAppGetUseCase:
    @_mutmut_mutated(mutants_xǁGitopsAppGetUseCaseǁ__init____mutmut)
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsAppGetUseCaseǁ__init____mutmut_orig(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port
    def xǁGitopsAppGetUseCaseǁ__init____mutmut_1(self, gitops_port: GitOpsPort) -> None:
        self._gitops = None

    @_mutmut_mutated(mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut)
    def execute(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_orig(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_1(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = None
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_2(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=None, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_3(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=None)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_4(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_5(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, )
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_6(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=None,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_7(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=None,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_8(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=None,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_9(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=None,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_10(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=None,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_11(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=None,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_12(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=None,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_13(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=None,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_14(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=None,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_15(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=None,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_16(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=None,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_17(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_18(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_19(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_20(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_21(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_22(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_23(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_24(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_25(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_26(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            message=app.message,
        )

    def xǁGitopsAppGetUseCaseǁexecute__mutmut_27(self, command: GitopsAppGetCommand) -> GitopsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,  # type: ignore
            source_url=app.source_url,  # type: ignore
            revision=app.revision,
            )

mutants_xǁGitopsAppGetUseCaseǁ__init____mutmut['_mutmut_orig'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁ__init____mutmut['xǁGitopsAppGetUseCaseǁ__init____mutmut_1'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['_mutmut_orig'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_1'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_2'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_3'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_4'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_5'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_6'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_7'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_8'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_9'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_10'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_11'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_12'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_13'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_14'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_15'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_16'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_17'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_18'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_19'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_20'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_21'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_22'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_23'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_24'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_25'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_26'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitopsAppGetUseCaseǁexecute__mutmut['xǁGitopsAppGetUseCaseǁexecute__mutmut_27'] = GitopsAppGetUseCase.xǁGitopsAppGetUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
