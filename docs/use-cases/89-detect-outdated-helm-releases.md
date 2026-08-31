# 89 — Detect Outdated Helm Releases

Detect Helm releases that are outdated compared to the latest available chart version
by querying installed releases and chart repositories, computing version deltas,
and flagging breaking changes for major upgrades.

## Sample Questions

- "Which Helm releases are out of date compared to the latest available chart version?"
- "Show me all Helm charts that need a version upgrade with changelogs."
- "Are there any major version updates pending that could break our services?"
- "List outdated Helm releases grouped by namespace."
- "What breaking changes should I be aware of before upgrading cert-manager?"

---

## 1. Happy Path

```mermaid
sequenceDiagram
    participant User
    participant MCP as MCP Tool
    participant UC as UseCase
    participant Svc as Service
    participant Engine as HelmOutdatedReleaseEngine
    participant Port as HelmReleaseVersionPort
    participant Adapter as HelmReleaseVersionAdapter
    participant Helm as helm CLI
    participant Repo as Chart Repo

    User->>MCP: detect_outdated_helm_releases()
    MCP->>Svc: DetectOutdatedHelmReleasesService(port)
    MCP->>UC: execute(command)
    UC->>Svc: detect_outdated(command)
    Svc->>Port: list_releases(None)
    Port->>Adapter: list_releases(None)
    Adapter->>Helm: helm list --all-namespaces -o json
    Helm-->>Adapter: [{name: nginx-ingress, chart: nginx-ingress-4.7.1, ...}]
    Adapter-->>Port: list[HelmReleaseRawData]
    Port-->>Svc: releases

    loop For each chart
        Svc->>Port: fetch_latest_version("nginx-ingress")
        Port->>Adapter: fetch_latest_version("nginx-ingress")
        Adapter->>Repo: helm search repo nginx-ingress -o json
        Repo-->>Adapter: {version: "4.10.3"}
        Adapter-->>Port: ChartLatestRawData(version="4.10.3")
        Port-->>Svc: latest
    end

    Svc->>Engine: compute(releases, latest_map)
    Engine->>Engine: _compare_semver("4.7.1", "4.10.3") → "minor"
    Engine-->>Svc: OutdatedHelmReport(outdated=5, up_to_date=3)
    Svc-->>UC: response
    MCP-->>User: outdated=5, up_to_date=3
```

## 2. Error Flows

```mermaid
sequenceDiagram
    participant Adapter as Adapter
    participant Helm as helm CLI
    participant Repo as Chart Repo
    participant Engine as Engine

    alt Helm CLI not installed
        Adapter->>Helm: helm list
        Helm-->>Adapter: FileNotFoundError
        Adapter-->>Engine: raise ComponentNotInstalledError
    else Chart repo unreachable
        Adapter->>Repo: helm search repo
        Repo-->>Adapter: timeout
        Adapter-->>Engine: ChartLatestRawData(repo_error="timeout")
        Engine->>Engine: delta_type="error", skip version check
    else Chart removed from repo
        Adapter->>Repo: helm search repo
        Repo-->>Adapter: no results
        Adapter-->>Engine: ChartLatestRawData(version="")
        Engine->>Engine: delta_type="deprecated"
    end
```

---

## Key Points

- Lists all Helm releases via `helm list --all-namespaces -o json`
- Queries chart repos via `helm search repo` for latest version
- SemVer comparison: major.minor.patch → delta classification
- Major updates always flagged with breaking changes warning
- Pinned releases (annotation `helm.sh/upgrade: skip`) excluded from report
- Chart repo errors return `delta_type="error"` without crashing
- Each chart queried only once (deduplication per chart name)

---

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_minor_delta_detected` | `test_outdated_helm_engine.py` | ✅ |
| `test_major_delta_critical` | `test_outdated_helm_engine.py` | ✅ |
| `test_up_to_date_not_counted_as_outdated` | `test_outdated_helm_engine.py` | ✅ |
| `test_repo_error_marks_as_skipped` | `test_outdated_helm_engine.py` | ✅ |
| `test_pinned_release_excluded` | `test_outdated_helm_engine.py` | ✅ |
| `test_chart_removed_from_repo_deprecated` | `test_outdated_helm_engine.py` | ✅ |
| `test_five_of_eight_outdated` | `test_outdated_helm_engine.py` | ✅ |
| `test_fetches_latest_once_per_chart` | `test_outdated_helm_port_and_service.py` | ✅ |
| `test_detects_minor_outdated_release` | `test_outdated_helm_port_and_service.py` | ✅ |
| `test_delegates_and_returns_dict` | `test_detect_outdated_helm_mcp.py` | ✅ |
| `test_build_helm_release_version_adapter_returns_port` | `tests/unit/test_server.py` | ✅ |

---

## Related Files

- `src/hexawyn/domain/models/outdated_helm.py`
- `src/hexawyn/domain/services/outdated_helm/outdated_helm_engine.py`
- `src/hexawyn/application/ports/driven/helm_release_version_port.py`
- `src/hexawyn/application/ports/driving/detect_outdated_helm_releases/`
- `src/hexawyn/application/service/detect_outdated_helm_releases_service.py`
- `src/hexawyn/application/use_case/detect_outdated_helm_releases/`
- `src/hexawyn/adapters/secondary/gitops/helm_release_version_adapter.py`
- `src/hexawyn/mcp/tools/detect_outdated_helm_releases.py`
- `src/hexawyn/mcp/server.py`
