# Schedule Commands — hexawyn scheduler

Audits récurrents planifiés via cron. v1 = CLI uniquement.

## Créer un check

```bash
# Certificats TLS — toutes les 6h
hexawyn schedule create --name certs --use-case certs_list --every 6h --notify on-change

# Audit RBAC — chaque nuit
hexawyn schedule create --name rbac-audit --use-case audit_excessive_rbac --every 24h --notify on-change

# Drift GitOps — toutes les heures (le drift doit être détecté vite)
hexawyn schedule create --name gitops-drift --use-case gitops_apps_list --every 1h --notify on-change

# Health check fleet — toutes les 30 min
hexawyn schedule create --name fleet-health --use-case global_health_check --every 30m --notify on-change

# Cron complet
hexawyn schedule create --name weekly-audit --use-case certs_list --cron "0 2 * * 1" --notify on-failure
```

## Gérer les checks

```bash
hexawyn schedule list                          # tous les checks
hexawyn schedule get certs                     # détail
hexawyn schedule enable certs                  # active
hexawyn schedule disable certs                 # désactive
hexawyn schedule delete certs                  # supprime
hexawyn schedule run certs                     # exécution manuelle immédiate
hexawyn schedule history certs --limit 10      # historique
hexawyn schedule status                        # vue d'ensemble
hexawyn schedule start --dry-run               # prochaines exécutions (sans lancer)
```

## Raccourcis cron

| Raccourci | Cron |
|---|---|
| `--every 15m` | `*/15 * * * *` |
| `--every 30m` | `*/30 * * * *` |
| `--every 1h` | `0 * * * *` |
| `--every 6h` | `0 */6 * * *` |
| `--every 12h` | `0 */12 * * *` |
| `--every 24h` | `0 0 * * *` |

## Use cases à planifier (valeur récurrente)

| Use case | Fréquence | Pourquoi |
|---|---|---|
| `certs_list` | 6h | Cert qui expire → alerte avant expiration |
| `audit_excessive_rbac` | 24h | Changements RBAC rares mais critiques |
| `detect_root_privileged_pods` | 12h | Nouveau pod root → alerte immédiate |
| `audit_secrets_not_rotated` | 24h | Secret qui dépasse le seuil d'ancienneté |
| `gitops_apps_list` | 1h | Drift GitOps = divergence avec vérité Git |
| `detect_helm_config_drift` | 6h | Config live vs chart Helm |
| `compute_slo_error_budget_burn` | 1h | Burn rate SLO |
| `rollouts_list` | 15m | Rollout bloqué en prod |
| `global_health_check` | 30m | Score de santé cluster |
| `detect_zombies` | 24h | Nouveau workload sans trafic |

## Use cases à NE PAS planifier

`list_pods`, `list_namespaces`, `get_kubernetes_resource` : inventaire brut → pas d'alerte, bruit.
