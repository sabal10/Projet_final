# Fichier : app/services/severity_strategy.py

from abc import ABC, abstractmethod

#  Interface du pattern Strategy
# Cette classe abstraite définit le contrat que toutes les stratégies concrètes doivent respecter.
class SeverityStrategy(ABC):
    @abstractmethod
    def evaluate(self, quantity: float) -> str:
        """
        Méthode d'évaluation à implémenter par chaque stratégie.
        Elle retourne une chaîne indiquant le niveau de gravité.
        """
        pass


#  Stratégie concrète pour les plastiques
class PlasticSeverityStrategy(SeverityStrategy):
    def evaluate(self, quantity: float) -> str:
        if quantity > 50:
            return "Urgent"
        elif quantity >= 10:
            return "Modéré"
        return "Faible"


#  Stratégie concrète pour les hydrocarbures
class HydrocarbonSeverityStrategy(SeverityStrategy):
    def evaluate(self, quantity: float) -> str:
        if quantity > 20:
            return "Urgent"
        elif quantity >= 5:
            return "Modéré"
        return "Faible"


#  Stratégie concrète pour les déchets chimiques
class ChemicalSeverityStrategy(SeverityStrategy):
    def evaluate(self, quantity: float) -> str:
        if quantity > 500:
            return "Urgent"
        elif quantity >= 100:
            return "Modéré"
        return "Faible"
