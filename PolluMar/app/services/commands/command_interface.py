# app/services/commands/command_interface.py

from abc import ABC, abstractmethod

class Command(ABC):
    """
    Interface de base pour toutes les commandes.
    Chaque commande concrète doit implémenter la méthode execute().
    """
    @abstractmethod
    def execute(self):
        pass
