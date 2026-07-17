from abc import ABC


class TestProjectBudgetServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.project_budget.project_budget_service_port import (
            ProjectBudgetServicePort,
        )

        assert issubclass(ProjectBudgetServicePort, ABC)

    def test_declares_project_method(self) -> None:
        from hexawyn.application.ports.driving.project_budget.project_budget_service_port import (
            ProjectBudgetServicePort,
        )

        assert "project" in ProjectBudgetServicePort.__abstractmethods__
