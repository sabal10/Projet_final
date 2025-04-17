# 📁 Fichier : app/services/severity_evaluator.py

from app.services.severity_strategy_factory import SeverityStrategyFactory
from app.utilities.logging_decorator import logging_decorator

class SeverityEvaluator:
    """
    🎯 Contexte du pattern Strategy : délègue l’évaluation de la gravité à une stratégie spécifique.
    La logique métier est entièrement externalisée dans les stratégies.
    """

    @logging_decorator
    def evaluate(self, pollution_type: str, quantity: float) -> str:
        """
        Évalue la gravité d’une pollution selon son type et sa quantité.
        Utilise la factory pour sélectionner dynamiquement la stratégie appropriée.
        """
        strategy = SeverityStrategyFactory.get_strategy(pollution_type)

        # Aucune stratégie disponible pour ce type de pollution
        if strategy is None:
            return "Inconnue"

        # Utilise la stratégie retournée pour effectuer l’analyse
        return strategy.evaluate(quantity)
