# Fichier : app/services/severity_evaluator.py

from app.services.severity_strategy_factory import SeverityStrategyFactory

# 🎯 Cette classe utilise le design pattern Strategy via une factory
# Elle ne contient plus de logique métier spécifique → elle délègue à la bonne stratégie
class SeverityEvaluator:
    def evaluate(self, pollution_type: str, quantity: float) -> str:
        # On obtient la stratégie correspondante via la factory
        strategy = SeverityStrategyFactory.get_strategy(pollution_type)

        # Si aucun type connu, on retourne "Inconnue"
        if strategy is None:
            return "Inconnue"

        # Sinon, on utilise la stratégie sélectionnée
        return strategy.evaluate(quantity)
