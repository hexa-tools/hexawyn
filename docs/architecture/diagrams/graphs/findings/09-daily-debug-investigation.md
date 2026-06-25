# Daily Debug — Investigation Pipeline (Wired ✅)

When the user types a debug command like "débogue payments-api", `_debug_pod()` finds the pod then delegates to `_investigate()`, which builds the 9-node LangGraph investigation graph, injects the adapter via `set_adapter()`, and invokes the full pipeline: parse_intent → check_cache → retrieve_context → execute_tool → generate_response → semantic_checker → llm_judge → store_memory → format_response. The LLM (DeepSeek) analyzes the pod and returns a diagnosis with suggestion chips.

```mermaid
sequenceDiagram
    participant User
    participant SS as SessionScreen
    participant CR as CommandRouter
    participant DP as _debug_pod
    participant INV as _investigate
    participant Graph as InvestigationGraph
    participant PI as parse_intent
    participant CC as check_cache
    participant L1 as CacheL1
    participant L2 as DuckDB
    participant RC as retrieve_context
    participant ET as execute_tool
    participant AD as Adapter
    participant K8s as K8s API
    participant GR as generate_response
    participant LLM as LLMService (DeepSeek)
    participant SC as semantic_checker
    participant LJ as llm_judge
    participant SM as store_memory
    participant FR as format_response

    User->>SS: types "débogue payments-api"
    SS->>SS: on_input_submitted (async)
    SS->>SS: _handle_command(text)
    SS->>CR: route_command(text, adapter)

    Note over CR: Keyword detection
    alt debug keywords match
        CR->>DP: _debug_pod(adapter, text)
        DP->>DP: adapter.list_pods() → find matching pod
        alt pod found
            DP->>INV: _investigate(adapter, query, pod)
            INV->>AD: get_cluster_context()
            AD-->>INV: ClusterContext
            INV->>INV: build AgentState { query, cluster_context, ... }
            INV->>INV: set_adapter(adapter)
            INV->>INV: build_investigation_graph()
            INV->>Graph: graph.invoke(initial_state)
        else pod not found
            DP-->>CR: CommandResult ("pod not found")
            CR-->>SS: result
            SS-->>User: "Je n'ai pas trouvé de pod..."
        end
    else pods/logs/pending keywords
        CR->>AD: direct adapter.list_pods() / search_logs()
        AD->>K8s: kubectl / API call
        K8s-->>AD: pod data
        AD-->>CR: CommandResult
        CR-->>SS: result
        SS-->>User: formatted pods/logs/pending
    end

    Note over Graph: Investigation graph (debug path)

    Graph->>PI: run(state) — parse user intent
    Note over PI: intent = "debug", tool_name = "describe_pod"
    PI-->>Graph: ParseIntentOutput { intent, tool_name, tool_args }

    Graph->>CC: run(state) — check cache L1 + L2

    alt L1 cache hit (in-memory, TTL 5min)
        CC->>L1: get(query_hash)
        L1-->>CC: CacheEntry (fresh)
        CC-->>Graph: cache_hit = True
        Graph->>FR: format_response
    else L2 VSS hit (DuckDB, cosine ≥ 0.80)
        CC->>L2: VSS search (embedding)
        L2-->>CC: similar past incident
        CC-->>Graph: cache_hit = True
        Graph->>FR: format_response
    else cache miss
        CC-->>Graph: cache_hit = False
        Graph->>RC: retrieve_context

        RC->>AD: get_cluster_context()
        AD-->>RC: ClusterContext { name, provider, namespace }
        RC-->>Graph: RetrieveContextOutput

        Graph->>ET: execute_tool
        ET->>AD: describe_pod(name, namespace)
        AD->>K8s: kubectl describe pod / API
        K8s-->>AD: pod details (CrashLoopBackOff, OOM, events)
        AD-->>ET: tool output
        ET-->>Graph: ExecuteToolOutput { raw_data }

        Graph->>GR: generate_response
        GR->>LLM: system_prompt + tool_output
        LLM-->>GR: "payments-api en CrashLoopBackOff — OOMKilled: 380Mi, limit=256Mi"
        GR-->>Graph: GenerateResponseOutput

        loop retry ≤ 3 times
            Graph->>SC: semantic_checker (deterministic)
            alt PASS
                SC-->>Graph: verdict = PASS
                Graph->>LJ: llm_judge (LLM validation)
                alt PASS
                    LJ-->>Graph: verdict = PASS
                    Graph->>SM: store_memory
                    SM->>L2: INSERT INTO incidents + L1 cache set
                    L2-->>SM: stored
                    SM-->>Graph: stored
                    Graph->>FR: format_response
                else FAIL
                    LJ-->>Graph: verdict = FAIL
                    Note over Graph: retry_count += 1
                else DEGRADED
                    LJ-->>Graph: verdict = DEGRADED
                    Graph->>FR: format_response [UNVERIFIED]
                end
            else FAIL | BLOCKED
                SC-->>Graph: verdict = FAIL | BLOCKED
                alt retry_count < 3
                    Note over Graph: retry → generate_response
                else max retries reached
                    Graph->>FR: format_response [DEGRADED]
                end
            end
        end
    end

    FR->>FR: format_result()
    Note over FR: CommandResult { lines[], chips[], summary }
    FR-->>Graph: FormatResponseOutput
    Graph-->>CR: CommandResult
    CR-->>SS: result

    SS->>SS: _render_result(log, result)
    SS->>SS: _update_chips(result.chips)
    SS->>SS: _refresh_aside()
    SS-->>User: [RichLog] réponse + [suggestion chips]
```

