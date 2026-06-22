# Demo Mode — Mock Adapter, No Quota

HEXAWYN_DEMO_MODE=true activates DemoAdapter. No real K8s API calls are made, no quota is consumed, and all data comes from pre-built scenario files. Perfect for demos, testing, and evaluation without a cluster.

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant AF as AdapterFactory
    participant DemoAdapter
    participant Scenario as Scenario File
    participant parse_intent
    participant execute_tool
    participant generate_response
    participant LLM
    participant store_memory
    participant format_response

    User->>CLI: make run-demo-aws

    Note over CLI: HEXAWYN_DEMO_MODE=true<br/>HEXAWYN_DEMO_SCENARIO=aws_eks

    CLI->>AF: build_adapters("test-cluster")
    Note over AF: DEMO_MODE=true → DemoAdapter
    AF->>DemoAdapter: DemoAdapter(scenario="aws_eks")
    DemoAdapter->>Scenario: load AWS_EKS_SCENARIO
    Scenario-->>DemoAdapter: health=76, pods, findings, chips
    AF-->>CLI: DemoAdapter instance

    User->>CLI: types question
    CLI->>parse_intent: query

    Note over parse_intent: [DEMO] quota check SKIPPED
    parse_intent-->>CLI: intent + tool_name

    CLI->>execute_tool: tool_name + args
    execute_tool->>DemoAdapter: list_pods(), get_findings(), etc.

    Note over DemoAdapter,Scenario: No real K8s API calls<br/>All data from scenario dict

    DemoAdapter->>Scenario: read pre-built data
    Scenario-->>DemoAdapter: mock pods, metrics, findings
    DemoAdapter-->>execute_tool: mock data
    execute_tool-->>CLI: tool output

    CLI->>generate_response: scenario data
    generate_response->>LLM: prompt + mock data
    LLM-->>generate_response: response
    generate_response-->>CLI: llm_response

    CLI->>store_memory: result + embedding

    Note over store_memory: [DEMO] quota increment SKIPPED

    store_memory-->>CLI: stored (no quota consumed)

    CLI->>format_response: result + chips
    format_response-->>CLI: formatted response

    CLI-->>User: response (no quota counter)
```

## Key Points

- Demo mode is activated by the single env var `HEXAWYN_DEMO_MODE=true` — checked at AdapterFactory and LangGraph nodes
- 5 pre-built scenarios: aws_eks (score 76), azure_aks (98), gcp_gke (84), openshift (71), datadog (79)
- Demo mode bypasses ALL quota operations — investigations are never counted against the monthly limit
- No real K8s API calls are made — all data comes from scenario Python files in `adapters/secondary/mock/scenarios/`
- LLM is still called with mock data — realistic responses with zero infrastructure cost
