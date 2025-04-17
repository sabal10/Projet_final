# 📁 app/services/sms_notification_adapter.py

from app.services.notification_adapter import NotificationAdapter

class SMSNotificationAdapter(NotificationAdapter):
    """
    Adaptateur pour simuler l’envoi d’un message SMS concernant un signalement.
    Implémente l’interface NotificationAdapter.
    Utilisé pour représenter un envoi rapide et concis d’alerte pollution.
    """

    def send(self, data: dict) -> None:
        """
        Simule l’envoi d’un SMS avec les informations essentielles du signalement.
        :param data: dictionnaire contenant les informations à transmettre.
        """
        print(f"[SMS] Envoi à {data['responder_name']} : Pollution {data['pollution_type']} à {data['location']}")
