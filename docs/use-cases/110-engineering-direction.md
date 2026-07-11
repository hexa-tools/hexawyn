# Use Case 110 — Direction Engineering (Night Interventions + Disruption Risks)

Deux use cases pour un Head of Engineering : charge d'astreinte nocturne et
prédiction des risques de rupture de service.

## Slice 1 — Night Intervention Load
- Tool: `report_night_interventions`
- Calcule la moyenne d'interventions par nuit et la tendance vs trimestre précédent.
- Formule vérifiable par checker : `(current - previous) / previous x 100`.

## Slice 2 — Disruption Risk Prediction
- Tool: `check_disruption_risks`
- Liste les risques de rupture dans les N prochains jours (défaut 7).
- Chaque risque porte un `business_service_name` (pas de nom technique).
- Aucun risque = "Aucun risque de rupture identifié".

## Related Files
19 fichiers source · 100% coverage · `docs/use-cases/110-engineering-direction.md`
