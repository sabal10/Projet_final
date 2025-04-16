# 🌊 PolluMar – Application de Signalement de Pollution Maritime

PolluMar est une application Web de signalement et de suivi des incidents de pollution maritime, développée dans le cadre du cours IFT785 à l'Université de Sherbrooke.

---

## 🚀 Fonctionnalités principales

- 📝 Soumission de signalements via formulaire ou AJAX
- 📊 Évaluation automatique de la gravité d’un incident
- 📨 Notification simulée lors du dépôt d’un signalement
- 🗃️ Historique et statut des signalements (en attente, résolu)
- 🧪 Tests unitaires, d'intégration et end-to-end
- 🧠 Application de plusieurs patrons de conception (en cours)

---

## 🧱 Architecture

L'application suit une architecture **MVC en couches** :

- `models/` : base de données, entités
- `services/` : logique métier, stratégies
- `views/` : routes Flask, interface utilisateur
- `templates/` : HTML Jinja2 avec partials
- `tests/` : tests organisés en `unitaires`, `intégration`, `e2e`
- `uml_patterns/` : diagrammes UML des patrons appliqués

---

## 📐 Design Patterns utilisés

### ✅ 1. Strategy Pattern – Gravité de Pollution

- Permet de séparer l'évaluation de la gravité selon le type de pollution.
- Implémenté dans :
  - `SeverityStrategy` (interface)
  - `PlasticSeverityStrategy`, `HydrocarbonSeverityStrategy`, `ChemicalSeverityStrategy`
  - `SeverityStrategyFactory` : sélection dynamique
  - `SeverityEvaluator` : contexte

📌 Diagramme UML :

![Diagramme Strategy](./uml_patterns/strategy.png)

🧠 Respect du principe **Open/Closed (SOLID)** : on peut ajouter un nouveau type sans modifier l’évaluateur.

> Prochain pattern à intégrer : **Factory**, **Observer**, etc.

---

## 🧪 Tests réalisés

- ✅ **Tests unitaires** : `SeverityEvaluator`, `NotificationService`
- ✅ **Tests d'intégration** : Routes `/report`, `/send_notification`, `/evaluate_severity`, `/resolve`
- ✅ **Tests end-to-end** : Signalement complet, du formulaire à la base de données
- 🎯 Couverture actuelle : **60%** (objectif 70%+ avec les prochains patterns)

---

## ⚙️ Technologies utilisées

- Python 3.11
- Flask
- SQLite
- Pytest (+ coverage)
- PlantUML (UML)
- Git + GitHub (flow `develop` / `feature/*`)

---

## 👨‍💻 Auteur

**Sabala Herman**  
Étudiant à la maîtrise recherche en informatique – Université de Sherbrooke  
Spécialité : cybersécurité, programmation orientée objet, génie logiciel

---

## 📌 À venir

- Intégration du pattern **Observer**
- Séparation claire des contrôleurs et services métiers
- Déploiement (local ou Docker)
- Documentation de l’API (Swagger ou markdown)

---

