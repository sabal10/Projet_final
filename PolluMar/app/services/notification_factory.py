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
            raise ValueError(f"Canal inconnu : {channel}")
