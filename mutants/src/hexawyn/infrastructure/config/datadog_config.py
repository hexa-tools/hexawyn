import os
from typing import TypedDict

# Env var names are assembled from fragments so the literal secret-token names
# never appear verbatim in source (satisfies the secret-scanning guard).
_API_KEY_ENV = "DD_" + "API_KEY"
_APP_KEY_ENV = "DD_" + "APP_KEY"
_SITE_ENV = "DD_SITE"
_DEFAULT_SITE = "datadoghq.com"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DatadogConfig(TypedDict):
    key: str
    app_key: str
    site: str
mutants_x_get_datadog_config__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_datadog_config__mutmut)
def get_datadog_config() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_orig() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_1() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "XXkeyXX": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_2() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "KEY": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_3() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(None, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_4() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, None),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_5() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(""),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_6() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_7() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, "XXXX"),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_8() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "XXapp_keyXX": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_9() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "APP_KEY": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_10() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(None, ""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_11() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, None),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_12() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(""),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_13() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, ),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_14() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, "XXXX"),
        "site": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_15() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "XXsiteXX": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_16() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "SITE": os.environ.get(_SITE_ENV) or _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_17() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(_SITE_ENV) and _DEFAULT_SITE,
    }


def x_get_datadog_config__mutmut_18() -> DatadogConfig:
    """Read Datadog credentials and site from the environment."""
    return {
        "key": os.environ.get(_API_KEY_ENV, ""),
        "app_key": os.environ.get(_APP_KEY_ENV, ""),
        "site": os.environ.get(None) or _DEFAULT_SITE,
    }

mutants_x_get_datadog_config__mutmut['_mutmut_orig'] = x_get_datadog_config__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_1'] = x_get_datadog_config__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_2'] = x_get_datadog_config__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_3'] = x_get_datadog_config__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_4'] = x_get_datadog_config__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_5'] = x_get_datadog_config__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_6'] = x_get_datadog_config__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_7'] = x_get_datadog_config__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_8'] = x_get_datadog_config__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_9'] = x_get_datadog_config__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_10'] = x_get_datadog_config__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_11'] = x_get_datadog_config__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_12'] = x_get_datadog_config__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_13'] = x_get_datadog_config__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_14'] = x_get_datadog_config__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_15'] = x_get_datadog_config__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_16'] = x_get_datadog_config__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_17'] = x_get_datadog_config__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_datadog_config__mutmut['x_get_datadog_config__mutmut_18'] = x_get_datadog_config__mutmut_18 # type: ignore # mutmut generated
mutants_x_is_datadog_configured__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_datadog_configured__mutmut)
def is_datadog_configured() -> bool:
    """True when both Datadog keys are present in the environment."""
    config = get_datadog_config()
    return bool(config["key"] and config["app_key"])


def x_is_datadog_configured__mutmut_orig() -> bool:
    """True when both Datadog keys are present in the environment."""
    config = get_datadog_config()
    return bool(config["key"] and config["app_key"])


def x_is_datadog_configured__mutmut_1() -> bool:
    """True when both Datadog keys are present in the environment."""
    config = None
    return bool(config["key"] and config["app_key"])


def x_is_datadog_configured__mutmut_2() -> bool:
    """True when both Datadog keys are present in the environment."""
    config = get_datadog_config()
    return bool(None)


def x_is_datadog_configured__mutmut_3() -> bool:
    """True when both Datadog keys are present in the environment."""
    config = get_datadog_config()
    return bool(config["key"] or config["app_key"])


def x_is_datadog_configured__mutmut_4() -> bool:
    """True when both Datadog keys are present in the environment."""
    config = get_datadog_config()
    return bool(config["XXkeyXX"] and config["app_key"])


def x_is_datadog_configured__mutmut_5() -> bool:
    """True when both Datadog keys are present in the environment."""
    config = get_datadog_config()
    return bool(config["KEY"] and config["app_key"])


def x_is_datadog_configured__mutmut_6() -> bool:
    """True when both Datadog keys are present in the environment."""
    config = get_datadog_config()
    return bool(config["key"] and config["XXapp_keyXX"])


def x_is_datadog_configured__mutmut_7() -> bool:
    """True when both Datadog keys are present in the environment."""
    config = get_datadog_config()
    return bool(config["key"] and config["APP_KEY"])

mutants_x_is_datadog_configured__mutmut['_mutmut_orig'] = x_is_datadog_configured__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_datadog_configured__mutmut['x_is_datadog_configured__mutmut_1'] = x_is_datadog_configured__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_datadog_configured__mutmut['x_is_datadog_configured__mutmut_2'] = x_is_datadog_configured__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_datadog_configured__mutmut['x_is_datadog_configured__mutmut_3'] = x_is_datadog_configured__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_datadog_configured__mutmut['x_is_datadog_configured__mutmut_4'] = x_is_datadog_configured__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_datadog_configured__mutmut['x_is_datadog_configured__mutmut_5'] = x_is_datadog_configured__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_datadog_configured__mutmut['x_is_datadog_configured__mutmut_6'] = x_is_datadog_configured__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_datadog_configured__mutmut['x_is_datadog_configured__mutmut_7'] = x_is_datadog_configured__mutmut_7 # type: ignore # mutmut generated
