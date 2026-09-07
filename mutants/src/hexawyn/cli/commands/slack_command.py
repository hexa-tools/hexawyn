import asyncio
import os

import click

from hexawyn.infrastructure.adapters.primary.slack.slack_chat_adapter import SlackChatAdapter
from hexawyn.infrastructure.adapters.primary.slack.slack_event_server import SlackEventServer
from hexawyn.infrastructure.adapters.primary.slack.slack_socket_client import SlackSocketClient
from hexawyn.infrastructure.adapters.secondary.slack.slack_alert_adapter import SlackAlertAdapter
from hexawyn.infrastructure.adapters.secondary.slack.slack_http_client import SlackHttpClient
from hexawyn.infrastructure.adapters.secondary.slack.slack_http_publisher import SlackHttpPublisher
from hexawyn.infrastructure.config.quota_manager import _get_current_slack_quota


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__require_env_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__require_env_token__mutmut)
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


def x__require_env_token__mutmut_orig(env_var: str, display_name: str) -> str | None:
    token = os.environ.get(env_var)
    if not token:
        click.echo(
            f"❌ {env_var} not set.\n"
            "Add it to your .env file or run:\n"
            f"  export {env_var}={display_name}"
        )
        return None
    return token


def x__require_env_token__mutmut_1(env_var: str, display_name: str) -> str | None:
    token = None
    if not token:
        click.echo(
            f"❌ {env_var} not set.\n"
            "Add it to your .env file or run:\n"
            f"  export {env_var}={display_name}"
        )
        return None
    return token


def x__require_env_token__mutmut_2(env_var: str, display_name: str) -> str | None:
    token = os.environ.get(None)
    if not token:
        click.echo(
            f"❌ {env_var} not set.\n"
            "Add it to your .env file or run:\n"
            f"  export {env_var}={display_name}"
        )
        return None
    return token


def x__require_env_token__mutmut_3(env_var: str, display_name: str) -> str | None:
    token = os.environ.get(env_var)
    if token:
        click.echo(
            f"❌ {env_var} not set.\n"
            "Add it to your .env file or run:\n"
            f"  export {env_var}={display_name}"
        )
        return None
    return token


def x__require_env_token__mutmut_4(env_var: str, display_name: str) -> str | None:
    token = os.environ.get(env_var)
    if not token:
        click.echo(
            None
        )
        return None
    return token


def x__require_env_token__mutmut_5(env_var: str, display_name: str) -> str | None:
    token = os.environ.get(env_var)
    if not token:
        click.echo(
            f"❌ {env_var} not set.\n"
            "XXAdd it to your .env file or run:\nXX"
            f"  export {env_var}={display_name}"
        )
        return None
    return token


def x__require_env_token__mutmut_6(env_var: str, display_name: str) -> str | None:
    token = os.environ.get(env_var)
    if not token:
        click.echo(
            f"❌ {env_var} not set.\n"
            "add it to your .env file or run:\n"
            f"  export {env_var}={display_name}"
        )
        return None
    return token


def x__require_env_token__mutmut_7(env_var: str, display_name: str) -> str | None:
    token = os.environ.get(env_var)
    if not token:
        click.echo(
            f"❌ {env_var} not set.\n"
            "ADD IT TO YOUR .ENV FILE OR RUN:\n"
            f"  export {env_var}={display_name}"
        )
        return None
    return token

mutants_x__require_env_token__mutmut['_mutmut_orig'] = x__require_env_token__mutmut_orig # type: ignore # mutmut generated
mutants_x__require_env_token__mutmut['x__require_env_token__mutmut_1'] = x__require_env_token__mutmut_1 # type: ignore # mutmut generated
mutants_x__require_env_token__mutmut['x__require_env_token__mutmut_2'] = x__require_env_token__mutmut_2 # type: ignore # mutmut generated
mutants_x__require_env_token__mutmut['x__require_env_token__mutmut_3'] = x__require_env_token__mutmut_3 # type: ignore # mutmut generated
mutants_x__require_env_token__mutmut['x__require_env_token__mutmut_4'] = x__require_env_token__mutmut_4 # type: ignore # mutmut generated
mutants_x__require_env_token__mutmut['x__require_env_token__mutmut_5'] = x__require_env_token__mutmut_5 # type: ignore # mutmut generated
mutants_x__require_env_token__mutmut['x__require_env_token__mutmut_6'] = x__require_env_token__mutmut_6 # type: ignore # mutmut generated
mutants_x__require_env_token__mutmut['x__require_env_token__mutmut_7'] = x__require_env_token__mutmut_7 # type: ignore # mutmut generated


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
mutants_x__start_http_listener__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__start_http_listener__mutmut)
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


