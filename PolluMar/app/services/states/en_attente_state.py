from app.services.states.state_interface import State

class EnAttenteState(State):
    """
    État concret : En attente.
    Représente un signalement qui vient d’être reçu.
    """
    def handle(self, report_data: dict) -> str:
        print("[EnAttenteState] ⏳ Traitement en attente pour le signalement :")
        return "En attente"
