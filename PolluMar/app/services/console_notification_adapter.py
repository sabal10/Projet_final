# 📁 app/services/console_notification_adapter.py

from app.services.notification_adapter import NotificationAdapter

class ConsoleNotificationAdapter(NotificationAdapter):
    """
    Adaptateur pour l’envoi de notifications via la console.
    Utilisé principalement pour les tests ou les environnements de développement.
    Implémente l’interface NotificationAdapter.
    """

    def send(self, data: dict) -> None:
        """
        Affiche un message de notification en console.
        :param data: dictionnaire contenant les informations du signalement.
        """
        print(f"[Console] Notification envoyée à {data['responder_name']} ({data['responder_email']})")
