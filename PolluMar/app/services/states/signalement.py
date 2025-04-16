# 📁 Fichier : app/services/states/signalement.py

from app.services.states.state_interface import State
from app.services.states.en_attente_state import EnAttenteState
from app.services.states.resolu_state import ResoluState



class Signalement:
    """
    Contexte — représente un signalement pouvant changer d’état (en attente, résolu, etc.).
    Il délègue le comportement à l’état actuel.
    """

    def __init__(self, data: dict):
        # Initialisation avec un statut par défaut si non présent
        self.data = data
        if "status" not in self.data:
            self.data["status"] = "En attente"
        self.state: State = EnAttenteState()

    def set_state(self, state: State) -> None:
        self.state = state

    def traiter(self) -> str:
        statut = self.state.handle(self.data)
        self.data["status"] = statut
        return statut
