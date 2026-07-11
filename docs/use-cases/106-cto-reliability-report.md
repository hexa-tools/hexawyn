# Use Case 106 — Rapport de fiabilité CTO (langage métier)

Répond à : *« Quelle est la fiabilité de notre plateforme ce mois-ci ? »* — pour
un dirigeant non-technique, en langage métier, sans aucun jargon Kubernetes.

Agrège les incidents du mois en un rapport exécutif : taux de disponibilité en
langage humain, nombre d'incidents par sévérité (majeur/mineur), temps de
résolution moyen avec tendance vs mois précédent, et impact financier estimé
(uniquement si le pricing est configuré — jamais inventé). Le résumé exécutif
tient en moins de 5 phrases ; le détail technique reste disponible en
drill-down.

## Sample Questions

- « Quelle est la fiabilité de notre plateforme ce mois-ci ? »
- « Combien d'incidents avons-nous eu ce mois, et de quelle gravité ? »
- « Notre temps de résolution s'améliore-t-il par rapport au mois dernier ? »
- « Quel a été l'impact financier des indisponibilités ce mois-ci ? »
- « Donne-moi un résumé de santé de la plateforme en langage clair pour la direction. »

## 1. Happy Path — chaîne hexagonale complète

```mermaid
sequenceDiagram
    participant CTO
    participant MCP as MCP Tool<br/>(report_platform_reliability)
    participant UC as UseCase
    participant Svc as Service applicatif
    participant Domain as Domaine<br/>(uptime + resolution_trend + financial_impact + summary)
    participant Port as Driven Port<br/>(PlatformReliabilityPort)
    participant Facade as Adapter Facade
    participant Sources as incidents · MTTR · pricing

    CTO->>MCP: report_platform_reliability(period="2026-06")
    MCP->>Svc: build service(port=facade)
    MCP->>UC: execute(command)
    UC->>Svc: report(command)
    Svc->>Port: get_reliability_data("2026-06")
    Port->>Facade: get_reliability_data(...)
    Facade->>Sources: incidents + MTTR mois précédent + coût/min (ou null)
    Sources-->>Svc: ReliabilityData
    Svc->>Domain: generate(data, period)
    Domain->>Domain: uptime = (1 - downtime/total) x 100 (maintenance exclue)
    Domain->>Domain: MTTR moyen + tendance vs mois dernier
    Domain->>Domain: impact financier (null si pricing absent)
    Domain->>Domain: résumé métier sans jargon (<= 5 phrases)
    Domain-->>Svc: PlatformReliabilityReport
    Svc-->>MCP: Response(report)
    MCP-->>CTO: « 99,95% de disponibilité, 2 incidents mineurs... »
```

## 2. Scénarios de contenu

```mermaid
sequenceDiagram
    participant Domain as PlatformReliabilityService
    participant Summary as executive_summary_builder

    Domain->>Summary: build_summary(...)
    alt mois sain (0 incident)
        Summary-->>Domain: « Plateforme stable. Aucun incident ce mois. »
    else 2 incidents mineurs
        Summary-->>Domain: « 99,97% de disponibilité, 2 incidents mineurs... »
    else 1 incident majeur (2h)
        Summary-->>Domain: « Incident critique le 14 juin : 2h. Cause : panne base de données. Corrigé. »
    end
    Note over Domain: impact financier inclus uniquement si pricing configuré
```

## 3. Checker Node — validations LLM (langage métier)

```mermaid
sequenceDiagram
    participant Gen as generate_response
    participant Checker as checker_node / semantic_layer
    participant Matrix as chiffres autoritaires du domaine
    participant Format as format_response

    Gen->>Checker: réponse LLM + PlatformReliabilityReport
    alt Jargon technique (« 3 pods en CrashLoopBackOff »)
        Checker->>Checker: détecte termes k8s interdits en mode direction
        Checker->>Gen: FAIL → reformuler en langage métier
    else Uptime incorrect (LLM dit 99,9% au lieu de 99,72%)
        Checker->>Matrix: uptime = (1 - downtime/total) x 100
        Checker->>Gen: FAIL
    else Impact financier inventé (pricing null mais LLM annonce 5000€)
        Checker->>Matrix: pricing = null ⇒ aucun chiffre financier
        Checker->>Gen: FAIL critique
    else Tendance non signalée (99,99% → 99,95%)
        Checker->>Matrix: compare snapshot DuckDB
        Checker->>Format: FLAG dégradation
    else PASS
        Checker->>Format: réponse exécutive validée
    end
```

## 4. DuckDB Memory (snapshot mensuel & tendance)

```mermaid
sequenceDiagram
    participant MCP as MCP Tool
    participant DuckDB
    participant Svc as Service

    MCP->>DuckDB: MTTR moyen du mois précédent
    alt mois précédent connu
        DuckDB-->>Svc: 14 min → tendance -15%
    else premier mois suivi
        DuckDB-->>Svc: null → tendance stable
    end
    Svc->>DuckDB: stocke le snapshot du mois (uptime, MTTR) pour comparaison
    alt DuckDB indisponible
        Svc-->>Svc: mode dégradé — pas de persistance, jamais de crash
    end
```

