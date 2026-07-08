from __future__ import annotations

from hexawyn.domain.models.kustomize_patch_conflict import (
    KustomizePatchConflictReport,
    PatchConflict,
    PatchRedundancy,
    PatchValue,
)


class KustomizePatchConflictEngine:
    def compute(
        self,
        patches: list[dict[str, object]],
        base_fields: list[dict[str, object]],
    ) -> KustomizePatchConflictReport:
        report = KustomizePatchConflictReport()

        conflict_map: dict[str, list[dict[str, object]]] = {}
        for p in patches:
            key = _field_key(p)
            if key not in conflict_map:
                conflict_map[key] = []
            conflict_map[key].append(p)

        base_map: dict[str, str] = {}
        for b in base_fields:
            base_map[_field_key(b)] = str(b.get("value", ""))

        for key, group in conflict_map.items():
            group.sort(key=lambda x: _as_int_for_sort(x.get("order")))

            values_seen: dict[str, list[dict[str, object]]] = {}
            for p in group:
                v = str(p.get("value", ""))
                if v not in values_seen:
                    values_seen[v] = []
                values_seen[v].append(p)

            unique_values = list(values_seen.keys())
            if len(unique_values) > 1:
                last_patch = group[-1]
                effective = str(last_patch.get("value", ""))
                field_path = str(group[0].get("field_path", ""))
                resource = str(group[0].get("resource", ""))

                conflict_values = [
                    PatchValue(
                        source_file=str(p.get("source_file", "")),
                        value=str(p.get("value", "")),
                        patch_type=str(p.get("patch_type", "strategic_merge")),
                    )
                    for p in group
                ]

                report.patch_conflicts.append(
                    PatchConflict(
                        field_path=field_path,
                        resource=resource,
                        conflicting_values=conflict_values,
                        effective_value=effective,
                        severity="warning",
                    )
                )
                report.total_conflicts += 1

            base_val = base_map.get(key)
            for p in group:
                v = str(p.get("value", ""))
                if base_val is not None and v == base_val:
                    report.patch_redundancies.append(
                        PatchRedundancy(
                            field_path=str(p.get("field_path", "")),
                            resource=str(p.get("resource", "")),
                            base_value=base_val,
                            patch_value=v,
                            source_file=str(p.get("source_file", "")),
                            severity="informational",
                        )
                    )
                    report.total_redundancies += 1
                else:
                    for earlier in group:
                        if earlier is p:
                            break
                        if str(earlier.get("value", "")) == v:
                            report.patch_redundancies.append(
                                PatchRedundancy(
                                    field_path=str(p.get("field_path", "")),
                                    resource=str(p.get("resource", "")),
                                    base_value="",
                                    patch_value=v,
                                    source_file=str(p.get("source_file", "")),
                                    severity="informational",
                                )
                            )
                            report.total_redundancies += 1
                            break

        base_resources: set[str] = {str(b.get("resource", "")) for b in base_fields}
        for p in patches:
            src = str(p.get("source_file", ""))
            res = str(p.get("resource", ""))
            if res and res not in base_resources and src not in report.orphan_patches:
                report.orphan_patches.append(src)

        return report


def _field_key(patch: dict[str, object]) -> str:
    return f"{patch.get('resource', '')}:{patch.get('field_path', '')}"


def _as_int_for_sort(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0
