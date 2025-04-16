# 📁 Fichier : app/services/observers/console_observer.py

from app.services.observers.observer_interface import Observer

class ConsoleObserver(Observer):
    """
    Observateur concret qui affiche un message dans la console lorsqu'un incident est mis à jour.
    Utilisé pour le suivi temps réel ou le débogage.
    """
    def update(self, data: dict):
        print(f"\n🖥️ [ConsoleObserver] Signalement modifié : {data['pollution_type']} à {data['location']} - Statut : {data.get('status', 'Inconnu')}")
