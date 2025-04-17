# app/services/commands/command_invoker.py

class CommandInvoker:
    """
    Gestionnaire de commandes. Permet d'empiler et d'exécuter des actions encapsulées.
    """
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        """
        Ajoute une commande à la liste.
        :param command: instance de Command
        """
        self._commands.append(command)

    def run(self):
        """
        Exécute toutes les commandes enregistrées dans l'ordre.
        """
        for command in self._commands:
            command.execute()
        self._commands.clear()
