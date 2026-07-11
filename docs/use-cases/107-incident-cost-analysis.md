# Use Case 107 — Analyse du coût d'un incident (Business Impact)

Répond à : *« Combien nous a coûté la panne d'hier ? »* — pour un CFO / décideur
financier, en langage métier, avec un montant **déterministe, traçable et jamais
inventé**.

Traduit la durée d'indisponibilité d'un incident en impact financier à partir de
paramètres business configurables (`revenue_per_minute`, `support_cost_per_hour`,
`sla_penalty_per_hour`). Chaque euro est reproductible et expose sa formule et ses
sources sur demande. Sans configuration de revenu, aucun montant n'est produit —
une explication est renvoyée à la place.

Premier slice de l'épopée « Business Impact & Financial Intelligence » (socle
config business + Incident Cost). Prediction ROI et Budget Intelligence
réutiliseront ce socle dans des tickets suivants.

## Sample Questions

- « Combien nous a coûté la panne d'hier ? »
- « Quel a été l'impact financier de l'incident du service Paiement ? »
- « Combien de chiffre d'affaires avons-nous perdu pendant l'indisponibilité ? »
- « Comment ce montant a-t-il été calculé ? »
- « Quel est le coût métier de l'incident de ce matin ? »

## 1. Happy Path — chaîne hexagonale complète

```mermaid
sequenceDiagram
    participant CFO
    participant MCP as MCP Tool<br/>(analyze_incident_cost)
    participant UC as UseCase
    participant Svc as Service applicatif
    participant Domain as Domaine<br/>(incident_cost_calculator)
    participant Port as Driven Port<br/>(IncidentCostPort)
    participant Facade as Adapter Facade
    participant Sources as incident + config business

    CFO->>MCP: analyze_incident_cost(incident_ref="yesterday")
    MCP->>Svc: build service(port=facade)
    MCP->>UC: execute(command)
    UC->>Svc: analyze(command)
    Svc->>Port: get_incident_cost_data("yesterday")
    Port->>Facade: get_incident_cost_data(...)
    Facade->>Sources: durée + services impactés + config business (ou null)
    Sources-->>Svc: IncidentCostData
    Svc->>Domain: compute_incident_cost(data)
    Domain->>Domain: revenue = downtime x revenue_per_minute
    Domain->>Domain: + support_cost + sla_penalty (si configurés)
    Domain->>Domain: calculation_basis (formule + config + sources)
    Domain-->>Svc: IncidentCostReport
    Svc-->>MCP: Response(report)
    MCP-->>CFO: « Service Paiement indisponible 27 min. 13 500 € affectés. »
```

## 2. Business Impact Graph (pourquoi ça compte)

```mermaid
flowchart TD
    A[Saturation CPU] --> B[Service Paiement ralenti]
    B --> C[Latence du paiement augmentée]
    C --> D[Taux de conversion en baisse]
    D --> E[Impact chiffre d'affaires estimé]
    E --> F["13 500 €"]
```

## 3. Checker Node — validations LLM (anti-hallucination financière)

```mermaid
sequenceDiagram
    participant Gen as generate_response
    participant Checker as checker_node / semantic_layer
    participant Domain as montant autoritaire du domaine
    participant Format as format_response

    Gen->>Checker: réponse LLM + IncidentCostReport
    alt Hallucination financière (revenue_per_minute null mais montant affiché)
        Checker->>Domain: config_available == false ⇒ aucun euro autorisé
        Checker->>Gen: FAIL
    else Arithmétique incorrecte (27 x 500 != montant affiché)
        Checker->>Domain: total = downtime x revenue_per_minute (+ support + sla)
        Checker->>Gen: FAIL
    else Vocabulaire technique (pod / deployment / node)
        Checker->>Checker: détecte termes k8s interdits
        Checker->>Gen: FAIL → remplacer par nom de service métier
    else Explication demandée (« comment est-ce calculé ? »)
        Checker->>Format: expose calculation_basis (formule + config + sources)
    else PASS
        Checker->>Format: réponse validée
    end
```

## 4. DuckDB Memory (traçabilité & reproductibilité)

