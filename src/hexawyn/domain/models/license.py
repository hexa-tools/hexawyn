from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass
class LicenseKey:
    """
    A signed license key that unlocks a specific tier.
    Kept for backward compatibility with existing callers.
    """

    tier: str
    expires_at: datetime | None
    licensee: str

    @property
    def is_expired(self) -> bool:
        if self.expires_at is None:
            return False
        return datetime.now(UTC) > self.expires_at

    @property
    def is_valid(self) -> bool:
        return not self.is_expired


@dataclass
class LicenseClaims:
    """Claims contained in the JWT signed by the license server."""

    sub: str
    plan: str
    clusters_max: int
    users_max: int
    investigations_monthly: int
    history_days: int
    providers: list[str]
    exp: int
    iat: int

    @classmethod
    def free(cls) -> "LicenseClaims":
        """Default claims when no license is present (Free tier)."""
        return cls(
            sub="anonymous",
            plan="free",
            clusters_max=1,
            users_max=1,
            investigations_monthly=50,
            history_days=7,
            providers=["vanilla"],
            exp=9999999999,
            iat=0,
        )
