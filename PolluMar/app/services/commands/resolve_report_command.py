# 📁 app/services/commands/resolve_report_command.py

from .command_interface import Command

class ResolveReportCommand(Command):
    """
    Commande concrète pour marquer un signalement comme résolu.
    """
    def __init__(self, report_manager, report_id):
        """
        :param report_manager: Service de gestion des signalements (accès DB)
        :param report_id: ID du signalement à résoudre
        """
        self.report_manager = report_manager
        self.report_id = report_id

    def execute(self):
        """
        Exécute la commande : met à jour le statut du signalement.
        """
        self.report_manager.resolve_report(self.report_id)
