# ✅ Fichier : app/services/notification_service.py

from app.models.database import Database
from app.services.notification_factory import NotificationAdapterFactory  # ✅ Import de la factory

class NotificationService:
    """
    Service responsable de :
    - Vérifier les données du signalement
    - Détecter les doublons récents
    - Insérer le signalement dans la base
    - Déléguer l'envoi via un adaptateur de notification (pattern Factory Method)
    """

    def __init__(self, channel="console"):
        # ✅ Instanciation dynamique de l'adaptateur via la factory
        self.adapter = NotificationAdapterFactory.create_adapter(channel)

    def send(self, data):
        # ✅ Champs obligatoires requis
        required_fields = [
            "name", "pollution_type", "description", "location",
            "quantity", "responder_name", "responder_email", "created_at"
        ]

        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Champ obligatoire manquant : {field}")

        db = Database()

        # 🔍 Vérification de doublon : un signalement identique récemment soumis
        existing = db.execute_query("""
            SELECT * FROM reports
            WHERE name = ? AND pollution_type = ? AND location = ?
              AND responder_name = ? AND responder_email = ?
              AND status = 'En attente'
              ORDER BY created_at DESC
            LIMIT 1
        """, (
            data["name"],
            data["pollution_type"],
            data["location"],
            data["responder_name"],
            data["responder_email"]
        ))

        if existing:
            print("⚠️ Doublon détecté : ce signalement existe déjà récemment.")
            return  # ⛔ Ne pas réinsérer

        # ✅ Gravité : si elle n’a pas été évaluée, on met "Inconnue"
        severity = data.get("severity", "Inconnue")

        # ✅ Insertion du signalement dans la base
        db.execute_query("""
            INSERT INTO reports (
                name, pollution_type, description, location, quantity,
                severity, status, responder_name, responder_email,
                created_at, resolved_at, comment
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL)
        """, (
            data["name"],
            data["pollution_type"],
            data["description"],
            data["location"],
            data["quantity"],
            severity,
            "En attente",
            data["responder_name"],
            data["responder_email"],
            data["created_at"]
        ))

        # ✅ Utilisation de l'adaptateur (dynamique via factory)
        self.adapter.send(data)
