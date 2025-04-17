# 📁 app/services/notification_adapter.py

from abc import ABC, abstractmethod

class NotificationAdapter(ABC):
    """
    Interface de base pour tous les canaux de notification.
    Elle définit la méthode 'send' que tous les adaptateurs doivent implémenter.
    Ce design permet de garantir un comportement uniforme pour tous les canaux
    (console, email, SMS, etc.) sans changer la logique métier.
    """

    @abstractmethod
    def send(self, data: dict) -> None:
        """
        Méthode d'envoi de notification.
        :param data: dictionnaire contenant les informations à transmettre.
        """
        pass