```mermaid
sequenceDiagram
    participant MCP as MCP Tool
    participant DuckDB
    participant Svc as Service

    MCP->>DuckDB: récupère l'incident historique (durée, services)
    alt incident enregistré
        DuckDB-->>Svc: 27 min, 3 services, résolu 14h23
    else pas d'incident
        DuckDB-->>Svc: durée 0 (rien à facturer)
    end
    Svc->>DuckDB: stocke le calcul (montant + basis) pour reproductibilité
    alt DuckDB indisponible
        Svc-->>Svc: mode dégradé — pas de persistance, jamais de crash
    end
```

## Key Points

- **Formule déterministe** : `downtime_minutes × revenue_per_minute + support_cost
  + sla_penalty`. Le résultat est reproductible et vérifiable par le checker.
- **Jamais de valeur inventée** : sans `revenue_per_minute`, `total_cost_eur`
  reste `None` et une explication est renvoyée (« Configurez revenue_per_minute »).
- **Traçabilité** : `calculation_basis` expose la formule, les valeurs de config
  utilisées et les métriques sources — chaque euro est explicable.
- **Support & SLA conditionnels** : ajoutés seulement si configurés ; la pénalité
  SLA uniquement en cas de breach.
- **Langage métier** : le domaine ne manipule que `business_service_name`
  (« Service Paiement ») — aucun nom de pod/deployment ne peut fuiter.

## Tests

Fichiers de tests créés pour ce use case :

```
tests/unit/test_incident_cost.py                             # domain model
tests/unit/test_incident_cost_port.py                        # driven port + TypedDicts
tests/unit/test_incident_cost_calculator.py                  # formule, config manquante, basis, langage métier
tests/unit/test_analyze_incident_cost_command.py             # driving command
tests/unit/test_analyze_incident_cost_response.py            # driving response
tests/unit/test_analyze_incident_cost_service_port.py        # driving service port (ABC)
tests/unit/test_analyze_incident_cost_service.py             # application service
tests/unit/test_analyze_incident_cost_use_case.py            # use case
tests/unit/test_incident_cost_adapter.py                     # Facade delegation
tests/unit/test_incident_cost_source.py                      # lecture config business (nullable)
tests/unit/test_analyze_incident_cost_mcp.py                 # MCP tool
tests/unit/test_server.py                                    # build_incident_cost_adapter factory
```

Stubs de logique domaine (formule, config manquante, traçabilité) :

```python
def test_twenty_seven_min_at_500_is_13500():
    # 27 x 500 => 13 500 € (démo principale)
    ...

def test_no_revenue_yields_no_euro_amount():
    # revenue_per_minute null => total None (jamais inventé)
    ...

def test_no_revenue_returns_explanation():
    # explication renvoyée à la place du montant
    ...

def test_sla_penalty_only_when_breached():
    # pénalité SLA uniquement si breach
    ...

def test_basis_records_formula_and_config():
    # calculation_basis expose formule + config + sources
    ...
```

| Scénario (ticket) | Test | Statut |
|---|---|---|
| 27 min @ 500 €/min → 13 500 € | `test_twenty_seven_min_at_500_is_13500` | ✅ |
| Revenu non configuré → durée seule | `test_no_revenue_keeps_duration_facts` | ✅ |
| « Comment est-ce calculé ? » → formule + sources | `test_calculation_basis_exposed` (mcp) | ✅ |
| Zéro jargon Kubernetes | `test_no_kubernetes_jargon_in_service_name` (mcp) | ✅ |
| Config manquante → explication, pas d'estimation | `test_missing_config_returns_explanation_no_amount` (mcp) | ✅ |

## Related Files

- `src/hexawyn/domain/models/incident_cost.py`
- `src/hexawyn/domain/services/incident_cost/incident_cost_calculator.py`
- `src/hexawyn/application/ports/driven/incident_cost_port.py`
- `src/hexawyn/application/ports/driving/analyze_incident_cost/`
- `src/hexawyn/application/service/analyze_incident_cost_service.py`
- `src/hexawyn/application/use_case/analyze_incident_cost/analyze_incident_cost_use_case.py`
- `src/hexawyn/adapters/secondary/gitops/incident_cost_adapter.py`
- `src/hexawyn/adapters/secondary/gitops/incident_cost_source.py`
- `src/hexawyn/mcp/tools/analyze_incident_cost.py`
- `src/hexawyn/mcp/server.py` (`build_incident_cost_adapter`)