## Key Points

- Debug commands route through `_debug_pod()` → `_investigate()` → 9-node investigation graph with LLM
- `_investigate()` builds `AgentState`, calls `set_adapter(adapter)`, then `graph.invoke()`
- The adapter is injected into LangGraph via `set_adapter()` so nodes can access K8s API
- Pods/logs/pending commands still use direct adapter calls (fast path, no LLM)
- Cache L1 (in-memory, TTL 5min) checked first — hit skips LLM entirely
- Cache L2 (DuckDB VSS, cosine ≥ 0.80) checked second — hit reuses past analysis
- The LLM is called twice: `generate_response` (main analysis) and `llm_judge` (semantic validation)
- Retry loop: up to 3 retries if `semantic_checker` or `llm_judge` returns FAIL
- BLOCKED stops the pipeline immediately (hard stop, no retries)
- DEGRADED skips `store_memory` and returns with `[UNVERIFIED]` label
- Successful investigation stores result in DuckDB and populates L1 cache for future reuse

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_investigation_graph_compiles` | `tests/unit/test_investigation_graph.py` | ✅ |
| `test_debug_keyword_routes_to_graph` | `tests/unit/test_investigation_graph.py` | ✅ |
| `test_cache_hit_returns_early` | `tests/unit/test_investigation_graph.py` | ✅ |
| `test_cache_miss_proceeds` | `tests/unit/test_investigation_graph.py` | ✅ |
| `test_checker_pass_triggers_judge` | `tests/unit/test_investigation_graph.py` | ✅ |
| `test_checker_fail_retries` | `tests/unit/test_investigation_graph.py` | ✅ |
| `test_max_retries_triggers_degraded` | `tests/unit/test_investigation_graph.py` | ✅ |
| `test_blocked_triggers_hard_stop` | `tests/unit/test_investigation_graph.py` | ✅ |
| `test_judge_pass_stores_memory` | `tests/unit/test_investigation_graph.py` | ✅ |
| `test_l1_hit_returns_cache_hit_true` | `tests/unit/test_check_cache_node.py` | ✅ |
| `test_semantic_checker_pass` | `tests/unit/test_semantic_checker.py` | ❌ (TBD) |

## Related Files

- `src/hexawyn/cli/command_router.py` — `_debug_pod()` → `_investigate()` → graph.invoke()
- `src/hexawyn/cli/tui.py` — SessionScreen._handle_command() → _render_result() + _update_chips()
- `src/hexawyn/lang_graph/graphs/findings/investigation_graph.py` — 9-node graph with conditional edges
- `src/hexawyn/lang_graph/services/k8s_service.py` — set_adapter() injects adapter into nodes
- `src/hexawyn/lang_graph/nodes/parse_intent.py` — LLM intent detection
- `src/hexawyn/lang_graph/nodes/check_cache.py` — L1 + L2 cache check
- `src/hexawyn/lang_graph/nodes/retrieve_context.py` — cluster context
- `src/hexawyn/lang_graph/nodes/execute_tool.py` — kubectl / API calls via adapter
- `src/hexawyn/lang_graph/nodes/generate_response.py` — LLM response generation
- `src/hexawyn/lang_graph/nodes/semantic_checker.py` — deterministic validation
- `src/hexawyn/lang_graph/nodes/llm_judge.py` — LLM semantic validation
- `src/hexawyn/lang_graph/nodes/store_memory.py` — DuckDB insert + L1 populate
- `src/hexawyn/lang_graph/nodes/format_response.py` — formatted output + chips
- `src/hexawyn/lang_graph/services/llm_service.py` — OpenAI-compatible LLM client
