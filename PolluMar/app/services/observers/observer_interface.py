# app/services/observers/observer_interface.py

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Interface du pattern Observer.
    Chaque observateur doit implémenter la méthode update().
    """
    @abstractmethod
    def update(self, data: dict) -> None:
        pass
