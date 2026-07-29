from dataclasses import dataclass


@dataclass(frozen=True)
class UnintendedExternalExposureCommand:
    namespace: str | None = None
