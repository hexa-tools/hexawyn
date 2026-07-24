from dataclasses import dataclass


@dataclass
class UnintendedExternalExposureResponse:
    error: str | None = None
