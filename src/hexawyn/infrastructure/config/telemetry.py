import json
import os
import threading
import urllib.request
from datetime import UTC, datetime

from hexawyn.infrastructure.config.license_manager import get_license_tier

TELEMETRY_URL = "https://api.hexawyn.com/v1/telemetry"
TELEMETRY_TIMEOUT = 5  # seconds


def is_telemetry_enabled() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("HEXAWYN_TELEMETRY", "").lower() == "true"


def _send_telemetry(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "hexawyn/0.1.0",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def send_startup_telemetry() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def send_investigation_telemetry(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()
