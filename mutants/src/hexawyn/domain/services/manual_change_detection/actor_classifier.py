from __future__ import annotations

from collections.abc import Sequence

from hexawyn.domain.models.manual_change import ActorType

_SERVICE_ACCOUNT_PREFIX = "system:serviceaccount:"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_actor__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_actor__mutmut)
def classify_actor(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller in actor for controller in gitops_controllers):
        return "gitops_controller"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "service_account"
    return "human"


def x_classify_actor__mutmut_orig(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller in actor for controller in gitops_controllers):
        return "gitops_controller"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "service_account"
    return "human"


def x_classify_actor__mutmut_1(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(None):
        return "gitops_controller"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "service_account"
    return "human"


def x_classify_actor__mutmut_2(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller not in actor for controller in gitops_controllers):
        return "gitops_controller"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "service_account"
    return "human"


def x_classify_actor__mutmut_3(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller in actor for controller in gitops_controllers):
        return "XXgitops_controllerXX"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "service_account"
    return "human"


def x_classify_actor__mutmut_4(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller in actor for controller in gitops_controllers):
        return "GITOPS_CONTROLLER"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "service_account"
    return "human"


def x_classify_actor__mutmut_5(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller in actor for controller in gitops_controllers):
        return "gitops_controller"
    if actor.startswith(None):
        return "service_account"
    return "human"


def x_classify_actor__mutmut_6(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller in actor for controller in gitops_controllers):
        return "gitops_controller"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "XXservice_accountXX"
    return "human"


def x_classify_actor__mutmut_7(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller in actor for controller in gitops_controllers):
        return "gitops_controller"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "SERVICE_ACCOUNT"
    return "human"


def x_classify_actor__mutmut_8(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller in actor for controller in gitops_controllers):
        return "gitops_controller"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "service_account"
    return "XXhumanXX"


def x_classify_actor__mutmut_9(actor: str, gitops_controllers: Sequence[str]) -> ActorType:
    if any(controller in actor for controller in gitops_controllers):
        return "gitops_controller"
    if actor.startswith(_SERVICE_ACCOUNT_PREFIX):
        return "service_account"
    return "HUMAN"

mutants_x_classify_actor__mutmut['_mutmut_orig'] = x_classify_actor__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_actor__mutmut['x_classify_actor__mutmut_1'] = x_classify_actor__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_actor__mutmut['x_classify_actor__mutmut_2'] = x_classify_actor__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_actor__mutmut['x_classify_actor__mutmut_3'] = x_classify_actor__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_actor__mutmut['x_classify_actor__mutmut_4'] = x_classify_actor__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_actor__mutmut['x_classify_actor__mutmut_5'] = x_classify_actor__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_actor__mutmut['x_classify_actor__mutmut_6'] = x_classify_actor__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_actor__mutmut['x_classify_actor__mutmut_7'] = x_classify_actor__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_actor__mutmut['x_classify_actor__mutmut_8'] = x_classify_actor__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_actor__mutmut['x_classify_actor__mutmut_9'] = x_classify_actor__mutmut_9 # type: ignore # mutmut generated
