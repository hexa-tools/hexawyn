import asyncio
import os

import click

from hexawyn.adapters.primary.slack.slack_chat_adapter import SlackChatAdapter
from hexawyn.adapters.primary.slack.slack_event_server import SlackEventServer
from hexawyn.adapters.primary.slack.slack_socket_client import SlackSocketClient
from hexawyn.adapters.secondary.slack.slack_alert_adapter import SlackAlertAdapter
from hexawyn.adapters.secondary.slack.slack_http_client import SlackHttpClient
from hexawyn.adapters.secondary.slack.slack_http_publisher import SlackHttpPublisher
from hexawyn.infrastructure.config.quota_manager import _get_current_slack_quota


def _require_env_token(env_var: str, display_name: str) -> str | None:
    token = os.environ.get(env_var)
    if not token:
        click.echo(
            f"❌ {env_var} not set.\n"
            "Add it to your .env file or run:\n"
            f"  export {env_var}={display_name}"
        )
        return None
    return token


@click.group()
def slack() -> None:
    """Manage Slack integration."""


@slack.command()
def test() -> None:
    """Send a test Slack alert to verify webhook configuration."""
    webhook_url = os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL")
    if not webhook_url:
        click.echo(
            "❌ HEXAWYN_SLACK_WEBHOOK_URL not set.\n"
            "Add it to your .env file or run:\n"
            "export HEXAWYN_SLACK_WEBHOOK_URL=https://hooks.slack.com/..."
        )
        return

    adapter = SlackAlertAdapter(webhook_url=webhook_url)

    if adapter.send_test_ping():
        click.echo("✅ Test alert sent successfully!")
    else:
        click.echo("❌ Failed to send test alert. Check your webhook URL.")


@slack.command()
@click.option(
    "--http",
    "use_http",
    is_flag=True,
    default=False,
    help="Use HTTP Events API (legacy) instead of Socket Mode.",
)
@click.option(
    "--port", default=8080, show_default=True, help="Port for HTTP listener (only with --http)."
)
@click.option(
    "--cluster",
    default=None,
    help="Target cluster name (overrides active kubectl context).",
)
def listen(use_http: bool, port: int, cluster: str | None) -> None:
    """Start the Slack listener (Socket Mode by default, no public URL needed).

    Socket Mode requires SLACK_APP_TOKEN (xapp-...) and SLACK_BOT_TOKEN (xoxb-...).
    Use --http for the legacy HTTP Events API listener.
    Use --cluster to target a specific cluster (default: active kubectl context).
    """
    if use_http:
        _start_http_listener(port)
        return
    asyncio.run(_start_socket_listener(cluster))


def _start_http_listener(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


async def _start_socket_listener(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    socket_client = SlackSocketClient(
        chat_adapter=chat_adapter,
        publisher=publisher,
        http_client=http_client,
        app_token=app_token,
        cluster_name=cluster_name,
    )

    display_cluster = cluster_name or "active kubectl context"
    click.echo("🔌 hexawyn Slack Socket Mode listener — no public URL needed")
    click.echo(f"   Cluster: {display_cluster}")
    click.echo("   Make sure Socket Mode is enabled in your Slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


@slack.command()
def status() -> None:
    """Show Slack integration status and quota."""
    webhook_url = os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL", "")
    bot_token = os.environ.get("SLACK_BOT_TOKEN", "")
    app_token = os.environ.get("SLACK_APP_TOKEN", "")
    quota = _get_current_slack_quota()

    click.echo("\nhexawyn Slack Status")
    click.echo("──────────────────────────────")
    click.echo(f"Webhook  : {'✅ configured' if webhook_url else '❌ not set'}")
    click.echo(f"Bot Token: {'✅ configured' if bot_token else '❌ not set'}")
    click.echo(f"App Token: {'✅ configured' if app_token else '❌ not set'}")
    click.echo(
        f"Mode     : {'Socket Mode (default)' if app_token else 'HTTP Events API (use --http)'}"
    )
    if quota.is_unlimited:
        click.echo("Alerts   : ⭐ Pro — unlimited")
    else:
        click.echo(
            f"Alerts   : {quota.count}/{quota.limit} this month" f" · {quota.remaining} remaining"
        )
