#  app/services/notification_factory.py

from app.services.notification_adapter import NotificationAdapter
from app.services.console_notification_adapter import ConsoleNotificationAdapter
from app.services.email_notification_adapter import EmailNotificationAdapter
from app.services.sms_notification_adapter import SMSNotificationAdapter

class NotificationAdapterFactory:
    """
     Pattern Factory Method :
    Retourne dynamiquement un adaptateur de notification
    (console, email, sms) qui respecte l’interface NotificationAdapter.
    """

    @staticmethod
    def create_adapter(channel: str) -> NotificationAdapter:
        """
        Retourne une instance d’adaptateur selon le canal fourni.
        :param channel: 'console', 'email' ou 'sms'
        :return: Instance de classe implémentant NotificationAdapter
        :raises ValueError: Si le canal est inconnu
        """
        channel = channel.strip().lower()  # ✅ normalisation

        if channel == "console":
            return ConsoleNotificationAdapter()
        elif channel == "email":
            return EmailNotificationAdapter()
        elif channel == "sms":
            return SMSNotificationAdapter()
        else:
            raise ValueError(f"Canal inconnu : {channel}")
