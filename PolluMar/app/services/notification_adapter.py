# Fichier : app/services/notification_adapter.py

from abc import ABC, abstractmethod

class NotificationAdapter(ABC):
    @abstractmethod
    def send(self, data: dict) -> None:
        pass


# ✅ Console (déjà existant)
class ConsoleNotificationAdapter(NotificationAdapter):
    def send(self, data: dict) -> None:
        print(f"[Console] Notification envoyée à {data['responder_name']} ({data['responder_email']})")


# ✅ Email (simulé)
class EmailNotificationAdapter(NotificationAdapter):
    def send(self, data: dict) -> None:
        print(f"[Email] Objet: Alerte Pollution\n"
              f"Destinataire: {data['responder_email']}\n"
              f"Contenu: Bonjour {data['responder_name']}, une pollution de type {data['pollution_type']} a été détectée ")


# ✅ SMS (simulé)
class SMSNotificationAdapter(NotificationAdapter):
    def send(self, data: dict) -> None:
        print(f"[SMS] Envoi à {data['responder_name']} : Pollution {data['pollution_type']} à {data['location']}\n")


# Fichier : app/services/notification_factory.py

from app.services.notification_adapter import (
    NotificationAdapter,
    ConsoleNotificationAdapter,
    EmailNotificationAdapter,
    SMSNotificationAdapter,
)

class NotificationAdapterFactory:
    @staticmethod
    def create_adapter(channel: str) -> NotificationAdapter:
        if channel == "console":
            return ConsoleNotificationAdapter()
        elif channel == "email":
            return EmailNotificationAdapter()
        elif channel == "sms":
            return SMSNotificationAdapter()
        else:
            raise ValueError(f"Canal de notification inconnu : {channel}")
