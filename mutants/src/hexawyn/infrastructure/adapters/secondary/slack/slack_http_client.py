import os

import httpx

_SLACK_API_BASE = "https://slack.com/api"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSlackHttpClientǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlackHttpClientǁpost__mutmut: MutantDict = {}  # type: ignore


class SlackHttpClient:
    """Low-level HTTP client for the Slack Web API. Injectable into secondary adapters."""

    @_mutmut_mutated(mutants_xǁSlackHttpClientǁ__init____mutmut)
    def __init__(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is not None else os.environ.get("SLACK_BOT_TOKEN", "")

    def xǁSlackHttpClientǁ__init____mutmut_orig(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is not None else os.environ.get("SLACK_BOT_TOKEN", "")

    def xǁSlackHttpClientǁ__init____mutmut_1(self, bot_token: str | None = None) -> None:
        self._token = None

    def xǁSlackHttpClientǁ__init____mutmut_2(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is None else os.environ.get("SLACK_BOT_TOKEN", "")

    def xǁSlackHttpClientǁ__init____mutmut_3(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is not None else os.environ.get(None, "")

    def xǁSlackHttpClientǁ__init____mutmut_4(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is not None else os.environ.get("SLACK_BOT_TOKEN", None)

    def xǁSlackHttpClientǁ__init____mutmut_5(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is not None else os.environ.get("")

    def xǁSlackHttpClientǁ__init____mutmut_6(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is not None else os.environ.get("SLACK_BOT_TOKEN", )

    def xǁSlackHttpClientǁ__init____mutmut_7(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is not None else os.environ.get("XXSLACK_BOT_TOKENXX", "")

    def xǁSlackHttpClientǁ__init____mutmut_8(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is not None else os.environ.get("slack_bot_token", "")

    def xǁSlackHttpClientǁ__init____mutmut_9(self, bot_token: str | None = None) -> None:
        self._token = bot_token if bot_token is not None else os.environ.get("SLACK_BOT_TOKEN", "XXXX")

    @_mutmut_mutated(mutants_xǁSlackHttpClientǁpost__mutmut)
    def post(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_orig(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_1(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = None
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_2(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            None,
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_3(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers=None,
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_4(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=None,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_5(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=None,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_6(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_7(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_8(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_9(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_10(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "XXAuthorizationXX": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_11(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_12(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "AUTHORIZATION": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_13(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "XXContent-TypeXX": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_14(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "content-type": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_15(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "CONTENT-TYPE": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_16(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "XXapplication/jsonXX",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_17(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "APPLICATION/JSON",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_18(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=11.0,
        )
        result: dict[str, object] = response.json()
        return result

    def xǁSlackHttpClientǁpost__mutmut_19(self, method: str, payload: dict[str, object]) -> dict[str, object]:
        """
        POST to a Slack API method (e.g. 'chat.postMessage').
        Returns the parsed JSON response.
        Raises on network errors — callers decide how to handle.
        """
        response = httpx.post(
            f"{_SLACK_API_BASE}/{method}",
            headers={
                "Authorization": f"Bearer {self._token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10.0,
        )
        result: dict[str, object] = None
        return result

mutants_xǁSlackHttpClientǁ__init____mutmut['_mutmut_orig'] = SlackHttpClient.xǁSlackHttpClientǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁ__init____mutmut['xǁSlackHttpClientǁ__init____mutmut_1'] = SlackHttpClient.xǁSlackHttpClientǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁ__init____mutmut['xǁSlackHttpClientǁ__init____mutmut_2'] = SlackHttpClient.xǁSlackHttpClientǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁ__init____mutmut['xǁSlackHttpClientǁ__init____mutmut_3'] = SlackHttpClient.xǁSlackHttpClientǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁ__init____mutmut['xǁSlackHttpClientǁ__init____mutmut_4'] = SlackHttpClient.xǁSlackHttpClientǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁ__init____mutmut['xǁSlackHttpClientǁ__init____mutmut_5'] = SlackHttpClient.xǁSlackHttpClientǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁ__init____mutmut['xǁSlackHttpClientǁ__init____mutmut_6'] = SlackHttpClient.xǁSlackHttpClientǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁ__init____mutmut['xǁSlackHttpClientǁ__init____mutmut_7'] = SlackHttpClient.xǁSlackHttpClientǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁ__init____mutmut['xǁSlackHttpClientǁ__init____mutmut_8'] = SlackHttpClient.xǁSlackHttpClientǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁ__init____mutmut['xǁSlackHttpClientǁ__init____mutmut_9'] = SlackHttpClient.xǁSlackHttpClientǁ__init____mutmut_9 # type: ignore # mutmut generated

mutants_xǁSlackHttpClientǁpost__mutmut['_mutmut_orig'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_1'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_2'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_3'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_4'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_5'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_6'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_7'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_8'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_9'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_10'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_11'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_12'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_13'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_14'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_15'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_16'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_17'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_18'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSlackHttpClientǁpost__mutmut['xǁSlackHttpClientǁpost__mutmut_19'] = SlackHttpClient.xǁSlackHttpClientǁpost__mutmut_19 # type: ignore # mutmut generated
