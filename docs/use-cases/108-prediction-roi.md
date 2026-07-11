# Use Case 108 — Prediction ROI (Business Impact Slice 2)

Répond à : « Combien avons-nous économisé grâce aux prédictions ce mois-ci ? »

Calcule le retour sur investissement des prédictions automatiques : chaque
détection ayant abouti à un incident évité génère un coût évité (downtime évité ×
revenue_per_minute), auquel on soustrait le coût d'infrastructure. Seuls les
incidents réellement évités (flag preveted=True) comptent, et chaque euro est
traçable à l'événement historique de référence.

## Sample Questions

- « Combien avons-nous économisé grâce aux prédictions ce mois-ci ? »
- « Quel est le ROI des alertes automatiques ? »
- « Combien d'incidents potentiels avons-nous détectés et évités ? »
- « Montre-moi les pertes évitées grâce à Hexawyn ce mois. »
- « How much did predictions save us this month? »

## Key Points

- **Seulement les détections avec preveted=True** génèrent un coût évité.
- **Sans revenue_per_minute** aucun montant n'est produit.
- **ROI = Σ coûts évités − coût infrastructure**.
- Chaque incident évité référence un `incident_ref` historique.

## Related Files (12)

`src/hexawyn/domain/models/prediction_roi.py` · `src/hexawyn/domain/services/prediction_roi/prediction_roi_calculator.py` · `src/hexawyn/application/ports/driven/prediction_roi_port.py` · `src/hexawyn/application/ports/driving/compute_prediction_roi/` · `src/hexawyn/application/service/compute_prediction_roi_service.py` · `src/hexawyn/application/use_case/compute_prediction_roi/compute_prediction_roi_use_case.py` · `src/hexawyn/adapters/secondary/gitops/prediction_roi_adapter.py` · `src/hexawyn/adapters/secondary/gitops/prediction_roi_source.py` · `src/hexawyn/mcp/tools/compute_prediction_roi.py` · `src/hexawyn/mcp/server.py`
