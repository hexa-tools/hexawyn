import asyncio
import functools
import logging
from collections.abc import Awaitable, Callable
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import ParamSpec, TypeVar, overload

P = ParamSpec("P")
R = TypeVar("R")

HEXAWYN_LOGGER_NAME: str = "hexawyn"
DEFAULT_LOG_DIR: str = "logs"
MAX_LOG_BYTES: int = 10_000_000
LOG_BACKUP_COUNT: int = 5


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__anonymize_log__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__anonymize_log__mutmut)
def _anonymize_log(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = RegexAnonymizerAdapter()
        policy = RedactionPolicy()
        record.msg = adapter.mask(str(record.msg), policy)[0]
    except Exception:
        pass


def x__anonymize_log__mutmut_orig(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = RegexAnonymizerAdapter()
        policy = RedactionPolicy()
        record.msg = adapter.mask(str(record.msg), policy)[0]
    except Exception:
        pass


def x__anonymize_log__mutmut_1(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = None
        policy = RedactionPolicy()
        record.msg = adapter.mask(str(record.msg), policy)[0]
    except Exception:
        pass


def x__anonymize_log__mutmut_2(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = RegexAnonymizerAdapter()
        policy = None
        record.msg = adapter.mask(str(record.msg), policy)[0]
    except Exception:
        pass


def x__anonymize_log__mutmut_3(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = RegexAnonymizerAdapter()
        policy = RedactionPolicy()
        record.msg = None
    except Exception:
        pass


def x__anonymize_log__mutmut_4(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = RegexAnonymizerAdapter()
        policy = RedactionPolicy()
        record.msg = adapter.mask(None, policy)[0]
    except Exception:
        pass


def x__anonymize_log__mutmut_5(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = RegexAnonymizerAdapter()
        policy = RedactionPolicy()
        record.msg = adapter.mask(str(record.msg), None)[0]
    except Exception:
        pass


def x__anonymize_log__mutmut_6(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = RegexAnonymizerAdapter()
        policy = RedactionPolicy()
        record.msg = adapter.mask(policy)[0]
    except Exception:
        pass


def x__anonymize_log__mutmut_7(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = RegexAnonymizerAdapter()
        policy = RedactionPolicy()
        record.msg = adapter.mask(str(record.msg), )[0]
    except Exception:
        pass


def x__anonymize_log__mutmut_8(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = RegexAnonymizerAdapter()
        policy = RedactionPolicy()
        record.msg = adapter.mask(str(None), policy)[0]
    except Exception:
        pass


def x__anonymize_log__mutmut_9(record: logging.LogRecord) -> None:
    try:
        from hexawyn.domain.models.anonymization import RedactionPolicy  # hexa-lazy-import
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import (
            RegexAnonymizerAdapter,  # hexa-lazy-import
        )

        adapter = RegexAnonymizerAdapter()
        policy = RedactionPolicy()
        record.msg = adapter.mask(str(record.msg), policy)[1]
    except Exception:
        pass

mutants_x__anonymize_log__mutmut['_mutmut_orig'] = x__anonymize_log__mutmut_orig # type: ignore # mutmut generated
mutants_x__anonymize_log__mutmut['x__anonymize_log__mutmut_1'] = x__anonymize_log__mutmut_1 # type: ignore # mutmut generated
mutants_x__anonymize_log__mutmut['x__anonymize_log__mutmut_2'] = x__anonymize_log__mutmut_2 # type: ignore # mutmut generated
mutants_x__anonymize_log__mutmut['x__anonymize_log__mutmut_3'] = x__anonymize_log__mutmut_3 # type: ignore # mutmut generated
mutants_x__anonymize_log__mutmut['x__anonymize_log__mutmut_4'] = x__anonymize_log__mutmut_4 # type: ignore # mutmut generated
mutants_x__anonymize_log__mutmut['x__anonymize_log__mutmut_5'] = x__anonymize_log__mutmut_5 # type: ignore # mutmut generated
mutants_x__anonymize_log__mutmut['x__anonymize_log__mutmut_6'] = x__anonymize_log__mutmut_6 # type: ignore # mutmut generated
mutants_x__anonymize_log__mutmut['x__anonymize_log__mutmut_7'] = x__anonymize_log__mutmut_7 # type: ignore # mutmut generated
mutants_x__anonymize_log__mutmut['x__anonymize_log__mutmut_8'] = x__anonymize_log__mutmut_8 # type: ignore # mutmut generated
mutants_x__anonymize_log__mutmut['x__anonymize_log__mutmut_9'] = x__anonymize_log__mutmut_9 # type: ignore # mutmut generated
mutants_xǁ_AnonymizerFilterǁfilter__mutmut: MutantDict = {}  # type: ignore


class _AnonymizerFilter(logging.Filter):
    @_mutmut_mutated(mutants_xǁ_AnonymizerFilterǁfilter__mutmut)
    def filter(self, record: logging.LogRecord) -> bool:
        _anonymize_log(record)
        return True
    def xǁ_AnonymizerFilterǁfilter__mutmut_orig(self, record: logging.LogRecord) -> bool:
        _anonymize_log(record)
        return True
    def xǁ_AnonymizerFilterǁfilter__mutmut_1(self, record: logging.LogRecord) -> bool:
        _anonymize_log(None)
        return True
    def xǁ_AnonymizerFilterǁfilter__mutmut_2(self, record: logging.LogRecord) -> bool:
        _anonymize_log(record)
        return False

mutants_xǁ_AnonymizerFilterǁfilter__mutmut['_mutmut_orig'] = _AnonymizerFilter.xǁ_AnonymizerFilterǁfilter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁ_AnonymizerFilterǁfilter__mutmut['xǁ_AnonymizerFilterǁfilter__mutmut_1'] = _AnonymizerFilter.xǁ_AnonymizerFilterǁfilter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁ_AnonymizerFilterǁfilter__mutmut['xǁ_AnonymizerFilterǁfilter__mutmut_2'] = _AnonymizerFilter.xǁ_AnonymizerFilterǁfilter__mutmut_2 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_setup_logging__mutmut)
def setup_logging(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_orig(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_1(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = None
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_2(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(None)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_3(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(None)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_4(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=None)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_5(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(None).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_6(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=False)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_7(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = None

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_8(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt=None,
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_9(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt=None,
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_10(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_11(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_12(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="XX%(asctime)s | %(levelname)s | %(name)s | %(message)sXX",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_13(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(ASCTIME)S | %(LEVELNAME)S | %(NAME)S | %(MESSAGE)S",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_14(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="XX%Y-%m-%dT%H:%M:%SXX",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_15(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%y-%m-%dt%h:%m:%s",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_16(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%M-%DT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_17(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = None
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_18(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(None)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_19(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(None)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_20(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(None)
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_21(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(None)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_22(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = None
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_23(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        None,
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_24(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=None,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_25(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=None,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_26(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding=None,
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_27(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_28(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_29(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_30(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_31(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) * "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_32(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(None) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_33(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "XXhexawyn.logXX",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_34(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "HEXAWYN.LOG",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_35(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="XXutf-8XX",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_36(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="UTF-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_37(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(None)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_38(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(None)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_39(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(None)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_40(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(None)

    logger.propagate = False

    return logger


def x_setup_logging__mutmut_41(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = None

    return logger


def x_setup_logging__mutmut_42(
    level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
) -> logging.Logger:
    logger = logging.getLogger(HEXAWYN_LOGGER_NAME)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    Path(log_dir).mkdir(exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(stream_handler)

    file_handler = RotatingFileHandler(
        Path(log_dir) / "hexawyn.log",
        maxBytes=MAX_LOG_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_AnonymizerFilter())
    logger.addHandler(file_handler)

    logger.propagate = True

    return logger

mutants_x_setup_logging__mutmut['_mutmut_orig'] = x_setup_logging__mutmut_orig # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_1'] = x_setup_logging__mutmut_1 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_2'] = x_setup_logging__mutmut_2 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_3'] = x_setup_logging__mutmut_3 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_4'] = x_setup_logging__mutmut_4 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_5'] = x_setup_logging__mutmut_5 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_6'] = x_setup_logging__mutmut_6 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_7'] = x_setup_logging__mutmut_7 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_8'] = x_setup_logging__mutmut_8 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_9'] = x_setup_logging__mutmut_9 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_10'] = x_setup_logging__mutmut_10 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_11'] = x_setup_logging__mutmut_11 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_12'] = x_setup_logging__mutmut_12 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_13'] = x_setup_logging__mutmut_13 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_14'] = x_setup_logging__mutmut_14 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_15'] = x_setup_logging__mutmut_15 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_16'] = x_setup_logging__mutmut_16 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_17'] = x_setup_logging__mutmut_17 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_18'] = x_setup_logging__mutmut_18 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_19'] = x_setup_logging__mutmut_19 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_20'] = x_setup_logging__mutmut_20 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_21'] = x_setup_logging__mutmut_21 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_22'] = x_setup_logging__mutmut_22 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_23'] = x_setup_logging__mutmut_23 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_24'] = x_setup_logging__mutmut_24 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_25'] = x_setup_logging__mutmut_25 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_26'] = x_setup_logging__mutmut_26 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_27'] = x_setup_logging__mutmut_27 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_28'] = x_setup_logging__mutmut_28 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_29'] = x_setup_logging__mutmut_29 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_30'] = x_setup_logging__mutmut_30 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_31'] = x_setup_logging__mutmut_31 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_32'] = x_setup_logging__mutmut_32 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_33'] = x_setup_logging__mutmut_33 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_34'] = x_setup_logging__mutmut_34 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_35'] = x_setup_logging__mutmut_35 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_36'] = x_setup_logging__mutmut_36 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_37'] = x_setup_logging__mutmut_37 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_38'] = x_setup_logging__mutmut_38 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_39'] = x_setup_logging__mutmut_39 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_40'] = x_setup_logging__mutmut_40 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_41'] = x_setup_logging__mutmut_41 # type: ignore # mutmut generated
mutants_x_setup_logging__mutmut['x_setup_logging__mutmut_42'] = x_setup_logging__mutmut_42 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_logger__mutmut)
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    root = setup_logging()
    logger.handlers = root.handlers[:]
    logger.setLevel(root.level)
    logger.propagate = False

    return logger


def x_get_logger__mutmut_orig(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    root = setup_logging()
    logger.handlers = root.handlers[:]
    logger.setLevel(root.level)
    logger.propagate = False

    return logger


def x_get_logger__mutmut_1(name: str) -> logging.Logger:
    logger = None

    if logger.handlers:
        return logger

    root = setup_logging()
    logger.handlers = root.handlers[:]
    logger.setLevel(root.level)
    logger.propagate = False

    return logger


def x_get_logger__mutmut_2(name: str) -> logging.Logger:
    logger = logging.getLogger(None)

    if logger.handlers:
        return logger

    root = setup_logging()
    logger.handlers = root.handlers[:]
    logger.setLevel(root.level)
    logger.propagate = False

    return logger


def x_get_logger__mutmut_3(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    root = None
    logger.handlers = root.handlers[:]
    logger.setLevel(root.level)
    logger.propagate = False

    return logger


def x_get_logger__mutmut_4(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    root = setup_logging()
    logger.handlers = None
    logger.setLevel(root.level)
    logger.propagate = False

    return logger


def x_get_logger__mutmut_5(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    root = setup_logging()
    logger.handlers = root.handlers[:]
    logger.setLevel(None)
    logger.propagate = False

    return logger


def x_get_logger__mutmut_6(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    root = setup_logging()
    logger.handlers = root.handlers[:]
    logger.setLevel(root.level)
    logger.propagate = None

    return logger


def x_get_logger__mutmut_7(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    root = setup_logging()
    logger.handlers = root.handlers[:]
    logger.setLevel(root.level)
    logger.propagate = True

    return logger

mutants_x_get_logger__mutmut['_mutmut_orig'] = x_get_logger__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_1'] = x_get_logger__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_2'] = x_get_logger__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_3'] = x_get_logger__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_4'] = x_get_logger__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_5'] = x_get_logger__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_6'] = x_get_logger__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_logger__mutmut['x_get_logger__mutmut_7'] = x_get_logger__mutmut_7 # type: ignore # mutmut generated
mutants_x__get_logger__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_logger__mutmut)
def _get_logger() -> logging.Logger:
    return logging.getLogger(HEXAWYN_LOGGER_NAME)


def x__get_logger__mutmut_orig() -> logging.Logger:
    return logging.getLogger(HEXAWYN_LOGGER_NAME)


def x__get_logger__mutmut_1() -> logging.Logger:
    return logging.getLogger(None)

mutants_x__get_logger__mutmut['_mutmut_orig'] = x__get_logger__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_logger__mutmut['x__get_logger__mutmut_1'] = x__get_logger__mutmut_1 # type: ignore # mutmut generated


@overload
def log_tool_execution(func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]: ...


@overload
def log_tool_execution(func: Callable[P, R]) -> Callable[P, R]: ...
mutants_x_log_tool_execution__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_log_tool_execution__mutmut)
def log_tool_execution(
    func: Callable[P, object],
) -> Callable[P, object]:
    tool_name: str = func.__name__
    logger = _get_logger()

    if asyncio.iscoroutinefunction(func):

        @functools.wraps(func)
        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
            logger.info("Executing tool: %s", tool_name)
            try:
                result = await func(*args, **kwargs)
                logger.info("Tool completed: %s", tool_name)
                return result
            except Exception:
                logger.exception("Tool failed: %s", tool_name)
                raise

        return async_wrapper

    @functools.wraps(func)
    def sync_wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
        logger.info("Executing tool: %s", tool_name)
        try:
            result = func(*args, **kwargs)
            logger.info("Tool completed: %s", tool_name)
            return result
        except Exception:
            logger.exception("Tool failed: %s", tool_name)
            raise

    return sync_wrapper


def x_log_tool_execution__mutmut_orig(
    func: Callable[P, object],
) -> Callable[P, object]:
    tool_name: str = func.__name__
    logger = _get_logger()

    if asyncio.iscoroutinefunction(func):

        @functools.wraps(func)
        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
            logger.info("Executing tool: %s", tool_name)
            try:
                result = await func(*args, **kwargs)
                logger.info("Tool completed: %s", tool_name)
                return result
            except Exception:
                logger.exception("Tool failed: %s", tool_name)
                raise

        return async_wrapper

    @functools.wraps(func)
    def sync_wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
        logger.info("Executing tool: %s", tool_name)
        try:
            result = func(*args, **kwargs)
            logger.info("Tool completed: %s", tool_name)
            return result
        except Exception:
            logger.exception("Tool failed: %s", tool_name)
            raise

    return sync_wrapper


def x_log_tool_execution__mutmut_1(
    func: Callable[P, object],
) -> Callable[P, object]:
    tool_name: str = None
    logger = _get_logger()

    if asyncio.iscoroutinefunction(func):

        @functools.wraps(func)
        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
            logger.info("Executing tool: %s", tool_name)
            try:
                result = await func(*args, **kwargs)
                logger.info("Tool completed: %s", tool_name)
                return result
            except Exception:
                logger.exception("Tool failed: %s", tool_name)
                raise

        return async_wrapper

    @functools.wraps(func)
    def sync_wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
        logger.info("Executing tool: %s", tool_name)
        try:
            result = func(*args, **kwargs)
            logger.info("Tool completed: %s", tool_name)
            return result
        except Exception:
            logger.exception("Tool failed: %s", tool_name)
            raise

    return sync_wrapper


def x_log_tool_execution__mutmut_2(
    func: Callable[P, object],
) -> Callable[P, object]:
    tool_name: str = func.__name__
    logger = None

    if asyncio.iscoroutinefunction(func):

        @functools.wraps(func)
        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
            logger.info("Executing tool: %s", tool_name)
            try:
                result = await func(*args, **kwargs)
                logger.info("Tool completed: %s", tool_name)
                return result
            except Exception:
                logger.exception("Tool failed: %s", tool_name)
                raise

        return async_wrapper

    @functools.wraps(func)
    def sync_wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
        logger.info("Executing tool: %s", tool_name)
        try:
            result = func(*args, **kwargs)
            logger.info("Tool completed: %s", tool_name)
            return result
        except Exception:
            logger.exception("Tool failed: %s", tool_name)
            raise

    return sync_wrapper


def x_log_tool_execution__mutmut_3(
    func: Callable[P, object],
) -> Callable[P, object]:
    tool_name: str = func.__name__
    logger = _get_logger()

    if asyncio.iscoroutinefunction(None):

        @functools.wraps(func)
        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
            logger.info("Executing tool: %s", tool_name)
            try:
                result = await func(*args, **kwargs)
                logger.info("Tool completed: %s", tool_name)
                return result
            except Exception:
                logger.exception("Tool failed: %s", tool_name)
                raise

        return async_wrapper

    @functools.wraps(func)
    def sync_wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
        logger.info("Executing tool: %s", tool_name)
        try:
            result = func(*args, **kwargs)
            logger.info("Tool completed: %s", tool_name)
            return result
        except Exception:
            logger.exception("Tool failed: %s", tool_name)
            raise

    return sync_wrapper

mutants_x_log_tool_execution__mutmut['_mutmut_orig'] = x_log_tool_execution__mutmut_orig # type: ignore # mutmut generated
mutants_x_log_tool_execution__mutmut['x_log_tool_execution__mutmut_1'] = x_log_tool_execution__mutmut_1 # type: ignore # mutmut generated
mutants_x_log_tool_execution__mutmut['x_log_tool_execution__mutmut_2'] = x_log_tool_execution__mutmut_2 # type: ignore # mutmut generated
mutants_x_log_tool_execution__mutmut['x_log_tool_execution__mutmut_3'] = x_log_tool_execution__mutmut_3 # type: ignore # mutmut generated
