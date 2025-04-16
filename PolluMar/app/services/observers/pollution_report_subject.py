# 📁 Fichier : app/services/observers/pollution_report_subject.py

from app.services.observers.observer_interface import Observer
from app.services.observers.subject import Subject


class PollutionReportSubject(Subject):
    """
    ConcreteSubject — représente un signalement d’incident de pollution.
    Il maintient une liste d’observateurs à notifier lors des mises à jour.
    """

    def __init__(self, report_id: int, description: str):
        self.report_id = report_id
        self.description = description
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        Ajoute un observateur s'il n'est pas déjà inscrit.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Supprime un observateur de la liste.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, data: dict) -> None:
        """
        Notifie tous les observateurs avec les données passées.
        """
        for observer in self._observers:
            observer.update(data)

    def resolve(self) -> None:
        """
        Méthode métier simulant la résolution du signalement.
        Elle notifie automatiquement tous les observateurs.
        """
        print(f"✅ Signalement #{self.report_id} résolu : {self.description}")
        self.notify({
            "pollution_type": "Inconnu",
            "location": "Non précisée",
            "responder_email": "non_disponible@pollumar.ca",
            "status": "Résolu"
        })
