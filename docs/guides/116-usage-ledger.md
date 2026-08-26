# Use Case 116 — Usage Ledger: Investigation Audit Trail

## Sample Questions

- "How many investigations did I run this month?"
- "Which tools consume the most SLM time?"
- "What's my average investigation duration this week?"
- "How many tokens did the SLM consume last month across all investigations?"
- "Show me my monthly usage report for July 2026"

---

Every investigation executed by `ChatCliService` is recorded in an append-only JSONL ledger (`.hexawyn/usage.jsonl`). The flow goes through: ChatCliService → UsageLedger (best-effort, never blocks the investigation). Token usage data originates from the control-plane `LLMService.last_usage` and is carried through `InvestigationOutput.usage` back to the CLI. The ledger supports read-back with time and tool filters, aggregate stats over N days, and monthly reports grouped by day.

### Flow 1 — Happy Path: Record Usage After Investigation

```mermaid
sequenceDiagram
    participant User as User
    participant CLI as ChatCliService
    participant RT as HttpRuntimeAdapter
    participant CP as Control-Plane
    participant LLM as LLMService (Ollama)
    participant UL as UsageLedger

    User->>CLI: "why is payments-api OOM?"

    Note over CLI: start = time.monotonic()

    CLI->>RT: run_investigation(query, context)
    RT->>CP: POST /api/v1/investigations/stream
    CP->>LLM: llm.generate(prompt)
    LLM->>LLM: POST /api/generate {model, prompt, stream:false}
    LLM-->>LLM: response + {prompt_eval_count:450, eval_count:180}
    Note over LLM: llm_service._last_usage = {prompt_tokens:450, completion_tokens:180, ...}
    LLM-->>CP: "OOM detected — memory limit 256Mi insufficient"
    CP-->>RT: InvestigationOutput {answer, status, usage:{prompt_tokens:450, ...}}
    RT-->>CLI: InvestigationOutput

    Note over CLI: duration_ms = (now - start) * 1000<br/>usage = output["usage"]

    CLI->>UL: record(InvestigationUsage{query, tool, verdict, duration_ms, tokens, model, provider})
    UL->>UL: append to .hexawyn/usage.jsonl

    CLI-->>User: "OOM detected — raise memory limit to 512Mi"
```

### Flow 2 — Read: Stats and Monthly Report

```mermaid
sequenceDiagram
    participant User as User / Dashboard
    participant UL as UsageLedger
    participant FS as .hexawyn/usage.jsonl

    User->>UL: stats(days=30)

    UL->>FS: read_all() — parse JSONL lines
    FS-->>UL: [entry, entry, entry, ...]

    Note over UL: compute aggregates:<br/>total_investigations, total_tokens,<br/>avg_duration_ms, top_tools,<br/>verdict_distribution, models_used

    UL-->>User: UsageStats {47 investigations, 18,400 tokens, avg 4.2s,<br/>top: crashloop_detector 15x, models: qwen3:8b 47x}

    User->>UL: monthly_report(2026, 7)

    UL->>FS: read_all(since="2026-07-01")
    FS-->>UL: [filtered entries]

    Note over UL: group by date → DailyStats per day<br/>compute monthly aggregates

    UL-->>User: MonthlyReport {year:2026, month:7, stats,<br/>daily_breakdown: [31 days]}
```

### Flow 3 — Error: Best-Effort (Ledger Never Blocks)

```mermaid
sequenceDiagram
    participant CLI as ChatCliService
    participant RT as RuntimeAdapter
    participant UL as UsageLedger
    participant FS as Disk

    CLI->>RT: run_investigation(query)
    RT-->>CLI: InvestigationOutput (success)

    CLI->>UL: record(usage)
    UL->>FS: open("usage.jsonl", "a")

    alt Disk Full
        FS-->>UL: OSError("no space left on device")
        Note over UL,CLI: Exception caught silently<br/>investigation result is returned to user
    else File Permissions
        FS-->>UL: PermissionError
        Note over UL,CLI: Best-effort — never blocks the user
    else JSONL Line Corruption (on read)
        FS-->>UL: json.JSONDecodeError on line N
        Note over UL: skip corrupted line, continue reading
    end

    CLI-->>CLI: return response to user (unaffected)
```

### Flow 4 — Token Tracking: Control-Plane LLMService → CLI UsageLedger

```mermaid
sequenceDiagram
    participant CP as Control-Plane (hexa-control-plane)
    participant LLM as LLMService
    participant Ollama as Ollama /api/generate
    participant RP as Reporter Node
    participant CLI as hexawyn CLI

    Note over CP: Investigation starts

    CP->>LLM: generate(prompt, system_prompt)

    alt Ollama Provider
        LLM->>Ollama: POST /api/generate {model, prompt, stream:false}
        Ollama-->>LLM: {response, prompt_eval_count:42, eval_count:18}
        Note over LLM: self._last_usage = {prompt_tokens:42, completion_tokens:18,<br/>total_tokens:60, model:"qwen3:8b", provider:"ollama"}
    else OpenAI-compatible Provider
        LLM-->>LLM: POST /chat/completions
        Note over LLM: parse response["usage"] {prompt_tokens, completion_tokens, total_tokens}
    end

    LLM-->>CP: response_text (str, backward-compat)

    CP->>RP: include llm_service.last_usage in report output
    RP-->>CP: InvestigationOutput {..., usage: {prompt_tokens:42, ...}}

    CP-->>CLI: HTTP stream → report node → usage dict

    Note over CLI: HttpRuntimeAdapter extracts usage<br/>from report_output["usage"]
    CLI->>CLI: record in usage.jsonl
```

