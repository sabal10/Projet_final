#  Fichier : app/services/observers/incident_subject.py

from app.services.observers.observer_interface import Observer
from app.services.observers.subject_interface import Subject

class IncidentSubject(Subject):
    """
    ConcreteSubject : Gère la liste des observateurs et notifie les changements d'état.
    Utilisé ici pour notifier lorsqu'un signalement est modifié (changement d'état ou ajout de commentaires).
    """

    def __init__(self):
        self._observers: list[Observer] = []
        self._incident_data: dict = {}  # Données du signalement modifié

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._incident_data)

    def set_incident_data(self, data: dict) -> None:
        """
        Méthode appelée lorsqu'un changement se produit sur un signalement (ex: ajout commentaire, changement de statut).
        """
        self._incident_data = data
        self.notify()
