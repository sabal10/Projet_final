# 📁 Fichier : app/services/observers/email_observer.py

from app.services.observers.observer_interface import Observer

class EmailObserver(Observer):
    """
    Observateur concret qui simule l'envoi d'un email à la personne répondante.
    """
    def update(self, data: dict):
        print(f"\n📧 [EmailObserver] Email envoyé à {data['responder_email']} : "
              f"Le signalement concernant {data['pollution_type']} à {data['location']} "
              f"est maintenant '{data.get('status', 'Inconnu')}'.")
