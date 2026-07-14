# Use Case 110 — Engineering Direction (Night Interventions + Disruption Risks)

Two use cases for a Head of Engineering: nightly on-call load and service
disruption risk prediction.

## Slice 1 — Night Intervention Load
- Tool: `report_night_interventions`
- Computes the average number of interventions per night and the trend vs the previous quarter.
- Checker-verifiable formula: `(current - previous) / previous x 100`.

## Slice 2 — Disruption Risk Prediction
- Tool: `check_disruption_risks`
- Lists disruption risks in the next N days (default 7).
- Each risk carries a `business_service_name` (no technical name).
- No risk = "No disruption risk identified".

## Related Files
19 source files · 100% coverage · `docs/use-cases/110-engineering-direction.md`
