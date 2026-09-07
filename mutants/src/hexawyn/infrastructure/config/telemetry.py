import json
import os
import threading
import urllib.request
from datetime import UTC, datetime

from hexawyn.infrastructure.config.license_manager import get_license_tier

TELEMETRY_URL = "https://api.hexawyn.com/v1/telemetry"
TELEMETRY_TIMEOUT = 5  # seconds


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_telemetry_enabled__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_telemetry_enabled__mutmut)
def is_telemetry_enabled() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("HEXAWYN_TELEMETRY", "").lower() == "true"


def x_is_telemetry_enabled__mutmut_orig() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("HEXAWYN_TELEMETRY", "").lower() == "true"


def x_is_telemetry_enabled__mutmut_1() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("HEXAWYN_TELEMETRY", "").upper() == "true"


def x_is_telemetry_enabled__mutmut_2() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get(None, "").lower() == "true"


def x_is_telemetry_enabled__mutmut_3() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("HEXAWYN_TELEMETRY", None).lower() == "true"


def x_is_telemetry_enabled__mutmut_4() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("").lower() == "true"


def x_is_telemetry_enabled__mutmut_5() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("HEXAWYN_TELEMETRY", ).lower() == "true"


def x_is_telemetry_enabled__mutmut_6() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("XXHEXAWYN_TELEMETRYXX", "").lower() == "true"


def x_is_telemetry_enabled__mutmut_7() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("hexawyn_telemetry", "").lower() == "true"


def x_is_telemetry_enabled__mutmut_8() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("HEXAWYN_TELEMETRY", "XXXX").lower() == "true"


def x_is_telemetry_enabled__mutmut_9() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("HEXAWYN_TELEMETRY", "").lower() != "true"


def x_is_telemetry_enabled__mutmut_10() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("HEXAWYN_TELEMETRY", "").lower() == "XXtrueXX"


def x_is_telemetry_enabled__mutmut_11() -> bool:
    """Telemetry is opt-in via HEXAWYN_TELEMETRY=true."""
    return os.environ.get("HEXAWYN_TELEMETRY", "").lower() == "TRUE"

mutants_x_is_telemetry_enabled__mutmut['_mutmut_orig'] = x_is_telemetry_enabled__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_1'] = x_is_telemetry_enabled__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_2'] = x_is_telemetry_enabled__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_3'] = x_is_telemetry_enabled__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_4'] = x_is_telemetry_enabled__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_5'] = x_is_telemetry_enabled__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_6'] = x_is_telemetry_enabled__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_7'] = x_is_telemetry_enabled__mutmut_7 # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_8'] = x_is_telemetry_enabled__mutmut_8 # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_9'] = x_is_telemetry_enabled__mutmut_9 # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_10'] = x_is_telemetry_enabled__mutmut_10 # type: ignore # mutmut generated
mutants_x_is_telemetry_enabled__mutmut['x_is_telemetry_enabled__mutmut_11'] = x_is_telemetry_enabled__mutmut_11 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__send_telemetry__mutmut)
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


def x__send_telemetry__mutmut_orig(payload: dict[str, str | int]) -> None:
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


def x__send_telemetry__mutmut_1(payload: dict[str, str | int]) -> None:
    data = None
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