def x__start_http_listener__mutmut_orig(port: int) -> None:
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


def x__start_http_listener__mutmut_1(port: int) -> None:
    bot_token = None
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


def x__start_http_listener__mutmut_2(port: int) -> None:
    bot_token = _require_env_token(None, "xoxb-...")
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


def x__start_http_listener__mutmut_3(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", None)
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


def x__start_http_listener__mutmut_4(port: int) -> None:
    bot_token = _require_env_token("xoxb-...")
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


def x__start_http_listener__mutmut_5(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", )
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


def x__start_http_listener__mutmut_6(port: int) -> None:
    bot_token = _require_env_token("XXSLACK_BOT_TOKENXX", "xoxb-...")
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


def x__start_http_listener__mutmut_7(port: int) -> None:
    bot_token = _require_env_token("slack_bot_token", "xoxb-...")
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


def x__start_http_listener__mutmut_8(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "XXxoxb-...XX")
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


def x__start_http_listener__mutmut_9(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "XOXB-...")
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


def x__start_http_listener__mutmut_10(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if bot_token:
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


def x__start_http_listener__mutmut_11(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = None
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_12(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=None)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_13(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = None
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_14(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=None)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_15(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = None
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_16(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = None

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_17(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=None, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_18(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=None)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_19(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_20(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, )

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_21(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(None)
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_22(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo(None)
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_23(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("XX   Point your Slack app's Event Subscriptions URL to:XX")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_24(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   point your slack app's event subscriptions url to:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_25(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   POINT YOUR SLACK APP'S EVENT SUBSCRIPTIONS URL TO:")
    click.echo(f"   http://<your-host>:{port}/slack/events")
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_26(port: int) -> None:
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    server = SlackEventServer(chat_adapter=chat_adapter, publisher=publisher)

    click.echo(f"🔌 hexawyn Slack HTTP listener — port {port}")
    click.echo("   Point your Slack app's Event Subscriptions URL to:")
    click.echo(None)
    click.echo("   Press Ctrl+C to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_27(port: int) -> None:
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
    click.echo(None)
    server.start(port=port)


def x__start_http_listener__mutmut_28(port: int) -> None:
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
    click.echo("XX   Press Ctrl+C to stop.\nXX")
    server.start(port=port)


def x__start_http_listener__mutmut_29(port: int) -> None:
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
    click.echo("   press ctrl+c to stop.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_30(port: int) -> None:
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
    click.echo("   PRESS CTRL+C TO STOP.\n")
    server.start(port=port)


def x__start_http_listener__mutmut_31(port: int) -> None:
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
    server.start(port=None)

mutants_x__start_http_listener__mutmut['_mutmut_orig'] = x__start_http_listener__mutmut_orig # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_1'] = x__start_http_listener__mutmut_1 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_2'] = x__start_http_listener__mutmut_2 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_3'] = x__start_http_listener__mutmut_3 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_4'] = x__start_http_listener__mutmut_4 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_5'] = x__start_http_listener__mutmut_5 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_6'] = x__start_http_listener__mutmut_6 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_7'] = x__start_http_listener__mutmut_7 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_8'] = x__start_http_listener__mutmut_8 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_9'] = x__start_http_listener__mutmut_9 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_10'] = x__start_http_listener__mutmut_10 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_11'] = x__start_http_listener__mutmut_11 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_12'] = x__start_http_listener__mutmut_12 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_13'] = x__start_http_listener__mutmut_13 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_14'] = x__start_http_listener__mutmut_14 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_15'] = x__start_http_listener__mutmut_15 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_16'] = x__start_http_listener__mutmut_16 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_17'] = x__start_http_listener__mutmut_17 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_18'] = x__start_http_listener__mutmut_18 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_19'] = x__start_http_listener__mutmut_19 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_20'] = x__start_http_listener__mutmut_20 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_21'] = x__start_http_listener__mutmut_21 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_22'] = x__start_http_listener__mutmut_22 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_23'] = x__start_http_listener__mutmut_23 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_24'] = x__start_http_listener__mutmut_24 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_25'] = x__start_http_listener__mutmut_25 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_26'] = x__start_http_listener__mutmut_26 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_27'] = x__start_http_listener__mutmut_27 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_28'] = x__start_http_listener__mutmut_28 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_29'] = x__start_http_listener__mutmut_29 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_30'] = x__start_http_listener__mutmut_30 # type: ignore # mutmut generated
mutants_x__start_http_listener__mutmut['x__start_http_listener__mutmut_31'] = x__start_http_listener__mutmut_31 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__start_socket_listener__mutmut)
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


async def x__start_socket_listener__mutmut_orig(cluster_name: str | None = None) -> None:
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


async def x__start_socket_listener__mutmut_1(cluster_name: str | None = None) -> None:
    app_token = None
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


async def x__start_socket_listener__mutmut_2(cluster_name: str | None = None) -> None:
    app_token = _require_env_token(None, "xapp-...")
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


async def x__start_socket_listener__mutmut_3(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", None)
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


async def x__start_socket_listener__mutmut_4(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("xapp-...")
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


async def x__start_socket_listener__mutmut_5(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", )
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


async def x__start_socket_listener__mutmut_6(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("XXSLACK_APP_TOKENXX", "xapp-...")
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


async def x__start_socket_listener__mutmut_7(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("slack_app_token", "xapp-...")
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


async def x__start_socket_listener__mutmut_8(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "XXxapp-...XX")
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


async def x__start_socket_listener__mutmut_9(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "XAPP-...")
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


async def x__start_socket_listener__mutmut_10(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if app_token:
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


async def x__start_socket_listener__mutmut_11(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = None
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


async def x__start_socket_listener__mutmut_12(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token(None, "xoxb-...")
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


async def x__start_socket_listener__mutmut_13(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", None)
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


async def x__start_socket_listener__mutmut_14(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("xoxb-...")
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


async def x__start_socket_listener__mutmut_15(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", )
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


async def x__start_socket_listener__mutmut_16(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("XXSLACK_BOT_TOKENXX", "xoxb-...")
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


async def x__start_socket_listener__mutmut_17(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("slack_bot_token", "xoxb-...")
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


async def x__start_socket_listener__mutmut_18(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "XXxoxb-...XX")
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


async def x__start_socket_listener__mutmut_19(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "XOXB-...")
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


async def x__start_socket_listener__mutmut_20(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if bot_token:
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


async def x__start_socket_listener__mutmut_21(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = None
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


async def x__start_socket_listener__mutmut_22(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=None)
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


async def x__start_socket_listener__mutmut_23(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = None
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


async def x__start_socket_listener__mutmut_24(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=None)
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


async def x__start_socket_listener__mutmut_25(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = None
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


async def x__start_socket_listener__mutmut_26(cluster_name: str | None = None) -> None:
    app_token = _require_env_token("SLACK_APP_TOKEN", "xapp-...")
    if not app_token:
        return
    bot_token = _require_env_token("SLACK_BOT_TOKEN", "xoxb-...")
    if not bot_token:
        return

    http_client = SlackHttpClient(bot_token=bot_token)
    publisher = SlackHttpPublisher(http_client=http_client)
    chat_adapter = SlackChatAdapter()
    socket_client = None

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


async def x__start_socket_listener__mutmut_27(cluster_name: str | None = None) -> None:
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
        chat_adapter=None,
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


async def x__start_socket_listener__mutmut_28(cluster_name: str | None = None) -> None:
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
        publisher=None,
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


async def x__start_socket_listener__mutmut_29(cluster_name: str | None = None) -> None:
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
        http_client=None,
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


async def x__start_socket_listener__mutmut_30(cluster_name: str | None = None) -> None:
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
        app_token=None,
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


async def x__start_socket_listener__mutmut_31(cluster_name: str | None = None) -> None:
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
        cluster_name=None,
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


async def x__start_socket_listener__mutmut_32(cluster_name: str | None = None) -> None:
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


async def x__start_socket_listener__mutmut_33(cluster_name: str | None = None) -> None:
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


async def x__start_socket_listener__mutmut_34(cluster_name: str | None = None) -> None:
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


async def x__start_socket_listener__mutmut_35(cluster_name: str | None = None) -> None:
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


async def x__start_socket_listener__mutmut_36(cluster_name: str | None = None) -> None:
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


async def x__start_socket_listener__mutmut_37(cluster_name: str | None = None) -> None:
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

    display_cluster = None
    click.echo("🔌 hexawyn Slack Socket Mode listener — no public URL needed")
    click.echo(f"   Cluster: {display_cluster}")
    click.echo("   Make sure Socket Mode is enabled in your Slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_38(cluster_name: str | None = None) -> None:
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

    display_cluster = cluster_name and "active kubectl context"
    click.echo("🔌 hexawyn Slack Socket Mode listener — no public URL needed")
    click.echo(f"   Cluster: {display_cluster}")
    click.echo("   Make sure Socket Mode is enabled in your Slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_39(cluster_name: str | None = None) -> None:
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

    display_cluster = cluster_name or "XXactive kubectl contextXX"
    click.echo("🔌 hexawyn Slack Socket Mode listener — no public URL needed")
    click.echo(f"   Cluster: {display_cluster}")
    click.echo("   Make sure Socket Mode is enabled in your Slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_40(cluster_name: str | None = None) -> None:
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

    display_cluster = cluster_name or "ACTIVE KUBECTL CONTEXT"
    click.echo("🔌 hexawyn Slack Socket Mode listener — no public URL needed")
    click.echo(f"   Cluster: {display_cluster}")
    click.echo("   Make sure Socket Mode is enabled in your Slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_41(cluster_name: str | None = None) -> None:
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
    click.echo(None)
    click.echo(f"   Cluster: {display_cluster}")
    click.echo("   Make sure Socket Mode is enabled in your Slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_42(cluster_name: str | None = None) -> None:
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
    click.echo("XX🔌 hexawyn Slack Socket Mode listener — no public URL neededXX")
    click.echo(f"   Cluster: {display_cluster}")
    click.echo("   Make sure Socket Mode is enabled in your Slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_43(cluster_name: str | None = None) -> None:
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
    click.echo("🔌 hexawyn slack socket mode listener — no public url needed")
    click.echo(f"   Cluster: {display_cluster}")
    click.echo("   Make sure Socket Mode is enabled in your Slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_44(cluster_name: str | None = None) -> None:
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
    click.echo("🔌 HEXAWYN SLACK SOCKET MODE LISTENER — NO PUBLIC URL NEEDED")
    click.echo(f"   Cluster: {display_cluster}")
    click.echo("   Make sure Socket Mode is enabled in your Slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_45(cluster_name: str | None = None) -> None:
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
    click.echo(None)
    click.echo("   Make sure Socket Mode is enabled in your Slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_46(cluster_name: str | None = None) -> None:
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
    click.echo(None)
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_47(cluster_name: str | None = None) -> None:
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
    click.echo("XX   Make sure Socket Mode is enabled in your Slack app settings.XX")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_48(cluster_name: str | None = None) -> None:
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
    click.echo("   make sure socket mode is enabled in your slack app settings.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_49(cluster_name: str | None = None) -> None:
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
    click.echo("   MAKE SURE SOCKET MODE IS ENABLED IN YOUR SLACK APP SETTINGS.")
    click.echo("   Press Ctrl+C to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_50(cluster_name: str | None = None) -> None:
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
    click.echo(None)

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_51(cluster_name: str | None = None) -> None:
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
    click.echo("XX   Press Ctrl+C to stop.\nXX")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_52(cluster_name: str | None = None) -> None:
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
    click.echo("   press ctrl+c to stop.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_53(cluster_name: str | None = None) -> None:
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
    click.echo("   PRESS CTRL+C TO STOP.\n")

    socket_client._running = True
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_54(cluster_name: str | None = None) -> None:
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

    socket_client._running = None
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_55(cluster_name: str | None = None) -> None:
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

    socket_client._running = False
    try:
        await socket_client.run()
    except KeyboardInterrupt:
        click.echo("\n👋 Slack listener stopped.")


async def x__start_socket_listener__mutmut_56(cluster_name: str | None = None) -> None:
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
        click.echo(None)


async def x__start_socket_listener__mutmut_57(cluster_name: str | None = None) -> None:
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
        click.echo("XX\n👋 Slack listener stopped.XX")


async def x__start_socket_listener__mutmut_58(cluster_name: str | None = None) -> None:
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
        click.echo("\n👋 slack listener stopped.")


async def x__start_socket_listener__mutmut_59(cluster_name: str | None = None) -> None:
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
        click.echo("\n👋 SLACK LISTENER STOPPED.")

mutants_x__start_socket_listener__mutmut['_mutmut_orig'] = x__start_socket_listener__mutmut_orig # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_1'] = x__start_socket_listener__mutmut_1 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_2'] = x__start_socket_listener__mutmut_2 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_3'] = x__start_socket_listener__mutmut_3 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_4'] = x__start_socket_listener__mutmut_4 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_5'] = x__start_socket_listener__mutmut_5 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_6'] = x__start_socket_listener__mutmut_6 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_7'] = x__start_socket_listener__mutmut_7 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_8'] = x__start_socket_listener__mutmut_8 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_9'] = x__start_socket_listener__mutmut_9 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_10'] = x__start_socket_listener__mutmut_10 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_11'] = x__start_socket_listener__mutmut_11 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_12'] = x__start_socket_listener__mutmut_12 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_13'] = x__start_socket_listener__mutmut_13 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_14'] = x__start_socket_listener__mutmut_14 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_15'] = x__start_socket_listener__mutmut_15 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_16'] = x__start_socket_listener__mutmut_16 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_17'] = x__start_socket_listener__mutmut_17 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_18'] = x__start_socket_listener__mutmut_18 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_19'] = x__start_socket_listener__mutmut_19 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_20'] = x__start_socket_listener__mutmut_20 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_21'] = x__start_socket_listener__mutmut_21 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_22'] = x__start_socket_listener__mutmut_22 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_23'] = x__start_socket_listener__mutmut_23 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_24'] = x__start_socket_listener__mutmut_24 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_25'] = x__start_socket_listener__mutmut_25 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_26'] = x__start_socket_listener__mutmut_26 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_27'] = x__start_socket_listener__mutmut_27 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_28'] = x__start_socket_listener__mutmut_28 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_29'] = x__start_socket_listener__mutmut_29 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_30'] = x__start_socket_listener__mutmut_30 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_31'] = x__start_socket_listener__mutmut_31 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_32'] = x__start_socket_listener__mutmut_32 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_33'] = x__start_socket_listener__mutmut_33 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_34'] = x__start_socket_listener__mutmut_34 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_35'] = x__start_socket_listener__mutmut_35 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_36'] = x__start_socket_listener__mutmut_36 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_37'] = x__start_socket_listener__mutmut_37 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_38'] = x__start_socket_listener__mutmut_38 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_39'] = x__start_socket_listener__mutmut_39 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_40'] = x__start_socket_listener__mutmut_40 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_41'] = x__start_socket_listener__mutmut_41 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_42'] = x__start_socket_listener__mutmut_42 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_43'] = x__start_socket_listener__mutmut_43 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_44'] = x__start_socket_listener__mutmut_44 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_45'] = x__start_socket_listener__mutmut_45 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_46'] = x__start_socket_listener__mutmut_46 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_47'] = x__start_socket_listener__mutmut_47 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_48'] = x__start_socket_listener__mutmut_48 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_49'] = x__start_socket_listener__mutmut_49 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_50'] = x__start_socket_listener__mutmut_50 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_51'] = x__start_socket_listener__mutmut_51 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_52'] = x__start_socket_listener__mutmut_52 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_53'] = x__start_socket_listener__mutmut_53 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_54'] = x__start_socket_listener__mutmut_54 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_55'] = x__start_socket_listener__mutmut_55 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_56'] = x__start_socket_listener__mutmut_56 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_57'] = x__start_socket_listener__mutmut_57 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_58'] = x__start_socket_listener__mutmut_58 # type: ignore # mutmut generated
mutants_x__start_socket_listener__mutmut['x__start_socket_listener__mutmut_59'] = x__start_socket_listener__mutmut_59 # type: ignore # mutmut generated


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
            f"Alerts   : {quota.count}/{quota.limit} this month · {quota.remaining} remaining"
        )
