"""hexa auth — manage hexawyn cloud authentication and licensing."""

import base64
import json
from datetime import UTC, datetime
from pathlib import Path

import click
import httpx

from hexawyn.infrastructure.config.config_manager import load_config, save_config

LICENSE_KEY_PATH = Path.home() / ".hexawyn" / "license.key"
HEXA_CLOUD_BASE_URL = "https://api.hexawyn.com"


@click.group()
def auth() -> None:
    """Manage hexawyn cloud license and authentication."""


@auth.command()
@click.argument("token")
@click.option(
    "--endpoint",
    default=HEXA_CLOUD_BASE_URL,
    help="hexa-cloud API endpoint",
    envvar="HEXAWYN_CLOUD_ENDPOINT",
)
def set_token(token: str, endpoint: str) -> None:
    """Activate a license by providing your hexawyn API key.

    TOKEN is the API key received by email after subscribing.
    """
    token = token.strip()

    url = f"{endpoint}/api/v1/license/activate"
    try:
        response = _activate_license(url, token)
    except httpx.ConnectError:
        click.echo(f"❌ Failed to connect to {endpoint}. Is the API reachable?", err=True)
        raise SystemExit(1)

    if response.status_code != 200:
        detail = "Unknown error"
        try:
            detail = response.json().get("detail", detail)
        except Exception:
            pass
        click.echo(f"❌ License activation failed: {detail}", err=True)
        raise SystemExit(1)

    data = response.json()
    jwt_token = data.get("token", "")
    plan = data.get("plan", "unknown")
    expires_at = data.get("expires_at", "")

    LICENSE_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LICENSE_KEY_PATH.write_text(jwt_token)

    config = load_config()
    config["hexawyn_token"] = token
    config["hexawyn_token_prefix"] = token[: min(len(token), 16)]
    save_config(config)

    click.echo(f"✅ License activated — Plan: {plan}")
    click.echo(f"   Token:  {token[:16]}...")
    click.echo(f"   Expires: {_format_expiry(expires_at)}")


@auth.command()
def status() -> None:
    """Show current license activation status."""
    jwt_raw = _read_license_key()
    if jwt_raw is None:
        click.echo("❌ License not configured. Run `hexa auth set-token <TOKEN>` to activate.")
        return

    payload = _decode_jwt_payload(jwt_raw)
    if payload is None:
        click.echo("❌ Could not read license data.")
        return

    plan = str(payload.get("plan", "unknown"))
    exp = payload.get("exp", 0)
    exp_int = int(exp) if isinstance(exp, int | float | str) else 0

    if _is_jwt_expired(exp_int):
        click.echo(f"⚠ License expired — Plan: {plan}")
        click.echo("   Run `hexa auth set-token <TOKEN>` to renew.")
        return

    click.echo(f"✅ License active — Plan: {plan}")
    click.echo(f"   Expires: {_format_expiry_from_timestamp(exp_int)}")


def _activate_license(url: str, token: str) -> httpx.Response:
    """Call the hexa-cloud license activation endpoint (synchronous)."""
    import asyncio

    async def _post() -> httpx.Response:
        from hexawyn.infrastructure.config.machine_id import get_machine_id

        machine_id = get_machine_id()
        async with httpx.AsyncClient(timeout=10) as client:
            return await client.post(
                url,
                json={
                    "api_key": token,
                    "machine_id": machine_id,
                    "client_version": "1.0.0",
                },
            )

    return asyncio.run(_post())


def _read_license_key() -> str | None:
    if not LICENSE_KEY_PATH.exists():
        return None
    raw = LICENSE_KEY_PATH.read_text().strip()
    return raw or None


def _decode_jwt_payload(jwt_raw: str) -> dict[str, object] | None:
    try:
        parts = jwt_raw.split(".")
        if len(parts) < 2:
            return None
        payload_b64 = parts[1]
        # Add padding if needed
        padding = 4 - len(payload_b64) % 4
        if padding != 4:
            payload_b64 += "=" * padding
        payload_json = base64.urlsafe_b64decode(payload_b64).decode()
        result: object = json.loads(payload_json)
        if isinstance(result, dict):
            return result
        return None
    except Exception:
        return None


def _is_jwt_expired(exp: int) -> bool:
    if not exp:
        return False
    try:
        return datetime.fromtimestamp(exp, tz=UTC) <= datetime.now(UTC)
    except (ValueError, OverflowError):
        return False


def _format_expiry(expires_at: str) -> str:
    if not expires_at:
        return "unknown"
    try:
        dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        days = (dt - datetime.now(UTC)).days
        return f"{expires_at} ({days} days)"
    except (ValueError, OverflowError):
        return expires_at


def _format_expiry_from_timestamp(exp: int) -> str:
    if not exp:
        return "unknown"
    try:
        dt = datetime.fromtimestamp(exp, tz=UTC)
        days = (dt - datetime.now(UTC)).days
        return f"{dt.isoformat()} ({days} days)"
    except (ValueError, OverflowError):
        return str(exp)


@auth.command()
def account() -> None:
    """Open the subscription management portal in your browser."""
    import webbrowser

    from hexawyn.infrastructure.config.config_manager import load_config

    config = load_config()
    token = config.get("hexawyn_token")

    if not token:
        click.echo(
            "❌ No license configured. Run `hexa auth set-token <TOKEN>` first.",
            err=True,
        )
        raise SystemExit(1)

    import httpx

    try:
        resp = httpx.post(
            "https://api.hexawyn.com/api/v1/billing/portal",
            json={"api_key": token},
            timeout=10,
        )
    except httpx.ConnectError:
        click.echo("❌ Cannot reach hexa-cloud. Visit polar.sh/purchases directly.")
        raise SystemExit(1)

    if resp.status_code != 200:
        if resp.status_code == 404:
            click.echo(
                "❌ Portal not available yet. Visit [link]https://polar.sh/purchases/subscriptions[/link]"
            )
        else:
            detail = "Unknown error"
            try:
                detail = resp.json().get("detail", detail)
            except Exception:
                pass
            click.echo(f"❌ {detail}")
        raise SystemExit(1)

    url = resp.json().get("url", "")
    if not url:
        click.echo("❌ No portal URL returned.", err=True)
        raise SystemExit(1)

    click.echo(f"Opening subscription portal: {url}")
    webbrowser.open(url)
