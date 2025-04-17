# 🐳 PolluMar – Application de Signalement de Pollution Maritime

PolluMar est une application Web développée dans le cadre du cours **IFT785 - Approches orientées objets** à l’Université de Sherbrooke. Elle permet de signaler, suivre et évaluer des incidents de pollution maritime.

---

## 🌊 Fonctionnalités

- Soumission de signalements
- Évaluation automatique de la gravité
- Notifications via console, email ou journal
- Suivi du statut (en attente, résolu)
- Tests automatisés (unitaires, intégration, E2E)
- Implémentation de 8 design patterns

---

## 🚀 Lancer l’application

```bash
cd Projet_final/PolluMar
python -m app
```

---

## 🧱 Architecture simplifiée

```
📂app/
 ├─ models/
 ├─ services/
 ├─ views/
 ├─ templates/
 ├─ utilities/
 └─ uml_patterns/
📂tests/ (unitaires, intégration, e2e)
```

---

## 🧠 Design Patterns

| Pattern     | Utilisation principale                        | Diagramme UML |
|-------------|-----------------------------------------------|----------------|
| Strategy    | Gravité dynamique selon type de pollution     | [strategy.png](uml_patterns/strategy.png) |
| Factory     | Création dynamique d’adaptateurs              | [factory_method.png](uml_patterns/factory_method.png) |
| Observer    | Notifications multiples d’un événement        | [observer_pattern.png](uml_patterns/observer_pattern.png) |
| State       | Gestion des états d’un signalement            | [state_pattern.png](uml_patterns/state_pattern.png) |
| Adapter     | Uniformisation des canaux de notification     | [adapter_pattern.png](uml_patterns/adapter_pattern.png) |
| Decorator   | Ajout du logging sans modifier le code        | [decorator_pattern.png](uml_patterns/decorator_pattern.png) |
| Command     | Encapsulation des actions (envoyer, résoudre) | [command_pattern.png](uml_patterns/command_pattern.png) |
| Singleton   | Connexion unique à la base de données         | [singleton_database.png](uml_patterns/singleton_database.png) |

---

## ✅ Tests automatisés

| Type             | Exemple de couverture        |
|------------------|------------------------------|
| Tests unitaires  | Gravité, État, Observateurs  |
| Tests intégration| Routes + Adaptateurs         |
| Tests E2E        | Simulation complète utilisateur |
| Couverture totale| **76 %**                     |

---

## 🛠️ Technologies

- Python 3.11 / Flask
- SQLite / Jinja2
- Pytest / Coverage
- Git + GitHub
- UML via PlantUML

---

## 👤 Auteur

**Sabala Herman** – Université de Sherbrooke – IFT785

