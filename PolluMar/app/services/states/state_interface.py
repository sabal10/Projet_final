# 📁 Fichier : app/services/states/state_interface.py

from abc import ABC, abstractmethod

class State(ABC):
    """
    Interface de l'état d'un signalement.
    Déclare une méthode que tous les états concrets doivent implémenter.
    """

    @abstractmethod
    def handle(self, report_data: dict) -> str:
        """
        Gère la transition d'état ou le comportement spécifique associé.
        Retourne le nom de l’état ou un message utile au contexte.
        """
        pass
