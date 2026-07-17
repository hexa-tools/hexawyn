from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort


class UsageMeterAdapter(UsageMeterPort):
    def __init__(self) -> None:
        self._counts: dict[str, int] = {}

    def set_usage(self, resource: str, count: int) -> None:
        self._counts[resource] = count

    def get_usage(self, resource: str) -> int:
        return self._counts.get(resource, 0)
