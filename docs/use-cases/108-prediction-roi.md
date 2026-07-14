# Use Case 108 — Prediction ROI (Business Impact Slice 2)

Answers: "How much did we save thanks to predictions this month?"

Computes the return on investment of automatic predictions: each detection that
resulted in an avoided incident generates an avoided cost (avoided downtime ×
revenue_per_minute), from which the infrastructure cost is subtracted. Only
genuinely avoided incidents (flag `prevented=True`) count, and every euro is
traceable to the reference historical event.

## Sample Questions

- "How much did we save thanks to predictions this month?"
- "What is the ROI of the automatic alerts?"
- "How many potential incidents did we detect and avoid?"
- "Show me the losses avoided thanks to Hexawyn this month."
- "How much did predictions save us this month?"

## Key Points

- **Only detections with `prevented=True`** generate an avoided cost.
- **Without `revenue_per_minute`** no amount is produced.
- **ROI = Σ avoided costs − infrastructure cost**.
- Each avoided incident references a historical `incident_ref`.

## Related Files (12)

`src/hexawyn/domain/models/prediction_roi.py` · `src/hexawyn/domain/services/prediction_roi/prediction_roi_calculator.py` · `src/hexawyn/application/ports/driven/prediction_roi_port.py` · `src/hexawyn/application/ports/driving/compute_prediction_roi/` · `src/hexawyn/application/service/compute_prediction_roi_service.py` · `src/hexawyn/application/use_case/compute_prediction_roi/compute_prediction_roi_use_case.py` · `src/hexawyn/adapters/secondary/gitops/prediction_roi_adapter.py` · `src/hexawyn/adapters/secondary/gitops/prediction_roi_source.py` · `src/hexawyn/mcp/tools/compute_prediction_roi.py` · `src/hexawyn/mcp/server.py`
