"""Unit tests for the log_tool_execution decorator and logger utilities."""

import asyncio
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from unittest.mock import patch

from hexawyn.infrastructure.logging.tool_decorator import (
    _AnonymizerFilter,
    get_logger,
    log_tool_execution,
    setup_logging,
)


class TestAnonymizerFilter:
    """Cover _AnonymizerFilter and _anonymize_log (lines 28-29)."""

    def test_filter_returns_true(self) -> None:
        record = logging.LogRecord(
            name="test",
            level=0,
            pathname="",
            lineno=0,
            msg="test",
            args=(),
            exc_info=None,
        )
        filter_instance = _AnonymizerFilter()
        assert filter_instance.filter(record) is True

    def test_anonymize_handles_import_error(self) -> None:
        record = logging.LogRecord(
            name="test",
            level=0,
            pathname="",
            lineno=0,
            msg="API_KEY=secret",
            args=(),
            exc_info=None,
        )
        filter_instance = _AnonymizerFilter()
        with patch(
            "hexawyn.runtime.adapters.anonymize.regex_anonymizer.RegexAnonymizerAdapter",
            side_effect=ImportError,
        ):
            result = filter_instance.filter(record)
            assert result is True

    def test_anonymize_handles_runtime_error(self) -> None:
        record = logging.LogRecord(
            name="test",
            level=0,
            pathname="",
            lineno=0,
            msg="API_KEY=secret",
            args=(),
            exc_info=None,
        )
        filter_instance = _AnonymizerFilter()
        with patch(
            "hexawyn.runtime.adapters.anonymize.regex_anonymizer.RegexAnonymizerAdapter",
            side_effect=TypeError("bad type"),
        ):
            result = filter_instance.filter(record)
            assert result is True


class TestSetupLogging:
    def test_returns_logger(self) -> None:
        logger = setup_logging(level=logging.WARNING)
        assert isinstance(logger, logging.Logger)

    def test_logger_has_stream_handler(self) -> None:
        logger = setup_logging()
        stream_handlers = [h for h in logger.handlers if isinstance(h, logging.StreamHandler)]
        assert len(stream_handlers) >= 1

    def test_logger_has_rotating_file_handler(self) -> None:
        logger = setup_logging()
        rotating_handlers = [h for h in logger.handlers if isinstance(h, RotatingFileHandler)]
        assert len(rotating_handlers) >= 1

    def test_creates_logs_directory(self, tmp_path: Path) -> None:
        logging.getLogger("hexawyn").handlers.clear()
        logs_dir = tmp_path / "logs"
        setup_logging(log_dir=str(logs_dir))
        assert logs_dir.exists()
        assert logs_dir.is_dir()

    def test_propagate_is_false(self) -> None:
        logger = setup_logging()
        assert logger.propagate is False


class TestGetLogger:
    def test_returns_logger_with_correct_name(self) -> None:
        logger = get_logger("hexawyn.cli")
        assert logger.name == "hexawyn.cli"

    def test_no_duplicate_handlers_on_second_call(self) -> None:
        first = get_logger("hexawyn.mcp.tools")
        initial_count = len(first.handlers)
        second = get_logger("hexawyn.mcp.tools")
        assert second is first
        assert len(second.handlers) == initial_count

    def test_child_logger_inherits_handlers(self) -> None:
        get_logger("hexawyn")
        child = get_logger("hexawyn.adapters.k8s")
        assert child.name == "hexawyn.adapters.k8s"
        assert child.propagate is False
        assert len(child.handlers) >= 1


class TestLogToolExecutionSync:
    def test_logs_tool_name_on_success(self, caplog) -> None:  # type: ignore[no-untyped-def]
        hexa = logging.getLogger("hexawyn")
        hexa.addHandler(caplog.handler)
        caplog.set_level(logging.INFO)

        @log_tool_execution
        def sample_tool(query: str) -> str:
            return f"result:{query}"

        result = sample_tool("test-query")
        assert result == "result:test-query"
        assert "Executing tool: sample_tool" in caplog.text
        assert "Tool completed: sample_tool" in caplog.text

    def test_logs_error_and_re_raises(self, caplog) -> None:  # type: ignore[no-untyped-def]
        hexa = logging.getLogger("hexawyn")
        hexa.addHandler(caplog.handler)
        caplog.set_level(logging.ERROR)

        @log_tool_execution
        def failing_tool() -> str:
            raise ValueError("something broke")

        try:
            failing_tool()
        except ValueError:
            pass

        assert "Tool failed: failing_tool" in caplog.text
        assert "something broke" in caplog.text

    def test_preserves_function_metadata(self) -> None:
        @log_tool_execution
        def my_tool(query: str) -> str:
            """Custom docstring."""
            return query

        assert my_tool.__name__ == "my_tool"
        assert my_tool.__doc__ == "Custom docstring."


class TestLogToolExecutionAsync:
    def test_logs_async_tool_name_on_success(self, caplog) -> None:  # type: ignore[no-untyped-def]
        hexa = logging.getLogger("hexawyn")
        hexa.addHandler(caplog.handler)
        caplog.set_level(logging.INFO)

        @log_tool_execution
        async def async_tool(query: str) -> str:
            await asyncio.sleep(0)
            return f"async:{query}"

        result = asyncio.run(async_tool("run"))
        assert result == "async:run"
        assert "Executing tool: async_tool" in caplog.text
        assert "Tool completed: async_tool" in caplog.text

    def test_logs_async_error_and_re_raises(self, caplog) -> None:  # type: ignore[no-untyped-def]
        hexa = logging.getLogger("hexawyn")
        hexa.addHandler(caplog.handler)
        caplog.set_level(logging.ERROR)

        @log_tool_execution
        async def async_failing() -> str:
            await asyncio.sleep(0)
            raise RuntimeError("async broke")

        with __import__("pytest").raises(RuntimeError):
            asyncio.run(async_failing())

        assert "Tool failed: async_failing" in caplog.text
        assert "async broke" in caplog.text

    def test_preserves_async_function_metadata(self) -> None:
        @log_tool_execution
        async def my_async_tool(query: str) -> str:
            """Async docstring."""
            return query

        assert my_async_tool.__name__ == "my_async_tool"
        assert my_async_tool.__doc__ == "Async docstring."
