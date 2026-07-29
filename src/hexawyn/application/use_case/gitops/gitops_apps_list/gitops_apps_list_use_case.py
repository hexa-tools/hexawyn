from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_apps_list.command import GitopsAppsListCommand
from hexawyn.application.use_case.gitops.gitops_apps_list.response import GitopsAppsListResponse


class GitopsAppsListUseCase:
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def execute(self, command: GitopsAppsListCommand) -> GitopsAppsListResponse:
        apps = self._gitops.list_apps(namespace=command.namespace)
        return GitopsAppsListResponse(apps=[asdict(app) for app in apps])
