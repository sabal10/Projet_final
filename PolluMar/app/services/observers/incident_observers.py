#  app/services/observers/incident_observers.py

from app.services.observers.observer_interface import Observer


class DeclarantObserver(Observer):
    """
    Observateur concret représentant le déclarant initial du signalement.
    Il est notifié lorsqu’un incident est mis à jour ou résolu.
    """

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def update(self, message: str) -> None:
        print(f"📬 [Notification - Déclarant] {self.name} ({self.email}) a reçu : {message}")


class PersonneRessourceObserver(Observer):
    """
    Observateur concret représentant la personne ressource responsable du suivi.
    Elle est notifiée en cas de changement sur un signalement.
    """

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def update(self, message: str) -> None:
        print(f"📬 [Notification - Responsable] {self.name} ({self.email}) a reçu : {message}")
