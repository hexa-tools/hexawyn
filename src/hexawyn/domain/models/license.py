from dataclasses import dataclass
from datetime import UTC, datetime

from hexawyn.domain.models.quota import LicenseTier


@dataclass
class LicenseKey:
    """
    A signed license key that unlocks a specific tier.

    Fields:
        tier: the LicenseTier this key activates
        expires_at: expiration date (UTC). None = perpetual.
        licensee: email or company name this key was issued to
    """

    tier: LicenseTier
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
