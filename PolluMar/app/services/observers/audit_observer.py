#  Fichier : app/services/observers/audit_observer.py

from app.services.observers.observer_interface import Observer

class AuditTrailLogger(Observer):
    """
    Observateur concret qui simule la journalisation d'un changement dans un audit.
    """
    def update(self, data: dict):
        print(f"\n [AuditTrailLogger] Journalisation : Incident '{data['description']}' modifié. Nouveau statut : {data.get('status', 'Inconnu')}")
