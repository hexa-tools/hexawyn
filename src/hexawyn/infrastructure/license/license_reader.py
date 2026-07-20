import base64
import json
import logging
import os
from pathlib import Path

import httpx

from hexawyn.domain.models.license import LicenseClaims
from hexawyn.domain.services.license_state import LicenseState, compute_license_state

LICENSE_KEY_PATH = Path.home() / ".hexawyn" / "license.key"
HEXA_CLOUD_URL = "https://api.hexawyn.com"
REFRESH_INTERVAL_SECONDS = 6 * 3600

logger = logging.getLogger(__name__)


def read_license_state() -> LicenseState:
    token = _read_license_key()
    if not token:
        return LicenseState(state="missing", plan="unknown", days_remaining=0, expiry_date="")

    try:
        parts = token.strip().split(".")
        if len(parts) < 2:
            return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")

        payload = parts[1]
        padding = 4 - len(payload) % 4
        if padding != 4:
            payload += "=" * padding
        claims_dict = json.loads(base64.urlsafe_b64decode(payload).decode())

        exp_value = claims_dict.get("exp", 0)
        if exp_value == 0 and "plan" in claims_dict:
            return LicenseState(
                state="active",
                plan=str(claims_dict.get("plan", "starter")),
                days_remaining=0,
                expiry_date="unknown",
            )

        claims = LicenseClaims(
            sub=claims_dict.get("sub", ""),
            plan=claims_dict.get("plan", "starter"),
            clusters_max=claims_dict.get("clusters_max", 1),
            users_max=claims_dict.get("users_max", 1),
            investigations_monthly=claims_dict.get("investigations_monthly", 50),
            history_days=claims_dict.get("history_days", 7),
            providers=claims_dict.get("providers", ["vanilla"]),
            exp=int(exp_value),
            iat=int(claims_dict.get("iat", 0)),
        )

        return compute_license_state(claims)
    except Exception:
        return LicenseState(state="invalid", plan="unknown", days_remaining=0, expiry_date="")


def _read_license_key() -> str | None:
    try:
        env_key = os.environ.get("HEXAWYN_LICENSE_KEY")
        if env_key:
            return env_key.strip()
        if LICENSE_KEY_PATH.exists():
            return LICENSE_KEY_PATH.read_text(encoding="utf-8").strip()
        return None
    except Exception:
        return None


def refresh_license() -> bool:
    try:
        from hexawyn.infrastructure.config.config_manager import load_config
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        config = load_config()
        token = config.get("hexawyn_token")
        if not token:
            return False

        machine_id = get_machine_id()
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{HEXA_CLOUD_URL}/api/v1/license/refresh",
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )
            if resp.status_code == 200:
                data = resp.json()
                jwt_token = data.get("token", "")
                if jwt_token:
                    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
                    LICENSE_KEY_PATH.write_text(jwt_token)
                    return True
        return False
    except Exception:
        return False
