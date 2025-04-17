# app/services/commands/send_notification_command.py

from app.services.commands.command_interface import Command

class SendNotificationCommand(Command):
    """
    Commande concrète pour envoyer une notification via un service de notification.
    """
    def __init__(self, notification_service, report):
        """
        :param notification_service: Instance de NotificationService (déjà injectée)
        :param report: Objet de signalement à notifier (dictionnaire ou modèle)
        """
        self.notification_service = notification_service
        self.report = report

    def execute(self):
        """
        Exécute la commande : envoie la notification avec le service fourni.
        """
        self.notification_service.send(self.report)
