# 📁 app/services/email_notification_adapter.py

from app.services.notification_adapter import NotificationAdapter

class EmailNotificationAdapter(NotificationAdapter):
    """
    Adaptateur pour simuler l’envoi d’un courriel de notification.
    Implémente l’interface NotificationAdapter.
    Ce comportement est utilisé pour notifier par email un répondant à un signalement.
    """

    def send(self, data: dict) -> None:
        """
        Simule l’envoi d’un email contenant les détails du signalement.
        :param data: dictionnaire contenant les informations à transmettre.
        """
        print(f"[Email] Objet: Alerte Pollution\n"
              f"Destinataire: {data['responder_email']}\n"
              f"Contenu: Bonjour {data['responder_name']}, "
              f"une pollution de type {data['pollution_type']} a été détectée.")