def x__send_telemetry__mutmut_2(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode(None)
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


def x__send_telemetry__mutmut_3(payload: dict[str, str | int]) -> None:
    data = json.dumps(None).encode("utf-8")
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


def x__send_telemetry__mutmut_4(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("XXutf-8XX")
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


def x__send_telemetry__mutmut_5(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("UTF-8")
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


def x__send_telemetry__mutmut_6(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = None
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_7(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        None,
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


def x__send_telemetry__mutmut_8(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=None,
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


def x__send_telemetry__mutmut_9(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers=None,
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_10(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "hexawyn/0.1.0",
        },
        method=None,
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_11(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
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


def x__send_telemetry__mutmut_12(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
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


def x__send_telemetry__mutmut_13(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_14(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "hexawyn/0.1.0",
        },
        )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_15(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "XXContent-TypeXX": "application/json",
            "User-Agent": "hexawyn/0.1.0",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_16(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "content-type": "application/json",
            "User-Agent": "hexawyn/0.1.0",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_17(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "CONTENT-TYPE": "application/json",
            "User-Agent": "hexawyn/0.1.0",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_18(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "XXapplication/jsonXX",
            "User-Agent": "hexawyn/0.1.0",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_19(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "APPLICATION/JSON",
            "User-Agent": "hexawyn/0.1.0",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_20(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "XXUser-AgentXX": "hexawyn/0.1.0",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_21(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "user-agent": "hexawyn/0.1.0",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_22(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "USER-AGENT": "hexawyn/0.1.0",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_23(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "XXhexawyn/0.1.0XX",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_24(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "HEXAWYN/0.1.0",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_25(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "hexawyn/0.1.0",
        },
        method="XXPOSTXX",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_26(payload: dict[str, str | int]) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        TELEMETRY_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "hexawyn/0.1.0",
        },
        method="post",
    )
    try:
        urllib.request.urlopen(req, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_27(payload: dict[str, str | int]) -> None:
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
        urllib.request.urlopen(None, timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_28(payload: dict[str, str | int]) -> None:
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
        urllib.request.urlopen(req, timeout=None)
    except Exception:
        pass


def x__send_telemetry__mutmut_29(payload: dict[str, str | int]) -> None:
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
        urllib.request.urlopen(timeout=TELEMETRY_TIMEOUT)
    except Exception:
        pass


def x__send_telemetry__mutmut_30(payload: dict[str, str | int]) -> None:
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
        urllib.request.urlopen(req, )
    except Exception:
        pass

mutants_x__send_telemetry__mutmut['_mutmut_orig'] = x__send_telemetry__mutmut_orig # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_1'] = x__send_telemetry__mutmut_1 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_2'] = x__send_telemetry__mutmut_2 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_3'] = x__send_telemetry__mutmut_3 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_4'] = x__send_telemetry__mutmut_4 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_5'] = x__send_telemetry__mutmut_5 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_6'] = x__send_telemetry__mutmut_6 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_7'] = x__send_telemetry__mutmut_7 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_8'] = x__send_telemetry__mutmut_8 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_9'] = x__send_telemetry__mutmut_9 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_10'] = x__send_telemetry__mutmut_10 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_11'] = x__send_telemetry__mutmut_11 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_12'] = x__send_telemetry__mutmut_12 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_13'] = x__send_telemetry__mutmut_13 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_14'] = x__send_telemetry__mutmut_14 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_15'] = x__send_telemetry__mutmut_15 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_16'] = x__send_telemetry__mutmut_16 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_17'] = x__send_telemetry__mutmut_17 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_18'] = x__send_telemetry__mutmut_18 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_19'] = x__send_telemetry__mutmut_19 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_20'] = x__send_telemetry__mutmut_20 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_21'] = x__send_telemetry__mutmut_21 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_22'] = x__send_telemetry__mutmut_22 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_23'] = x__send_telemetry__mutmut_23 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_24'] = x__send_telemetry__mutmut_24 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_25'] = x__send_telemetry__mutmut_25 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_26'] = x__send_telemetry__mutmut_26 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_27'] = x__send_telemetry__mutmut_27 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_28'] = x__send_telemetry__mutmut_28 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_29'] = x__send_telemetry__mutmut_29 # type: ignore # mutmut generated
mutants_x__send_telemetry__mutmut['x__send_telemetry__mutmut_30'] = x__send_telemetry__mutmut_30 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_send_startup_telemetry__mutmut)
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


def x_send_startup_telemetry__mutmut_orig() -> None:
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


def x_send_startup_telemetry__mutmut_1() -> None:
    """Non-blocking telemetry ping on application start."""
    if is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_2() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = None

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_3() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "XXeventXX": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_4() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "EVENT": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_5() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "XXstartupXX",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_6() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "STARTUP",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_7() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "XXtierXX": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_8() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "TIER": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_9() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "XXtimestampXX": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_10() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "TIMESTAMP": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_11() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(None).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_12() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "XXversionXX": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_13() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "VERSION": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_14() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "XX0.1.0XX",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_15() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = None
    thread.start()


def x_send_startup_telemetry__mutmut_16() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=None, args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_17() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=None, daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_18() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=None)
    thread.start()


def x_send_startup_telemetry__mutmut_19() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(args=(payload,), daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_20() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, daemon=True)
    thread.start()


def x_send_startup_telemetry__mutmut_21() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), )
    thread.start()


def x_send_startup_telemetry__mutmut_22() -> None:
    """Non-blocking telemetry ping on application start."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "startup",
        "tier": get_license_tier().value,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=False)
    thread.start()

mutants_x_send_startup_telemetry__mutmut['_mutmut_orig'] = x_send_startup_telemetry__mutmut_orig # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_1'] = x_send_startup_telemetry__mutmut_1 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_2'] = x_send_startup_telemetry__mutmut_2 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_3'] = x_send_startup_telemetry__mutmut_3 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_4'] = x_send_startup_telemetry__mutmut_4 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_5'] = x_send_startup_telemetry__mutmut_5 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_6'] = x_send_startup_telemetry__mutmut_6 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_7'] = x_send_startup_telemetry__mutmut_7 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_8'] = x_send_startup_telemetry__mutmut_8 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_9'] = x_send_startup_telemetry__mutmut_9 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_10'] = x_send_startup_telemetry__mutmut_10 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_11'] = x_send_startup_telemetry__mutmut_11 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_12'] = x_send_startup_telemetry__mutmut_12 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_13'] = x_send_startup_telemetry__mutmut_13 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_14'] = x_send_startup_telemetry__mutmut_14 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_15'] = x_send_startup_telemetry__mutmut_15 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_16'] = x_send_startup_telemetry__mutmut_16 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_17'] = x_send_startup_telemetry__mutmut_17 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_18'] = x_send_startup_telemetry__mutmut_18 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_19'] = x_send_startup_telemetry__mutmut_19 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_20'] = x_send_startup_telemetry__mutmut_20 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_21'] = x_send_startup_telemetry__mutmut_21 # type: ignore # mutmut generated
mutants_x_send_startup_telemetry__mutmut['x_send_startup_telemetry__mutmut_22'] = x_send_startup_telemetry__mutmut_22 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_send_investigation_telemetry__mutmut)
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


def x_send_investigation_telemetry__mutmut_orig(investigation_count: int) -> None:
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


def x_send_investigation_telemetry__mutmut_1(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if is_telemetry_enabled():
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


def x_send_investigation_telemetry__mutmut_2(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = None

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_3(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "XXeventXX": "investigation",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_4(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "EVENT": "investigation",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_5(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "XXinvestigationXX",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_6(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "INVESTIGATION",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_7(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "XXtierXX": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_8(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "TIER": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_9(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "tier": get_license_tier().value,
        "XXmonthly_countXX": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_10(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "tier": get_license_tier().value,
        "MONTHLY_COUNT": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_11(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "XXtimestampXX": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_12(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "TIMESTAMP": datetime.now(UTC).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_13(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(None).isoformat(),
        "version": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_14(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "XXversionXX": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_15(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "VERSION": "0.1.0",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_16(investigation_count: int) -> None:
    """Non-blocking telemetry ping after each investigation."""
    if not is_telemetry_enabled():
        return

    payload: dict[str, str | int] = {
        "event": "investigation",
        "tier": get_license_tier().value,
        "monthly_count": investigation_count,
        "timestamp": datetime.now(UTC).isoformat(),
        "version": "XX0.1.0XX",
    }

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_17(investigation_count: int) -> None:
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

    thread = None
    thread.start()


def x_send_investigation_telemetry__mutmut_18(investigation_count: int) -> None:
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

    thread = threading.Thread(target=None, args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_19(investigation_count: int) -> None:
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

    thread = threading.Thread(target=_send_telemetry, args=None, daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_20(investigation_count: int) -> None:
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

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=None)
    thread.start()


def x_send_investigation_telemetry__mutmut_21(investigation_count: int) -> None:
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

    thread = threading.Thread(args=(payload,), daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_22(investigation_count: int) -> None:
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

    thread = threading.Thread(target=_send_telemetry, daemon=True)
    thread.start()


def x_send_investigation_telemetry__mutmut_23(investigation_count: int) -> None:
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

    thread = threading.Thread(target=_send_telemetry, args=(payload,), )
    thread.start()


def x_send_investigation_telemetry__mutmut_24(investigation_count: int) -> None:
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

    thread = threading.Thread(target=_send_telemetry, args=(payload,), daemon=False)
    thread.start()

mutants_x_send_investigation_telemetry__mutmut['_mutmut_orig'] = x_send_investigation_telemetry__mutmut_orig # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_1'] = x_send_investigation_telemetry__mutmut_1 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_2'] = x_send_investigation_telemetry__mutmut_2 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_3'] = x_send_investigation_telemetry__mutmut_3 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_4'] = x_send_investigation_telemetry__mutmut_4 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_5'] = x_send_investigation_telemetry__mutmut_5 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_6'] = x_send_investigation_telemetry__mutmut_6 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_7'] = x_send_investigation_telemetry__mutmut_7 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_8'] = x_send_investigation_telemetry__mutmut_8 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_9'] = x_send_investigation_telemetry__mutmut_9 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_10'] = x_send_investigation_telemetry__mutmut_10 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_11'] = x_send_investigation_telemetry__mutmut_11 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_12'] = x_send_investigation_telemetry__mutmut_12 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_13'] = x_send_investigation_telemetry__mutmut_13 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_14'] = x_send_investigation_telemetry__mutmut_14 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_15'] = x_send_investigation_telemetry__mutmut_15 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_16'] = x_send_investigation_telemetry__mutmut_16 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_17'] = x_send_investigation_telemetry__mutmut_17 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_18'] = x_send_investigation_telemetry__mutmut_18 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_19'] = x_send_investigation_telemetry__mutmut_19 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_20'] = x_send_investigation_telemetry__mutmut_20 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_21'] = x_send_investigation_telemetry__mutmut_21 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_22'] = x_send_investigation_telemetry__mutmut_22 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_23'] = x_send_investigation_telemetry__mutmut_23 # type: ignore # mutmut generated
mutants_x_send_investigation_telemetry__mutmut['x_send_investigation_telemetry__mutmut_24'] = x_send_investigation_telemetry__mutmut_24 # type: ignore # mutmut generated
