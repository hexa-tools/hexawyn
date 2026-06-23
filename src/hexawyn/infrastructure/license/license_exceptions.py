from hexawyn.domain.errors import HexawynError


class LicenseInvalidError(HexawynError):
    """Invalid or corrupted license."""


class LicenseExpiredError(HexawynError):
    """License has expired."""


class LicenseMissingError(HexawynError):
    """No license found."""


class ProviderNotLicensedError(HexawynError):
    """The requested provider is not covered by this license."""


LicenseValidationError = LicenseInvalidError
