import json
import logging
from datetime import UTC, datetime, timedelta
from pathlib import Path

from hexawyn.application.ports.driven.usage_ledger_port import UsageLedgerPort
from hexawyn.domain.models.usage import (
    DailyStats,
    InvestigationUsage,
    MonthlyReport,
    ToolStat,
    UsageStats,
)

logger = logging.getLogger(__name__)

_MAX_MONTHLY_LINES = 100_000


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁUsageLedgerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁUsageLedgerǁrecord__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUsageLedgerǁread_all__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUsageLedgerǁstats__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUsageLedgerǁmonthly_report__mutmut: MutantDict = {}  # type: ignore


class UsageLedger(UsageLedgerPort):
    @_mutmut_mutated(mutants_xǁUsageLedgerǁ__init____mutmut)
    def __init__(self, path: Path | None = None) -> None:
        if path is None:
            path = Path.home() / ".hexawyn" / "usage.jsonl"
        self._path = path
    def xǁUsageLedgerǁ__init____mutmut_orig(self, path: Path | None = None) -> None:
        if path is None:
            path = Path.home() / ".hexawyn" / "usage.jsonl"
        self._path = path
    def xǁUsageLedgerǁ__init____mutmut_1(self, path: Path | None = None) -> None:
        if path is not None:
            path = Path.home() / ".hexawyn" / "usage.jsonl"
        self._path = path
    def xǁUsageLedgerǁ__init____mutmut_2(self, path: Path | None = None) -> None:
        if path is None:
            path = None
        self._path = path
    def xǁUsageLedgerǁ__init____mutmut_3(self, path: Path | None = None) -> None:
        if path is None:
            path = Path.home() / ".hexawyn" * "usage.jsonl"
        self._path = path
    def xǁUsageLedgerǁ__init____mutmut_4(self, path: Path | None = None) -> None:
        if path is None:
            path = Path.home() * ".hexawyn" / "usage.jsonl"
        self._path = path
    def xǁUsageLedgerǁ__init____mutmut_5(self, path: Path | None = None) -> None:
        if path is None:
            path = Path.home() / "XX.hexawynXX" / "usage.jsonl"
        self._path = path
    def xǁUsageLedgerǁ__init____mutmut_6(self, path: Path | None = None) -> None:
        if path is None:
            path = Path.home() / ".HEXAWYN" / "usage.jsonl"
        self._path = path
    def xǁUsageLedgerǁ__init____mutmut_7(self, path: Path | None = None) -> None:
        if path is None:
            path = Path.home() / ".hexawyn" / "XXusage.jsonlXX"
        self._path = path
    def xǁUsageLedgerǁ__init____mutmut_8(self, path: Path | None = None) -> None:
        if path is None:
            path = Path.home() / ".hexawyn" / "USAGE.JSONL"
        self._path = path
    def xǁUsageLedgerǁ__init____mutmut_9(self, path: Path | None = None) -> None:
        if path is None:
            path = Path.home() / ".hexawyn" / "usage.jsonl"
        self._path = None

    @_mutmut_mutated(mutants_xǁUsageLedgerǁrecord__mutmut)
    def record(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_orig(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_1(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=None, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_2(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=None)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_3(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_4(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, )
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_5(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=False, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_6(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=False)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_7(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(None, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_8(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, None) as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_9(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open("a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_10(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, ) as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_11(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "XXaXX") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_12(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "A") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_13(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(None)
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_14(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) - "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_15(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(None, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_16(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=None) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_17(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_18(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_19(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=True) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_20(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "XX\nXX")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_21(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug(None, exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_22(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=None)

    def xǁUsageLedgerǁrecord__mutmut_23(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug(exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_24(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", )

    def xǁUsageLedgerǁrecord__mutmut_25(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("XXFailed to record usage entryXX", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_26(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("failed to record usage entry", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_27(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("FAILED TO RECORD USAGE ENTRY", exc_info=True)

    def xǁUsageLedgerǁrecord__mutmut_28(self, usage: InvestigationUsage) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "a") as f:
                f.write(json.dumps(usage, ensure_ascii=False) + "\n")
        except Exception:
            logger.debug("Failed to record usage entry", exc_info=False)

    @_mutmut_mutated(mutants_xǁUsageLedgerǁread_all__mutmut)
    def read_all(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_orig(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_1(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = None
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_2(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_3(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_4(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(None) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_5(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(None) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_6(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = None
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_7(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_8(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        break
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_9(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = None
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_10(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(None)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_11(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        break
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_12(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_13(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        break
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_14(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_15(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = None
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_16(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(None)
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_17(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(None))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_18(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get(None, "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_19(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", None)))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_20(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_21(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", )))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_22(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("XXtimestampXX", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_23(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("TIMESTAMP", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_24(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "XXXX")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_25(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None and entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_26(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is not None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_27(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts <= since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_28(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            break
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_29(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None or entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_30(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_31(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get(None, "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_32(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", None) != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_33(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_34(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", ) != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_35(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("XXtool_nameXX", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_36(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("TOOL_NAME", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_37(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "XXXX") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_38(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") == tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_39(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        break
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_40(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(None)
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_41(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(None))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_42(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug(None, exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_43(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=None)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_44(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug(exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_45(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", )
        return entries

    def xǁUsageLedgerǁread_all__mutmut_46(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("XXFailed to read usage ledgerXX", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_47(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("failed to read usage ledger", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_48(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("FAILED TO READ USAGE LEDGER", exc_info=True)
        return entries

    def xǁUsageLedgerǁread_all__mutmut_49(
        self, since: str | None = None, tool: str | None = None
    ) -> list[InvestigationUsage]:
        entries: list[InvestigationUsage] = []
        if not self._path.exists():
            return entries
        since_dt = _parse_iso(since) if since else None
        try:
            with open(self._path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(entry, dict):
                        continue
                    if since_dt is not None:
                        entry_ts = _parse_iso(str(entry.get("timestamp", "")))
                        if entry_ts is None or entry_ts < since_dt:
                            continue
                    if tool is not None and entry.get("tool_name", "") != tool:
                        continue
                    entries.append(_coerce_entry(entry))
        except OSError:
            logger.debug("Failed to read usage ledger", exc_info=False)
        return entries

    @_mutmut_mutated(mutants_xǁUsageLedgerǁstats__mutmut)
    def stats(self, days: int = 30) -> UsageStats:
        entries = self.read_all(since=_iso_days_ago(days))
        return _compute_stats(entries)

    def xǁUsageLedgerǁstats__mutmut_orig(self, days: int = 30) -> UsageStats:
        entries = self.read_all(since=_iso_days_ago(days))
        return _compute_stats(entries)

    def xǁUsageLedgerǁstats__mutmut_1(self, days: int = 31) -> UsageStats:
        entries = self.read_all(since=_iso_days_ago(days))
        return _compute_stats(entries)

    def xǁUsageLedgerǁstats__mutmut_2(self, days: int = 30) -> UsageStats:
        entries = None
        return _compute_stats(entries)

    def xǁUsageLedgerǁstats__mutmut_3(self, days: int = 30) -> UsageStats:
        entries = self.read_all(since=None)
        return _compute_stats(entries)

    def xǁUsageLedgerǁstats__mutmut_4(self, days: int = 30) -> UsageStats:
        entries = self.read_all(since=_iso_days_ago(None))
        return _compute_stats(entries)

    def xǁUsageLedgerǁstats__mutmut_5(self, days: int = 30) -> UsageStats:
        entries = self.read_all(since=_iso_days_ago(days))
        return _compute_stats(None)

    @_mutmut_mutated(mutants_xǁUsageLedgerǁmonthly_report__mutmut)
    def monthly_report(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_orig(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_1(self, year: int, month: int) -> MonthlyReport:
        start = None
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_2(self, year: int, month: int) -> MonthlyReport:
        start = datetime(None, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_3(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, None, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_4(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, None, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_5(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=None).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_6(self, year: int, month: int) -> MonthlyReport:
        start = datetime(month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_7(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_8(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_9(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, ).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_10(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 2, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_11(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month != 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_12(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 13:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_13(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = None
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_14(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(None, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_15(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, None, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_16(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, None, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_17(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=None).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_18(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_19(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_20(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_21(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, ).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_22(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year - 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_23(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 2, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_24(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 2, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_25(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 2, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_26(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = None
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_27(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(None, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_28(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, None, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_29(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, None, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_30(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=None).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_31(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_32(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_33(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_34(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, ).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_35(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month - 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_36(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 2, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_37(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 2, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_38(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = None
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_39(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=None)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_40(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = None

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_41(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["XXtimestampXX"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_42(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["TIMESTAMP"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_43(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] <= end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_44(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = None
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_45(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = None
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_46(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["XXtimestampXX"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_47(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["TIMESTAMP"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_48(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:11]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_49(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_50(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = None
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_51(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=None, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_52(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=None, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_53(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=None)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_54(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_55(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_56(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, )
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_57(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=1, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_58(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=1)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_59(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] = 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_60(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] -= 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_61(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["XXinvestigationsXX"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_62(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["INVESTIGATIONS"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_63(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 2
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_64(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] = entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_65(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] -= entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_66(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["XXtokensXX"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_67(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["TOKENS"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_68(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] - entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_69(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["XXprompt_tokensXX"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_70(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["PROMPT_TOKENS"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_71(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["XXcompletion_tokensXX"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_72(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["COMPLETION_TOKENS"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_73(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=None,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_74(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=None,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_75(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=None,
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_76(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=None,
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_77(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_78(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_79(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_80(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            )

    def xǁUsageLedgerǁmonthly_report__mutmut_81(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(None),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_82(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(None, key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_83(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=None),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_84(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(key=lambda d: d["date"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_85(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), ),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_86(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: None),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_87(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["XXdateXX"]),
        )

    def xǁUsageLedgerǁmonthly_report__mutmut_88(self, year: int, month: int) -> MonthlyReport:
        start = datetime(year, month, 1, tzinfo=UTC).isoformat()
        if month == 12:  # noqa: PLR2004
            end = datetime(year + 1, 1, 1, tzinfo=UTC).isoformat()
        else:
            end = datetime(year, month + 1, 1, tzinfo=UTC).isoformat()
        month_entries = self.read_all(since=start)
        month_entries = [e for e in month_entries if e["timestamp"] < end]

        daily: dict[str, DailyStats] = {}
        for entry in month_entries:
            date_key = entry["timestamp"][:10]
            if date_key not in daily:
                daily[date_key] = DailyStats(date=date_key, investigations=0, tokens=0)
            daily[date_key]["investigations"] += 1
            daily[date_key]["tokens"] += entry["prompt_tokens"] + entry["completion_tokens"]

        return MonthlyReport(
            year=year,
            month=month,
            stats=_compute_stats(month_entries),
            daily_breakdown=sorted(daily.values(), key=lambda d: d["DATE"]),
        )

mutants_xǁUsageLedgerǁ__init____mutmut['_mutmut_orig'] = UsageLedger.xǁUsageLedgerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁ__init____mutmut['xǁUsageLedgerǁ__init____mutmut_1'] = UsageLedger.xǁUsageLedgerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁ__init____mutmut['xǁUsageLedgerǁ__init____mutmut_2'] = UsageLedger.xǁUsageLedgerǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁ__init____mutmut['xǁUsageLedgerǁ__init____mutmut_3'] = UsageLedger.xǁUsageLedgerǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁ__init____mutmut['xǁUsageLedgerǁ__init____mutmut_4'] = UsageLedger.xǁUsageLedgerǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁ__init____mutmut['xǁUsageLedgerǁ__init____mutmut_5'] = UsageLedger.xǁUsageLedgerǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁ__init____mutmut['xǁUsageLedgerǁ__init____mutmut_6'] = UsageLedger.xǁUsageLedgerǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁ__init____mutmut['xǁUsageLedgerǁ__init____mutmut_7'] = UsageLedger.xǁUsageLedgerǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁ__init____mutmut['xǁUsageLedgerǁ__init____mutmut_8'] = UsageLedger.xǁUsageLedgerǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁ__init____mutmut['xǁUsageLedgerǁ__init____mutmut_9'] = UsageLedger.xǁUsageLedgerǁ__init____mutmut_9 # type: ignore # mutmut generated

mutants_xǁUsageLedgerǁrecord__mutmut['_mutmut_orig'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_1'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_2'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_3'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_4'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_5'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_6'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_7'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_8'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_9'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_10'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_11'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_12'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_13'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_14'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_15'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_16'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_17'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_18'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_19'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_20'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_20 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_21'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_21 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_22'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_22 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_23'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_23 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_24'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_24 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_25'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_25 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_26'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_26 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_27'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_27 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁrecord__mutmut['xǁUsageLedgerǁrecord__mutmut_28'] = UsageLedger.xǁUsageLedgerǁrecord__mutmut_28 # type: ignore # mutmut generated

mutants_xǁUsageLedgerǁread_all__mutmut['_mutmut_orig'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_1'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_2'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_3'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_4'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_5'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_6'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_7'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_8'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_9'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_10'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_11'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_12'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_13'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_14'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_15'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_16'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_17'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_18'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_19'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_20'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_20 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_21'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_21 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_22'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_22 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_23'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_23 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_24'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_24 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_25'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_25 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_26'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_26 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_27'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_27 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_28'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_28 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_29'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_29 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_30'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_30 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_31'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_31 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_32'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_32 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_33'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_33 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_34'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_34 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_35'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_35 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_36'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_36 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_37'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_37 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_38'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_38 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_39'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_39 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_40'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_40 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_41'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_41 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_42'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_42 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_43'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_43 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_44'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_44 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_45'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_45 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_46'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_46 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_47'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_47 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_48'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_48 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁread_all__mutmut['xǁUsageLedgerǁread_all__mutmut_49'] = UsageLedger.xǁUsageLedgerǁread_all__mutmut_49 # type: ignore # mutmut generated

mutants_xǁUsageLedgerǁstats__mutmut['_mutmut_orig'] = UsageLedger.xǁUsageLedgerǁstats__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁstats__mutmut['xǁUsageLedgerǁstats__mutmut_1'] = UsageLedger.xǁUsageLedgerǁstats__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁstats__mutmut['xǁUsageLedgerǁstats__mutmut_2'] = UsageLedger.xǁUsageLedgerǁstats__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁstats__mutmut['xǁUsageLedgerǁstats__mutmut_3'] = UsageLedger.xǁUsageLedgerǁstats__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁstats__mutmut['xǁUsageLedgerǁstats__mutmut_4'] = UsageLedger.xǁUsageLedgerǁstats__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁstats__mutmut['xǁUsageLedgerǁstats__mutmut_5'] = UsageLedger.xǁUsageLedgerǁstats__mutmut_5 # type: ignore # mutmut generated

mutants_xǁUsageLedgerǁmonthly_report__mutmut['_mutmut_orig'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_1'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_2'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_3'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_4'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_5'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_6'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_7'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_8'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_9'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_10'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_11'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_12'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_13'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_14'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_15'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_16'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_16 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_17'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_17 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_18'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_18 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_19'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_19 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_20'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_20 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_21'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_21 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_22'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_22 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_23'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_23 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_24'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_24 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_25'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_25 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_26'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_26 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_27'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_27 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_28'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_28 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_29'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_29 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_30'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_30 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_31'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_31 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_32'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_32 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_33'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_33 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_34'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_34 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_35'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_35 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_36'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_36 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_37'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_37 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_38'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_38 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_39'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_39 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_40'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_40 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_41'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_41 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_42'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_42 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_43'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_43 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_44'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_44 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_45'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_45 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_46'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_46 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_47'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_47 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_48'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_48 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_49'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_49 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_50'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_50 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_51'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_51 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_52'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_52 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_53'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_53 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_54'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_54 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_55'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_55 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_56'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_56 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_57'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_57 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_58'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_58 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_59'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_59 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_60'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_60 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_61'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_61 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_62'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_62 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_63'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_63 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_64'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_64 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_65'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_65 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_66'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_66 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_67'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_67 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_68'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_68 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_69'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_69 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_70'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_70 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_71'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_71 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_72'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_72 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_73'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_73 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_74'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_74 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_75'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_75 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_76'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_76 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_77'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_77 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_78'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_78 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_79'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_79 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_80'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_80 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_81'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_81 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_82'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_82 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_83'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_83 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_84'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_84 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_85'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_85 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_86'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_86 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_87'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_87 # type: ignore # mutmut generated
mutants_xǁUsageLedgerǁmonthly_report__mutmut['xǁUsageLedgerǁmonthly_report__mutmut_88'] = UsageLedger.xǁUsageLedgerǁmonthly_report__mutmut_88 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__coerce_entry__mutmut)
def _coerce_entry(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_orig(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_1(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=None,
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_2(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=None,
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_3(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=None,
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_4(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=None,
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_5(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=None,
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_6(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_7(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=None,
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_8(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=None,
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_9(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=None,
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_10(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=None,
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_11(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=None,
    )


def x__coerce_entry__mutmut_12(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_13(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_14(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_15(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_16(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_17(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_18(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_19(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_20(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_21(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_22(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        )


def x__coerce_entry__mutmut_23(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(None),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_24(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get(None, "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_25(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", None)),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_26(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_27(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", )),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_28(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("XXtimestampXX", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_29(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("TIMESTAMP", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_30(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "XXXX")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_31(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(None),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_32(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get(None, "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_33(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", None)),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_34(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_35(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", )),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_36(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("XXqueryXX", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_37(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("QUERY", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_38(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "XXXX")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_39(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(None),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_40(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get(None, "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_41(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", None)),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_42(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_43(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", )),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_44(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("XXtool_nameXX", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_45(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("TOOL_NAME", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_46(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "XX-XX")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_47(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(None),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_48(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get(None, "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_49(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", None)),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_50(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_51(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", )),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_52(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("XXverdictXX", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_53(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("VERDICT", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_54(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "XXN/AXX")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_55(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "n/a")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_56(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(None),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_57(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get(None, "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_58(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", None)),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_59(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_60(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", )),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_61(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("XXcluster_nameXX", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_62(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("CLUSTER_NAME", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_63(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "XXXX")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_64(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(None) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_65(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["XXnamespaceXX"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_66(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["NAMESPACE"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_67(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get(None) else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_68(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("XXnamespaceXX") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_69(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("NAMESPACE") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_70(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(None),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_71(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(None)),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_72(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get(None, 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_73(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", None))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_74(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get(0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_75(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", ))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_76(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("XXduration_msXX", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_77(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("DURATION_MS", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_78(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 1))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_79(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(None),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_80(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(None)),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_81(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get(None, 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_82(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", None))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_83(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get(0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_84(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", ))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_85(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("XXprompt_tokensXX", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_86(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("PROMPT_TOKENS", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_87(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 1))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_88(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(None),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_89(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(None)),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_90(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get(None, 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_91(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", None))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_92(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get(0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_93(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", ))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_94(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("XXcompletion_tokensXX", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_95(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("COMPLETION_TOKENS", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_96(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 1))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_97(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(None),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_98(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get(None, "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_99(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", None)),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_100(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_101(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", )),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_102(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("XXmodelXX", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_103(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("MODEL", "-")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_104(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "XX-XX")),
        provider=str(raw.get("provider", "-")),
    )


def x__coerce_entry__mutmut_105(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(None),
    )


def x__coerce_entry__mutmut_106(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get(None, "-")),
    )


def x__coerce_entry__mutmut_107(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", None)),
    )


def x__coerce_entry__mutmut_108(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("-")),
    )


def x__coerce_entry__mutmut_109(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", )),
    )


def x__coerce_entry__mutmut_110(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("XXproviderXX", "-")),
    )


def x__coerce_entry__mutmut_111(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("PROVIDER", "-")),
    )


def x__coerce_entry__mutmut_112(raw: dict[str, object]) -> InvestigationUsage:
    return InvestigationUsage(
        timestamp=str(raw.get("timestamp", "")),
        query=str(raw.get("query", "")),
        tool_name=str(raw.get("tool_name", "-")),
        verdict=str(raw.get("verdict", "N/A")),
        cluster_name=str(raw.get("cluster_name", "")),
        namespace=str(raw["namespace"]) if raw.get("namespace") else None,
        duration_ms=int(str(raw.get("duration_ms", 0))),
        prompt_tokens=int(str(raw.get("prompt_tokens", 0))),
        completion_tokens=int(str(raw.get("completion_tokens", 0))),
        model=str(raw.get("model", "-")),
        provider=str(raw.get("provider", "XX-XX")),
    )

mutants_x__coerce_entry__mutmut['_mutmut_orig'] = x__coerce_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_1'] = x__coerce_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_2'] = x__coerce_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_3'] = x__coerce_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_4'] = x__coerce_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_5'] = x__coerce_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_6'] = x__coerce_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_7'] = x__coerce_entry__mutmut_7 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_8'] = x__coerce_entry__mutmut_8 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_9'] = x__coerce_entry__mutmut_9 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_10'] = x__coerce_entry__mutmut_10 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_11'] = x__coerce_entry__mutmut_11 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_12'] = x__coerce_entry__mutmut_12 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_13'] = x__coerce_entry__mutmut_13 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_14'] = x__coerce_entry__mutmut_14 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_15'] = x__coerce_entry__mutmut_15 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_16'] = x__coerce_entry__mutmut_16 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_17'] = x__coerce_entry__mutmut_17 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_18'] = x__coerce_entry__mutmut_18 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_19'] = x__coerce_entry__mutmut_19 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_20'] = x__coerce_entry__mutmut_20 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_21'] = x__coerce_entry__mutmut_21 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_22'] = x__coerce_entry__mutmut_22 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_23'] = x__coerce_entry__mutmut_23 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_24'] = x__coerce_entry__mutmut_24 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_25'] = x__coerce_entry__mutmut_25 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_26'] = x__coerce_entry__mutmut_26 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_27'] = x__coerce_entry__mutmut_27 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_28'] = x__coerce_entry__mutmut_28 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_29'] = x__coerce_entry__mutmut_29 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_30'] = x__coerce_entry__mutmut_30 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_31'] = x__coerce_entry__mutmut_31 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_32'] = x__coerce_entry__mutmut_32 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_33'] = x__coerce_entry__mutmut_33 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_34'] = x__coerce_entry__mutmut_34 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_35'] = x__coerce_entry__mutmut_35 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_36'] = x__coerce_entry__mutmut_36 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_37'] = x__coerce_entry__mutmut_37 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_38'] = x__coerce_entry__mutmut_38 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_39'] = x__coerce_entry__mutmut_39 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_40'] = x__coerce_entry__mutmut_40 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_41'] = x__coerce_entry__mutmut_41 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_42'] = x__coerce_entry__mutmut_42 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_43'] = x__coerce_entry__mutmut_43 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_44'] = x__coerce_entry__mutmut_44 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_45'] = x__coerce_entry__mutmut_45 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_46'] = x__coerce_entry__mutmut_46 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_47'] = x__coerce_entry__mutmut_47 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_48'] = x__coerce_entry__mutmut_48 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_49'] = x__coerce_entry__mutmut_49 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_50'] = x__coerce_entry__mutmut_50 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_51'] = x__coerce_entry__mutmut_51 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_52'] = x__coerce_entry__mutmut_52 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_53'] = x__coerce_entry__mutmut_53 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_54'] = x__coerce_entry__mutmut_54 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_55'] = x__coerce_entry__mutmut_55 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_56'] = x__coerce_entry__mutmut_56 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_57'] = x__coerce_entry__mutmut_57 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_58'] = x__coerce_entry__mutmut_58 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_59'] = x__coerce_entry__mutmut_59 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_60'] = x__coerce_entry__mutmut_60 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_61'] = x__coerce_entry__mutmut_61 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_62'] = x__coerce_entry__mutmut_62 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_63'] = x__coerce_entry__mutmut_63 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_64'] = x__coerce_entry__mutmut_64 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_65'] = x__coerce_entry__mutmut_65 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_66'] = x__coerce_entry__mutmut_66 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_67'] = x__coerce_entry__mutmut_67 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_68'] = x__coerce_entry__mutmut_68 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_69'] = x__coerce_entry__mutmut_69 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_70'] = x__coerce_entry__mutmut_70 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_71'] = x__coerce_entry__mutmut_71 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_72'] = x__coerce_entry__mutmut_72 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_73'] = x__coerce_entry__mutmut_73 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_74'] = x__coerce_entry__mutmut_74 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_75'] = x__coerce_entry__mutmut_75 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_76'] = x__coerce_entry__mutmut_76 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_77'] = x__coerce_entry__mutmut_77 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_78'] = x__coerce_entry__mutmut_78 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_79'] = x__coerce_entry__mutmut_79 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_80'] = x__coerce_entry__mutmut_80 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_81'] = x__coerce_entry__mutmut_81 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_82'] = x__coerce_entry__mutmut_82 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_83'] = x__coerce_entry__mutmut_83 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_84'] = x__coerce_entry__mutmut_84 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_85'] = x__coerce_entry__mutmut_85 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_86'] = x__coerce_entry__mutmut_86 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_87'] = x__coerce_entry__mutmut_87 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_88'] = x__coerce_entry__mutmut_88 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_89'] = x__coerce_entry__mutmut_89 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_90'] = x__coerce_entry__mutmut_90 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_91'] = x__coerce_entry__mutmut_91 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_92'] = x__coerce_entry__mutmut_92 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_93'] = x__coerce_entry__mutmut_93 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_94'] = x__coerce_entry__mutmut_94 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_95'] = x__coerce_entry__mutmut_95 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_96'] = x__coerce_entry__mutmut_96 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_97'] = x__coerce_entry__mutmut_97 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_98'] = x__coerce_entry__mutmut_98 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_99'] = x__coerce_entry__mutmut_99 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_100'] = x__coerce_entry__mutmut_100 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_101'] = x__coerce_entry__mutmut_101 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_102'] = x__coerce_entry__mutmut_102 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_103'] = x__coerce_entry__mutmut_103 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_104'] = x__coerce_entry__mutmut_104 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_105'] = x__coerce_entry__mutmut_105 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_106'] = x__coerce_entry__mutmut_106 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_107'] = x__coerce_entry__mutmut_107 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_108'] = x__coerce_entry__mutmut_108 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_109'] = x__coerce_entry__mutmut_109 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_110'] = x__coerce_entry__mutmut_110 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_111'] = x__coerce_entry__mutmut_111 # type: ignore # mutmut generated
mutants_x__coerce_entry__mutmut['x__coerce_entry__mutmut_112'] = x__coerce_entry__mutmut_112 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_stats__mutmut)
def _compute_stats(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_orig(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_1(entries: list[InvestigationUsage]) -> UsageStats:
    if entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_2(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=None,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_3(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=None,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_4(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=None,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_5(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=None,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_6(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=None,
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_7(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution=None,
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_8(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used=None,
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_9(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_10(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_11(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_12(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_13(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_14(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_15(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_16(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=1,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_17(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=1,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_18(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=1,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_19(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=1,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_20(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = None
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_21(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 1
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_22(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = None
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_23(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 1
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_24(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = None
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_25(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = None
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_26(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = None
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_27(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = None

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_28(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens = entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_29(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens -= entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_30(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] - entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_31(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["XXprompt_tokensXX"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_32(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["PROMPT_TOKENS"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_33(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["XXcompletion_tokensXX"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_34(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["COMPLETION_TOKENS"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_35(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms = entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_36(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms -= entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_37(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["XXduration_msXX"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_38(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["DURATION_MS"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_39(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = None
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_40(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["XXtool_nameXX"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_41(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["TOOL_NAME"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_42(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = None
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_43(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) - 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_44(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(None, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_45(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, None) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_46(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_47(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, ) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_48(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 1) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_49(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 2
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_50(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = None

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_51(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) - entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_52(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(None, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_53(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, None) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_54(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_55(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, ) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_56(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 1) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_57(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["XXduration_msXX"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_58(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["DURATION_MS"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_59(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = None
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_60(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["XXverdictXX"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_61(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["VERDICT"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_62(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = None

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_63(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) - 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_64(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(None, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_65(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, None) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_66(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_67(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, ) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_68(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 1) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_69(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 2

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_70(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = None
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_71(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["XXmodelXX"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_72(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["MODEL"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_73(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model or model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_74(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model == "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_75(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "XX-XX":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_76(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = None

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_77(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) - 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_78(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(None, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_79(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, None) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_80(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_81(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, ) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_82(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 1) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_83(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 2

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_84(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = None

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_85(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=None, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_86(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=None, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_87(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=None)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_88(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_89(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_90(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, )
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_91(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] / c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_92(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(None, key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_93(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=None, reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_94(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=None)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_95(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_96(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_97(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], )[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_98(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: None, reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_99(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[2], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_100(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=False)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_101(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:11]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_102(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=None,
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_103(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=None,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_104(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=None,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_105(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=None,
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_106(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=None,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_107(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=None,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_108(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=None,
    )


def x__compute_stats__mutmut_109(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_110(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_111(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_112(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_113(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_114(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        models_used=model_counts,
    )


def x__compute_stats__mutmut_115(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms // len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        )


def x__compute_stats__mutmut_116(entries: list[InvestigationUsage]) -> UsageStats:
    if not entries:
        return UsageStats(
            total_investigations=0,
            total_tokens=0,
            total_duration_ms=0,
            avg_duration_ms=0,
            top_tools=[],
            verdict_distribution={},
            models_used={},
        )

    total_tokens = 0
    total_duration_ms = 0
    tool_counts: dict[str, int] = {}
    tool_durations: dict[str, int] = {}
    verdict_counts: dict[str, int] = {}
    model_counts: dict[str, int] = {}

    for entry in entries:
        total_tokens += entry["prompt_tokens"] + entry["completion_tokens"]
        total_duration_ms += entry["duration_ms"]

        tool = entry["tool_name"]
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
        tool_durations[tool] = tool_durations.get(tool, 0) + entry["duration_ms"]

        verdict = entry["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1

        model = entry["model"]
        if model and model != "-":
            model_counts[model] = model_counts.get(model, 0) + 1

    top_tools: list[ToolStat] = [
        ToolStat(tool_name=t, count=c, avg_duration_ms=tool_durations[t] // c)
        for t, c in sorted(tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    ]

    return UsageStats(
        total_investigations=len(entries),
        total_tokens=total_tokens,
        total_duration_ms=total_duration_ms,
        avg_duration_ms=total_duration_ms / len(entries),
        top_tools=top_tools,
        verdict_distribution=verdict_counts,
        models_used=model_counts,
    )

mutants_x__compute_stats__mutmut['_mutmut_orig'] = x__compute_stats__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_1'] = x__compute_stats__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_2'] = x__compute_stats__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_3'] = x__compute_stats__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_4'] = x__compute_stats__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_5'] = x__compute_stats__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_6'] = x__compute_stats__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_7'] = x__compute_stats__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_8'] = x__compute_stats__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_9'] = x__compute_stats__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_10'] = x__compute_stats__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_11'] = x__compute_stats__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_12'] = x__compute_stats__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_13'] = x__compute_stats__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_14'] = x__compute_stats__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_15'] = x__compute_stats__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_16'] = x__compute_stats__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_17'] = x__compute_stats__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_18'] = x__compute_stats__mutmut_18 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_19'] = x__compute_stats__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_20'] = x__compute_stats__mutmut_20 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_21'] = x__compute_stats__mutmut_21 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_22'] = x__compute_stats__mutmut_22 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_23'] = x__compute_stats__mutmut_23 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_24'] = x__compute_stats__mutmut_24 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_25'] = x__compute_stats__mutmut_25 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_26'] = x__compute_stats__mutmut_26 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_27'] = x__compute_stats__mutmut_27 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_28'] = x__compute_stats__mutmut_28 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_29'] = x__compute_stats__mutmut_29 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_30'] = x__compute_stats__mutmut_30 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_31'] = x__compute_stats__mutmut_31 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_32'] = x__compute_stats__mutmut_32 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_33'] = x__compute_stats__mutmut_33 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_34'] = x__compute_stats__mutmut_34 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_35'] = x__compute_stats__mutmut_35 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_36'] = x__compute_stats__mutmut_36 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_37'] = x__compute_stats__mutmut_37 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_38'] = x__compute_stats__mutmut_38 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_39'] = x__compute_stats__mutmut_39 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_40'] = x__compute_stats__mutmut_40 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_41'] = x__compute_stats__mutmut_41 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_42'] = x__compute_stats__mutmut_42 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_43'] = x__compute_stats__mutmut_43 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_44'] = x__compute_stats__mutmut_44 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_45'] = x__compute_stats__mutmut_45 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_46'] = x__compute_stats__mutmut_46 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_47'] = x__compute_stats__mutmut_47 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_48'] = x__compute_stats__mutmut_48 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_49'] = x__compute_stats__mutmut_49 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_50'] = x__compute_stats__mutmut_50 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_51'] = x__compute_stats__mutmut_51 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_52'] = x__compute_stats__mutmut_52 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_53'] = x__compute_stats__mutmut_53 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_54'] = x__compute_stats__mutmut_54 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_55'] = x__compute_stats__mutmut_55 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_56'] = x__compute_stats__mutmut_56 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_57'] = x__compute_stats__mutmut_57 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_58'] = x__compute_stats__mutmut_58 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_59'] = x__compute_stats__mutmut_59 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_60'] = x__compute_stats__mutmut_60 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_61'] = x__compute_stats__mutmut_61 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_62'] = x__compute_stats__mutmut_62 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_63'] = x__compute_stats__mutmut_63 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_64'] = x__compute_stats__mutmut_64 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_65'] = x__compute_stats__mutmut_65 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_66'] = x__compute_stats__mutmut_66 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_67'] = x__compute_stats__mutmut_67 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_68'] = x__compute_stats__mutmut_68 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_69'] = x__compute_stats__mutmut_69 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_70'] = x__compute_stats__mutmut_70 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_71'] = x__compute_stats__mutmut_71 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_72'] = x__compute_stats__mutmut_72 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_73'] = x__compute_stats__mutmut_73 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_74'] = x__compute_stats__mutmut_74 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_75'] = x__compute_stats__mutmut_75 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_76'] = x__compute_stats__mutmut_76 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_77'] = x__compute_stats__mutmut_77 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_78'] = x__compute_stats__mutmut_78 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_79'] = x__compute_stats__mutmut_79 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_80'] = x__compute_stats__mutmut_80 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_81'] = x__compute_stats__mutmut_81 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_82'] = x__compute_stats__mutmut_82 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_83'] = x__compute_stats__mutmut_83 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_84'] = x__compute_stats__mutmut_84 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_85'] = x__compute_stats__mutmut_85 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_86'] = x__compute_stats__mutmut_86 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_87'] = x__compute_stats__mutmut_87 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_88'] = x__compute_stats__mutmut_88 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_89'] = x__compute_stats__mutmut_89 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_90'] = x__compute_stats__mutmut_90 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_91'] = x__compute_stats__mutmut_91 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_92'] = x__compute_stats__mutmut_92 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_93'] = x__compute_stats__mutmut_93 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_94'] = x__compute_stats__mutmut_94 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_95'] = x__compute_stats__mutmut_95 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_96'] = x__compute_stats__mutmut_96 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_97'] = x__compute_stats__mutmut_97 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_98'] = x__compute_stats__mutmut_98 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_99'] = x__compute_stats__mutmut_99 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_100'] = x__compute_stats__mutmut_100 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_101'] = x__compute_stats__mutmut_101 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_102'] = x__compute_stats__mutmut_102 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_103'] = x__compute_stats__mutmut_103 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_104'] = x__compute_stats__mutmut_104 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_105'] = x__compute_stats__mutmut_105 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_106'] = x__compute_stats__mutmut_106 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_107'] = x__compute_stats__mutmut_107 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_108'] = x__compute_stats__mutmut_108 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_109'] = x__compute_stats__mutmut_109 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_110'] = x__compute_stats__mutmut_110 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_111'] = x__compute_stats__mutmut_111 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_112'] = x__compute_stats__mutmut_112 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_113'] = x__compute_stats__mutmut_113 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_114'] = x__compute_stats__mutmut_114 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_115'] = x__compute_stats__mutmut_115 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_116'] = x__compute_stats__mutmut_116 # type: ignore # mutmut generated
mutants_x__parse_iso__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_iso__mutmut)
def _parse_iso(value: str) -> datetime | None:
    try:
        val = value.replace("Z", "+00:00")
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def x__parse_iso__mutmut_orig(value: str) -> datetime | None:
    try:
        val = value.replace("Z", "+00:00")
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def x__parse_iso__mutmut_1(value: str) -> datetime | None:
    try:
        val = None
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def x__parse_iso__mutmut_2(value: str) -> datetime | None:
    try:
        val = value.replace(None, "+00:00")
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def x__parse_iso__mutmut_3(value: str) -> datetime | None:
    try:
        val = value.replace("Z", None)
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def x__parse_iso__mutmut_4(value: str) -> datetime | None:
    try:
        val = value.replace("+00:00")
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def x__parse_iso__mutmut_5(value: str) -> datetime | None:
    try:
        val = value.replace("Z", )
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def x__parse_iso__mutmut_6(value: str) -> datetime | None:
    try:
        val = value.replace("XXZXX", "+00:00")
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def x__parse_iso__mutmut_7(value: str) -> datetime | None:
    try:
        val = value.replace("z", "+00:00")
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def x__parse_iso__mutmut_8(value: str) -> datetime | None:
    try:
        val = value.replace("Z", "XX+00:00XX")
        return datetime.fromisoformat(val)
    except (ValueError, TypeError):
        return None


def x__parse_iso__mutmut_9(value: str) -> datetime | None:
    try:
        val = value.replace("Z", "+00:00")
        return datetime.fromisoformat(None)
    except (ValueError, TypeError):
        return None

mutants_x__parse_iso__mutmut['_mutmut_orig'] = x__parse_iso__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_iso__mutmut['x__parse_iso__mutmut_1'] = x__parse_iso__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_iso__mutmut['x__parse_iso__mutmut_2'] = x__parse_iso__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_iso__mutmut['x__parse_iso__mutmut_3'] = x__parse_iso__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_iso__mutmut['x__parse_iso__mutmut_4'] = x__parse_iso__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_iso__mutmut['x__parse_iso__mutmut_5'] = x__parse_iso__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_iso__mutmut['x__parse_iso__mutmut_6'] = x__parse_iso__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_iso__mutmut['x__parse_iso__mutmut_7'] = x__parse_iso__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_iso__mutmut['x__parse_iso__mutmut_8'] = x__parse_iso__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_iso__mutmut['x__parse_iso__mutmut_9'] = x__parse_iso__mutmut_9 # type: ignore # mutmut generated
mutants_x__iso_days_ago__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__iso_days_ago__mutmut)
def _iso_days_ago(days: int) -> str:
    return (datetime.now(UTC) - timedelta(days=days)).isoformat()


def x__iso_days_ago__mutmut_orig(days: int) -> str:
    return (datetime.now(UTC) - timedelta(days=days)).isoformat()


def x__iso_days_ago__mutmut_1(days: int) -> str:
    return (datetime.now(UTC) + timedelta(days=days)).isoformat()


def x__iso_days_ago__mutmut_2(days: int) -> str:
    return (datetime.now(None) - timedelta(days=days)).isoformat()


def x__iso_days_ago__mutmut_3(days: int) -> str:
    return (datetime.now(UTC) - timedelta(days=None)).isoformat()

mutants_x__iso_days_ago__mutmut['_mutmut_orig'] = x__iso_days_ago__mutmut_orig # type: ignore # mutmut generated
mutants_x__iso_days_ago__mutmut['x__iso_days_ago__mutmut_1'] = x__iso_days_ago__mutmut_1 # type: ignore # mutmut generated
mutants_x__iso_days_ago__mutmut['x__iso_days_ago__mutmut_2'] = x__iso_days_ago__mutmut_2 # type: ignore # mutmut generated
mutants_x__iso_days_ago__mutmut['x__iso_days_ago__mutmut_3'] = x__iso_days_ago__mutmut_3 # type: ignore # mutmut generated
