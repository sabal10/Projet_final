##  PolluMar – Application de Signalement de Pollution Maritime

PolluMar est une application Web de signalement et de suivi des incidents de pollution maritime, développée dans le cadre du cours IFT785 à l'Université de Sherbrooke.

##  Fonctionnalités principales

-  Soumission de signalements via formulaire 
-  Évaluation automatique de la gravité d’un incident
-  Notification simulée lors du dépôt d’un signalement
-  Historique et statut des signalements (en attente, résolu)
-  Tests unitaires, d'intégration et end-to-end
-  Application de plusieurs patrons de conception (en cours)

##  Architecture

L'application suit une architecture **MVC en couches** :

- models/ : base de données, entités
- services/ : logique métier, stratégies
- views/ : routes Flask, interface utilisateur
- templates/ : HTML Jinja2 avec partials
- tests/ : tests organisés en `unitaires`, `intégration`, `e2e`
- uml_patterns/ : diagrammes UML des patrons appliqués

##  Design Patterns utilisés

# 1. Strategy Pattern – Gravité de Pollution

- Permet d'évaluer dynamiquement la gravité selon le type de pollution. Ajout de nouveaux comportements sans modifier l'évaluateur.
- Implémenté dans :
  - SeverityStrategy (interface)
  - PlasticSeverityStrategy, HydrocarbonSeverityStrategy, ChemicalSeverityStrategy
  - SeverityStrategyFactory : sélection dynamique
  - SeverityEvaluator : contexte
📌 Lien : Diagramme UML : ![Diagramme Strategy](./uml_patterns/strategy.png)

## 2. Factory Method 
Permet de créer dynamiquement un adaptateur de notification selon le canal (console, email, sms)
Classes :
- NotificationAdapter (interface)
- ConsoleNotificationAdapter, EmailNotificationAdapter, SMSNotificationAdapter
- NotificationAdapterFactory : fabrique d’adaptateurs
- NotificationService : utilise un adaptateur injecté
Lien : Diagramme UML : ![Diagramme Factory Method](./uml_patterns/factory_method.png)

## 🧪 Tests réalisés

- ✅ **Tests unitaires** : `SeverityEvaluator`, `NotificationService`
- ✅ **Tests d'intégration** : Routes `/report`, `/send_notification`, `/evaluate_severity`, `/resolve`
- ✅ **Tests end-to-end** : Signalement complet, du formulaire à la base de données
- 🎯 Couverture actuelle : **60%** (objectif 70%+ avec les prochains patterns)

##  Technologies utilisées

- Python 3.11
- Flask
- SQLite
- Pytest (+ coverage)
- PlantUML (UML)
- Git + GitHub (flow `develop` / `feature/*`)

## Tests
- ✅ **Tests unitaires** :  
  - Évaluateur de gravité (`SeverityEvaluator`)  
  - Stratégies concrètes (`Plastic`, `Hydrocarbures`, `Déchets Chimiques`)  
  - Adaptateurs de notification (`Console`, `Email`, `SMS`)  
  - Fabrique d’adaptateurs (`NotificationAdapterFactory`)  
  - Service de notification (`NotificationService`)  

- ✅ **Tests d’intégration** :  
  - Routes `/report`, `/send_notification`, `/evaluate_severity`, `/resolve`  
  - Intégration complète des adaptateurs avec injection dynamique (Factory Method)

- ✅ **Tests end-to-end (E2E)** :  
  - Scénario complet de signalement via AJAX : évaluation → notification → insertion DB

- 📈 **Couverture de code actuelle** : **66 %**  
  

