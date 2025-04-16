# Fichier : app/services/observers/subject.py

from typing import List
from app.services.observers.observer_interface import Observer

class Subject:
    """
    Classe de base Observable (aussi appelée Subject).
    Gère l'enregistrement, la suppression et la notification des observateurs.
    """

    def __init__(self):
        self._observers: List[Observer] = []

    def register(self, observer: Observer) -> None:
        """Ajoute un nouvel observateur à la liste."""
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer: Observer) -> None:
        """Retire un observateur de la liste."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, data: dict) -> None:
        """Notifie tous les observateurs inscrits avec les données fournies."""
        for observer in self._observers:
            observer.update(data)
