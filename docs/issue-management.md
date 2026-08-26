# Process de gestion des Issues — hexawyn

**Document de référence pour hexawyn** — comment les grands projets open-source tiennent leur issue tracker.
Sources : documentation officielle Kubernetes (kubernetes.dev) et OpenTelemetry (opentelemetry.io / github.com/open-telemetry).

---

## 1. ☸️ Kubernetes — le gold standard (Prow + SIGs)

Kubernetes gère un flux d'issues massif grâce à **Prow** (bot) + une taxonomie de labels rigoureuse + une gouvernance par **SIGs** (Special Interest Groups).

### Le flux de triage officiel

```text
Nouvelle issue
   ↓
[bot] labels automatiques : needs-triage, needs-sig, needs-kind, needs-priority
   ↓
Triage (humain, en réunion ou asynchrone) :
   /triage accepted  → triage/accepted (prête à travailler)
   /triage duplicate → fermeture
   /kind bug|feature|cleanup|support
   /sig network|cluster-lifecycle|...  → propriétaire identifié
   /priority P0|P1|P2|P3
   ↓
Si SIG identifié mais aucune action pendant 30 jours → escalade au meeting du SIG
   ↓
Si aucune activité pendant 90 jours → [k8s-triage-robot] lifecycle/stale
   ├─ /lifecycle frozen  → protégée contre la fermeture (issues importantes)
   ├─ /remove-lifecycle stale → réactivée
   └─ sinon → lifecycle/rotten → fermeture auto
```

### La taxonomie de labels (essentielle)

| Famille | Exemples | Rôle |
|---|---|---|
| `sig/*` | `sig/network`, `sig/cluster-lifecycle` | **Qui possède** l'issue (gouvernance décentralisée) |
| `kind/*` | `kind/bug`, `kind/feature`, `kind/cleanup` | **Type** de travail |
| `priority/*` | `priority/critical-urgent` → `awaiting-more-evidence` | **Urgence** |
| `triage/*` | `triage/accepted`, `triage/needs-information` | **État du triage** |
| `lifecycle/*` | `lifecycle/stale`, `frozen`, `rotten`, `active` | **Cycle de vie** automatique |
| `needs-*` | `needs-sig`, `needs-kind`, `needs-triage`, `needs-ok-to-test` | **Prérequis manquants** (bloquants bots) |
| Onboarding | `help wanted`, `good first issue` | **Recrutement de contributeurs** |

### Les règles du bot (Prow)
- **`needs-triage`** : appliqué automatiquement à toute nouvelle issue — c'est le signal booléen « pas encore triée »
- **`require-matching-label`** : une issue ne peut pas rester sans `kind/*` et `sig/*`
- **OWNERS files** : chaque dossier a des approvers ; un PR nécessite l'approbation d'un OWNER (`/approve`, `lgtm`)
- **Gouvernance par SIG** : chaque SIG trie ses propres issues, décide de ses priorités, tient ses meetings

---

## 2. 📊 OpenTelemetry — la taxonomie de décision la plus claire

OpenTelemetry (CNCF) documente son process dans `issue-management.md`. Sa force : **3 états de décision explicites** avec des chemins de sortie définis.

### Les 3 familles de triage

```text
triage:deciding:*   → en cours d'analyse
   ├─ triage:deciding:tc-inbox       → bloque sur les mainteneurs
   ├─ triage:deciding:needs-info     → attend des infos de l'auteur
   ├─ triage:deciding:community-feedback → mérite discussion communautaire
   └─ triage:deciding:new-issue      → état initial automatique

triage:accepted:*   → acceptée
   ├─ triage:accepted:ready           → petit scope, travaillable immédiatement
   ├─ triage:accepted:needs-pr        → attend un PR
   └─ triage:accepted:needs-sponsor   → attend un sponsor (modèle spec)

triage:rejected:*   → refusée (avec la raison !)
   ├─ triage:rejected:duplicate       → doublon (règle : ~80% de recouvrement)
   ├─ triage:rejected:invalid         → invalide
   ├─ triage:rejected:insufficient-info → auteur muet > 2 semaines
   ├─ triage:rejected:out-of-scope    → hors périmètre
   ├─ triage:rejected:scope-too-large → trop grosse → rediriger vers un OTEP
   └─ triage:rejected:declined        → pas aligné avec la stratégie projet
```

