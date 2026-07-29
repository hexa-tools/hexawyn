from dataclasses import dataclass


@dataclass(frozen=True)
class EastWestNetworkSegmentationCommand:
    namespace: str | None = None
