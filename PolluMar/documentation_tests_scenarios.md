# 🧪 Documentation des Scénarios de Test

## 1. Tests Unitaires

| ID   | Composant Testé              | Fonctionnalité Vérifiée                               | Résultat Attendu                              |
|------|------------------------------|--------------------------------------------------------|-----------------------------------------------|
| TU01 | `SeverityEvaluator`          | Évaluation de la gravité selon le type et la quantité | Retourne une sévérité correcte (Léger, etc.)  |
| TU02 | `NotificationService.send`   | Vérifie la validation des champs obligatoires         | Soulève une erreur si champ manquant          |
| TU03 | `NotificationService.send`   | Vérifie l'insertion du signalement en base            | Le signalement est bien ajouté                |
| TU04 | `ConsoleNotificationAdapter` | Envoi via console                                     | Affiche les données dans la console           |
| TU05 | `State Pattern`              | Passage d'un état à un autre                         | Comportement dynamique selon l'état           |
| TU06 | `Command Pattern`            | Exécution de `ResolveReportCommand`                   | Met à jour le statut en "Résolu"              |
| TU07 | `Singleton Database`         | Unicité de l'instance                                 | Deux appels renvoient la même instance        |

---

## 2. Tests d'Intégration

| ID   | Élément Intégré                       | Objectif du Test                                      | Résultat Attendu                               |
|------|----------------------------------------|--------------------------------------------------------|------------------------------------------------|
| TI01 | Route `/send_notification`            | Envoi d’un signalement complet                        | Retourne 200 avec "Notification envoyée"       |
| TI02 | Route `/resolve/<id>`                 | Résolution d’un signalement                          | Statut mis à jour et commentaire ajouté         |
| TI03 | Factory + Adapter                     | Création dynamique d’adaptateur                      | Utilise le bon canal (`console`, `email`, etc.) |
| TI04 | Observer + Subject                    | Notification multiple lors d’un signalement          | Tous les observateurs sont appelés              |

---

## 3. Tests End-to-End (E2E)

| ID   | Scénario                                | Étapes                                                       | Résultat Attendu                               |
|------|------------------------------------------|--------------------------------------------------------------|------------------------------------------------|
| E2E01| Soumission d’un signalement via UI      | Formulaire > Bouton Envoyer > Notification envoyée          | Signalement visible dans Accueil/Manage        |
| E2E02| Commande `/command/send_notification`   | Envoie un POST avec données JSON complètes                  | Retourne 200 + Enregistrement dans la base     |
| E2E03| Résolution via `/resolve/<id>`          | Soumission d’un commentaire de résolution                   | Statut = Résolu, visible dans Historique       |

---

## 4. Couverture

- ✅ Couverture totale : **76%** (unitaires, intégration, E2E)
- Tous les patrons de conception sont testés :
  - Strategy ✅
  - Factory ✅
  - Observer ✅
  - State ✅
  - Decorator ✅
  - Adapter ✅
  - Command ✅
  - Singleton ✅

---

📁 Fichier généré pour : **IFT785 – Projet PolluMar**
👤 Auteur : Sabala Herman – Université de Sherbrooke