## Key Points

- **Zéro jargon Kubernetes** : le résumé exécutif est construit dans le domaine,
  en langage métier français, et ne contient jamais pod/kubectl/namespace/node.
- **Formule d'uptime autoritaire** : `(1 - downtime/total) x 100`, maintenance
  planifiée exclue — c'est la source de vérité que le checker valide (2h/720h → 99,72%).
- **Impact financier honnête** : `None` strict si le pricing n'est pas configuré ;
  aucun chiffre financier n'est jamais inventé.
- **Tendance MTTR signée** (« -15% vs mois dernier ») + improving/degrading/stable.
- **Sévérité métier** (majeur/mineur), pas de niveaux techniques k8s.
- **Résumé ≤ 5 phrases** en mode exécutif ; drill-down technique via `incidents[]`.

## Tests

Fichiers de tests créés pour ce use case :

```
tests/unit/test_platform_reliability.py                          # domain model
tests/unit/test_platform_reliability_port.py                     # driven port + TypedDicts
tests/unit/test_platform_uptime_calculator.py                    # formule uptime + maintenance
tests/unit/test_resolution_trend.py                              # MTTR + delta% + tendance
tests/unit/test_financial_impact.py                              # null si pas de pricing
tests/unit/test_executive_summary_builder.py                     # langage métier, sans jargon, <=5 phrases
tests/unit/test_platform_reliability_service.py                  # orchestration
tests/unit/test_platform_reliability_adapter.py                  # Facade delegation
tests/unit/test_platform_reliability_source.py                   # source par défaut (mois sain)
tests/unit/test_report_platform_reliability_command.py           # driving command
tests/unit/test_report_platform_reliability_response.py          # driving response
tests/unit/test_report_platform_reliability_service_port.py      # driving service port (ABC)
tests/unit/test_report_platform_reliability_service.py           # application service
tests/unit/test_report_platform_reliability_use_case.py          # use case
tests/unit/test_report_platform_reliability_mcp.py               # MCP tool
tests/unit/test_server.py                                        # build_platform_reliability_adapter factory
```

Stubs de logique domaine (uptime, tendance, impact, résumé) :

```python
def test_two_hours_over_thirty_days_is_99_72():
    # 120 min / 43200 min => 99.72% (formule vérifiée par le checker)
    ...

def test_planned_maintenance_excluded():
    # fenêtre de maintenance => exclue du downtime
    ...

def test_none_when_pricing_not_configured():
    # cost_per_minute None => impact financier None (jamais inventé)
    ...

def test_improving_when_faster_than_previous():
    # 12 min vs 14 => -15%, tendance improving
    ...

def test_summary_contains_no_kubernetes_jargon():
    # résumé sans pod/kubectl/namespace/node
    ...

def test_summary_at_most_five_sentences():
    # mode exécutif <= 5 phrases
    ...
```

| Scénario (ticket) | Test | Statut |
|---|---|---|
| Mois sain (0 incident) → « Plateforme stable » | `test_zero_incidents` | ✅ |
| 2 incidents mineurs → 99,9x% + RCA dispo | `test_two_minor_incidents` | ✅ |
| 1 incident majeur (2h) → date + cause racine | `test_major_incident` | ✅ |
| Drill-down technique | `incidents[]` dans la réponse du tool | ✅ |
| Jargon interdit détecté | `test_summary_contains_no_kubernetes_jargon` | ✅ |
| Uptime = (1 - downtime/total) | `test_two_hours_over_thirty_days_is_99_72` | ✅ |
| Impact financier null si pas de pricing | `test_no_financial_figure_without_pricing` | ✅ |
| Tendance vs mois précédent | `test_resolution_trend_improving` | ✅ |

## Related Files

- `src/hexawyn/domain/models/platform_reliability.py`
- `src/hexawyn/domain/services/platform_reliability/uptime_calculator.py`
- `src/hexawyn/domain/services/platform_reliability/resolution_trend.py`
- `src/hexawyn/domain/services/platform_reliability/financial_impact.py`
- `src/hexawyn/domain/services/platform_reliability/executive_summary_builder.py`
- `src/hexawyn/domain/services/platform_reliability/platform_reliability_service.py`
- `src/hexawyn/application/ports/driven/platform_reliability_port.py`
- `src/hexawyn/application/ports/driving/report_platform_reliability/`
- `src/hexawyn/application/service/report_platform_reliability_service.py`
- `src/hexawyn/application/use_case/report_platform_reliability/report_platform_reliability_use_case.py`
- `src/hexawyn/adapters/secondary/gitops/platform_reliability_adapter.py`
- `src/hexawyn/adapters/secondary/gitops/platform_reliability_source.py`
- `src/hexawyn/mcp/tools/report_platform_reliability.py`
- `src/hexawyn/mcp/server.py` (`build_platform_reliability_adapter`)
