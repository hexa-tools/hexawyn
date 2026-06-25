# CLI Launch — Startup Graph Pipeline

When the user launches `hexa start`, the app checks LLM configuration, loads the kubeconfig, runs the 12-node LangGraph startup pipeline to scan the cluster, then opens the Textual TUI with the scan results. The LLM is called only once at the end (generate_suggestions) with graceful degradation if unavailable.

```mermaid
sequenceDiagram
    participant User
    participant CLI as hexa start
    participant App as HexawynApp
    participant Config as ConfigManager
    participant KR as KubeconfigReader
    participant AF as AdapterFactory
    participant KG as LangGraph
    participant K8s as K8s API
    participant LLM as LLMService (DeepSeek/OpenAI)
    participant TUI as HexawynTUI
    participant SS as SessionScreen

    User->>CLI: hexa start
    CLI->>App: run()

    Note over App,Config: Step 1 — LLM config
    App->>Config: _load_api_key_to_env()
    Config->>Config: get_llm_config() → ~/.hexawyn/config.yaml
    Config-->>App: has_key = true | false

    alt no API key and not demo mode
        App->>TUI: _run_tui(needs_setup=True)
        TUI->>TUI: push_screen(WelcomeScreen)
        TUI->>TUI: push_screen(ProviderSetupScreen)
        Note over TUI: User configures provider
        TUI-->>User: [dismissed → WelcomeScreen]
    end

    Note over App,KR: Step 2 — Kubeconfig
    App->>KR: context_service.startup_status()
    KR->>KR: load_kubeconfig()
    Note over KR: KUBECONFIG env var (filter empty files)
    KR->>K8s: config.load_kube_config()
    K8s-->>KR: CoreV1Api client
    KR-->>App: KubernetesStartupStatus

    Note over App,AF: Step 3 — Adapter
    App->>AF: build_adapters(cluster_name)
    Note over AF: Cloud auto-detection (eks/aks/gke/vanilla)
    AF-->>App: adapter (AWSAdapter | AzureAdapter | VanillaAdapter)

    Note over App,KG: Step 4 — Startup scan (12-node LangGraph)

    App->>KG: build_startup_graph()
    App->>KG: graph.invoke({cluster_name})

    activate KG
    KG->>K8s: load_pods → list_pod_for_all_namespaces()
    K8s-->>KG: PodInfo[]
    KG->>K8s: load_nodes → list_node()
    K8s-->>KG: node names[]

    KG->>KG: detect_provider (deterministic, no LLM)

    par 9 parallel detectors (deterministic)
        KG->>KG: detect_crashloop
        KG->>KG: detect_pending_pod
        KG->>KG: detect_image_pull
        KG->>KG: detect_oomkilled
        KG->>KG: detect_high_restart
        KG->>KG: detect_node_not_ready
        KG->>KG: detect_pvc_pending
        KG->>KG: detect_tls_expiration
        KG->>KG: detect_failed_deployment
    end

    KG->>KG: aggregate_findings (dedup + sort)
    KG->>KG: compute_cluster_summary (pod/node counts)

    KG->>LLM: generate_suggestions (system_prompt + findings JSON)
    alt LLM available
        LLM-->>KG: narrative_summary, top_issues, suggestions[]
    else LLM unavailable or error
        Note over KG: degraded → raw findings, health_score deterministic
        KG-->>KG: degraded=True
    end
    deactivate KG

    KG-->>App: StartupState { health_score, narrative_summary, top_issues, suggestions, findings }

    Note over App,TUI: Step 5 — Open TUI
    App->>TUI: HexawynTUI(adapter, startup_result, ...)
    TUI->>TUI: on_mount → push_screen(WelcomeScreen)
    TUI->>TUI: push_screen(SessionScreen)
    TUI->>SS: on_mount

    SS->>SS: Logo banner + startup lines
    SS->>SS: Context info (cluster, namespace, warnings)

    alt startup_result present
        SS->>SS: _render_startup_result(log, startup_result)
        SS-->>User: Health Score (color-coded) + narrative_summary
        SS-->>User: Top Issues list
        alt degraded mode
            SS-->>User: "⚠ DEGRADED (LLM unavailable)"
        end
        SS->>SS: Merge startup suggestions into chips
    end

    SS-->>User: Suggestion chips + "Essaie : liste les pods…"
```

## Key Points

- LLM is configured BEFORE kubeconfig — if no key and not demo, the ProviderSetupScreen is shown first
- The startup graph has 12 nodes but only ONE calls the LLM (generate_suggestions)
- All 9 detectors are deterministic (regex-based, no AI) and run in parallel after provider detection
- If the LLM is unavailable, the graph enters `degraded` mode — health score is computed deterministically and raw findings are shown
- Kubeconfig empty files (0 bytes) are filtered out before loading to avoid `ConfigException`
- startup_result is rendered immediately in SessionScreen via `_render_startup_result()` — health score (color-coded), narrative, top issues

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_startup_graph_compiles` | `tests/unit/test_startup_graph.py` | ✅ |
| `test_startup_graph_run_with_vanilla_adapter` | `tests/unit/test_startup_graph.py` | ✅ |
| `test_load_pods_node` | `tests/unit/test_startup_graph.py` | ✅ |
| `test_detect_provider_vanilla` | `tests/unit/test_detect_provider.py` | ✅ |
| `test_degraded_when_llm_unavailable` | `tests/unit/test_startup_graph.py` | ✅ |
| `test_kubeconfig_filters_empty_files` | `tests/unit/test_kubeconfig_reader.py` | ❌ (TBD) |

## Related Files

- `src/hexawyn/cli/app.py` — HexawynApp.run() orchestrates startup
- `src/hexawyn/lang_graph/graphs/cli_launch/startup_graph.py` — 12-node graph definition
- `src/hexawyn/lang_graph/nodes/generate_startup_suggestions.py` — only LLM call
- `src/hexawyn/lang_graph/services/llm_service.py` — OpenAI-compatible LLM client
- `src/hexawyn/infrastructure/config/kubeconfig_reader.py` — kubeconfig loading (filters empty files)
- `src/hexawyn/infrastructure/config/config_manager.py` — LLM config from ~/.hexawyn/
- `src/hexawyn/adapters/secondary/adapter_factory.py` — cloud auto-detection
- `src/hexawyn/cli/tui.py` — SessionScreen._render_startup_result() displays scan output