### Les automatisations
- **`triage:followup`** : un workflow (`triage-helper/app.py`) marque les issues `deciding` avec activité récente → **re-triage après 14 jours d'inactivité**, retiré sous 7 jours
- **Stale bot** (collector-contrib) : stale après **60 jours**, fermeture 60 jours plus tard, avec **ping des code owners** avant fermeture (script custom `mark-issues-as-stale.sh`)
- **Codeowners** : avant de fermer une issue stale, le bot ping les propriétaires du composant (`get-codeowners.sh`) — la fermeture n'est jamais silencieuse
- **Modèle sponsor** (spec) : une issue acceptée attend un **spec issue sponsor** volontaire ; les PR avant sponsor sont refusés ; sans sponsor, l'issue retombe en `community-feedback` après 3 mois

### La culture (citée dans leur propre issue #3821)
> « Having an intractable number of open issues doesn't provide any additional visibility over closing them. Adopt a culture where we close stale issues and are comfortable re-opening them when relevant again. »

---

## 3. 🔀 Tableau comparatif

| Aspect | ☸️ Kubernetes | 📊 OpenTelemetry |
|---|---|---|
| Backlog ouvert | Maîtrisé (SIGs) | Maîtrisé (taxonomie stricte) |
| Triage automatique | Prow (`needs-*`, `require-matching-label`) | Workflow custom + stale bot |
| Décision humaine | SIG meetings + `/triage accepted` | `deciding:*` explicite |
| Fermeture des invalides | `lifecycle/stale→rotten` | `rejected:*` **avec raison** |
| Signal communautaire | `help wanted` / `good first issue` | `community-feedback` + 👍 |
| Propriété | **SIGs + OWNERS files** | Codeowners par composant |
| Protection | `lifecycle/frozen` | `forever` |

---

## 4. 🎯 Process recommandé pour hexawyn (synthèse)

### Jour 1 — la taxonomie de labels (copier Kubernetes, allégée)

```
type/*        type/bug · type/feature · type/cleanup · type/question
area/*        area/harness · area/mcp · area/cli · area/graph · area/agent
triage/*      triage/needs-triage (auto) · triage/accepted · triage/needs-info
              triage/duplicate · triage/out-of-scope · triage/insufficient-info
priority/*    priority/P0 · P1 · P2 · P3
lifecycle/*   lifecycle/stale · lifecycle/frozen (protégé)
onboarding    help wanted · good first issue
```

### Jour 1 — le bot minimal (GitHub Actions, ~100 lignes)
1. Nouvelle issue → label `triage/needs-triage` automatique
2. Issue sans `type/*` ou `area/*` après 48h → commentaire bot « merci d'ajouter les labels » (règle `require-matching-label` allégée)
3. **Stale** : 45 jours sans activité → commentaire + `lifecycle/stale` → **fermeture 30 jours après** si rien (plus agressif qu'OTEL : une jeune communauté doit rester propre)
4. `lifecycle/frozen` = protection mainteneur (issues roadmap)
5. **Ping des code owners avant fermeture stale** (pattern OTEL : fermeture jamais silencieuse)

### Le process humain (copier Kubernetes/OTEL)
- **Chaque issue obtient une décision** : `accepted` / `rejected:<raison>` / `needs-info` — jamais d'état flou
- **Deux chemins d'acceptation** : `needs-maintainer-review` (technique) et `needs-product-decision` (produit / roadmap) — routés explicitement
- **Signal communautaire** : 3 réactions (👍 / 🚨 / 🐛) suffisent pour prioriser sans effort mainteneur
- **Objectif de backpressure** : garder < 10% d'issues ouvertes, time-to-close médian < 14 jours
- **Une issue fermée n'est jamais une insulte** : la culture « close and re-open when relevant » d'OTEL doit être écrite dans le CONTRIBUTING

### Quand grandir (au-delà de 1 000 issues/mois)
- Passer aux **SIGs/OWNERS files** (modèle Kubernetes) — la propriété décentralisée est le seul moyen de tenir à l'échelle
- Ajouter `good first issue` + `help wanted` systématiques (recrutement)
- Réunions de triage hebdomadaires (modèle Kubernetes)

---

## 5. Sources

- Kubernetes Issue Triage Guidelines : https://www.kubernetes.dev/docs/guide/issue-triage/
- Kubernetes label_sync : https://github.com/kubernetes/test-infra/blob/master/label_sync/labels.yaml
- Kubernetes Prow bot commands : https://go.k8s.io/bot-commands
- OTEL issue-management : https://github.com/open-telemetry/opentelemetry-specification/blob/main/issue-management.md
- OTEL SIG practices (stale/followup) : https://opentelemetry.io/docs/contributing/sig-practices/
- OTEL stale script : https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/98f18734/.github/workflows/scripts/mark-issues-as-stale.sh
- OTEL spec rework discussion : https://github.com/open-telemetry/opentelemetry-specification/issues/3821
