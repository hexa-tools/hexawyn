from abc import ABC


class TestScheduleStorePortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.schedule_store_port import (
            ScheduleStorePort,
        )

        assert issubclass(ScheduleStorePort, ABC)

    def test_declares_required_methods(self) -> None:
        from hexawyn.application.ports.driven.schedule_store_port import (
            ScheduleStorePort,
        )

        expected = {
            "list_checks",
            "get_check",
            "save_check",
            "delete_check",
            "save_result",
            "last_result",
            "history",
        }

        assert expected <= ScheduleStorePort.__abstractmethods__