## Key Points

- **Append-only JSONL** — one line per investigation, human-readable, grep-friendly. No database required.
- **Best-effort** — the ledger never blocks or crashes an investigation. Disk full, permission errors, JSON corruption are all caught silently.
- **Token tracking via `LLMService.last_usage`** — the control-plane LLM service now stores usage metadata on every `generate()` call. Ollama `prompt_eval_count`+`eval_count`, OpenAI-compatible `usage` field.
- **Backward-compat** — `LLMService.generate()` still returns `str`. The `last_usage` property is read separately by the caller (Reporter node) when assembling `InvestigationOutput`.
- **`InvestigationOutput.usage`** — new optional dict field (`{prompt_tokens, completion_tokens, total_tokens, model, provider}`). Absent or empty means no LLM was called (e.g. `list_pods`).
- **Monthly rotation** — the ledger supports reading by date range, and a future rotation mechanism (one file per month) will handle files > 100k lines.
- **Stats aggregation** — `stats(days)` computes total investigations, tokens, duration, top tools, verdict distribution, and models used. `monthly_report(year, month)` adds daily breakdown.
- **FinOps transparency** — the ledger is not for billing (SLM local + abonnement fixe) but for monitoring, debugging performance regressions, and monthly usage transparency.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_required_fields` | `tests/unit/test_usage.py` | ✅ |
| `test_namespace_can_be_none` | `tests/unit/test_usage.py` | ✅ |
| `test_zero_tokens_for_non_llm_investigation` | `tests/unit/test_usage.py` | ✅ |
| `test_empty_stats` | `tests/unit/test_usage.py` | ✅ |
| `test_record_writes_line_to_file` | `tests/unit/test_usage_ledger.py` | ✅ |
| `test_record_creates_parent_directories` | `tests/unit/test_usage_ledger.py` | ✅ |
| `test_record_appends_multiple_entries` | `tests/unit/test_usage_ledger.py` | ✅ |
| `test_read_all_returns_entries` | `tests/unit/test_usage_ledger.py` | ✅ |
| `test_read_all_since_filters_by_timestamp` | `tests/unit/test_usage_ledger.py` | ✅ |
| `test_read_all_tool_filter` | `tests/unit/test_usage_ledger.py` | ✅ |
| `test_read_all_skips_corrupted_lines` | `tests/unit/test_usage_ledger.py` | ✅ |
| `test_stats_computes_aggregates` | `tests/unit/test_usage_ledger.py` | ✅ |
| `test_stats_top_tools_sorted_by_count` | `tests/unit/test_usage_ledger.py` | ✅ |
| `test_monthly_report_groups_by_day` | `tests/unit/test_usage_ledger.py` | ✅ |
| `test_records_usage_after_investigation` | `tests/unit/test_chat_cli_service.py` | ✅ |
| `test_no_ledger_is_safe` | `tests/unit/test_chat_cli_service.py` | ✅ |
| `test_ledger_exception_does_not_block_investigation` | `tests/unit/test_chat_cli_service.py` | ✅ |
| `test_ollama_generate_tracks_usage` | `tests/unit/test_llm_service.py` (hexa-control-plane) | ✅ |
| `test_openai_generate_tracks_usage` | `tests/unit/test_llm_service.py` (hexa-control-plane) | ✅ |
| `test_last_usage_reset_on_error` | `tests/unit/test_llm_service.py` (hexa-control-plane) | ✅ |

## Related Files

- `src/hexawyn/domain/models/usage.py` — InvestigationUsage, UsageStats, DailyStats, MonthlyReport TypedDicts/dataclasses
- `src/hexawyn/application/ports/driven/usage_ledger_port.py` — UsageLedgerPort ABC
- `src/hexawyn/infrastructure/monitoring/usage_ledger.py` — UsageLedger (JSONL append-only implementation)
- `src/hexawyn/application/ports/driven/runtime_port.py` — InvestigationOutput (added `usage` field)
- `src/hexawyn/application/service/chat_cli_service.py` — ChatCliService (UsageLedger injection + _record_usage)
- `src/hexawyn/application/service/http_runtime_adapter.py` — HttpRuntimeAdapter (extracts usage from report output)
- `src/hexawyn/application/service/runtime_adapter.py` — StubRuntimeAdapter (usage={})
- `src/hexawyn/lang_graph/services/llm_service.py` (hexa-control-plane) — LLMService.last_usage, LLMUsageInfo TypedDict
