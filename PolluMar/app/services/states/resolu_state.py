# 📁 app/services/states/resolu_state.py

from app.services.states.state_interface import State

class ResoluState(State):
    """
    État concret : Résolu.
    Représente un signalement qui a été traité.
    """
    def handle(self, report_data: dict) -> str:
        print("[ResoluState] ✅ Signalement traité et archivé :", report_data.get("description", ""))
        return "Résolu"
