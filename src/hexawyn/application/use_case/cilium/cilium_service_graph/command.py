from dataclasses import dataclass


@dataclass(frozen=True)
class CiliumServiceGraphCommand:
    time_window_minutes: int = 60
