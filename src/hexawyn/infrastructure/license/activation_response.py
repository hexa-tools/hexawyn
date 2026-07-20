"""Activation response contract — validated when received from hexa-cloud."""

from datetime import datetime

from pydantic import BaseModel, field_validator

_VALID_PLANS = {"starter", "team", "scale_up"}


class ActivationResponse(BaseModel):
    token: str
    plan: str
    expires_at: str

    @field_validator("plan")
    @classmethod
    def plan_must_be_valid(cls, value: str) -> str:
        if value not in _VALID_PLANS:
            raise ValueError(f"plan must be one of {sorted(_VALID_PLANS)}")
        return value

    @field_validator("expires_at")
    @classmethod
    def expires_at_must_be_iso(cls, value: str) -> str:
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
        except (ValueError, TypeError):
            raise ValueError("expires_at must be ISO 8601")
        return value
