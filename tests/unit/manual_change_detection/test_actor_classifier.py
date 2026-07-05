"""Unit tests for classify_actor — GitOps-controller allow-list (substring)
first, system:serviceaccount: prefix second, human default last."""

from __future__ import annotations

_CONTROLLERS = ("argocd-application-controller", "flux-kustomize-controller")


class TestGitOpsControllerDetection:
    def test_exact_manager_name_is_gitops_controller(self) -> None:
        from hexawyn.domain.services.manual_change_detection.actor_classifier import (
            classify_actor,
        )

        assert classify_actor("argocd-application-controller", _CONTROLLERS) == "gitops_controller"

    def test_full_service_account_identity_containing_controller_name_is_gitops_controller(
        self,
    ) -> None:
        from hexawyn.domain.services.manual_change_detection.actor_classifier import (
            classify_actor,
        )

        actor = "system:serviceaccount:argocd:argocd-application-controller"
        assert classify_actor(actor, _CONTROLLERS) == "gitops_controller"

    def test_flux_controller_is_gitops_controller(self) -> None:
        from hexawyn.domain.services.manual_change_detection.actor_classifier import (
            classify_actor,
        )

        assert classify_actor("flux-kustomize-controller", _CONTROLLERS) == "gitops_controller"


class TestServiceAccountDetection:
    def test_ci_pipeline_service_account_is_service_account(self) -> None:
        from hexawyn.domain.services.manual_change_detection.actor_classifier import (
            classify_actor,
        )

        actor = "system:serviceaccount:ci:pipeline-runner"
        assert classify_actor(actor, _CONTROLLERS) == "service_account"

    def test_human_sounding_service_account_name_is_still_service_account(self) -> None:
        """Edge case: SA name looks like a human user — heuristic is the
        system:serviceaccount: prefix, never name-shape guessing."""
        from hexawyn.domain.services.manual_change_detection.actor_classifier import (
            classify_actor,
        )

        actor = "system:serviceaccount:default:jane-lookalike"
        assert classify_actor(actor, _CONTROLLERS) == "service_account"


class TestHumanDetection:
    def test_user_prefixed_actor_is_human(self) -> None:
        from hexawyn.domain.services.manual_change_detection.actor_classifier import (
            classify_actor,
        )

        assert classify_actor("user:john.doe@company.com", _CONTROLLERS) == "human"

    def test_managed_fields_manager_name_is_human_by_default(self) -> None:
        """Fallback path: managedFields manager names like kubectl-client-side-apply
        carry no serviceaccount/controller signal, so default to human."""
        from hexawyn.domain.services.manual_change_detection.actor_classifier import (
            classify_actor,
        )

        assert classify_actor("kubectl-client-side-apply", _CONTROLLERS) == "human"

    def test_bare_email_is_human(self) -> None:
        from hexawyn.domain.services.manual_change_detection.actor_classifier import (
            classify_actor,
        )

        assert classify_actor("jane.ops@company.com", _CONTROLLERS) == "human"
