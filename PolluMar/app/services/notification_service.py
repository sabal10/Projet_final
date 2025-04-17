from app.models.database import Database
from app.services.notification_factory import NotificationAdapterFactory
from app.services.severity_evaluator import SeverityEvaluator
from app.utilities.logging_decorator import logging_decorator

class NotificationService:
    """
    Service responsable de :
    - Vérifier les données du signalement
    - Détecter les doublons récents
    - Évaluer la gravité si non précisée
    - Insérer le signalement dans la base
    - Déléguer l'envoi via un adaptateur de notification (Factory Method)
    """

    def __init__(self, channel="console"):
        self.adapter = NotificationAdapterFactory.create_adapter(channel)

    @logging_decorator
    def send(self, data):
        """
        Envoie une notification après validation, détection de doublon,
        évaluation automatique de la gravité (si absente), insertion en base,
        puis notification via l’adaptateur.
        """
        # ✅ Vérification des champs obligatoires
        required_fields = [
            "name", "pollution_type", "description", "location",
            "quantity", "responder_name", "responder_email", "created_at"
        ]

        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Champ obligatoire manquant : {field}")

        db = Database()

        # 🔍 Vérification de doublon récent
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
            return "Doublon détecté"

        # ✅ Gravité automatique si absente ou inconnue
        if "severity" not in data or data["severity"] == "Inconnue":
            evaluator = SeverityEvaluator()
            try:
                data["severity"] = evaluator.evaluate(
                    data["pollution_type"],
                    float(data["quantity"])
                )
            except Exception as e:
                print(f"❌ Erreur lors de l’évaluation de la gravité : {e}")
                data["severity"] = "Inconnue"  # Fallback sécurisé

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
            data["severity"],
            "En attente",
            data["responder_name"],
            data["responder_email"],
            data["created_at"]
        ))

        # ✅ Envoi de la notification via l’adaptateur (Factory)
        self.adapter.send(data)

        return "Notification envoyée"
