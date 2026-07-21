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


class _AnonymizerFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        _anonymize_log(record)
        return True


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


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    root = setup_logging()
    logger.handlers = root.handlers[:]
    logger.setLevel(root.level)
    logger.propagate = False

    return logger


def _get_logger() -> logging.Logger:
    return logging.getLogger(HEXAWYN_LOGGER_NAME)


@overload
def log_tool_execution(func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]: ...


@overload
def log_tool_execution(func: Callable[P, R]) -> Callable[P, R]: ...


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
