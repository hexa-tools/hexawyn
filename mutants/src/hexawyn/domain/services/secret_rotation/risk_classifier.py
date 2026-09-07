from __future__ import annotations

from hexawyn.domain.models.constants import SecretRotationConstants
from hexawyn.domain.models.secret_rotation import RiskLevel

_cfg = SecretRotationConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_risk_level__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_risk_level__mutmut)
def classify_risk_level(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_orig(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_1(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type not in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_2(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "XXcriticalXX"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_3(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "CRITICAL"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_4(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = None
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_5(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.lower() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_6(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(None):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_7(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment not in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_8(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "XXcriticalXX"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_9(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "CRITICAL"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_10(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(None):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_11(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment not in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"


def x_classify_risk_level__mutmut_12(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "XXmediumXX"
    return "low"


def x_classify_risk_level__mutmut_13(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "MEDIUM"
    return "low"


def x_classify_risk_level__mutmut_14(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "XXlowXX"


def x_classify_risk_level__mutmut_15(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "LOW"

mutants_x_classify_risk_level__mutmut['_mutmut_orig'] = x_classify_risk_level__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_1'] = x_classify_risk_level__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_2'] = x_classify_risk_level__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_3'] = x_classify_risk_level__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_4'] = x_classify_risk_level__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_5'] = x_classify_risk_level__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_6'] = x_classify_risk_level__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_7'] = x_classify_risk_level__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_8'] = x_classify_risk_level__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_9'] = x_classify_risk_level__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_10'] = x_classify_risk_level__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_11'] = x_classify_risk_level__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_12'] = x_classify_risk_level__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_13'] = x_classify_risk_level__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_14'] = x_classify_risk_level__mutmut_14 # type: ignore # mutmut generated
mutants_x_classify_risk_level__mutmut['x_classify_risk_level__mutmut_15'] = x_classify_risk_level__mutmut_15 # type: ignore # mutmut generated
