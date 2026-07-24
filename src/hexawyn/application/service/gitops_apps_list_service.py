from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops_apps_list.command import (
    GitOpsAppsListCommand,
)
from hexawyn.application.use_case.gitops_apps_list.response import (
    GitOpsAppsListResponse,
)
from hexawyn.application.ports.driving.gitops_apps_list.gitops_apps_list_service_port import (
    GitOpsAppsListServicePort,
)


class GitOpsAppsListService(GitOpsAppsListServicePort):
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def list_apps(self, command: GitOpsAppsListCommand) -> GitOpsAppsListResponse:
        apps = self._gitops.list_apps(namespace=command.namespace)
        return GitOpsAppsListResponse(
            apps=[asdict(app) for app in apps],
        )
