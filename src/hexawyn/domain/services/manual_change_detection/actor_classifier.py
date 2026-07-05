from __future__ import annotations

from collections.abc import Sequence

from hexawyn.domain.models.manual_change import ActorType

_SERVICE_ACCOUNT_PREFIX = "system:serviceaccount:"


def classify_actor(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller in actor for controller in gitops_controllers):
        return "gitops_controller"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "service_account"
    return "human"
