# 90 — Detect Kustomize Patch Conflicts

Detect conflicting or redundant patches in Kustomize overlay directories
by parsing patch files and identifying fields overwritten by multiple
patches with different or identical values.

## Sample Questions

- "Which Kustomize overlays override the same field across multiple patches?"
- "Are any of my Kustomize patches setting the same field to different values in production?"
- "Show me redundant patches that set values already defined in the base."
- "Which patches target resources that don't exist in my base — flag orphan patches."
- "List all conflicting fields in the production overlay with the winning value."

---

## 1. Happy Path

```mermaid
sequenceDiagram
    participant User
    participant MCP as MCP Tool
    participant UC as UseCase
    participant Svc as Service
    participant Engine as KustomizePatchConflictEngine
    participant Port as KustomizePatchAnalysisPort
    participant Adapter as KustomizeCLIPatchAdapter
    participant CLI as kustomize CLI

    User->>MCP: detect_kustomize_patch_conflicts("overlays/prod")
    MCP->>Svc: DetectKustomizePatchConflictsService(port)
    MCP->>UC: execute(command)
    UC->>Svc: detect_conflicts(command)
    Svc->>Port: extract_patch_fields("overlays/prod")
    Svc->>Port: extract_base_fields("overlays/prod")
    Port->>Adapter: extract_patch_fields()
    Adapter->>CLI: kustomize build overlays/prod
    CLI-->>Adapter: rendered manifests
    Adapter->>Adapter: parse kustomization.yaml patches
    Adapter-->>Port: list[PatchFieldRawData]
    Port-->>Svc: patch fields
    Svc->>Engine: compute(patches, base)
    Engine->>Engine: group by (resource:field_path)
    Engine->>Engine: detect conflicts (different values)
    Engine->>Engine: detect redundancies (same as base)
    Engine-->>Svc: KustomizePatchConflictReport
    MCP-->>User: 3 conflicts, 2 redundancies
```

## 2. Checker Node

```mermaid
sequenceDiagram
    participant Checker as Checker
    participant Engine as Engine

    Checker->>Engine: compute(patches, base)

    alt FAIL — wrong winner
        Engine-->>Checker: patch-a=2, patch-b=5, winner=5 (last)
        Checker->>Checker: verify order: last patch wins
    else FAIL — redundancy not detected
        Engine-->>Checker: base=3, patch=3 → must flag redundant
    else FLAG — orphan patch not flagged
        Engine-->>Checker: patch targets nonexistent resource
    end
```

---

## Key Points

- Groups patches by `(resource, field_path)` key for conflict detection
- Last patch in `kustomization.yaml` order wins (Kustomize linear application)
- Fields with same value across patches are not conflicts (no diverging intent)
- Redundancy: patch sets field to same value as base or earlier patch
- Orphan: patch targets resource not present in base manifests
- JSON6902 vs strategic merge distinguished by `patch_type` field

---

## Related Files

- `src/hexawyn/domain/models/kustomize_patch_conflict.py`
- `src/hexawyn/domain/services/kustomize_patch_conflict/kustomize_patch_conflict_engine.py`
- `src/hexawyn/application/ports/driven/kustomize_patch_analysis_port.py`
- `src/hexawyn/application/ports/driving/detect_kustomize_patch_conflicts/`
- `src/hexawyn/application/service/detect_kustomize_patch_conflicts_service.py`
- `src/hexawyn/application/use_case/detect_kustomize_patch_conflicts/`
- `src/hexawyn/adapters/secondary/gitops/kustomize_patch_adapter.py`
- `src/hexawyn/mcp/tools/detect_kustomize_patch_conflicts.py`
